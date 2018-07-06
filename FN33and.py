#!/usr/bin/env python
import os, sys, threading
import _thread
from libFN33and import *
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
                    objno2,curattachdirpc=appendnewpic(SS[0],SS[1],SS[2],SS[3],SS[4],1)
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
        global TT, TT2
        root = tk.Tk()
        m = Button(root, text="Pause R", command=Suspend1)
        newf = Button(root, text="New F", command=newnotz)
        TT=Label(root, relief='raised')
        TT2=Label(root)
        m.pack()
        newf.pack()
        TT.pack()
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
        root.geometry('%dx%d+%d+%d' % (wn, hn, x,y) )
        root.resizable(False, False)
        root.update_idletasks()
        root.overrideredirect(True)
        Suspend1()
        root.mainloop()
    def ClearTT():
        TT.config(text="")
        return True
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

if sys.platform in ['linux', 'linux2']:
    Default()
    CN=checknotz(curnotelocpc)
    newdir1=CN[0]
    objno2=CN[1]
    _thread.start_new_thread(task2, ())
    print(newdir1)
    print(objno2)
    if __name__=='__main__':
        while 1:
            Listener().run()
