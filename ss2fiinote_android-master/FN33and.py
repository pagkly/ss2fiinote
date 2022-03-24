#!/usr/bin/env python
## sudo apt-get install python3-xlib python3-psutil wmctrl thunar\
#python3 install --upgrade pip
#python3 install psutil
import os, sys, threading
import _thread
import subprocess
import shutil
import psutil
import re
from datetime import datetime
from time import gmtime,strftime
import time
import binascii
import math
import pyscreenshot
import tkinter as tk
from tkinter import *
from tkinter import Tk

if sys.platform in ['linux', 'linux2']:
    from Xlib.display import Display
    import Xlib.display as display
    from Xlib import X, XK
    from Xlib.ext import record
    from Xlib.protocol import rq
    import signal
    
    dirand="/run/user/1000/gvfs"
    dirand2=os.listdir(dirand)
    fnsavedirand=dirand+"/"+dirand2[0]+"/Internal shared storage/fiinote/notes/"
    subprocess.call("nautilus file:///home/user/Documents/Docs/Tech/Automate/PDF/Sem2",shell=True)
if sys.platform in ['Windows', 'win32', 'cygwin']:
    dirand="Z:\\"
    fnsavedirand=dirand+"fiinote\\notes\\"
    
##fnnotespdir=dir_path+os.path.sep+"FiiNote"+os.path.sep+"Save"+os.path.sep+"@pagkly"+os.path.sep+"notes"+os.path.sep
andfndir="/storage/emulated/0/fiinote/notes/"
andfndir2="/storage/emulated/0/fiinote/notes"
fnnotespdir=fnsavedirand
dir_path = os.path.dirname(os.path.realpath(__file__))
##curnotedir="/home/user/Documents/Docs/Tech/Automate/andimages.txt"
curnotedir=dir_path+os.path.sep+"andimages.txt"
print(curnotedir)
curpicdir=dir_path+os.path.sep+"attach"
fndir = dir_path+os.path.sep+"FiiNote"+os.path.sep+"FiiNote.exe"
readerdir=dir_path+os.path.sep+"SumatraPDF-3.1.2"+os.path.sep+"SumatraPDF.exe"
winefndir="wine "+fndir
winereaderdir="wine "+readerdir

textclick=0
pause=0
is_recording=0
    
def Default():
    textclick=0
    pause=0
    is_recording=0

if sys.platform in ['linux', 'linux2'] or sys.platform in ['Windows', 'win32', 'cygwin']:
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
            
    def mouselu(event):
        global textclick, clickStartX, clickStopX, clickStartY, clickStopY, objno2
        if pause==0 :
            if (textclick==0):
                subprocess.call("adb shell \"su -c 'input keyevent KEYCODE_ESCAPE && sleep 0.1 && killall com.fiistudio.fiinote'\"", shell=True)
                if sys.platform in ['linux', 'linux2']:
                    clickStartX, clickStartY=MouseGetPos()
                if sys.platform in ['Windows', 'win32', 'cygwin']:
                    clickStartX, clickStartY=event.Position
                print(clickStartX, clickStartY)
                TT.config(text="C")
                textclick=1
            elif (textclick==1):
                if sys.platform in ['linux', 'linux2']:
                    clickStopX, clickStopY=MouseGetPos()
                if sys.platform in ['Windows', 'win32', 'cygwin']:
                    clickStopX, clickStopY=event.Position
                print(clickStopX, clickStopY)
                if clickStartX<clickStopX :
                    clickStartX=int(clickStartX)
                    clickStartY=int(clickStartY)
                    clickStopX=int(clickStopX)
                    clickStopY=int(clickStopY)
                    ##try:
                    SS=SS1(clickStartX,clickStartY,clickStopX,clickStopY)
                    print(SS)
                    objno2=appendnewpic(SS[0],SS[1],SS[2],SS[3],SS[4])
                    imgdir=curpicdir+os.path.sep+SS[2]
                    subprocess.call("adb push -p "+imgdir+" "+andfndir+newdir1+".notz/attach",shell=True)
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
        os.remove(curnotedir)
        CN=checknotz(curnotedir)
        newdir1=CN[0]
        objno2=CN[1]
        TT2.config(text="NEW")

    def term(scriptn):
        if sys.platform in ['linux', 'linux2'] :
            python_path=""
            subprocess.call("python3 "+str(dir_path)+"/"+str(scriptn)+".py", shell=True)
            print(python_path+"sudo python3 "+str(dir_path)+"/"+scriptn)
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            python_path=dir_path+os.path.sep+"WinPython-32bit-3.5.3.1Qt5"+os.path.sep+"scripts"+os.path.sep
            subprocess.call(python_path+"python "+str(dir_path)+"\\"+str(scriptn)+".py", shell=True)
        return True

