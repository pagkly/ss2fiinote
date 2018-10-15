#5b\b3b5c3e922dd
#b'blob 62200\x00
#!/usr/bin/env python3
"""
ph3fn="pyhook-1.6.1-cp35-cp35m-win32.whl"
ph3downdir="\\\\$ph3fn"
ph3downlink="https://files.pythonhosted.org/packages/00/36/c08af743a671d94da7fe10ac2d078624f3efc09273ffae7b18601a8414fe/PyHook3-1.6.1-cp35-win32.whl"
curl -o "$ph3fn" "$ph3downlink"
"""
import os, signal, sys, threading
import _thread
from FN33andlib import *
from functools import partial

#https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.
#pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
#                       shell=True, preexec_fn=os.setsid) 

dir0 = os.path.dirname(os.path.realpath(__file__))
textclick=0
pause=0
is_recording=0
linuxpc=1
def Default():
    textclick=0
    pause=0
    is_recording=0
Default()
def checkdep():
    deplist=["pyautogui pyuserinput"]
    deplist.split()
    if sys.platform in ['linux', 'linux2']:
        callpip="pip3"
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        callpip="pip"
    for f in deplist:
        subprocess.call(callpip+" install "+str(f),shell=True)
#checkdep()
def MouseGetPos():
    if sys.platform in ['linux', 'linux2']:
        screenroot=display.Display().screen().root
        pointer = screenroot.query_pointer()
        data = pointer._data
        x=data["root_x"]
        y=data["root_y"]
        return x, y
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        pass

import win32api, win32con
import win32com.client as comclt
wsh=comclt.Dispatch("WScript.Shell")
"""
wsh.AppActivate("Notepad") # select another application
wsh.AppActivate("%USERPROFILE%\\Documents\\Docs\\Automate\\FiiNoteWINE\\FiiNote.exe")
focusprog("FiiNote")
"""
def mouseclick(x,y):
    time.sleep(0.1)
    x=int(x)
    y=int(y)
    if sys.platform in ['linux', 'linux2']:
        subprocess.call("xdotool mousemove "+str(x)+" "+str(y)+" click 1", shell=True)
        pass
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        pass
def dragfromto(startx,starty,stopx,stopy):
    startx=int(startx)
    starty=int(starty)
    stopx=int(stopx)
    stopy=int(stopy)
    if sys.platform in ['linux', 'linux2']:
        #subprocess.call("xdotool mousemove "+str(x)+" "+str(y)+" click 1", shell=True)
        subprocess.call("xdotool mousemove "+startx+" "+starty+" mousedown 1", shell=True)
        subprocess.call("xdotool mousemove "+stopx+" "+stopy+" mouseup 1", shell=True)
        pass
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        win32api.SetCursorPos((startx,starty))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,startx,starty,0,0)
        #time.sleep(0.9)
        win32api.SetCursorPos((stopx,stopy))
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,stopx,stopy,0,0)
        pass
def sendthiskey(thekey):
    global wsh
    time.sleep(0.1)
    if sys.platform in ['linux', 'linux2']:
        subprocess.call("xdotool "+thekey, shell=True)
        pass
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        wsh.SendKeys(str(thekey))
        pass
def FindColor():
    import pyscreenshot as ImageGrab
    from PIL import Image
    if sys.platform in ['linux', 'linux2'] :
        screenw = Home.winfo_screenwidth()
        screenh = Home.winfo_screenheight()
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        from win32api import GetSystemMetrics
        screenw=GetSystemMetrics(0)
        screenh=GetSystemMetrics(1)
    im=pyscreenshot.grab(bbox=(0,0,screenw,screenh),childprocess=False)
    for x in range(1,int(screenw)):
        for y in range(1,int(screenh)):
            px = im.getpixel((x, y))
            if px[0]>230 and px[0]<250 and px[1]>140 and px[2]>140 and px[1]<208 and px[2]<208 and px[1] == px[2]:
                pos=x,y
                #px = im.getpixel((x, y))
                print("Red="+str(pos))
                #sys.exit()
                return pos
roottrans=""
def spawntrans():
    global roottrans
    #roottrans = tk.Tk()
    roottrans=tk.Toplevel()
    if sys.platform in ['linux', 'linux2'] :
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        w=GetSystemMetrics(0)
        h=GetSystemMetrics(1)
    h=95/100*h
    starth=1.8/100*h
    #roottrans.attributes('-alpha', 0.3)
    roottrans.wm_attributes('-alpha',0.1,'-topmost',1)
    roottrans.geometry('%dx%d+%d+%d' % (w, h, 0,starth))
    roottrans.resizable(False, False)
    roottrans.update_idletasks()
    roottrans.overrideredirect(True)
def closetrans():
    global roottrans
    if roottrans:
        roottrans.destroy()
    roottrans=""
    
