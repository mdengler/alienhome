"""
Copyright (C) Peter Hollobon 2005
Copyright Martin Dengler 2006-11
"""

# pylint: disable-msg=C0103
# pylint: disable-msg=C0111

# pylint: disable-msg=W0212
# pylint: disable-msg=W0622
# pylint: disable-msg=W0703
# pylint: disable-msg=W6501

import time
import logging

logging.basicConfig(level=logging.DEBUG)

import ctypes
import pyHook
import pythoncom
import win32api
#import win32com
#import win32com.client
import win32con
import win32gui

#from ctypes import wintypes

byref = ctypes.byref
user = ctypes.windll.user32
kernel = ctypes.windll.kernel32

OpenDesktop = user.OpenDesktopA
OpenInputDesktop = user.OpenInputDesktop
SwitchDesktop = user.SwitchDesktop
GetTopWindow = user.GetTopWindow
DESKTOP_SWITCHDESKTOP = 0x0100

_leftMouseButtonDown = False
_middleMouseButtonDown = False
_rightMouseButtonDown = False

_moving = False

snapToScreenEdges = True
snapToScreenEdgesThreshold = 30
snapToWindowEdges = True
snapToWindowEdgesThreshold = 10



def dump_keyfreqs():
    fh = open(r"\\kbcfp\london\u\denglerm\keyfrequencies.txt", "a")
    today = time.strftime("%Y%m%d", time.localtime())
    for key, freq in key_frequencies.iteritems():
        fh.write("%s,%s,%s\n" % (today, key, freq))
    fh.flush()
    fh.close()
    key_frequencies.clear()


def exit():
    try:
        dump_keyfreqs()
    finally:
        import os
        os._exit(1)



class RECT(ctypes.Structure):
    _fields_ = [
        ('left', ctypes.c_long),
        ('top', ctypes.c_long),
        ('right', ctypes.c_long),
        ('bottom', ctypes.c_long)
        ]
    def dump(self):
        return map(int, (self.left, self.top, self.right, self.bottom))

class MONITORINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', ctypes.c_ulong),
        ('rcMonitor', RECT),
        ('rcWork', RECT),
        ('dwFlags', ctypes.c_ulong)
      ]

class GUITHREADINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_ulong),
        ("flags", ctypes.c_ulong),
        ("hwndActive", ctypes.c_ulong),
        ("hwndFocus", ctypes.c_ulong),
        ("hwndCapture", ctypes.c_ulong),
        ("hwndMenuOwner", ctypes.c_ulong),
        ("hwndMoveSize", ctypes.c_ulong),
        ("hwndCaret", ctypes.c_ulong),
        ("rcCaret", RECT)
      ]



class TITLEBARINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),
        ("rcTitleBar", RECT),
        ("rgstate", ctypes.c_uint * 6)
    ]

class WINDOWINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),
        ("rcWindow", RECT),
        ("rcClient", RECT),
        ("dwStyle", ctypes.c_uint),
        ("dwExStyle", ctypes.c_uint),
        ("dwWindowStatus", ctypes.c_uint),
        ("cxWindowBorders", ctypes.c_uint),
        ("cyWindowBorders", ctypes.c_uint),
        ("atomWindowType", ctypes.c_uint),
        ("wCreatorVersion", ctypes.c_ushort),
    ]

def get_titlebar_size(windowHandle):
    tbi = TITLEBARINFO()
    #tbi.cbSize = ctypes.sizeof(TITLEBARINFO)
    user.GetTitleBarInfo(windowHandle, byref(tbi))
    win32api.FormatMessage(win32api.GetLastError())

    return (tbi.rcTitleBar.b.x - tbi.rcTitleBar.a.x, tbi.rcTitleBar.b.y - tbi.rcTitleBar.a.y)

def get_border_size(windowHandle):
    wi = WINDOWINFO()
    wi.cbSize = ctypes.sizeof(WINDOWINFO)
    user.GetWindowInfo(windowHandle, byref(wi))

    return wi.cxWindowBorders, wi.cyWindowBorders
    #return wi.rcClient.a.x - wi.r