def getdateinhex():
    my_date="05/11/2009"
    b_date = datetime.strptime(my_date, '%d/%m/%Y')
    diffYear=int((datetime.today() - b_date).days/365)
    diffMonth=int((datetime.today() - b_date).days/30)
    diffMonthHex=str(format(diffMonth,'x')).zfill(2)
    diffDay=int(((datetime.today() - b_date).days-(diffMonth*30)))
    diffDayHex=str(format(diffDay,'x')).zfill(2)
    return diffDayHex, diffMonthHex

def checknotz(curnotedir):
    subprocess.call("adb shell \"su -c 'input keyevent KEYCODE_ESCAPE && sleep 0.1 && killall com.fiistudio.fiinote'\"", shell=True)
    global objno2
    if os.path.exists(curnotedir):
        with open(curnotedir) as f:
            for line in f:
                if re.search(r"\.notz",str(line)):
                    newdir1=line
                    newdir1 = re.sub('.notz', '', newdir1)
        curnotz=fnnotespdir+newdir1+".notz"
        curnotef=fnnotespdir+newdir1+".notz"+os.path.sep+newdir1+".note"
        curpicdir2=fnnotespdir+newdir1+".notz"+os.path.sep+"attach"
        print(curnotef)
        if os.path.exists(curnotz) and os.path.exists(curnotef) and os.path.exists(curpicdir2):
            print("checkingcnf")
            with open(curnotef,"rb") as f:
                    content=f.read()
                    contenthex=str(binascii.hexlify(content).decode('utf-8'))
                    regex_number=r'(0302010201)(..)'
                    mo1 = re.search(regex_number,contenthex)
                    mo2 = re.compile(regex_number)
                    if mo2.search(contenthex):
                        objno2=int(mo1.group(2), 16)
                    else:
                        objno2=1
                    print(str(objno2))
                    f.close()
        if (not os.path.exists(curnotz) or not os.path.exists(curnotef) or not os.path.exists(curpicdir2)) :
            ##or (objno2>=30)
            objno2=1
            Time=strftime("%Y%m%d%H%M%S")
            newdir1="AOWNLPC00000"+Time
            ##curnotz=fnnotespdir+newdir1+".notz"
            ##curnotef=fnnotespdir+newdir1+".notz"+os.path.sep+newdir1+".note"
            ##curpicdir2=fnnotespdir+newdir1+".notz"+os.path.sep+"attach"
            ##curnotz=dir_path+os.path.sep+newdir1+".notz"
            ##curnotef=dir_path+os.path.sep+newdir1+".notz"+os.path.sep+newdir1+".note"
            ##curpicdir2=dir_path+os.path.sep+newdir1+".notz"+os.path.sep+"attach"
            ##curnotz=andfndir+newdir1+".notz"
            ##curnotef=andfndir+newdir1+".notz"+os.path.sep+newdir1+".note"
            ##curpicdir2=andfndir+newdir1+".notz"+os.path.sep+"attach"
            curnotz=andfndir+newdir1+".notz"
            curnotef2=andfndir+newdir1+".notz"+os.path.sep+newdir1+".note"
            curpicdir2=andfndir+newdir1+".notz"+os.path.sep+"attach"
            curnotef=dir_path+os.path.sep+"ConvertedPDF"+os.path.sep+newdir1+".note"
            if not os.path.exists(curnotz):
                ##os.mkdir(curnotz)
                subprocess.call("adb shell mkdir "+curnotz,shell=True)
            if not os.path.exists(curpicdir2):
                ##os.mkdir(curpicdir2)
                subprocess.call("adb shell mkdir -p "+curpicdir2,shell=True)
            if not os.path.exists(curnotef):
                ##curnotefinpc=dir_path+"/attach/"+newdir1+".note"
                f2=open(curnotef,"w+")
                f2.close()
                ##subprocess.call("adb shell touch "+curnotef,shell=True)
                firstlineappend(newdir1,curnotef)
                subprocess.call("adb push "+curnotef+" "+curnotz,shell=True)
                print("appendfline")
            ##os.remove(curnotef)
            f1=open(curnotedir,"w+")
            f1.write(newdir1+".notz")
            f1.close()
            ##subprocess.call("adb push "+curnotz+" "+andfndir,shell=True)
            appendnewnote(newdir1,fnnotespdir)
             
    elif not os.path.exists(curnotedir) or (not os.path.exists(curnotz)) :
        ##or (objno2>=30)
        objno2=1
        Time=strftime("%Y%m%d%H%M%S")
        newdir1="AOWNLPC00000"+Time
        curnotz=andfndir+newdir1+".notz"
        curnotef2=andfndir+newdir1+".notz"+os.path.sep+newdir1+".note"
        curpicdir2=andfndir+newdir1+".notz"+os.path.sep+"attach"
        curnotef=dir_path+os.path.sep+"ConvertedPDF"+os.path.sep+newdir1+".note"
        if not os.path.exists(curnotz):
            subprocess.call("adb shell mkdir "+curnotz,shell=True)
        if not os.path.exists(curpicdir2):
            subprocess.call("adb shell mkdir -p "+curpicdir2,shell=True)
        if not os.path.exists(curnotef):
            f2=open(curnotef,"w+")
            f2.close()
            firstlineappend(newdir1,curnotef)
            subprocess.call("adb push "+curnotef+" "+curnotz,shell=True)
            print("appendfline")
        ##os.remove(curnotef)
        f1=open(curnotedir,"w+")
        f1.write(newdir1+".notz")
        f1.close()
        appendnewnote(newdir1,fnnotespdir)
    return newdir1,objno2