im=None
screengrab=True
sgrabauto=False
fnmove=False
detectred=False
rectcoordlist=[]
picdirlist=[]
if sys.platform in ['linux', 'linux2'] or sys.platform in ['Windows', 'win32', 'cygwin']:
    def mouselu(event):
        global textclick, clickStartX, clickStartY, clickStopX, clickStopY, objno2, Home,im
        global picdirlist
        rectcoordlist=[]
        
        if pause==0 and not Home:
            if sys.platform in ['linux', 'linux2']:
                clickX, clickY=MouseGetPos()
            if sys.platform in ['Windows', 'win32', 'cygwin']:
                clickX, clickY=event.Position
                #lastapp=active_window_process_name()
                #if "FiiNote.exe" in lastapp:
                #    wsh.SendKeys("^s")
            if (textclick==0):
                clickStartX, clickStartY=clickX, clickY
                print(clickStartX, clickStartY)
                TT.config(text="C")
                if screengrab or sgrabauto:
                    TT.config(text="C1")
                    #spawntrans()

                    if (linuxpc==0) and os.path.exists("/run/user/1000/gvfs/*/Internal"):
                        subprocess.call("adb shell \"su -c 'input keyevent KEYCODE_ESCAPE && sleep 0.1 && killall com.fiistudio.fiinote'\"", shell=True)
                    clickStartX, clickStartY=clickX, clickY
                    grabscreen()
                    #_thread.start_new_thread(grabscreen,())
                textclick=1
                if fnmove:
                    textclick=5
                    if detectred:
                        #sendthiskey("alt+3")
                        #sendthiskey("alt+s")
                        #mouseclick(clickStartX,clickStartY)
                        if sys.platform in ['linux', 'linux2'] :
                            sendthiskey("ctrl+x")
                            pass
                        if sys.platform in ['Windows', 'win32', 'cygwin']:
                            sendthiskey("^x")
                            pass
                    textclick=5
            elif (textclick==1):
                clickStopX, clickStopY=clickX, clickY
                print(clickStopX, clickStopY)
                clickStartX=int(clickStartX)
                clickStartY=int(clickStartY)
                clickStopX=int(clickStopX)
                clickStopY=int(clickStopY)
                TT.config(text="P")
                if screengrab or sgrabauto:
                    if clickStartX<clickStopX and clickStartY<clickStopY:
                        global curattachdirpc
                        TT.config(text="P2")
                        #SS=SS1(clickStartX,clickStartY,clickStopX,clickStopY,curattachdirpc)
                        SS=SS2(clickStartX,clickStartY,clickStopX,clickStopY,curattachdirpc)
                        print(SS)
                        newdir1=getnewdirlatest()
                        if objno2<=2:
                            if screengrab:
                                columntype="nearlatest;;firstcolumn;;firstline"
                            if sgrabauto:
                                columntype="slide1"
                                rectcoordlist=everyletter(curattachdirpc,SS[2],"contouredc"+SS[2],1000,"",withcolour=True,testing=False,wledposdir="",rectcoordlist=rectcoordlist)
                                objno2=convertjpg2note(curattachdirpc,0,newdir1,objno2,"",rectcoordlist,"")
                        if objno2>2:
                            if screengrab:
                                columntype="nearlatest;;firstcolumn;;nextline"
                            if sgrabauto:
                                with open(curnotefpc, 'rb') as f:
                                    content = f.read()
                                    cihx=str(binascii.hexlify(content).decode('utf-8'))
                                    regexc1=re.compile(patternpic)
                                    print("findpatternpic1")
                                    if regexc1.search(cihx):
                                        print("findpatternpic2")
                                        mox= re.search(patternpicx,cihx)
                                        prevxcoordinate=mox.group(5)
                                        prevycoordinate=mox.group(7)
                                        prevdefyscale=mox.group(11)
                                        prevendyscale=mox.group(13)
                                        column="exactcopyrest;;"+prevycoordinate
                                    print(str(column))
                                lastline=""
                                columntype="slidenextline"
                                rectcoordlist=everyletter(curattachdirpc,SS[2],"contouredc"+SS[2],1000,"",withcolour=True,testing=False,wledposdir="",rectcoordlist=rectcoordlist)
                                objno2=convertjpg2note(curattachdirpc,column,newdir1,objno2,"",rectcoordlist,"")
                                TT.config(text="DoneP")
                        #objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],newdir1,SS[4],columntype,rectcoordlist,"")
                        lastapp=active_window_process_name()
                        #if "FiiNote.exe" in lastapp and screengrab:
                        if "FiiNote.exe" in lastappglobal and screengrab:
                            print(lastappglobal)
                            pass
                        else:
                            objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],newdir1,SS[4],columntype,rectcoordlist,"")
                        imgdir=curattachdirpc+os.path.sep+SS[2]
                        picdirlist.append(imgdir)
                        if (linuxpc==0) and os.path.exists("/run/user/1000/gvfs/*/Internal"):
                            subprocess.call("adb push -p "+imgdir+" "+fnnotesanddirint+newdir1+".notz/attach",shell=True)
                        TT2.config(text=str(objno2))
                        ##subprocess.call("adb shell su -c 'monkey -p com.fiistudio.fiinote -c android.intent.category.LAUNCHER 1'", shell=True)
                            ## \\"su -c 'killall com.fiistudio.fiinote'\\"
                        #except :
                            ##TT.config(text="try")
                        ##monkey -p com.fiistudio.fiinote.editor.Fiinote -c android.intent.category.LAUNCHER 1
                        textclick=0
                        #closetrans()
                    else:
                        TT.config(text="Rep")
                if fnmove:
                    textclick=6
                    TT.config(text="pasting")
                    if detectred:
                        if sys.platform in ['linux', 'linux2'] :
                            #sendthiskey("alt+3 alt+s")
                            #sendthiskey("ctrl+v")
                            pass
                        if sys.platform in ['Windows', 'win32', 'cygwin']:
                            #sendthiskey("!3")
                            #sendthiskey("!s")
                            #sendthiskey("^v")
                            pass
                        time.sleep(0.5)
                        TT.config(text="lookred")
                        Redpos=FindColor()
                        if "None" in str(Redpos):
                            TT.config(text="noRed")
                        else:
                            RedX, RedY=Redpos
                            clickStartX,clickStartY=str(RedX+20),RedY
                            TT.config(text="gotRed")
                    
                        #if sys.platform in ['linux', 'linux2'] :
                        #    sendthiskey("alt+3 alt+s")
                        #if sys.platform in ['Windows', 'win32', 'cygwin']:
                        #    sendthiskey("!3")
                        #    sendthiskey("!s")
                        #time.sleep(0.3)
                    mouseclick(clickStartX,clickStartY)
                    time.sleep(0.1)
                    dragfromto(clickStartX,clickStartY,clickStopX,clickStopY)
                    textclick=0
            if fnmove:
                if textclick==5:
                    textclick=1
    def task2():
        global root,TT,TT2
        #global fnnotesdirpc
        root=tk.Tk()
        #root=tk.Toplevel()
        m = Button(root, text="Pause R", command=Suspend1,height=3,width=3)
        m.pack()
        newf = Button(root, text="New F", command=newnotz1,height=3,width=3)
        newf.pack()
        clickmodebutton = Button(root, text="clickmode", command=changeclickmode,height=3,width=3)
        clickmodebutton.pack()
        selallk = Button(root, text="selallcp", command=selallkey,height=3,width=3)
        selallk.pack()
        copyk = Button(root, text="copy", command=copykey,height=3,width=3)
        copyk.pack()
        pastek = Button(root, text="paste", command=pastekey,height=3,width=3)
        pastek.pack()
        delk = Button(root, text="delete", command=delkey,height=3,width=3)
        delk.pack()
        restartgui=Button(root, text="restart", command=restartguifn,height=3,width=3)
        restartgui.pack()
        choosepdf=Button(root, text="choosepdf", command=choosepdfguiinit,height=3,width=3)
        choosepdf.pack()
        exitall=Button(root, text="exitsc", command=quitthis,height=1,width=3)
        exitall.pack()
        rnotz=Button(root, text="rbnotz", command=rebuildnotzguiinit,height=1,width=3)
        rnotz.pack()
        rindex=Button(root, text="rbindex", command=partial(rebuildindex,fnnotesdirpc),height=1,width=3)
        rindex.pack()
        #scmtext="cto=Normal"
        #scmtext="cto=Auto"
        #scmodeb=Button(root, text=str(scmtext), command=scmodechange,height=1,width=3)
        #scmodeb.pack()
        TT=Label(root, relief='raised')
        TT.pack()
        TT2=Label(root)
        TT2.pack()
        #root.withdraw()
        if sys.platform in ['linux', 'linux2'] :
            w = root.winfo_screenwidth()
            h = root.winfo_screenheight()
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            w=GetSystemMetrics(0)
            h=GetSystemMetrics(1)
        x = w-70
        y = h-(h*1300/1440)
        wn=50
        #hn=800
        hn=int(0.7*h)
        root.wm_attributes('-alpha',0.50,'-topmost',1)
        root.geometry('%dx%d+%d+%d' % (wn, hn, x,y))
        root.resizable(False, False)
        root.update_idletasks()
        root.overrideredirect(True)
        Suspend1()
        #MainApplication(rootimgv).pack(side="top", fill="both", expand=True)
        root.mainloop()
    def pastethistoapp():
        return True
    def pastethistobend():
        return True
    def quitthis():
        global root,hm, pro
        hm.UnhookMouse()
        hm.UnhookKeyboard()
        if root:
            root.destroy()
        #os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
        sys.exit()
        exit()
        quit()
        os.exit(0)
    def restartguifn():
        global root
        root.destroy()
        root=""
        time.sleep(0.5)
        #if sys.platform in ['linux', 'linux2'] :
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            #subprocess.call("%USERPROFILE%\\Documents\\GitHub\\FN35OCVbside\\fn33andguistart.bat",shell=True)
            username=subprocess.getoutput("echo %USERNAME%")
            if username=="SP3":
                pythondir=userhomedir+"\\Documents\\Docs\\Automate\\3WinPython-32bit-3.5.3.1Qt5\\python-3.5.3\\python.exe"
                subprocess.call(pythondir+" %USERPROFILE%\\Documents\\GitHub\\FN35OCVbside\\FN33and.py",shell=True)
        time.sleep(2)
        quitthis()
        return True
    def choosepdfguiinit():
        _thread.start_new_thread(choosepdfgui,())
        #choosepdfgui()
        return True
    def ClearTT():
        TT.config(text="")
        return True
    def delkey():
        if sys.platform in ['linux', 'linux2'] :
            pass
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            import win32com.client as comclt
            wsh=comclt.Dispatch("WScript.Shell")
            #wsh.AppActivate("Notepad") # select another application
            #wsh.AppActivate("%USERPROFILE%\\Documents\\Docs\\Automate\\FiiNoteWINE\\FiiNote.exe")
            focusprog("FiiNote")
            wsh.SendKeys("%{TAB}")
            time.sleep(0.3)
            wsh.SendKeys("{DELETE}")
    def selallkey():
        if sys.platform in ['linux', 'linux2'] :
            pass
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            import win32com.client as comclt
            wsh=comclt.Dispatch("WScript.Shell")
            #wsh.AppActivate("Notepad") # select another application
            #wsh.AppActivate("%USERPROFILE%\\Documents\\Docs\\Automate\\FiiNoteWINE\\FiiNote.exe")
            focusprog("FiiNote")
            wsh.SendKeys("%{TAB}")
            time.sleep(0.3)
            wsh.SendKeys("%s")
            time.sleep(0.3)
            wsh.SendKeys("^a") # send the keys you want
            time.sleep(0.3)
            wsh.SendKeys("^c")
            
    def copykey():
        #if sys.platform in ['linux', 'linux2'] :
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            import win32com.client as comclt
            wsh=comclt.Dispatch("WScript.Shell")
            #wsh.AppActivate("Notepad") # select another application
            #wsh.AppActivate("%USERPROFILE%\\Documents\\Docs\\Automate\\FiiNoteWINE\\FiiNote.exe")
            focusprog("FiiNote")
            wsh.SendKeys("%{TAB}")
            time.sleep(0.3)
            wsh.SendKeys("^c") # send the keys you want
    def pastekey():
        #if sys.platform in ['linux', 'linux2'] :
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            import win32com.client as comclt
            wsh=comclt.Dispatch("WScript.Shell")
            #wsh.AppActivate("%USERPROFILE%\\Documents\\Docs\\Automate\\FiiNoteWINE\\FiiNote.exe")
            #focusprog("Atom")
            focusprog("FiiNote")
            wsh.SendKeys("%{TAB}")
            time.sleep(0.3)
            wsh.SendKeys("^v") # send the keys you want
    clickmode=0
    def changeclickmode():
        global screengrab, sgrabauto, fnmove,TT,textclick,clickmode
        clickmode+=1
        if clickmode==1:
            screengrab=False
            sgrabauto=True
            fnmove=False
            TT.config(text="sgrabauto")
        elif clickmode==2:
            screengrab=False
            sgrabauto=False
            fnmove=True
            TT.config(text="fnmove")
        elif clickmode>2 or clickmode==0:
            clickmode=0
            screengrab=True
            sgrabauto=False
            fnmove=False
            TT.config(text="scrngrab")
            
        """
        if screengrab and not fnmove:
            screengrab=False
            fnmove=True
            TT.config(text="fnmove")
        elif fnmove and not screengrab:
            screengrab=True
            fnmove=False
            TT.config(text="scrngrab")
        """
        textclick=0

    import win32api
    from win32con import *
    import win32com.client as comclt
    wsh=comclt.Dispatch("WScript.Shell")
    nircmddir="%USERPROFILE%\\Documents\\GitHub\\FN35OCVbside\\others\\nircmd-x64\\nircmdc.exe"
    from pynput.mouse import Button, Controller
    mouse = Controller()
    lastappglobal=""
    def Suspend1():
        global pause, textclick, screengrab
        global picdirlist
        global lastappglobal
        fnpicmode=False
        countscroll=0
        if pause==0:
            pause=1
            TT.config(text="Suspended")
            fiinotew10pcdir=userhomedir+"\\\\Documents\\\\Docs\\\\Automate\\\\FiiNoteWINE\\\\FiiNote.exe"
            closetrans()
            if sys.platform in ['Windows', 'win32', 'cygwin'] and screengrab:
                #restartfn()
                if picdirlist:
                    print("Copying picdirlist...")
                    for picdir in picdirlist:
                        #https://superuser.com/questions/372602/how-to-copy-picture-from-a-file-to-clipboard
                        print(nircmddir+" clipboard copyimage "+picdir)
                        subprocess.call(nircmddir+" clipboard copyimage "+picdir, shell=True)
                        lastapp=active_window_process_name()
                        if "FiiNote.exe" in lastapp:
                            #scrolldown
                            if not fnpicmode:
                                focusprog("FiiNote")
                                #sendthiskey("%{TAB}")
                                sendthiskey("%3")
                                sendthiskey("%s")
                                if len(picdirlist)>2:
                                    #sendthiskey("^{=}^{=}^{=}^{=}^{=}^{=}^{=}^{=}^{=}^{=}^{=}^{=}^{=}^{=}^{=}")
                                    
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    sendthiskey("^{=}")
                                    
                                fnpicmode=True
                            #win32api.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, -15, 0)
                            #mouse.scroll(0, 20)
                            sendthiskey("{DOWN}")
                            sendthiskey("^v")
                            time.sleep(0.1)
                            countscroll+=1
                    for f in range(countscroll):
                        #win32api.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, 15, 0)
                        sendthiskey("{UP}")
                        #mouse.scroll(0, -20)
                        pass
                    if len(picdirlist)>2:
                        sendthiskey("^{-}{-}{-}{-}{-}{-}{-}{-}{-}{-}{-}{-}{-}{-}{-}")
                        
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        sendthiskey("^{-}")
                        
                    picdirlist=[]
                pass
        elif pause==1:
            pause=0
            TT.config(text="Resume")
            if sys.platform in ['Windows', 'win32', 'cygwin'] and screengrab:
                picdirlist=[]
                lastapp=active_window_process_name()
                lastappglobal=lastapp
                if "FiiNote.exe" in lastapp:
                    wsh.SendKeys("^s")
                    
                    #subprocess.call("taskkill /F /IM FiiNote.exe /T",shell=True)
                pass
                spawntrans()
        textclick=0
    def wlstatus():
        global wlareastatus
        if wlareastatus==True:
            wlareastatus=False
            TT.config(text="wl=off")
        elif wlareastatus==False:
            wlareastatus=True
            TT.config(text="wl=on")
    def newnotz1():
        global newdir1,objno2
        #newnotz0()
        #print(curnotzpc,curnotefpc,curattachdirpc,curnotzand,curattachdirand)
        newdir1,objno2=newnotz(fnnotesdirpc,fnnotesdirpc)
        TT2.config(text="NEW")
    def term(scriptn):
        if sys.platform in ['linux', 'linux2'] :
            python_path=""
            subprocess.call("python3 "+str(dir0)+"/"+str(scriptn)+".py", shell=True)
            print(python_path+"sudo python3 "+str(dir0)+"/"+scriptn)
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            python_path=dir0+os.path.sep+"WinPython-32bit-3.5.3.1Qt5"+os.path.sep+"scripts"+os.path.sep
            subprocess.call(python_path+"python "+str(dir0)+"\\"+str(scriptn)+".py", shell=True)
            return True

