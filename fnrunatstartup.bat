REM be\62390b b'blob 511\x00
REM shell:startup
REM shell:common startup
REM PS $env:UserName
taskkill /F /IM powershell.exe /T
taskkill /F /IM FiiNote.exe /T
REM install swigwin & vbcppbuildtools
REM pip install psutil pyscreenshot pillow opencv-python pywin32 imutils PyHook3 pyautogui
if '%USERNAME%' == 'SP3' (
REM start /MIN "" powershell -noexit -command "echo %USERPROFILE% ; %USERPROFILE%\Documents\Docs\Automate\3WinPython-32bit-3.5.3.1Qt5\scripts\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33and.py"
start /MIN "" powershell -noexit -command "python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33and.py"
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
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\slides_master(1).pdf" -d 120 -t 1 -nc 2 -ps "197-336;;337-472;;473-"
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\10003_Polyzos _Lecture_7(2).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\10003_Polyzos _Lecture_8(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\10003_Polyzos _Lecture_9(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\10003_Polyzos _Lecture_10(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\10003_Polyzos _Lecture_11(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\10003_Polyzos _Lecture_12(1).pdf" -d 120 -t 1 -nc 2 ;

.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\lecture1_new(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\lecture1-2.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\lecture2_new(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\lecture3_new(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\lecture4_new(2).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\lecture5_new(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\CHEM10003\lecture6_new.pdf" -d 120 -t 1 -nc 2 ;

.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week01a.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week01b.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week01c.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week02a.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week02b.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week02c(1).pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week03a.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week03b.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week03c_guest_lecture_security.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week03c-advanced.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week04a.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week05a.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week05b.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week05c.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week06a.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week06b.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week06c.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week07c.pdf" -d 120 -t 1 -nc 2 ;
.\python %USERPROFILE%\Documents\GitHub\FN35OCVbside\FN33andlib.py -p "%USERPROFILE%\Documents\GitHub\DocsSem2\SEM0218\COMP10001\week08a.pdf" -d 120 -t 1 -nc 2 ;
:comment