def firstlineappend(newdir1,curnotef):
    diffTime=getdateinhex()
    diffDayHex=diffTime[0]
    diffMonthHex=diffTime[1]
    newdir1hex="".join("{:02x}".format(ord(c)) for c in newdir1)
    filetypehex="060000" + \
                 "01" + diffMonthHex + diffDayHex + "FFFFFF" + "0000" + \
                 "01" + diffMonthHex + diffDayHex + "FFFFFF" + \
                 "001A" + newdir1hex + \
                 "000000" + "ffff" + \
                 "000000" + "000000" + \
                 "000000" + "000000" + \
                 "000000" + "000000" + \
                 "01" + \
                 "000000" + "000000" + \
                 "000000" + "000000" + \
                 "01" + diffMonthHex + diffDayHex + "FFFFFF" + \
                 "010302010201"+ \
                 "01"
    append=filetypehex
    with open(curnotef,"wb") as fout:
        append=bytes(bytearray.fromhex(append))
        fout.write(append)
        fout.close()
            
def SS1(clickStartX,clickStartY,clickStopX,clickStopY):
    Time=strftime("%Y%m%d%H%M%S")
    picname=Time+'abcdefghijklmno.jpg'
    imgdir=curpicdir+os.path.sep+picname
    im=pyscreenshot.grab(bbox=(clickStartX,clickStartY,clickStopX,clickStopY),childprocess=False)
    w,h=im.size
    im.save(imgdir)
    print(imgdir)
    return w,h,picname,newdir1,objno2

    #if (objno2<32):
    #    prefixposyhex="A9"
    #    quot=objno2/2;
    #    rem=objno2%2;
    #    objnonow=224+quot+1;

    #elif (objno2>=32):
    #    prefixposy=int(objno2/34)+169
    #    prefixposyhex=format(math.trunc(prefixposy), 'x')
    #    quot=objno2/2;
    #    rem=objno2%2;
    #    objnonow=224+quot+1;