def choosepdfgui0():
    global rootimgv,Top,Mid,mfwidth,mfheight
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        userhomedir=subprocess.getoutput("echo %USERPROFILE%")
    #rootimgv = tk.Tk()
    rootimgv=tk.Toplevel()
    width = 600
    height = 300
    screen_width = rootimgv.winfo_screenwidth()
    screen_height = rootimgv.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    rootimgv.geometry("%dx%d+%d+%d" % (width, height, x, y))
    rootimgv.resizable(0, 0)
    #================================FRAMES=========================================
    mfwidth=500
    mfheight=200
    Top = Frame(rootimgv, width=mfwidth, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    Mid = Frame(rootimgv, width=mfwidth, height=mfheight, bd=1, relief=SOLID)
    Mid.pack_propagate(0)
    Mid.pack(pady=20)
    lbl_title = Label(Top, text="Python: Simple Image Viewer", width=mfwidth, font=("arial", 20))
    lbl_title.pack(fill=X)
    allfilesdir,allfilesname,allfilesfulldir=listfilesext(dir0,".pdf")
    placebutton(allfilesdir,allfilesname,allfilesfulldir)
    #rootimgv.mainloop()
def choosepdfgui():
    global Top,Mid,mfwidth,mfheight,Home1
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        userhomedir=subprocess.getoutput("echo %USERPROFILE%")
    Home1=Toplevel()
    width = 600
    height = 800
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home1.resizable(0, 0)
    #================================FRAMES=========================================
    mfwidth=600
    mfheight=800
    Top = Frame(Home1, width=mfwidth, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    Mid = Frame(Home1, width=mfwidth, height=mfheight, bd=1, relief=SOLID)
    Mid.pack_propagate(0)
    Mid.pack(pady=20)
    lbl_title = Label(Top, text="Python: Simple Image Viewer", width=mfwidth, font=("arial", 20))
    lbl_title.pack(fill=X)
    allfilesdir,allfilesname,allfilesfulldir=listfilesext(dir0,".pdf")
    placebutton(allfilesdir,allfilesname,allfilesfulldir,Top,Mid)
#https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
#https://www.sourcecodester.com/tutorials/python/12128/python-simple-image-viewer.html
#================================METHODS========================================
def changepage(pdfdir,pdfname,lastpage,ptype):
    global Home1,Home,panel,panel1
    if panel1:
        panel1.destroy()
    if panel:
        panel.destroy()
    if ptype=="prev":
        choosepage=int(lastpage)-1
    elif ptype=="next":
        choosepage=int(lastpage)+1
    print("lpcp="+str(choosepage))
    DisplayImage(pdfdir,pdfname,choosepage,[])
    return True
def choosepageguiinit(pdfdir,pdfname):
    _thread.start_new_thread(partial(choosepagegui,pdfdir,pdfname),())
def choosepagegui(pdfdir,pdfname):
    def show_entry_fields():
        print("First Name: %s" % (e1.get()))
        choosepage=int(e1.get())
        DisplayImage(pdfdir,pdfname,choosepage,[])
    print(pdfdir+" "+pdfname)
    Home2=Toplevel()
    Label(Home2, text="Page").grid(row=0)
    e1 = Entry(Home2)
    e1.grid(row=0, column=1)
    Button(Home2, text='Show', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)

def rebuildnotzguiinit():
    _thread.start_new_thread(rebuildnotzgui,())
def rebuildnotzgui():
    global curattachdirpc
    def show_entry_fields():
        global curattachdirpc,objno2
        print("Attachdir: %s" % (e1.get()))
        attachdir=str(e1.get())
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            #attachdirfix=re.sub(r"\\\\","\\\\",attachdir)
            attachdirfix=attachdir
        else:
            attachdirfix=attachdir
        print(attachdirfix)
        newnotz1()
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(attachdirfix) if isfile(join(attachdirfix, f))]
        for files in onlyfiles:
            picname=files
            oldimgdir=attachdirfix+os.path.sep+files
            newimgdir=curattachdirpc+os.path.sep+files
            print("capc="+curattachdirpc,"obj2="+str(objno2),oldimgdir,newimgdir)
            shutil.copy(oldimgdir,newimgdir)
            w, h=imgsize(newimgdir)
            objno2,curattachdirpc=appendnewpic(w,h,picname,newdir1,objno2,"nearlatest")
    Home2=Toplevel()
    Label(Home2, text="AttachDir").grid(row=0)
    e1 = Entry(Home2)
    e1.grid(row=0, column=1)
    Button(Home2, text='Rebuild', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
def whitelistpagearea(page,x,y):
    import cv2
    return True
def progresspage(page):
    return True
def progresspagewhitelist():
    return True
def perccolor(imgdir):
    #https://stackoverflow.com/questions/43167867/color-percentage-in-image-python-opencv-using-histogram
    import numpy as np
    import cv2
    img = cv2.imread(imgdir)
    brown = [145, 80, 40]  # RGB
    diff = 20
    boundaries = [([brown[2]-diff, brown[1]-diff, brown[0]-diff],
                   [brown[2]+diff, brown[1]+diff, brown[0]+diff])]
    # in order BGR as opencv represents images as numpy arrays in reverse order
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(img, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)

        ratio_brown = cv2.countNonZero(mask)/(img.size/3)
        #print('brown pixel percentage:', np.round(ratio_brown*100, 2))

        cv2.imshow("images", np.hstack([img, output]))
        cv2.waitKey(0)

###bindkeyboardandmouse
  ###http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
  ##Example:http://www.java2s.com/Code/Python/Event/MouseeventsonaframeMouseclickedposition.htm
  ##https://www.daniweb.com/programming/software-development/threads/364829/mouse-position-tkinter
  ##class:https://stackoverflow.com/questions/3288047/how-do-i-get-mouse-position-relative-to-the-parent-widget-in-tkinter
#https://www.reddit.com/r/learnpython/comments/gwrig/questions_about_getting_mouse_coordinates_in/
#https://bytes.com/topic/python/answers/888796-how-get-x-coordinate-image
#https://stackoverflow.com/questions/38428593/getting-the-absolute-position-of-cursor-in-tkinter
#https://www.quora.com/In-Python-using-Tkinter-how-can-I-get-the-mouse-position-on-the-screen
#print root.winfo_pointerxy()
xpos1=""
ypos1=""
xpos2=""
ypos2=""
prevx1=""
prevx2=""
prevy1=""
prevy2=""
def gettkinterxypos(eventorigin,convimgdir,wledimgdir,pdfdir,pdfname,lastpage,anglecorrection,imgw,imgh,showimgw,showimgh):
    global pause,textclick,wlareastatus
    print(str(pause)+" "+str(textclick))
    def callback():
        global root
        global textclick,pause,xpos1,ypos1,xpos2,ypos2
        global prevx1,prevx2,prevy1,prevy2
        global newdir1,objno2,curattachdirpc
        global Home
        global xcorrection,ycorrection
        xcorrection=0
        ycorrection=0
        xandy=False
        if pause==0 and textclick==0:
            xpos1=eventorigin.x
            ypos1=eventorigin.y
            print(str(xpos1)+" "+str(ypos1))
            textclick=1
        elif pause==0 and textclick==1:
            xpos2=eventorigin.x
            ypos2=eventorigin.y
            print(str(xpos2)+" "+str(ypos2))
            if os.path.exists(wledimgdir):
                global screenw,screenh
                if screenw==1920 and screenh==1080:
                    ycorrection=10
                else:
                    #ycorrection=20
                    ycorrection=0
                if anglecorrection==270:
                    if ypos1>ypos2 and xpos2>xpos1:
                        xpos1ac=imgw-ypos1
                        xpos2ac=imgw-ypos2
                        ypos1ac=xpos1
                        ypos2ac=xpos2
                        xcorrection=60
                        ycorrection=0
                        xandy=True
                    elif ypos2>ypos1 and xpos2>xpos1:
                        xpos1ac=imgw-ypos2
                        xpos2ac=imgw-ypos1
                        ypos1ac=xpos1
                        ypos2ac=xpos2
                        xcorrection=60
                        ycorrection=0
                    else:
                        print("trya")
                        return True
                    actxp1=int(imgw/showimgw*xpos1ac)+xcorrection
                    actyp1=int(imgh/showimgh*ypos1ac)+ycorrection
                    actxp2=int(imgw/showimgw*xpos2ac)+xcorrection
                    actyp2=int(imgh/showimgh*ypos2ac)+ycorrection
                else:
                    if screenh>screenw:
                        ycorrection=0
                    print(ycorrection)
                    xpos1ac=xpos1
                    xpos2ac=xpos2
                    ypos1ac=ypos1
                    ypos2ac=ypos2
                    actxp1=int(imgw/showimgw*xpos1ac)+xcorrection
                    actyp1=int(imgh/showimgh*ypos1ac)+ycorrection
                    actxp2=int(imgw/showimgw*xpos2ac)+xcorrection
                    actyp2=int(imgh/showimgh*ypos2ac)+ycorrection
                print(actxp1,actxp2,actyp1,actyp2)
            if (actxp2>actxp1 and actyp2>actyp1) or xandy:
                SS=cutarea(pdfdir,pdfname,lastpage,actxp1,actyp1,actxp2,actyp2,convimgdir,anglecorrection)
                print(SS)
                if objno2<=2:
                    objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],SS[3],SS[4],"nearlatest;;firstcolumn;;firstline")
                if objno2>2:
                    if prevx1 and actxp1>prevx1 and (actyp1 in range(prevy1-50,prevy1+50)):
                        objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],SS[3],SS[4],"nearlatest;;nextcolumn;;sameline")
                    elif prevx1 and actyp1>prevy1:
                        objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],SS[3],SS[4],"nearlatest;;firstcolumn;;nextline")
                    else:
                        objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],SS[3],SS[4],"nearlatest;;firstcolumn;;sameline")
                #objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],SS[3],SS[4],"nearlatest")
                imgdir=curattachdirpc+os.path.sep+SS[2]
                if (linuxpc==0) and os.path.exists("/run/user/1000/gvfs/*/Internal"):
                    subprocess.call("adb push -p "+imgdir+" "+fnnotesanddirint+newdir1+".notz/attach",shell=True)
                    ##subprocess.call("adb shell su -c 'monkey -p com.fiistudio.fiinote -c android.intent.category.LAUNCHER 1'", shell=True)
                    ## \"su -c 'killall com.fiistudio.fiinote'\"w
                    #except :
                    ##TT.config(text="try")
                    ##monkey -p com.fiistudio.fiinote.editor.Fiinote -c android.intent.category.LAUNCHER 1
                TT.config(text="P")
                TT2.config(text=str(objno2))
                if wlareastatus:
                    loadimg=whitelistarea(pdfdir,pdfname,lastpage,actxp1,actyp1,actxp2,actyp2,wledimgdir)
                    DisplayImage(pdfdir,pdfname,lastpage,loadimg)
                prevx1,prevx2,prevy1,prevy2=actxp1,actxp2,actyp1,actyp2
            else:
                TT.config(text="Rep")
                textclick=0
                pass
            textclick=0
        else:
            textclick=0
            pass
        print("objno2="+str(objno2))
    callback()
    return True
