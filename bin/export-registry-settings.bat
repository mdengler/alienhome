CALL H:\bin\windate.cmd

reg export HKEY_CURRENT_USER\Software\Simontatham   H:\etc\reg\putty-defaults-reg-%V_Year%%V_Month%%V_Day%.reg
copy H:\etc\reg\putty-defaults-reg-%V_Year%%V_Month%%V_Day%.reg H:\etc\putty-defaults-reg.reg

reg export HKCU\Console                             H:\etc\reg\windows-cmdexe-bash-console-settings-%V_Year%%V_Month%%V_Day%.reg
copy H:\etc\reg\windows-cmdexe-bash-console-settings-%V_Year%%V_Month%%V_Day%.reg H:\etc\windows-cmdexe-bash-console-settings.reg

reg export HKEY_CURRENT_USER\Software\Classes\txtfile   H:\etc\reg\windows-filetypes-txtfile-HKCU-%V_Year%%V_Month%%V_Day%.reg
REM copy H:\etc\reg\windows-filetypes-txtfile-HKCU-%V_Year%%V_Month%%V_Day%.reg H:\etc\windows-filetypes-txtfile-HKCU.reg


REM SEE http://best-windows.vlaurie.com/environment-variables.html and http://support.microsoft.com/kb/104011
reg export HKEY_CURRENT_USER\Environment H:\etc\reg\windows-environment-variables-%V_Year%%V_Month%%V_Day%.reg
copy H:\etc\reg\windows-environment-variables-%V_Year%%V_Month%%V_Day%.reg H:\etc\reg\windows-environment-variables.reg