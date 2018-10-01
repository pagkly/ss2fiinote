@echo off
setlocal enabledelayedexpansion enableextensions

set xres=1680
call :dectohex xres
echo "xres=%xres%"
DisplaySwitch.exe /external
REM Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Hardware Profiles\UnitedVideo\CONTROL\VIDEO\{E8158789-5E2F-11E8-8A30-00155D006D0F}\0000\
REM Attach.ToDesktop
REM DefaultSettings.XResolution
REM DefaultSettings.YResolution
exit /B %ERRORLEVEL%

:dectohex
set /a dec=%~1
set "hex="
set "map=0123456789ABCDEF"
for /L %%N in (1,1,8) do (
    set /a "d=dec&15,dec>>=4"
    for %%D in (!d!) do set "hex=!map:~%%D,1!!hex!"
)
( ENDLOCAL & REM RETURN VALUES
    IF "%~2" NEQ "" (SET %~2=%hex%) ELSE ECHO.0x%hex%
	set %1=0x%hex%
)
goto:EOF