def cutarea(pdfdir,pdfname,lastpage,actxp1,actyp1,actxp2,actyp2,convimgdir,anglecorrection):
    global curattachdirpc,newdir1,objno2
    picname=strftime("%Y%m%d%H%M%S")+'abcdefghijklmno.jpg'
    imgdir=curattachdirpc+os.path.sep+picname
    print(convimgdir)
    print(imgdir)
    print(str(actyp1)+" "+str(actyp2)+","+str(actxp1)+":"+str(actxp2))
    temp=cv2.imread(convimgdir)
    img=temp[actyp1:actyp2,actxp1:actxp2]
    cv2.imwrite(imgdir,img)
    w,h=imgsize(imgdir)
    print(str(w)+" "+str(h))
    print(newdir1+" "+str(objno2))
    return w,h,picname,newdir1,objno2
def whitelistarea(pdfdir,pdfname,lastpage,actxp1,actyp1,actxp2,actyp2,wledimgdir):
    convimgdir=re.sub(r"wled","conv",wledimgdir)
    image=cv2.imread(wledimgdir)
    #imgh,imgw,channels=image.shape
    #load2=np.zeros((imgh,imgw,4))
    cv2.rectangle(image, (actxp1, actyp1), (actxp2, actyp2), white_color, -1)
    #cv2.imwrite(wledimgdir, image)
    #src=cv2.imread(wledimgdir)
    src=image
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    cv2.imwrite(wledimgdir, dst)
    print("donewlarea="+wledimgdir)
    wledposfile=re.sub(r"wled","wledpos",wledimgdir)
    wledposfile=re.sub(r"(.jpg|.png)","",wledposfile)
    appendpos=str(actxp1)+","+str(actyp1)+","+str(actxp2)+","+str(actyp2)
    print(appendpos)
    appendtext(wledposfile,appendpos,"a")
    return dst

