@echo off
setlocal enabledelayedexpansion enableextensions
REM https://askubuntu.com/questions/61408/what-is-a-command-to-compile-and-run-c-programs
REM cd \ && cd windows\system32

:setvar
goto:EOF
:sleep
REM https://stackoverflow.com/questions/1672338/how-to-sleep-for-5-seconds-in-windowss-command-prompt-or-dos?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
echo sleep %1
set /a sleeptime=%1+1
ping 127.0.0.1 -n %sleeptime% > nul
goto:EOF

REM cl /EHsc C:\Users\user\Documents\GitHub\reinstallw10\pdftonote.cpp
echo bla
call :sleep 100