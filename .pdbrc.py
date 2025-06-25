
_pdbrc_read = None
def _pdbrc_init():
    global _pdbrc_read
    if _pdbrc_read:
        return
    # Save history across sessions
    import os, readline
    histfile = os.path.expanduser("~/.pdb-pyhist")
    prev_h_len = None
    try:
        readline.read_history_file(histfile)
        prev_h_len = readline.get_current_history_length()
    except IOError:
        pass
    def save(prev_h_len, histfile):
        if not os.path.exists(histfile):
            readline.write_history_file(histfile)
        else:
            save_h_len = readline.get_current_history_length()
            if prev_h_len is not None:
                save_h_len -= prev_h_len
            readline.append_history_file(save_h_len, histfile)
    import atexit
    atexit.register(save, prev_h_len, histfile)
    readline.set_history_length(-1)
    _pdbrc_read = True

_pdbrc_init()
del _pdbrc_init