def removelastlinefromfile(thefile):
    #sys.argv[1]
    file = open(thefile, "r+", encoding = "utf-8")
    #Move the pointer (similar to a cursor in a text editor) to the end of the file.
    file.seek(0, os.SEEK_END)
    #This code means the following code skips the very last character in the file -
    #i.e. in the case the last line is null we delete the last line
    #and the penultimate one
    pos = file.tell() - 1
    #Read each character in the file one at a time from the penultimate
    #character going backwards, searching for a newline character
    #If we find a new line, exit the search
    while pos > 0 and file.read(1) != "\n":
        pos -= 1
        file.seek(pos, os.SEEK_SET)
    #So long as we're not at the start of the file, delete all the characters ahead of this position
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()
    file.close()
#https://mail.python.org/pipermail/python-list/2005-January/315395.html
def awk_it(instring,index,delimiter):
  try:
    return [instring,instring.split(delimiter)[index-1]][max(0,min(1,index))]
  except:
    return ""
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
#https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv
def undolatestwl(pdfdir,pdfname,convimgdir,wledimgdir,lastpage):
    global Home
    #imgtype="png"
    #Home.destroy()
    #wledimgdir=re.sub(r"conv","wled",convimgdir)
    wledposfile=re.sub(r"conv","wledpos",convimgdir)
    wledposfile=re.sub(r"(.jpg|.png)","",wledposfile)
    with open(wledposfile, 'r') as f:
        try:
            lines = f.read().splitlines()
            last_line = lines[-1]
            print("lastline="+last_line)
        except:
            last_line=""
    if last_line!="" :
        temp = cv2.imread(convimgdir)
        ypos1=int(awk_it(last_line,2,","))
        ypos2=int(awk_it(last_line,4,","))
        xpos1=int(awk_it(last_line,1,","))
        xpos2=int(awk_it(last_line,3,","))
        img=temp[ypos1:ypos2+3,xpos1:xpos2+3]
        target=cv2.imread(wledimgdir)
        if ".png" in wledimgdir:
            print("png",str(xpos1),str(xpos2),str(ypos1),str(ypos2))
            src=target
            cv2.rectangle(src, (xpos1, ypos1), (xpos2+3, ypos2+3), black_color, -1)
            tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
            b, g, r = cv2.split(src)
            rgba = [b,g,r, alpha]
            dst = cv2.merge(rgba,4)
            cv2.imwrite(wledimgdir, dst)
        if ".jpg" in wledimgdir:
            target[ypos1:ypos2+3,xpos1:xpos2+3]=img
        #imgwled=re.sub("wled","img",wledimgdir)
        #newwled=re.sub("wled","newwled",wledimgdir)
        #cv2.imwrite(imgwled,img)
        #cv2.imwrite(newwled, target)
            cv2.imwrite(wledimgdir, target)

        file = open(wledposfile)
        filetext=file.read()
        newwledpos=re.sub("\n"+last_line,"",str(filetext))
        print("readf="+str(filetext),"nwwpos="+newwledpos)
        appendtext(wledposfile,newwledpos,"w+")
        #removelastlinefromfile(wledposfile)
    DisplayImage(pdfdir,pdfname,lastpage,[])
    return True
    
