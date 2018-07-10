#!/usr/bin/env python
#pyhook
#ph3fn="pyhook-1.6.1-cp35-cp35m-win32.whl"
#ph3downdir="\\$ph3fn"
#ph3downlink="https://files.pythonhosted.org/packages/00/36/c08af743a671d94da7fe10ac2d078624f3efc09273ffae7b18601a8414fe/PyHook3-1.6.1-cp35-win32.whl"
#curl -o "$ph3fn" "$ph3downlink"
#
import os, sys, threading
import _thread
from FN33andlib import *
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
if sys.platform in ['linux', 'linux2'] or sys.platform in ['Windows', 'win32', 'cygwin']:
    def mouselu(event):
        global textclick, clickStartX, clickStopX, clickStartY, clickStopY, objno2
        if pause==0 :
            if sys.platform in ['linux', 'linux2']:
                clickX, clickY=MouseGetPos()
            if sys.platform in ['Windows', 'win32', 'cygwin']:
                clickX, clickY=event.Position
            if (textclick==0):
                if (linuxpc==0) and os.path.exists("/run/user/1000/gvfs/*/Internal"):
                    subprocess.call("adb shell \"su -c 'input keyevent KEYCODE_ESCAPE && sleep 0.1 && killall com.fiistudio.fiinote'\"", shell=True)
                clickStartX, clickStartY=clickX, clickY
                print(clickStartX, clickStartY)
                TT.config(text="C")
                textclick=1
            elif (textclick==1):
                clickStopX, clickStopY=clickX, clickY
                print(clickStopX, clickStopY)
                clickStartX=int(clickStartX)
                clickStartY=int(clickStartY)
                clickStopX=int(clickStopX)
                clickStopY=int(clickStopY)
                if clickStartX<clickStopX :
                    SS=SS1(clickStartX,clickStartY,clickStopX,clickStopY)
                    print(SS)
                    objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],SS[3],SS[4],"nearlatest")
                    imgdir=curattachdirpc+os.path.sep+SS[2]
                    if (linuxpc==0) and os.path.exists("/run/user/1000/gvfs/*/Internal"):
                        subprocess.call("adb push -p "+imgdir+" "+fnnotesanddirint+newdir1+".notz/attach",shell=True)
                    TT.config(text="P")
                    TT2.config(text=str(objno2))
                    ##subprocess.call("adb shell su -c 'monkey -p com.fiistudio.fiinote -c android.intent.category.LAUNCHER 1'", shell=True)
                        ## \"su -c 'killall com.fiistudio.fiinote'\"
                    #except :
                        ##TT.config(text="try")
                    ##monkey -p com.fiistudio.fiinote.editor.Fiinote -c android.intent.category.LAUNCHER 1
                else:
                    TT.config(text="Rep")
                textclick=0
    def task2():
        global TT,TT2,root
        root = tk.Tk()
        m = Button(root, text="Pause R", command=Suspend1,height=3,width=3)
        m.pack()
        newf = Button(root, text="New F", command=newnotz,height=3,width=3)
        newf.pack()
        copyk = Button(root, text="copy", command=copykey,height=3,width=3)
        copyk.pack()
        pastek = Button(root, text="paste", command=pastekey,height=3,width=3)
        pastek.pack()
        restartgui=Button(root, text="restart", command=restartguifn,height=3,width=3)
        restartgui.pack()
        #button1.config( height = WHATEVER, width = WHATEVER2 )
        #button1 = Button(self, text = "Send", command = self.response1, height = 100, width = 100)
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
        hn=770
        root.wm_attributes('-alpha',0.50,'-topmost',1)
        root.geometry('%dx%d+%d+%d' % (wn, hn, x,y))
        root.resizable(False, False)
        root.update_idletasks()
        root.overrideredirect(True)
        Suspend1()
        root.mainloop()
    def quit():
        global root
        root.destroy()
        #root.quit()
    def restartguifn():
        quit()
        #if sys.platform in ['linux', 'linux2'] :
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            subprocess.call("%USERPROFILE%\\Documents\\GitHub\\FN35OCVbside\\fn33andguistart.bat",shell=True)
        return True
    def ClearTT():
        TT.config(text="")
        return True
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
    def Suspend1():
        global pause
        if pause==0:
            pause=1
            TT.config(text="Suspended")
        elif pause==1:
            pause=0
            TT.config(text="Resume")
    def newnotz():
        global newdir1, objno2
        os.remove(curnotelocpc)
        CN=checknotz(curnotelocpc)
        newdir1=CN[0]
        objno2=CN[1]
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
        keys = str(list(self.keys_down))
        #print(keys)
        if keys == "['Shift']" or keys == "['Button2']":
            Suspend1()
        if pause==0 :
            if keys == "['Button1']":
               mouselu("")


if sys.platform in ['Windows', 'win32', 'cygwin']:
    from tkinter import *
    from tkinter import Tk
    import tkinter as tk
    import ctypes
    from win32api import GetSystemMetrics
    import win32com.client as comclt
    import win32gui, win32con
    #import pyHook
    import pythoncom,PyHook3
    import pyautogui
    import psutil
    from pymouse import PyMouse
    from PyHook3 import HookManager, GetKeyState, HookConstants

    m = PyMouse()
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
        global is_recording
        if event.KeyID == HookConstants.VKeyToID('VK_RSHIFT'):
            #print("Paused")
            Suspend1()
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
                    #if RegExMatch(A_ThisHotkey,"\^=|\^-|\^0"):
                    #append(".+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.1.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.")
                    return True
                elif GetKeyState(HookConstants.VKeyToID('VK_LSHIFT')) and GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and HookConstants.IDToName(event.KeyID) == 'A' :
                    print("1")
                    #elif RegExMatch(A_ThisHotkey,"\+\^a"):
                    #append(".+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.2.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.")
                    return True
                    #elif RegExMatch(A_ThisHotkey,"\+(Up|Down|Left|Right)"):
                elif GetKeyState(HookConstants.VKeyToID('VK_LSHIFT')) and (event.KeyID == HookConstants.VKeyToID('VK_UP') or event.KeyID == HookConstants.VKeyToID('VK_DOWN') or event.KeyID == HookConstants.VKeyToID('VK_LEFT') or event.KeyID == HookConstants.VKeyToID('VK_RIGHT')):
                    print("2")
                    #append(".+.+.+.+.+.+.+.+.+.3.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.")
                    return True
                else:

                    return True
            else:
                return True

    def onclicka(event):
        X, Y=event.Position
        if (event.MessageName=='mouse left up'):
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
        #if __name__ == "__main__":


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
_thread.start_new_thread(task2, ())
print(newdir1)
print(objno2)

if __name__=='__main__':
    if sys.platform in ['linux', 'linux2']:
        while 1:
            Listener().run()
    if sys.platform in ['Windows', 'win32', 'cygwin']:
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
        pythoncom.PumpMessages()
        hm.UnhookMouse()
        ##hm.UnhookKeyboard()