def appendnewpic(w,h,picname,newdir1,objno2):
    objno2=int(objno2)
    print("number"+str(objno2))
    curnotef=fnnotespdir+newdir1+".notz"+os.path.sep+newdir1+".note"
    newlinehex="0AC480C391C391C39101";
    secondobjhex="C88A";
    xlochex="E5A5AA"+\
             "E5AB81"+\
             "E5A5A9"+\
             "E19E81"+\
             "E5A5A9"+\
             "E19E81";
    w=int(w)
    h=int(h)
    objno2c1=int(objno2/14);
    ##if (objno2c1==0):
    ##    prefixposy=169
    ##elif (objno2c1>0):
    ##    prefixposy=169+objno2c1
    if (objno2c1<32):
        prefixposy=169
    elif (objno2c1>=32):
        prefixposy=int(objno2c1/34)+169
    prefixposyhex=format(math.trunc(prefixposy), 'x')
    quot=objno2/2;
    rem=objno2%2;
    objnonow=224+quot+1;
    objnohex=format(math.trunc(objnonow), 'x')
    print(objnohex)
    print("w="+str(w))
    print("h="+str(h))
    if (quot==0):
        if (rem>0):
            posyhex="9E"
        else:
            posyhex="81"
    else:
        if (rem!=0):
            posyhex="9E"
        if(rem==0):
            posyhex="81"
    ylochex="E5A5A9"+\
             "E19E81"+\
             "E5A5AA"+\
             "E5AB81"+\
             "E5A5"+prefixposyhex+\
             objnohex+posyhex+"81"
    zlochex="E5A5A9"+\
             "E19E81"+\
             "E5A5A9"+\
             "E19E81"+\
             "E5A5AA"+\
             "E5AB81"
    print(ylochex)
    print(zlochex)
    if (w<128):
        xpixshex=format(w,'x')
        xpixshex=str(xpixshex).zfill(2)
    if (w>=128):
        xquothexint=int(math.trunc(192+(w/64)));
        xremhexint=int(math.trunc(128+(w%64)));
        xquothexs=format(xquothexint,'x')
        xremhexs=format(xremhexint,'x')
        xpixshex=xquothexs+xremhexs;

    if (h<128):
        ypixshex=format(h,'x')
        ypixshex=str(ypixshex).zfill(2)
    if (h>=128):
        yquothexint=int(math.trunc(192+(h/64)));
        yremhexint=int(math.trunc(128+(h%64)));
        yquothexs=format(yquothexint,'x')
        yremhexs=format(yremhexint,'x')
        ypixshex=yquothexs+yremhexs;
    yscalehexs="";
    xscalehexs="";
    ysuffix="";

    if (w<h):
        a=2717*w;
        div=h*64;
        xscalequotinta=int(math.trunc(a/div));
        xscalequotint=148+xscalequotinta;
        xscalequothexs=format(xscalequotint,'x')
        xrem=(((a/div)-xscalequotinta)*64);
        xscaleremint=int(128+xrem);
        xscaleremhexs=format(xscaleremint,'x')
        xscalehexs="E2"+xscalequothexs+xscaleremhexs;
        yscalehexs="E2BE9D";
    elif (w>h):
        xscalehexs="E38EBF";
        a=3711*h;
        div=w*64;
        yscalequotint=0;
        yscalequotinta=int(math.trunc(a/div));
        if (yscalequotinta>=43):
            ysuffix="E3";
            yscalequotint=int(math.trunc(128+(((3711*h)/(w*64))-43)));
        if (yscalequotinta<43):
            ysuffix="E2";
            yscalequotint=int(math.trunc(148+((3711*h)/(w*64))));
        yscalequothexs=format(yscalequotint,'x')
        yrem=int(math.trunc((((a/div)-yscalequotinta)*64)));
        yscaleremint=int(128+yrem);
        yscaleremhexs=format(yscaleremint,'x')
        yscalehexs=ysuffix+yscalequothexs+yscaleremhexs;
    elif (w==h):
        xscalehexs="E2BAA3";
        yscalehexs="E2BAA3";

    objscalehex="0303E293B903E293B903"+xscalehexs+"03"+yscalehexs+"22";
    picnamehex="".join("{:02x}".format(ord(c)) for c in picname)
    hexc = newlinehex+secondobjhex+xlochex+ylochex+zlochex+objscalehex+picnamehex+xpixshex+ypixshex+"01"
    #print(hexc)
    if os.path.exists(curnotef) and objno2>=1:
        with open(curnotef,"rb") as f:
            content=f.read()
            cihx=str(binascii.hexlify(content).decode('utf-8'))
            regex_number=r'(0302010201)(.{2}){0,1}(.{2})(0A)'
            ##(0A){0,1}
            mo1=re.search(regex_number,cihx)
            mo2=re.compile(regex_number)
            if mo2.search(cihx):
                print("found")
                objno2=int(mo1.group(3), 16)
                objno2+=1
                prefixhex=""
                if (objno2==128):
                    prefixhex="c2";
                if (objno2>128):
                    prefix=int((objno2-128)/64);
                    prefixhex=194+prefix;
                    prefixhex=str(format(prefixhex,'x')).zfill(2)
                if (objno2>=192):
                    prefix=int((objno2-192)/64);
                    prefixhex=195+prefix;
                    prefixhex=str(format(prefixhex,'x')).zfill(2)
                if (objno2<192):
                    totalobjhex=str(format(objno2,'x')).zfill(2)
                if (objno2>=192):
                    totalobjhex=str(format((128+int((objno2-192)%64)),'x')).zfill(2)
                print(totalobjhex)
                ##
                ##+mo1.group(4)
                if not mo1.group(4):
                    a=""
                else:
                    a=mo1.group(4)
                    
                replace1 = re.sub(regex_number, mo1.group(1)+prefixhex+totalobjhex+a, cihx)
                append=replace1+hexc
            else:
                regex_number=r'(0302010201)(.{2})'
                mo1=re.search(regex_number,cihx)
                mo2=re.compile(regex_number)
                if mo2.search(cihx):
                    print("found")
                    objno2=int(mo1.group(2), 16)
                    objno2+=1
                    prefixhex=""
    
                    totalobjhex=str(format(objno2,'x')).zfill(2)
                    print(totalobjhex)
                    
                    replace1 = re.sub(regex_number, mo1.group(1)+totalobjhex, cihx)
                    append=replace1+hexc
                
            with open(curnotef,"wb") as fout:
                append=bytes(bytearray.fromhex(append))
                fout.write(append)
                fout.close()
    return objno2