Home=""
choosepdfpagenext=""
choosepdfpageprev=""
undowlarea=""
cpageg=""
wlbutton=""
rootimgv=""
pdfdir=""
pdfname=""
pdfdir0=""
pdfname0=""
lastpage=""
load=None
imgh=None
imgw=None
panel=None
panel1=None
touchpanel=None
screenw=None
screenh=None
loadimg=None
prevlastpage=None
wlareastatus=True
black_color= (0, 0, 0, 255)
white_color= (255, 255, 255, 255)
red_color = (0, 0, 255, 255)
green_color = (0, 255, 0, 255)
blue_color = (255, 0, 0, 255)
convpdfdirpc=dir0+os.path.sep+"ConvertedPDF"
import imutils
from array import array
def DisplayImage(pdfdir,pdfname,choosepage,loadimg0,*args,**kwargs):
    global root,hm
    global Home1,Home,panel,panel1,touchpanel,pdfdir0,pdfname0,lastpage,convimgdir
    global screenw,screenh,load
    global imgh,imgw
    global prevlastpage
    from FN33andlib import conwindirtovwsldir,convertpdf2jpg2
    #imgdir=convpdfdirpc+os.path.sep+"29.pdf"+os.path.sep+"conv0001.jpg"
    #================================FRAMES=========================================
    pdfdir0=pdfdir
    pdfname0=pdfname
    imgtype="png"
    if Home1:
        Home1.destroy()
        Home1=""
    if panel1:
        panel1.destroy()
        panel1=""
    #if touchpanel:
    #    touchpanel.destroy()
    #    touchpabel=""
    convpdfdirpcwithpdf=convpdfdirpc+os.path.sep+pdfname
    if not choosepage:
        if os.path.exists(convpdfdirpcwithpdf):
            choosepage=curpage(pdfname,convpdfdirpcwithpdf)
            if not choosepage:
                choosepage=1
        else:
            choosepage=1
    lastpage=choosepage
    prevpage=lastpage-1
    nextpage=lastpage+1
    if prevpage>0:
        prevconvpname,previmgdir=convertpdf2jpg2(pdfdir,pdfname,120,prevpage,convpdfdirpcwithpdf,"")
    nextconvpname,nextimgdir=convertpdf2jpg2(pdfdir,pdfname,120,nextpage,convpdfdirpcwithpdf,"")

    convpname,convimgdir=convertpdf2jpg2(pdfdir,pdfname,120,choosepage,convpdfdirpcwithpdf,"")
    wledimgdir=re.sub(r"conv","wled",convimgdir)
    wledimgdir=re.sub(r".jpg","."+imgtype,wledimgdir)
    #imgdir=convimgdir
    imgdir0=convimgdir

    #try:
    #    loadimg=loadimg0
    #    load=loadimg
    #    imgh, imgw, channels = load.shape
    #except NameError:
    #    load=cv2.imread(convimgdir)
    #    imgh, imgw, channels = load.shape
    #    print('a does not exist.')
    #except AttributeError:
    #    load=cv2.imread(convimgdir)
    #    imgh, imgw, channels = load.shape
    #    print('a does not have a shape property.')

    #if not imgh:
    if prevlastpage!=lastpage:
        load=cv2.imread(convimgdir)
        imgh, imgw, channels = load.shape
    print(str(convimgdir),str(imgw))
    if not os.path.exists(wledimgdir):
        if imgtype=="jpg":
            shutil.copy(convimgdir,wledimgdir)
        if imgtype=="png":
            #size = imgw, imgh, 4
            #load1 = np.zeros(size, dtype=np.uint8)
            load1=np.zeros((imgh,imgw,4))
            load2=np.zeros((imgh,imgw,4))
            cv2.rectangle(load1, (0, 0), (0, 0), white_color, 5)
            cv2.rectangle(load2, (0, 0), (0, 0), white_color, 5)
            res = load1[:] #copy the first layer into the resulting image
            #copy only the pixels we were drawing on from the 2nd and 3rd layers
            #(if you don't do this, the black background will also be copied)
            cnd = load2[:, :, 3] > 0
            res[cnd] = load2[cnd]
            cv2.imwrite(wledimgdir, res)
    if os.path.exists(wledimgdir):
        #imgdir=wledimgdir
        imgdir1=wledimgdir
        print(imgdir1)
        load1=cv2.imread(imgdir1)
        if imgtype=="png":
            src=load1
            tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
            b, g, r = cv2.split(src)
            rgba = [b,g,r, alpha]
            load1 = cv2.merge(rgba,4)
    print(imgdir1+" "+str(lastpage))
    
    if sys.platform in ['linux', 'linux2'] :
        screenw = Home.winfo_screenwidth()
        screenh = Home.winfo_screenheight()
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        from win32api import GetSystemMetrics
        screenw=GetSystemMetrics(0)
        screenh=GetSystemMetrics(1)
        hm.UnhookMouse()
    
    #load=PIL.Image.open(open(imgdir, 'rb'))
    #imgw, imgh = load.size
    print(imgw,imgh)
    global showimgw,showimgh
    showimgw=int(((screenh/imgh)*imgw)*95/100)
    showimgh=int(screenh*95/100)
    if screenw>screenh and imgh>imgw and screenw==2160 and screenh==1440:
        anglecorrection=270
        if prevlastpage!=lastpage:
            load=imutils.rotate_bound(load, anglecorrection)
        load1=imutils.rotate_bound(load1, anglecorrection)
        screenh=screenh-100
        screenw=screenw-100
        showimgwb=int((screenh/imgw)*imgh)
        showimghb=int(screenh)
        showimgw=showimghb
        showimgh=showimgwb
        x = (screenw/2) - (showimgwb/2)
        y = (screenh/2) - (showimghb/2)
    else:
        anglecorrection=0
        screenh=screenh
        showimgwb=showimgw
        showimghb=showimgh
        x = (screenw/2) - (showimgwb/2)
        y = (screenh/2) - (showimghb/2)-50
    if screenh>screenw and imgh>imgw:
        anglecorrection=0
        #screenh=2160-100
        #screenw=1440-100
        screenh=screenh-100
        screenw=screenw-100
        showimgw=int(screenw)
        showimgh=int((screenw/imgw)*imgh)
        showimgwb=showimgw
        showimghb=showimgh
        x = (screenw/2) - (showimgwb/2)
        y = (screenh/2) - (showimghb/2)
        print(screenw,screenh)
        print(showimgw,showimgh)

    #load[load[:, :, 1:].all(axis=-1)] = 0
    #load1[load1[:, :, 1:].all(axis=-1)] = 0
    #dst = cv2.addWeighted(load, 1, load1, 1, 0)
    if not Home:
        print("not home")
        Home=Toplevel()
        Home.geometry("%dx%d+%d+%d" % (showimgwb, showimghb, x,y))
        Home.resizable(1, 1)
        pass
    else:
        print("home exists")
        pass
    #Home.geometry("%dx%d+%d+%d" % (showimgwb, showimghb, x,y))
    #Home.resizable(1, 1)
    Home.title(str(choosepage))
    #render = PIL.ImageTk.PhotoImage(load)
    # Convert the Image object into a TkPhoto object
    if imgtype=="jpg":
        im = PIL.Image.fromarray(load1)
        load = im.resize((showimgwb, showimghb), PIL.Image.ANTIALIAS)
        render = PIL.ImageTk.PhotoImage(image=load)
        panel = Label(Home,border=0,image=render)
        panel.image=render
        panel.bind("<Button 1>",partial(gettkinterxypos,convimgdir=convimgdir,wledimgdir=wledimgdir,pdfdir=pdfdir,pdfname=pdfname,lastpage=lastpage,anglecorrection=anglecorrection,imgw=imgw,imgh=imgh,showimgw=showimgw,showimgh=showimgh))
        #panel.pack(fill=BOTH, expand=YES)
        panel.place(relx=0.0, rely=1.0, anchor='sw')
    if imgtype=="png":
        if prevlastpage!=lastpage:
            im = PIL.Image.fromarray(load)
            load = im.resize((showimgwb, showimghb), PIL.Image.ANTIALIAS)
        im1 = PIL.Image.fromarray(load1)
        load1 = im1.resize((showimgwb, showimghb), PIL.Image.ANTIALIAS)
        load2=load
        load2.paste(load1,(0,0),load1)
        render1 = PIL.ImageTk.PhotoImage(image=load2)
        panel1 = Label(Home,border=0, image=render1)
        panel1.image=render1
        panel1.bind("<Button 1>",partial(gettkinterxypos,convimgdir=convimgdir,wledimgdir=wledimgdir,pdfdir=pdfdir,pdfname=pdfname,lastpage=lastpage,anglecorrection=anglecorrection,imgw=imgw,imgh=imgh,showimgw=showimgw,showimgh=showimgh))
        #panel1.pack(fill=BOTH, expand=YES)
        panel1.place(relx=0.0, rely=1.0, anchor='sw')
    #touchpanel=Label(Home,border=0)
    #touchpanel.bind("<Button 1>",partial(gettkinterxypos,convimgdir=convimgdir,wledimgdir=wledimgdir,pdfdir=pdfdir,pdfname=pdfname,lastpage=lastpage,anglecorrection=anglecorrection,imgw=imgw,imgh=imgh,showimgw=showimgw,showimgh=showimgh))
    ##touchpanel.pack(fill=BOTH, expand=YES)
    #touchpanel.place(relx=0.0, rely=1.0, anchor='sw')
    
    def callbackhome():
        return True
    def callbackhome1():
        global choosepdfpagenext,choosepdfpageprev,undowlarea,cpageg,wlbutton,lastpage,convimgdir
        if choosepdfpagenext:  
            choosepdfpagenext.destroy()
        if choosepdfpageprev:
            choosepdfpageprev.destroy()
        if undowlarea:
            undowlarea.destroy()
        if cpageg:
            cpageg.destroy()
        if wlbutton:
            wlbutton.destroy()
        choosepdfpagenext=Button(root, text="Page+1", command=partial(changepage,pdfdir,pdfname,lastpage,"next"),height=1,width=3)
        choosepdfpagenext.pack()
        choosepdfpageprev=Button(root, text="Page-1", command=partial(changepage,pdfdir,pdfname,lastpage,"prev"),height=1,width=3)
        choosepdfpageprev.pack()
        cpageg=Button(root, text="cpage", command=partial(choosepageguiinit,pdfdir,pdfname),height=1,width=3)
        cpageg.pack()
        wlbutton=Button(root, text="wlmode", command=wlstatus,height=1,width=3)
        wlbutton.pack()
        undowlarea=Button(root, text="undolwl", command=partial(undolatestwl,pdfdir,pdfname,convimgdir,wledimgdir,lastpage),height=1,width=3)
        undowlarea.pack()
        #scbutton=Button(root, text="scmode", command=partial(convertthispage,),height=1,width=3)
        #scbutton.pack()
        #alldetextbutton=Button(root, text="alldetext", command=partial(detextthispage),height=1,width=3)
        #alldetextbutton.pack()
    #root.after_idle(callbackhome)
    root.after_idle(callbackhome1)
    prevlastpage=None
    return True
def detextthispage():
    subprocess.call("",shell=True)
    restartfn()
    return True

