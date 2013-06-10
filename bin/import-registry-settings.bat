call H:\bin\windate.cmd
for /f "usebackq delims=|" %%f in (`dir /b "H:\etc\reg"`) do reg import "H:\etc\reg\%%f"

REM reg import   H:\etc\putty-defaults-reg.reg
REM reg import   H:\etc\windows-cmdexe-bash-console-settings.reg
REM reg import   "h:\etc\Registering Outlook 2007 to a URL Protocol.reg"
REM reg import   h:\etc\windows-filetypes-txtfile-HKCU.reg
REM reg import   h:\etc\windows-filetypes-web-HKCU.reg
