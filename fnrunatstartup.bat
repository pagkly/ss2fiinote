REM be\62390b b'blob 511\x00
REM shell:startup
REM shell:common startup
REM PS $env:UserName
taskkill /F /IM powershell.exe /T
taskkill /F /IM FiiNote.exe /T
if '%USERNAME%' == 'SP3' (
start /MIN "" powershell -noexit -command "echo %USERPROFILE% ; %USERPROFILE%\Documents\Docs\Automate\3WinPython-32bit-3.5.3.1Qt5\scripts\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33and.py"
start /MIN "" powershell -noexit -command "cd %USERPROFILE%\Documents\Docs\Automate\3WinPython-32bit-3.5.3.1Qt5\scripts"
) else (
REM start /MIN "" powershell -noexit -command "echo %USERPROFILE% ; %USERPROFILE%\Documents\Docs\Automate\3WinPython-64bit-3.5.3.1Qt5\scripts\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33and.py"
REM start /MIN "" powershell -noexit -command "cd %USERPROFILE%\Documents\Docs\Automate\3WinPython-32bit-3.5.3.1Qt5\scripts"
start /MIN "" powershell -noexit -command "python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33and.py"
start /MIN "" powershell -noexit -command "cd %USERPROFILE%\Documents\Docs\Automate\3WinPython-32bit-3.5.3.1Qt5\scripts"
)
start /MAX "" %USERPROFILE%\\Documents\\Docs\\Automate\\FiiNoteWINE\\FiiNote.exe

goto comment
ayumi shinoda
asahi mizuno
kurea hasumi
aika
yua mikami
shunka ayami
airi mashiro
ai uehara
tia bejean
miri mizuki
nami itoshino
shiina sora
mao hamasaki
ruri tachibana
yuki jin
momoka nishina
karen uehara
riri-houshou
xcopy C:\Users\SP3\AppData\Roaming\FiiNote\@pagkly\notes Z:\fiinote /h/i/c/k/e/r/y
#https://improve.dk/simple-file-synchronization-using-robocopy/
robocopy /MIR /Z /W:1 /R:1
robocopy C:\Users\SP3\AppData\Roaming\FiiNote\@pagkly\notes Z:\fiinote\notes /mir /z /w:5 /xc /xn /xo /FFT
/xc /xn /xo
/copyall
bookpages
 .\python C:\Users\SP3\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "C:\Users\SP3\Documents\GitHub\DocsSem2\SEM0218\MAST10005\booklet(5).pdf" -d 120 -t 1 -nc 2 -ps "9;;15+16;;23"
python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Downloads\Chem10003 GNLJ Lectures part 1.pdf" -d 120 -t 1 -nc 2
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\ECON10004\lecture 16 and 17 S2_2018.pdf" -d 120 -t 1 -nc 2
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "C:\Users\SP3\Documents\GitHub\DocsSem2\SEM0218\MAST10005\slides_master(1).pdf" -d 120 -t 1 -nc 2 -ps "197-336;;337-472;;473-"
:comment