#https://stackoverflow.com/questions/5436810/adding-zooming-in-and-out-with-a-tkinter-canvas-widget
class GUI:
    def __init__(self, root):
        # ... omitted rest of initialization code
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        self.scale = 1.0
        self.orig_img = PIL.Image.open(File)
        self.img = None
        self.img_id = None
        # draw the initial image at 1x scale
        self.redraw()
        # ... rest of init, bind buttons, pack frame
    def zoom(self,event):
        if event.num == 4:
            self.scale *= 2
        elif event.num == 5:
            self.scale *= 0.5
        self.redraw(event.x, event.y)
    def redraw(self, x=0, y=0):
        if self.img_id:
            self.canvas.delete(self.img_id)
        iw, ih = self.orig_img.size
        size = int(iw * self.scale), int(ih * self.scale)
        self.img = PIL.ImageTk.PhotoImage(self.orig_img.resize(size))
        self.img_id = self.canvas.create_image(x, y, image=self.img)
        # tell the canvas to scale up/down the vector objects as well
        self.canvas.scale(ALL, x, y, self.scale, self.scale)

#https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
def listfilesext(dir,ext):
    allfilesdir=[]
    allfilesname=[]
    allfilesfulldir=[]
    for file in os.listdir(dir):
        if file.endswith(ext):
            #and os.path.isfile(os.path.join(dir, file))
            #os.path.isdir("bob")
            allfilesdir.append(dir)
            allfilesname.append(file)
            allfilesfulldir.append(os.path.join(dir, file))
    print(allfilesfulldir)
    return allfilesdir,allfilesname,allfilesfulldir
#https://stackoverflow.com/questions/10927234/setting-the-position-on-a-button-in-python
#https://stackoverflow.com/questions/10865116/python-tkinter-creating-buttons-in-for-loop-passing-command-arguments
def placebutton(allfilesdir,allfilesname,allfilesfulldir,Top,Mid):
    x=len(allfilesfulldir)
    value=int(x)
    bwidth=500
    bheight=25
    for i in range(value):
        print(allfilesdir[i])
        print(allfilesname[i])
        #b=Button(Mid,text=allfilesfulldir[i],command=lambda: DisplayImage(allfilesdir[i],allfilesname[i]))
        b=Button(Mid,text=allfilesfulldir[i],command=partial(DisplayImage,allfilesdir[i],allfilesname[i],"",[]))
        b.place(x=mfwidth/2-bwidth/2, y=i*30, width=bwidth, height=bheight)
def lastmodfile(num_files, directory):
    import os,stat
    import datetime as dt
    from pprint import pprint
    """gets a list of files sorted by modified time
    keyword args:
    num_files -- the n number of files you want to print
    directory -- the starting root directory of the search"""
    modified = []
    accessed = []
    rootdir = os.path.join(os.getcwd(), directory)
    print("dir="+ directory)
    for root, sub_folders, files in os.walk(rootdir):
        for file in files:
            try:
                unix_modified_time = os.stat(os.path.join(root, file))[stat.ST_MTIME]
                unix_accessed_time = os.stat(os.path.join(root, file))[stat.ST_ATIME]
                human_modified_time = dt.datetime.fromtimestamp(unix_modified_time).strftime('%Y-%m-%d %H:%M:%S')
                human_accessed_time = dt.datetime.fromtimestamp(unix_accessed_time).strftime('%Y-%m-%d %H:%M:%S')
                filename = os.path.join(root, file)
                modified.append((human_modified_time, filename))
                accessed.append((human_accessed_time, filename))
            except:
                pass
    modified.sort(key=lambda a: a[0], reverse=True)
    accessed.sort(key=lambda a: a[0], reverse=True)
    print('Modified')
    print(modified[0][1])
    #print('Accessed')
    #pprint(accessed[:num_files])
    return modified[0][1]
def curpage(pdfname,convpdfdirpc):
    print("curcpdfpc="+convpdfdirpc)
    if os.path.exists(convpdfdirpc):
        lastimg=lastmodfile(1, convpdfdirpc)
        print("li="+str(lastimg))
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            lastimg0=lastimg.rsplit("\\\\",1)[1]
        if sys.platform in ['linux', 'linux2']:
            lastimg0=lastimg.rsplit("/",1)[1]
        lastimg0=lastimg.rsplit("\\\\",1)[1]
        lastpage=re.sub(r"(conv|wledpos|wled)(0)*","",lastimg0)
        lastpage=re.sub(r"(.jpg|.png)","",lastpage)
    if not os.path.exists(convpdfdirpc):
        lastpage=1
    print("lp="+str(lastpage))
    return int(lastpage)

if sys.platform in ['linux', 'linux2']:
    # Adapted from http://stackoverflow.com/questions/22367358/
    class Listener:
      def __init__(self):
        self.disp = None
        self.keys_down = set()
      def keycode_to_key(self, keycode, state):
        i = 0
        #if state & X.ShiftMask:
        #i += 1
        #if state & X.Mod1Mask:
          #i += 2
        return self.disp.keycode_to_keysym(keycode, i)
      def key_to_string(self, key):
        keys = []
        for name in dir(XK):
          if name.startswith("XK_") and getattr(XK, name) == key:
            keys.append(name.lstrip("XK_").replace("_L", "").replace("_R", ""))
        if keys:
          return " or ".join(keys)
        return "[%d]" % key
      def keycode_to_string(self, keycode, state):
        return self.key_to_string(self.keycode_to_key(keycode, state))
      def mouse_to_string(self, code):
        if code == X.Button1:
          return "Button1"
        elif code == X.Button2:
          return "Button2"
        elif code == X.Button3:
          return "Button3"
        elif code == X.Button4:
          return "Button4"
        elif code == X.Button5:
          return "Button5"
        else:
          return "{%d}" % code
      def down(self, key):
        self.keys_down.add(key)
        self.print_keys()
      def up(self, key):
        if key in self.keys_down:
          self.keys_down.remove(key)
          self.print_keys()

      def print_keys(self):
        keys = str(list(self.keys_down))
        #print(keys)
        self.EventL()
      def event_handler(self, reply):
        data = reply.data
        while data:
          event, data = rq.EventField(None).parse_binary_value(data, self.disp.display, None, None)
          if event.type == X.KeyPress:
            self.down(self.keycode_to_string(event.detail, event.state))
          elif event.type == X.KeyRelease:
            self.up(self.keycode_to_string(event.detail, event.state))
          elif event.type == X.ButtonPress:
            self.down(self.mouse_to_string(event.detail))
          elif event.type == X.ButtonRelease:
            self.up(self.mouse_to_string(event.detail))
      def run(self):
        self.disp = Display()
        XK.load_keysym_group('xf86')
        root = self.disp.screen().root
        ctx = self.disp.record_create_context(0,
                                          [record.AllClients],
                                          [{
                                            'core_requests': (0, 0),
                                            'core_replies': (0, 0),
                                            'ext_requests': (0, 0, 0, 0),
                                            'ext_replies': (0, 0, 0, 0),
                                            'delivered_events': (0, 0),
                                            'device_events': (X.KeyReleaseMask, X.ButtonReleaseMask),
                                            'errors': (0, 0),
                                            'client_started': False,
                                            'client_died': False,
                                          }])
        self.disp.record_enable_context(ctx, lambda reply: self.event_handler(reply))
        self.disp.record_free_context(ctx)
        while True:
            event = root.display.next_event()
      def EventL(self):
        global Home
        keys = str(list(self.keys_down))
        #print(keys)
        if keys == "['Shift']" or keys == "['Button2']":
            Suspend1()
        if pause==0 and not Home:
            if keys == "['Button1']":
               mouselu("")