def appendnewnote(newdir1,fnnotespdir):
    global replace1, replace2
    replace1=""
    replace2=""
    indexcur = fnnotespdir+'index.nti'
    indexold = fnnotespdir+'indexold.nti'
    with open(indexcur, 'rb') as f:
        print("checkingindexcur")
        content = f.read()
        cihx=str(binascii.hexlify(content).decode('utf-8'))
        regexp1=r'(01)(.{8})(.{4})(011a)'
        regexc1=re.compile(regexp1)
        if regexc1.search(cihx):
            mo1= re.search(regexp1,cihx)
            p1d=(int(mo1.group(3), 16))+1
            p1dhex="%0.4X" % p1d
            regexr1=mo1.group(1)+mo1.group(2)+p1dhex+mo1.group(4)
            replace1 = re.sub(regexp1, regexr1, cihx)
        else:
            pass
        diffTime=getdateinhex()
        diffDayHex=diffTime[0]
        diffMonthHex=diffTime[1]
        newdir1hex="".join("{:02x}".format(ord(c)) for c in newdir1)
        newfolderhex1="011A"+newdir1hex+"00" + \
                        "00" + \
                        "04" + \
                        "00" + \
                        "00" + \
                        "01" + diffMonthHex + diffDayHex + "FFFFFF" + "0000" + \
                        "01" + diffMonthHex + diffDayHex + "FFFFFF" + "0000" + \
                        "001A" + newdir1hex + \
                        "00" + "1123236E6F7465732F2323756E66696C6564" + "05" + \
                        "00"+ \
                        "000000" + \
                        "000000" + \
                        "000000" + \
                        "01" + diffMonthHex + diffDayHex + "FFFFFF" + "0000" + \
                        "01" + diffMonthHex + diffDayHex + "FFFFFF"
        ##.+
        regexp2=r'(1123236e6f7465732f2323756e66696c6564(?!.*1123236e6f7465732f2323756e66696c6564))(.*?)(00\d\d\d\d00\d\d)(2323)'
        regexc2=re.compile(regexp2)
        if regexc2.search(replace1):
            mo2 = re.search(regexp2,replace1)
            regexr2=mo2.group(1)+mo2.group(2)+newfolderhex1+mo2.group(3)+mo2.group(4)
            replace2 = re.sub(regexp2, regexr2, replace1)
        else:
            pass
        print("checkingindexcurfinal")
        newindexhex=bytes(bytearray.fromhex(replace2))
        with open(indexcur,"wb") as fout:
            fout.write(newindexhex)
            fout.close()
        print("donecheckingindexcur")
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
    CN=checknotz(curnotedir)
    newdir1=CN[0]
    objno2=CN[1]
    _thread.start_new_thread(task2, ())
    print(newdir1)
    print(objno2)
    if __name__=='__main__':
        while 1:
            Listener().run()
            


    
