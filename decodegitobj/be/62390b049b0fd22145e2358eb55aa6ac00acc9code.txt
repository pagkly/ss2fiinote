REM be\62390b b'blob 511\x00
REM shell:startup
REM shell:common startup
REM PS $env:UserName
taskkill /F /IM powershell.exe /T
taskkill /F /IM FiiNote.exe /T
start /MIN "" powershell -noexit -command "%USERPROFILE%\Documents\Docs\Automate\3WinPython-32bit-3.5.3.1Qt5\scripts\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33and.py"
start /MIN "" powershell -noexit -command "cd %USERPROFILE%\Documents\Docs\Automate\3WinPython-32bit-3.5.3.1Qt5\scripts"
start /MAX "" %USERPROFILE%\\Documents\\Docs\\Automate\\FiiNoteWINE\\FiiNote.exe