def is_movable_window(windowHandle):
    wi = WINDOWINFO()
    wi.cbSize = ctypes.sizeof(WINDOWINFO)
    user.GetWindowInfo(windowHandle, byref(wi))
    return win32gui.IsWindowVisible(windowHandle) and (wi.dwStyle & win32con.WS_CHILDWINDOW == 0)

def get_top_window(windowHandle):
    while not is_movable_window(windowHandle) and win32gui.GetParent(windowHandle):
        try:
            windowHandle = win32gui.GetParent(windowHandle)
        except Exception, msg_:
            break
    return windowHandle

def exceed_windows():
    return all_in_class("EXCEEDW:MWCLIENT0")

def all_in_class(winclass):
    retval = []
    last_wh = win32con.NULL
    while True:
        #logging.info("%s %s " % (last_wh, winclass))
        try:
            last_wh = win32gui.FindWindowEx(win32con.NULL, last_wh, winclass, None)
            retval.append(last_wh)
            #logging.info("\tgot %s - %s" % (last_wh, win32gui.GetWindowText(last_wh)))
            if last_wh == win32con.NULL:
                break
        except Exception, msg_:
            break
    return retval

def primary_monitor_info():
    r = RECT()
    user.SystemParametersInfoA(win32con.SPI_GETWORKAREA, 0, ctypes.byref(r), 0)
    logging.info("primary_monitor_info(): got %s", r.dump())
    return (map(int, (r.left, r.top, r.right, r.bottom)))

def get_monitors():
    retval = []
    CBFUNC = ctypes.WINFUNCTYPE(ctypes.c_int,
                                ctypes.c_ulong,
                                ctypes.c_ulong,
                                ctypes.POINTER(RECT),
                                ctypes.c_double)
    def cb(hMonitor, hdcMonitor, lprcMonitor, dwData):
        r = lprcMonitor.contents
        logging.info("cb: %s %s %s %s %s %s %s %s",
            hMonitor, type(hMonitor),
            hdcMonitor, type(hdcMonitor),
            lprcMonitor, type(lprcMonitor),
            dwData, type(dwData))
        logging.info("get_monitors() cb: adding %s/%s to data", hMonitor, r.dump())
        retval.append([hMonitor, r.dump()])
        return 1
    cbfunc = CBFUNC(cb)
    res_ = user.EnumDisplayMonitors(0, 0, cbfunc, 0)
    return retval


def monitor_areas():
    retval = []
    monitors = get_monitors()
    for hMonitor, extents_ in monitors:
        data = [hMonitor]
        mi = MONITORINFO()
        #mi.cbSize = ctypes.sizeof(MONITORINFO)
        res_ = user.GetMonitorInfoA(hMonitor, ctypes.byref(mi))
        data.append(mi.rcMonitor.dump())
        data.append(mi.rcWork.dump())
        retval.append(data)
    return retval


# http://mail.python.org/pipermail/python-win32/2007-April/005715.html
#import wmi
#import win32api
#c = wmi.WMI()
#for this_machine in c.Win32_ComputerSystem():
#  for user in this_machine.associators(wmi_result_class="Win32_UserAccount"):
#    if user.Name == win32api.GetUserName ():
#      for desktop in user.associators (wmi_result_class="Win32_Desktop"):
#        print desktop.Wallpaper, desktop.WallpaperStretched, desktop.WallpaperTiled


def islocked():
    hDesktop = OpenDesktop("default", 0, False, DESKTOP_SWITCHDESKTOP)
    hDesktop = OpenInputDesktop(0, False, DESKTOP_SWITCHDESKTOP)
    return SwitchDesktop(hDesktop) == 0


def all_true(l):
    for i in l:
        if not i:
            return False
    return True