#pip install --upgrade setuptools
#pip install psutil pymouse pyautogui pillow pyscreenshot numpy scipy matplotlib opencv-python pypiwin32 pynput
#win32gui pillow
#pip install %USERPROFILE%\\Downloads\\PyHook3-1.6.1-cp35-none-win_amd64.whl
#pip install %USERPROFILE%\\Downloads\\pyhook-1.6.1-cp37-cp37m-amd64.whl
#pip install %USERPROFILE%\\Downloads\\pyhook-1.6.1-cp35-cp35m-win32.whl
#pip install %USERPROFILE%\\Downloads\\pyhook-1.6.1-cp35-none-win_amd64.whl
#Pillow-5.2.0-cp37-cp37m-win_amd64.whl
if sys.platform in ['Windows', 'win32', 'cygwin']:
    from tkinter import *
    from tkinter import Tk
    import tkinter as tk
    import ctypes
    from win32api import GetSystemMetrics
    import win32com.client as comclt
    import win32gui, win32con
    #import pyHook
    import pythoncom
    import PyHook3
    #import pyHook
    import pyautogui
    import psutil
    #from pymouse import PyMouse
    from PyHook3 import HookManager, GetKeyState, HookConstants
    #m=PyMouse()
    w=win32gui
    wingui=w.GetWindowText(w.GetForegroundWindow())
    wsh= comclt.Dispatch("WScript.Shell")
    def eventmessage():
        print ('MessageName:',event.MessageName )
        print ('Message:',event.Message)
        print ('Time:',event.Time)
        print ('Window:',event.Window)
        print ('WindowName:',event.WindowName)
        print ('Ascii:', event.Ascii, chr(event.Ascii) )
        print ('Key:', event.Key)
        print ('KeyID:', event.KeyID)
        print ('ScanCode:', event.ScanCode)
        print ('Extended:', event.Extended)
        print ('Injected:', event.Injected)
        print ('Alt', event.Alt)
        print ('Transition', event.Transition)
        print ('---')
    def OnKeyboardEventA(event):
        global is_recording,pause
        global Home,pdfdir0,pdfname0,lastpage
        if event.KeyID == HookConstants.VKeyToID('VK_RSHIFT'):
            #print("Paused")
            Suspend1()
            return True
        elif event.KeyID == HookConstants.VKeyToID('VK_LEFT') and Home and pause==0:
            print("pn0="+pdfname0)
            #changepage(pdfdir0,pdfname0,lastpage,"prev")
            return True
        elif event.KeyID == HookConstants.VKeyToID('VK_RIGHT') and Home and pause==0:
            print("pn0="+pdfname0)
            #changepage(pdfdir0,pdfname0,lastpage,"next")
            return True
        elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            sys.exit()
            return True
        elif event.KeyID == HookConstants.VKeyToID('VK_F6'):
            return True
        elif event.KeyID == HookConstants.VKeyToID('VK_F7'):
            return True
        elif event.KeyID == HookConstants.VKeyToID('VK_F8'):
            return True
        elif event.KeyID == HookConstants.VKeyToID('VK_F9'):
            return True
        elif event.KeyID == HookConstants.VKeyToID('VK_F10'):
            return True
        elif event.KeyID == HookConstants.VKeyToID('VK_F12'):
            return True
        elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and HookConstants.IDToName(event.KeyID) == 'P' :
            print("Pause Recording")
            return True

        elif event.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            sys.exit()
        else:
            if is_recording==1:
                newhndl = ctypes.windll.user32.GetForegroundWindow()
                appname=get_app_name(newhndl)
                print(appname)
                title=win32gui.GetWindowText (win32gui.GetForegroundWindow())
                print(title)
                Hold=0
                print("recording")
                print('Key:', event.Key)
                #if (RegexMatch(activeprocess,"Acrobat|SumatraPDF|chrome|opera")):
                if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and (self.Key == 'Oem_Plus' or self.Key == 'Oem_Minus' or HookConstants.IDToName(event.KeyID) == '0'):
                    print("captured")
                    #if RegExMatch(A_ThisHotkey,"\\^=|\\^-|\\^0"):
                    #append(".+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.1.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.")
                    return True
                elif GetKeyState(HookConstants.VKeyToID('VK_LSHIFT')) and GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and HookConstants.IDToName(event.KeyID) == 'A' :
                    print("1")
                    #elif RegExMatch(A_ThisHotkey,"\\+\\^a"):
                    #append(".+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.2.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.")
                    return True
                    #elif RegExMatch(A_ThisHotkey,"\\+(Up|Down|Left|Right)"):
                elif GetKeyState(HookConstants.VKeyToID('VK_LSHIFT')) and (event.KeyID == HookConstants.VKeyToID('VK_UP') or event.KeyID == HookConstants.VKeyToID('VK_DOWN') or event.KeyID == HookConstants.VKeyToID('VK_LEFT') or event.KeyID == HookConstants.VKeyToID('VK_RIGHT')):
                    print("2")
                    #append(".+.+.+.+.+.+.+.+.+.3.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.")
                    return True
                else:

                    return True
            else:
                return True

    def onclicka(event):
        global Home
        X, Y=event.Position
        if (event.MessageName=='mouse left up') and not Home:
            #mouselu(event)
            mouselu(event)
            return True
        elif (event.MessageName=='mouse left down'):
            #mouselu(event)
            return True
        elif (event.MessageName=='mouse move'):
            #print("move")
            #print(X,Y)
            return True
        elif (event.MessageName=='mouse wheel'):
            #print("wheel")
            return True
        else:
            #print(event.MessageName)
            return True

    def windowEnumerationHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    def focusprog(appname):
            results = []
            top_windows = []
            win32gui.EnumWindows(windowEnumerationHandler, top_windows)
            for i in top_windows:
                if appname in i[1].lower():
                    print (i)
                    win32gui.ShowWindow(i[0],win32con.SW_MAXIMIZE)
                    win32gui.SetForegroundWindow(i[0])
                    j=os.getpid()
                    print(j)
                    break
    def closeprog(appname):
            results = []
            top_windows = []
            win32gui.EnumWindows(windowEnumerationHandler, top_windows)
            for i in top_windows:
                if appname in i[1].lower():
                    print (i)
                    win32gui.ShowWindow(i[0],win32con.SW_MAXIMIZE)
                    win32gui.SetForegroundWindow(i[0])
                    win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0)
                    j=os.getpid()
                    print(j)
                    break
    def runfn():
        PROCNAME = "FiiNote.exe"
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                subprocess.Popen([fndir])
                win32gui.EnumWindows(focusfn, None)
                break
            else:
                subprocess.Popen([fndir])
                win32gui.EnumWindows(focusfn, None)
                break

        pass
    def focusfn(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            if 'Notes\\' in win32gui.GetWindowText(hwnd):
                win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)
                win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
                win32gui.SetForegroundWindow(hwnd)
                pass
    def focusfn2(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            if 'Untitled' in win32gui.GetWindowText(hwnd):
                win32gui.SetForegroundWindow(hwnd)
                win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
    def spdfhandler(hwnd, lParam):
        for proc in psutil.process_iter():
            if proc.name() == "SumatraPDF.exe":
                if win32gui.IsWindowVisible(hwnd):
                    if 'SumatraPDF' in win32gui.GetWindowText(hwnd):
                        win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)
                        win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
                        win32gui.SetForegroundWindow(hwnd)
                        break
            else:
                subprocess.Popen(readerdir)
                break
    def currenthwnd():
        newhndl = ctypes.windll.user32.GetForegroundWindow()
        appname=get_app_path(newhndl)
        print(newhndl,appname)
    def get_app_path(hwnd):
        global exepath
        """Get applicatin path given hwnd."""
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            for p in c.query('SELECT ExecutablePath FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
                exepath = p.ExecutablePath
                break
        except:
            return None
        else:
            return exepath
    def get_app_name(hwnd):
        global exename
        """Get applicatin filename given hwnd."""
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            for p in c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
                exename = p.Name
                break
        except:
            return None
        else:
            return exename


Default()
CN=checknotz(curnotelocpc)
newdir1=CN[0]
objno2=CN[1]
curnotzpc,curnotefpc,curattachdirpc,curnotzand,curattachdirand=setvarnotz(fnnotesdirpc,newdir1)
#curnotzpc=CN[2]
#curnotefpc=CN[3]
#curattachdirpc=CN[4]
#curnotzand=CN[5]
#curattachdirand=CN[6]
#_thread.start_new_thread(task2, ())
print(newdir1)
print(objno2)
print(curattachdirpc)
if __name__=='__main__':
    if sys.platform in ['linux', 'linux2']:
        while 1:
            Listener().run()
            #_thread.start_new_thread(Listener().run, ())
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        global hm
        #https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook
        #https://stackoverflow.com/questions/43417601/using-pyhook-to-detect-key-up-and-down
        ##https://stackoverflow.com/questions/45113813/check-if-mouse-up-or-mouse-down-with-pyhook
        #win32gui.EnumWindows(spdfhandler, None)
        #runfn()
        #win32gui.EnumWindows(focusfn, None)
        #currenthwnd()
        hm = PyHook3.HookManager()
        hm.HookMouse()
        hm.MouseAll = onclicka
        #hm.MouseLeftDown = OnDown
        #hm.MouseLeftUp = OnUp
        hm.HookKeyboard()
        hm.KeyDown = OnKeyboardEventA
        #pythoncom.PumpMessages()
        #hm.UnhookMouse()
        ##hm.UnhookKeyboard()
    task2()
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        _thread.start_new_thread(pythoncom.PumpMessages, ())
        _thread.start_new_thread(hm.UnhookMouse, ())
        
    