def suppress_alt_if_mousedown(vk, id_, keydown_, mousedown):
    if vk == "Lmenu":  #TODO: confirm should not test for keyup here?
        passon = not mousedown
        if not passon:
            t = time.time()
            logging.info(
                "OKE_Lmenu: suppressing Lmenu key: %s (%s vs. %s)"
                % (self._last_mouse_move - t, t, self._last_mouse_move))


class mover(object):
    def __init__(self):
        self.xmax_hist = {}
        self.ymax_hist = {}

        self.hm = pyHook.HookManager()

        # register two callbacks
        self.hm.MouseAllButtons = self.OnMouseClick
        self.hm.KeyDown = self.OnKeyboardEvent
        self.hm.KeyUp = self.OnKeyboardEvent

        # hook into the mouse and keyboard events
        self.hm.HookMouse()
        self.hm.HookKeyboard()

        self.monitors = get_monitors()
        primary_monitor_info()

        #self._ftable = {}
        self._modifier_down = {
            "Lwin": False,
            "Rwin": False,
            "Lcontrol": False,
            "Rcontrol": False,
            "Lmenu": False,
            "Rmenu": False,
            }
        self._mouse_botton_down = {
            "L": False,
            "R": False,
            "M": False,
            }

        self._window_handle = 0
        self._client_pos = None

        self._xrp = None
        self._yrp = None
        self._original_pos = None
        self._window_size = None
        self._window_pos = None

        self._last_mouse_move = None

        self._keyeventring = []
        self._key_frequencies = {}


    def OnMouseClick(self, event):

        if event.MessageName.startswith("mouse"):
            #logging.info("mouse event: %s"  % event.MessageName)
            if event.MessageName.endswith("down"):
                if event.MessageName == 'mouse left down':
                    self._mouse_botton_down["L"] = True
                elif event.MessageName == 'mouse middle down':
                    self._mouse_botton_down["M"] = True
                elif event.MessageName == 'mouse right down':
                    self._mouse_botton_down["R"] = True

                if self._modifier_down["ALT"]:

                    guiti = GUITHREADINFO(cbSize=ctypes.sizeof(GUITHREADINFO))
                    user.GetGUIThreadInfo(0, ctypes.byref(guiti))
                    wi = WINDOWINFO()
                    wi.cbSize = ctypes.sizeof(WINDOWINFO)

                    win = win32gui.WindowFromPoint(event.Position)
                    #win = guiti.hwndFocus

                    win = get_top_window(win)

                    user.GetWindowInfo(win, byref(wi))

                    #wp = win32gui.GetWindowPlacement(win)
                    self._original_pos = event.Position
                    self._client_pos = win32gui.ScreenToClient(win, self._original_pos)
                    w_rect = win32gui.GetWindowRect(win)
                    self._window_size = (w_rect[2] - w_rect[0],
                                         w_rect[3] - w_rect[1])
                    self._window_pos = w_rect[0:2]

                    self._xrp =  self._client_pos[0] / (self._window_size[0] / 2)
                    self._yrp =  self._client_pos[1] / (self._window_size[1] / 2)

                    self._window_handle = win
                    self.hm.MouseMove = self.OnMouseMove

                    return False

            elif event.MessageName.endswith("up"):
                if event.MessageName == 'mouse left up':
                    self._mouse_botton_down["L"] = False
                elif event.MessageName == 'mouse middle up':
                    self._mouse_botton_down["M"] = False
                elif event.MessageName == 'mouse right up':
                    self._mouse_botton_down["R"] = False

                #print win32gui.GetWindowRect(win32gui.GetDesktopWindow())
                self._window_handle = 0
                self.hm.MouseMove = None
                if self._modifier_down["ALT"]:
                    self._modifier_down["ALT"] = False

        return True


    def OnMouseMove(self, event):
        passon = True
        if (self._modifier_down["ALT"]
            and
            (_leftMouseButtonDown or _middleMouseButtonDown)):
            self._last_mouse_move = time.time()

        if _leftMouseButtonDown:
            win32gui.SetWindowPos(
                self._window_handle,
                0,
                event.Position[0] - self._client_pos[0] - 6,
                event.Position[1] - self._client_pos[1] - 29,
                0,
                0,
                win32con.SWP_NOSIZE)
        elif _middleMouseButtonDown:
            cx = event.Position[0] - self._original_pos[0]
            cy = event.Position[1] - self._original_pos[1]

            if self._xrp == 0:
                px = self._window_pos[0] + cx
                sx = self._window_size[0] - cx
            else:
                px = self._window_pos[0]
                sx = self._window_size[0] + cx

            if self._yrp == 0:
                py = self._window_pos[1] + cy
                sy = self._window_size[1] - cy
            else:
                py = self._window_pos[1]
                sy = self._window_size[1] + cy

            win32gui.SetWindowPos(self._window_handle, 0, px, py, sx, sy, 0)

        passon = False

        win32api.SetCursorPos(event.Position)

        return passon

    def unpack(self, keyevent):
        vk = keyevent.GetKey()
        id = keyevent.KeyID
        keydown = keyevent.IsTransition() == 0
        mousedown = (_leftMouseButtonDown or _middleMouseButtonDown or _rightMouseButtonDown)
        return vk, id, keydown, mousedown



    actions = {
      "V": [("Lwin",), mover.ymax_currwin],
      }
    modifier_hacks = {
        "Lmenu": (suppress_alt_if_mousedown, ),
        }

    def OnKeyboardEvent(self, event):
        vk, id, keydown, mousedown = self.unpack(event)
        passon = True

        self._keyeventring.append(event)
        if len(self._keyeventring) > 10:
            self._keyeventring = self._keyeventring[-5:]

        #logging.info("got key:\tid:%s\tvk:%s\tkeydown:%s\tmousedown:%s" % (id, vk, keydown, mousedown))

        self._key_frequencies.setdefault(vk, 0)
        self._key_frequencies[vk] += 1

        if vk in self._modifier_down:
            self._modifier_down[vk] = keydown
            for func in mover.modifier_hacks.get(vk, []):
                func(vk, id, keydown, mousedown)

        if vk in mover.actions:
            modifiers_required, func = mover.actions[vk]
            vk, id, keydown, mousedown = self.unpack(event)
            passon = True

            if keydown and all_true(
                [self._modifier_down[m] for m in modifiers_required]):
                passon = func(event)

        return passon

    # def OnKeyboardEvent_orig(self, event):
    #     vk, id, keydown, mousedown = self.unpack(event)
    #     global keyeventring
    #     keyeventring.append(event)
    #     if len(keyeventring) > 10:
    #         keyeventring = keyeventring[-5:]
    #     passon = True
    #     #logging.info("got key:\tid:%s\tvk:%s\tkeydown:%s\tmousedown:%s" % (id, vk, keydown, mousedown))

    #     funcstr = "self.OnKeyboardEvent_%s" % vk

    #     key_frequencies.setdefault(vk, 0)
    #     key_frequencies[vk] += 1

    #     if not (funcstr in self._ftable):
    #         try:
    #             #print funcstr
    #             self._ftable[funcstr] = eval(funcstr)
    #         except Exception, e:
    #             self._ftable[funcstr] = None
    #             if "object has no attribute" not in str(e):
    #                 logging.info("Exception calling %s: %s" % (funcstr, e))

    #     func = self._ftable.get(funcstr)
    #     if func:
    #         passon = func(event)

    #     return passon


    def OnKeyboardEvent_Lmenu(self, event):
        vk_, id_, keydown, mousedown = self.unpack(event)
        t = time.time()
        #passon = not (mousedown or t - _lastMouseMoveTrapped < 5.0)

        passon = not mousedown
        #passon = True

        self._modifier_down["ALT"] = keydown
        if not passon:
            logging.info("OKE_Lmenu: suppressing Lmenu key: %s (%s vs. %s)",
                         self._last_mouse_move - t, t, self._last_mouse_move)
        return passon

    def OnKeyboardEvent_Lshift(self, event):
        vk_, id_, keydown, mousedown = self.unpack(event)
        passon = True
        self._modifier_down["SHIFT"] = keydown
        return passon

    def OnKeyboardEvent_Rshift(self, event):
        return self.OnKeyboardEvent_Lshift(event)

    def OnKeyboardEvent_Lcontrol(self, event):
        vk_, id_, keydown, mousedown = self.unpack(event)
        passon = True
        self._modifier_down["CTRL"] = keydown

        if self._modifier_down["CTRL"]:
          elapsed = time.clock()
          if elapsed - self._last_down_times.get("control", -100) < 1:
            logging.info("double-Control pressed")
            elapsed = -100
          self._last_down_times["control"] = elapsed

        return passon

    def OnKeyboardEvent_Rcontrol(self, event):
        return self.OnKeyboardEvent_Lcontrol(event)

    def OnKeyboardEvent_Lwin(self, event):
        vk, id, keydown, mousedown = self.unpack(event)
        passon = True
        if not keydown:
            #logging.info("got Win/Super: %s %s" % (vk, keydown))
            pass
        self._modifier_down["SUPER"] = keydown
        return passon

    def OnKeyboardEvent_Rwin(self, event):
        return self.OnKeyboardEvent_Lwin(event)

    def OnKeyboardEvent_W(self, event):
      orig_wallpaper=win32gui.SystemParametersInfo(Action=win32con.SPI_GETDESKWALLPAPER)
      print 'Original: ',orig_wallpaper
      for bmp in glob.glob(os.path.join(os.environ['windir'],'*.bmp')):
        print bmp
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, Param=bmp)
        print win32gui.SystemParametersInfo(Action=win32con.SPI_GETDESKWALLPAPER)
        time.sleep(1)

      win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, Param=orig_wallpaper)

    def OnKeyboardEvent_V(self, event):
        vk, id, keydown, mousedown = self.unpack(event)
        passon = True
        #if self._modifier_down["SUPER"] and keydown:
        if self._modifier_down["ALT"] and self._modifier_down["CTRL"] and keydown:
            self.ymax_currwin(event, self._modifier_down["SHIFT"])
            passon = False
        return passon

    def OnKeyboardEvent_H(self, event):
        vk, id, keydown, mousedown = self.unpack(event)
        passon = True
        #if self._modifier_down["SUPER"] and keydown:
        if self._modifier_down["ALT"] and self._modifier_down["CTRL"] and keydown:
            self.xmax_currwin(event, self._modifier_down["SHIFT"])
            passon = False
        return passon

    def OnKeyboardEvent_F(self, event):
        vk, id, keydown, mousedown = self.unpack(event)
        passon = True
        if self._modifier_down["ALT"] and self._modifier_down["CTRL"] and keydown:
            dump_keyfreqs()
            passon = False
        return passon

    def OnKeyboardEvent_Q(self, event):
        vk, id, keydown, mousedown = self.unpack(event)
        passon = True
        if self._modifier_down["ALT"] and self._modifier_down["CTRL"] and keydown:
            exit()
            passon = False
        return passon

    def OnKeyboardEvent_E(self, event):
        vk, id, keydown, mousedown = self.unpack(event)
        passon = True
        #if self._modifier_down["SUPER"] and keydown:
        if self._modifier_down["ALT"] and self._modifier_down["CTRL"] and keydown:
            self.focus_window(title="emacs", bring_to_front=True)
            passon = False
        return passon


    def focus_window(self, title=None, bring_to_front=False):
        pass
        return True


    def ymax_currwin(self, event, onlyEnd=False):
        mi = MONITORINFO(cbSize=ctypes.sizeof(MONITORINFO))
        guiti = GUITHREADINFO(cbSize=ctypes.sizeof(GUITHREADINFO))
        user.GetGUIThreadInfo(0, ctypes.byref(guiti))
        wi = WINDOWINFO()
        wi.cbSize = ctypes.sizeof(WINDOWINFO)
        win = guiti.hwndFocus
        user.GetWindowInfo(win, byref(wi))

        win = get_top_window(win)

        winr = RECT()
        user.GetWindowRect(win, ctypes.byref(winr))
        hMonitor = user.MonitorFromRect(ctypes.byref(winr), 0)
        res = user.GetMonitorInfoA(hMonitor, ctypes.byref(mi))

        curheight = winr.bottom - winr.top
        abstop = 0
        absbottom = mi.rcWork.bottom
        newtop = abstop
        newbottom = absbottom
        #newheight = oldheight + (absbottom - winr.bottom)

        uFlags = win32con.SWP_ASYNCWINDOWPOS | win32con.SWP_NOACTIVATE

        if self.ymax_hist.has_key(win):
            oldr = self.ymax_hist[win]
            newtop = oldr.top
            newbottom = oldr.bottom
            del self.ymax_hist[win]
        else:
            self.ymax_hist[win] = winr
            if onlyEnd:
                uFlags |= win32con.SWP_NOMOVE
                newtop = winr.top

        width = winr.right - winr.left
        newheight = newbottom - newtop

        res = win32gui.SetWindowPos(win, 0, winr.left, newtop, width, newheight, uFlags)

        logging.info("ymax info: %s, %s, %s, %s, %s"
                     % (res, winr.dump(), mi.rcWork.dump(), curheight, newheight))


    def xmax_currwin(self, event, spanMonitors=True, onlyEnd=False):
        mi = MONITORINFO(cbSize=ctypes.sizeof(MONITORINFO))
        guiti = GUITHREADINFO(cbSize=ctypes.sizeof(GUITHREADINFO))
        user.GetGUIThreadInfo(0, ctypes.byref(guiti))
        wi = WINDOWINFO()
        wi.cbSize = ctypes.sizeof(WINDOWINFO)
        win = guiti.hwndFocus
        user.GetWindowInfo(win, byref(wi))

        win = get_top_window(win)

        winr = RECT()
        user.GetWindowRect(win, ctypes.byref(winr))
        hMonitor = user.MonitorFromRect(ctypes.byref(winr), 0)
        res = user.GetMonitorInfoA(hMonitor, ctypes.byref(mi))

        curwidth = winr.right - winr.left
        absleft = mi.rcWork.left
        absright = mi.rcWork.right
        if spanMonitors:
            res = user.GetMonitorInfoA(self.monitors[0][0], ctypes.byref(mi))
            absleft = mi.rcWork.left
            res = user.GetMonitorInfoA(self.monitors[-1][0], ctypes.byref(mi))
            absright = mi.rcWork.right
        newleft = absleft
        newright = absright

        uFlags = win32con.SWP_ASYNCWINDOWPOS | win32con.SWP_NOACTIVATE

        if self.xmax_hist.has_key(win):
            oldr = self.xmax_hist[win]
            newleft = oldr.left
            newright = oldr.right
            del self.xmax_hist[win]
        else:
            self.xmax_hist[win] = winr
            if onlyEnd:
                uFlags |= win32con.SWP_NOMOVE
                newleft = winr.left

        newwidth = newright - newleft
        height = winr.bottom - winr.top

        res = win32gui.SetWindowPos(win, 0, newleft, winr.top, newwidth, height, uFlags)

        logging.info("xmax info: %s, %s, %s, %s, %s, %s",
                     res, winr.dump(), mi.rcWork.dump(), curwidth, newwidth, absleft)


if __name__ == "__main__":
    try:
        mover()
        pythoncom.PumpMessages()
        #msg = wintypes.MSG()
        #while user.GetMessageA(byref(msg), None, 0, 0) != 0:
        #    user.TranslateMessage(byref(msg))
        #    user.DispatchMessageA(byref(msg))
    except KeyboardInterrupt, e:
        logging.info("KeyboardInterrupt - exiting")
        exit()
    else:
        logging.info("finally")
