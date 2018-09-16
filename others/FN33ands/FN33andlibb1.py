#!/usr/bin/env python
import os, sys, threading
import _thread
import subprocess
import shutil
import psutil

import binascii
import re
import time
from datetime import datetime
from time import gmtime,strftime
import math
import tkinter as tk
from tkinter import *
from tkinter import Tk
import pyscreenshot
import argparse
#from PIL import Image
import PIL.Image
import PIL.ImageTk
def pythoninstall():
    subprocess.call("",shell=True)
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-pdir","--pdfdir",help="Loc of PDF. Example: -pdir /home/")
    parser.add_argument("-p","--pdfname",help="Name of PDF. Example: -p ABC.pdf")
    parser.add_argument("-ps","--pagestart",help="Starting Page. Example: -ps 1")
    parser.add_argument("-pe","--pageend",help="End Page. Example: -pe 6")
    parser.add_argument("-d","--density",help="DPI. Example: -d 100")
    parser.add_argument("-t","--type",help="OCV Type. Example: -t 1")
    parser.add_argument("-nc","--noconversion",help="OCV Type. Example: -nc 1")
    parser.add_argument("-pmdir","--pdfmdir",help="Loc of PDFs. Example: -pdir /home/user")
    parser.add_argument("-cont","--continuenote",help="continue previous note.")
    parser.add_argument("-test","--testing",help="Testing mode")
    parser.add_argument("-shpdf","--showpdf",help="Testing mode")
    return parser.parse_args()
def checkfile(filename):
    if not os.path.exists(filename):
        f = open(filename,\'w\')
        f.close()
def checkdir(dirname,mode):
    if mode=="rw":
        shutil.rmtree(dirname)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    return True
def checkfileand(filename):
    if not os.path.exists(filename):
        f = open(filename,\'w\')
        f.close()
def checkdirand(dirname):
    if os.path.exists(dirname):
        #shutil.rmtree(dirname)
        subprocess.call("adb shell mkdir -p "+dirname,shell=True)
    else:
        subprocess.call("adb shell mkdir "+dirname,shell=True)
    return True
def copyfile(source,dest):
    if sys.platform in [\'linux\', \'linux2\']:
        subprocess.call("cp "+source+" "+dest,shell=True)
    if sys.platform in [\'Windows\', \'win32\', \'cygwin\']:
        subprocess.call("cp "+source+" "+dest,shell=True)
    return True
def removefile(dirname):
    if sys.platform in [\'linux\', \'linux2\']:
        if os.path.exists(dirname):
            subprocess.call("rm -rf "+dirname+" ;", shell=True)
def convasciitohex(text,texttype):
    if texttype==1:
        textinhex="".join("{:02x}".format(ord(c)) for c in text)
    elif texttype==2:
        textinhex=bytes(bytearray.fromhex(text))
    elif textype==3:
        textinhex=format(int(text),\'x\')
    return textinhex
def appendtext(filedir,text,textformat):
    if textformat=="w":
        if not os.path.exists(filedir):
            f = open(filedir,\'w\')
            f.close()
    if textformat=="w+":
        f = open(filedir,\'w+\')
        f.write(text)
        f.close()
    if textformat=="a":
        #f=open(filedir,"a")
        #f.write("\
"+text)
        with open(filedir,"a") as f:
            f.write("\
"+text)
            f.close()
    if textformat=="wb":
        with open(filedir,"wb") as f:
            append=bytes(bytearray.fromhex(text))
            f.write(append)
            f.close()
def getdateinhex0():
    my_date="05/11/2009"
    b_date = datetime.strptime(my_date, \'%d/%m/%Y\')
    diffYear=int((datetime.today() - b_date).days/365)
    diffMonth=int((datetime.today() - b_date).days/30)
    diffMonthHex=str(format(diffMonth,\'x\')).zfill(2)
    diffDay=int(((datetime.today() - b_date).days-(diffMonth*30)))
    diffDayHex=str(format(diffDay,\'x\')).zfill(2)
    return diffDayHex, diffMonthHex
def getdateinhex():
    diffDayHex, diffMonthHex=getdateinhex0()
    difftime=diffDayHex+diffMonthHex
    print(diffDayHex, diffMonthHex)
    print(difftime)
    return difftime
def imgsize(imgdir):
    im = PIL.Image.open(imgdir)
    w, h = im.size
    return w,h
def grabimg(startx,starty,stopx,stopy):
    im=pyscreenshot.grab(bbox=(startx,starty,stopx,stopy),childprocess=False)
    return im
def SS1(clickStartX,clickStartY,clickStopX,clickStopY,curattachdirpc):
    picname=strftime("%Y%m%d%H%M%S")+\'abcdefghijklmno.jpg\'
    imgdir=curattachdirpc+os.path.sep+picname
    im=grabimg(clickStartX,clickStartY,clickStopX,clickStopY)
    w,h=im.size
    im.save(imgdir)
    print(imgdir)
    return w,h,picname,newdir1,objno2
def checkadbdevices():
    global curanddevice
    curanddevice=subprocess.getoutput("adb devices | awk \'{gsub(\\"List of devices attached\\",\\"\\");print}\'")
    print(curanddevice)
    deviceconnected="device"
    if not deviceconnected in curanddevice:
        print("notconnected")
        pass
    return curanddevice
def runadbcommand(command):
    curanddevice=checkadbdevices()
    #nulldevice="error: device \'(null)\' not found"
    deviceconnected="device"
    if deviceconnected in curanddevice:
        subprocess.call(command, shell=True)
checkadbdevices()
dir0=os.path.dirname(os.path.realpath(__file__))
regexindex1=r\'(01)(.{8})(.{4})(011a)\'
patternpic=r\'(010ac480c391c391c391(?!.*010ac480c391c391c391))(.*?)(01c88a)(.{36})(.{28})(.{2})(.{2})(.{2})(.{2})(.{36})(0303)(.{102,})\'
regexindex2=r\'(1123236e6f7465732f2323756e66696c6564(?!.*1123236e6f7465732f2323756e66696c6564))(.*?)(00\\d\\d\\d\\d00\\d\\d)(2323)\'
regexnote1=r\'(0302010201)(.{2})(0a){0,1}\'
regexnote2=r\'(0302010201)(.{2})(.{2})(0a){0,1}\'
thedir=dir0+os.path.sep+"ConvPDF"
wsldir="/mnt/c/Windows"

if sys.platform in [\'linux\', \'linux2\']:
    userid=subprocess.getoutput("awk -F: \'!/root/ && /(\\/bin\\/bash)/ {print $1}\' /etc/passwd")
    userhomedir="/home/"+userid
    from Xlib.display import Display
    import Xlib.display as display
    from Xlib import X, XK
    from Xlib.ext import record
    from Xlib.protocol import rq
    import signal
    dirand="/run/"+userid+"/1000/gvfs"
    dirandcheck=dirand+"*/Internal shared storage"
    if os.path.exists(dirandcheck):
        dirand2=os.listdir(dirand)
        fnnotesdirand=dirand+os.path.sep+dirand2[0]+"/Internal shared storage/fiinote/notes"
        subprocess.call("nautilus file://"+schooldirpc,shell=True)
    if os.path.exists(wsldir):
        thedirw="C:\\\\Users\\\\"+userid+"\\\\AppData\\\\Roaming\\\\FiiNote\\\\@pagkly\\\
otes"
        print(thedirw)
        #thedir=subprocess.getoutput("echo "+thedirw+" | awk \'{gsub(\\"C:\\",\\"/mnt/c\\");gsub(\\"\\\\\\\\\\",\\"/\\");print}\'")
        thedir=re.sub(r"C:","/mnt/c",thedirw)
        thedir=re.sub(r"\\\\","/",thedir)
        print(thedir)
if sys.platform in [\'Windows\', \'win32\', \'cygwin\']:
    print("Windows10")
    userid=subprocess.getoutput("echo %USERNAME%")
    userhomedir=subprocess.getoutput("echo %USERPROFILE%")
    dirand="Z:"
    dirand2=userhomedir+os.path.sep+"AppData"+os.path.sep+"Roaming"+os.path.sep+"FiiNote"+os.path.sep+"@pagkly"+os.path.sep+"notes"

    #time.sleep(3600)
    if os.path.exists(dirand):
        fnnotesdirand=dirand+os.path.sep+"fiinote"+os.path.sep+"notes"+os.path.sep
    if os.path.exists(dirand2):
        thedir=dirand2

autodirpc=userhomedir+os.path.sep+"Documents"+os.path.sep+"Docs"+os.path.sep+"Tech"+os.path.sep+"Automate"
schooldirpc=autodirpc+os.path.sep+"PDF"+os.path.sep+"Sem2"
pdftonotedir=autodirpc+os.path.sep+"FN35AOCV"+os.path.sep+"pdf2note.py"
fnexedir=dir0+os.path.sep+"FiiNote"+os.path.sep+"FiiNote.exe"
pdfreaderexedir=dir0+os.path.sep+"SumatraPDF-3.1.2"+os.path.sep+"SumatraPDF.exe"
winefnexedir="wine "+fnexedir
winepdfreaderexedir="wine "+pdfreaderexedir
#thedir=autodir+"/FiiNote/Save/@pagkly/notes/"
print("THEDIR="+thedir)
fnnotesdirpc=thedir
fnnotesdirandint="/storage/emulated/0/fiinote/notes"
curnotelocpc=fnnotesdirpc+os.path.sep+"andimages.txt"
convpdfdirpc=dir0+os.path.sep+"ConvertedPDF"
noconversion=False
quality=100
pagestart=1
ocvtype=0
#os.remove(curnotelocpc)
#####pdf2note
def dependencies():
    if sys.platform in [\'linux\', \'linux2\']:
        subprocess.call("",shell=True)
    if sys.platform in [\'Windows\', \'win32\', \'cygwin\']:
        subprocess.call("",shell=True)
def setvarnotz(thedir,newdir1):
    global notzdn,notefn,curindexpc,curindexoldpc,curnotzpc,curnotefpc,curattachdirpc,curnotzand,curattachdirand,convpdfdirpc
    notzdn=newdir1+".notz"
    notefn=newdir1+".note"
    curindexpc=thedir+os.path.sep+"index.nti"
    curindexoldpc=thedir+os.path.sep+"index.ntiold"
    curnotzpc=thedir+os.path.sep+notzdn
    curnotefpc=curnotzpc+os.path.sep+notefn
    curattachdirpc=curnotzpc+os.path.sep+"attach"
    curnotefpc1=thedir+os.path.sep+"ConvertedPDF"+os.path.sep+notefn
    curnotzand=fnnotesdirandint+os.path.sep+notzdn
    curattachdirand=curnotzand+os.path.sep+"attach"
    checkdir(curnotzpc,"")
    checkdir(curattachdirpc,"")
    if not os.path.exists(curnotefpc):
        checkfile(curnotefpc)
        ##subprocess.call("adb shell touch "+curnotefand,shell=True)
        firstlineappend(newdir1,curnotefpc)
        runadbcommand("adb push "+curnotefpc+" "+curnotzand)
        print("appendfline")
    appendtext(curnotelocpc,newdir1+".notz","w+")
    runadbcommand("adb push "+curnotzpc+" "+fnnotesdirandint)
    return curnotzpc,curnotefpc,curattachdirpc,curnotzand,curattachdirand
def checknotz(curnotelocpc):
    global objno2,newdir1
    runadbcommand("adb shell \\"su -c \'input keyevent KEYCODE_ESCAPE && sleep 0.1 && killall com.fiistudio.fiinote\'\\"")
    if os.path.exists(curnotelocpc):
        with open(curnotelocpc) as f:
            for line in f:
                if re.search(r"\\.notz",str(line)):
                    newdir1=line
                    newdir1 = re.sub(\'.notz\', \'\', newdir1)
        setvarnotz(fnnotesdirpc,newdir1)
        print(curnotefpc)
        if os.path.exists(curnotzpc) and os.path.exists(curnotefpc) and os.path.exists(curattachdirpc):
            print("checkingcnf")
            with open(curnotefpc,"rb") as f:
                content=f.read()
                contenthex=str(binascii.hexlify(content).decode(\'utf-8\'))
                mo1 = re.search(regexnote1,contenthex)
                mo2 = re.compile(regexnote1)
                if mo2.search(contenthex):
                    objno2=int(mo1.group(2), 16)
                else:
                    mo1 = re.search(regexnote2,contenthex)
                    mo2 = re.compile(regexnote2)
                    if mo2.search(contenthex):
                        prefix=int(mo1.group(2), 16)
                        objno2=int(mo1.group(3), 16)
                        prefix0=((prefix-194)*128)
                        objno2=prefix0+objno2
                    else:
                        objno2=1
                f.close()
        if (not os.path.exists(curnotzpc) or not os.path.exists(curnotefpc) or not os.path.exists(curattachdirpc)) :
            newdir1,objno2=newnotz(fnnotesdirpc,fnnotesdirpc)
    elif not os.path.exists(curnotelocpc) or (not os.path.exists(curnotzpc)):
        newdir1,objno2=newnotz(fnnotesdirpc,fnnotesdirpc)
    print(str(objno2))
    if (objno2>=350):
        newdir1,objno2=newnotz(fnnotesdirpc,fnnotesdirpc)
    return newdir1,objno2,curnotzpc,curnotefpc,curattachdirpc,curnotzand,curattachdirand

def newnotz(thedir1,thedir2):
    global newdir1, objno2
    os.remove(curnotelocpc)
    objno2=1
    newdir1="AOWNLPC00000"+strftime("%Y%m%d%H%M%S")
    #setvarnotz(fnnotesdirandint,newdir1)
    setvarnotz(thedir1,newdir1)
    appendnewnote(newdir1,curindexpc,curindexoldpc)
    return newdir1,objno2
def newnotz0():
    global newdir1, objno2
    os.remove(curnotelocpc)
    CN=checknotz(curnotelocpc)
    newdir1=CN[0]
    objno2=CN[1]

def firstlineappendindex(newdir1,curindexpc):
    return True
def firstlineappend(newdir1,curnotef):
    difftime=getdateinhex()
    newdir1hex=convasciitohex(newdir1,1)
    filetypehex="060000" + \\
                 "01" + difftime + "FFFFFF" + "0000" + \\
                 "01" + difftime + "FFFFFF" + \\
                 "001A" + newdir1hex + \\
                 "000000" + "ffff" + \\
                 "000000" + "000000" + \\
                 "000000" + "000000" + \\
                 "000000" + "000000" + \\
                 "01" + \\
                 "000000" + "000000" + \\
                 "000000" + "000000" + \\
                 "01" + difftime + "FFFFFF" + \\
                 "010302010201"+ \\
                 "01"
    appendtext(curnotef,filetypehex,"wb")


def appendnewpic(w,h,picname,newdir1,objno2,column):
    objno2=int(objno2)
    w=int(w)
    h=int(h)
    newlinehex="0AC480C391C391C39101";
    secondobjhex="C88A";

    objno2c1=int(objno2/14);
    objno2c2=int(objno2/28);
    objno2c21=int(objno2%28);

    #if (objno2c1<32):
    #    prefixposy=169
    #elif (objno2c1>=32):
    #    prefixposy=(int(objno2c1)/34)+169

    if (objno2c1==0):
        prefixposy=169
    elif (objno2c1>0):
        prefixposy=int(objno2c1)+169

    quot=objno2/2;
    rem=objno2%2;
    objnonowc1=objno2/28
    objnonowc2=objno2%28
    objnonowquot14=objnonowc2/2;

    objnonowrem=objnonowc2%2;
    #if (quot>=31):
    #    quotc1=objno2%31;
    #    objnonow=224+quotc1+1;
    #else:
    #    objnonow=224+quot+1;
    #C:\\Users\\SP3\\Documents\\GitHub\\2.3.OCV\\app\\src\\main\\java\\com\\example\\user\\ocv
    ##export DISPLAY=:0.0 && python3 /mnt/c/Users/SP3/Documents/GitHub/FN35OCVbside/FN33and.py
    if objnonowc2==0:
        if objnonowc1>0:
            prefixposy=int(objnonowc1)+169
        objnonow=224+1
    elif objnonowc2>0:
        objnonow=224+objnonowquot14+1
    prefixposyhex=format(math.trunc(prefixposy), \'x\')
    objnohex=format(math.trunc(objnonow), \'x\')

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

    if column=="nearlatest":
        print("picnearlatest;"+str(objno2))
        if objno2<=2:
            print("picnearlatest1")
            column=1
            column=int(column)
            columnc1=int(column/8);
            columnc2=int(column%8);
            if (columnc1==0):
                prefixposx=169
                posx=224+columnc2
            if (columnc1>0):
                prefixposx=169+columnc1
                if (columnc2==0):
                    posx=225
                else:
                    posx=225+columnc2
            posxhex=format(posx, \'x\')
            prefixposxhex=format(prefixposx, \'x\')
            xlochex="E5A5AA"+\\
            "E5AB81"+\\
            "E5A5A9"+\\
            "E19E81"+\\
            "E5A5"+prefixposxhex+\\
            posxhex+"9E81"
        if objno2>2:
            with open(curnotefpc, \'rb\') as f:
                content = f.read()
                cihx=str(binascii.hexlify(content).decode(\'utf-8\'))
                regexc1=re.compile(patternpic)
                #mo1= re.search(patternpic,cihx)
                print("findpatternpic1")
                if regexc1.search(cihx):
                    print("findpatternpic2")
                    mo1= re.search(patternpic,cihx)
                    xlochex=mo1.group(4);
                    prefixposyhex=mo1.group(6);
                    prefixposy=(int(prefixposyhex,16));
                    objnohex=mo1.group(7);
                    objnonow=(int(objnohex,16));
                    posy=(int(mo1.group(8),16))+20;
                    #bf
                    if posy<=191:
                        posyhex="%0.2X" % posy
                    if posy>191:
                        objnonow=objnonow+1
                        if objnonow>231:
                            objnonow=225
                            prefixposy=prefixposy+1
                            prefixposyhex=format(math.trunc(prefixposy), \'x\')
                        objnohex=format(math.trunc(objnonow), \'x\')
                        posy=129+10;
                        posyhex="%0.2X" % posy
                else:
                    pass
    ylochex="E5A5A9"+\\
    "E19E81"+\\
    "E5A5AA"+\\
    "E5AB81"+\\
    "E5A5"+prefixposyhex+\\
    objnohex+posyhex+"81"
    zlochex="E5A5A9"+\\
    "E19E81"+\\
    "E5A5A9"+\\
    "E19E81"+\\
    "E5A5AA"+\\
    "E5AB81"
    #print(xlochex)
    #print(ylochex)
    #print(zlochex)
    if (w<128):
        xpixshex=format(w,\'x\')
        xpixshex=str(xpixshex).zfill(2)
    if (w>=128):
        xquothexint=int(math.trunc(192+(w/64)));
        xremhexint=int(math.trunc(128+(w%64)));
        xquothexs=format(xquothexint,\'x\')
        xremhexs=format(xremhexint,\'x\')
        xpixshex=xquothexs+xremhexs;

    if (h<128):
        ypixshex=format(h,\'x\')
        ypixshex=str(ypixshex).zfill(2)
    if (h>=128):
        yquothexint=int(math.trunc(192+(h/64)));
        yremhexint=int(math.trunc(128+(h%64)));
        yquothexs=format(yquothexint,\'x\')
        yremhexs=format(yremhexint,\'x\')
        ypixshex=yquothexs+yremhexs;

    yscalehexs="";
    xscalehexs="";
    ysuffix="";
    if (w<h):
        a=2717*w;
        div=h*64;
        xscalequotinta=int(math.trunc(a/div));
        xscalequotint=148+xscalequotinta;
        xscalequothexs=format(xscalequotint,\'x\')
        xrem=(((a/div)-xscalequotinta)*64);
        xscaleremint=int(128+xrem);
        xscaleremhexs=format(xscaleremint,\'x\')
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
        yscalequothexs=format(yscalequotint,\'x\')
        yrem=int(math.trunc((((a/div)-yscalequotinta)*64)));
        yscaleremint=int(128+yrem);
        yscaleremhexs=format(yscaleremint,\'x\')
        yscalehexs=ysuffix+yscalequothexs+yscaleremhexs;
    elif (w==h):
        xscalehexs="E2BAA3";
        yscalehexs="E2BAA3";
    objscalehex="0303E293B903E293B903"+xscalehexs+"03"+yscalehexs+"22";
    picnamehex=convasciitohex(picname,1)
    hexc = newlinehex+secondobjhex+xlochex+ylochex+zlochex+objscalehex+picnamehex+xpixshex+ypixshex+"01"

    print("number"+str(objno2))
    print("column"+str(column))
    print("w="+str(w))
    print("h="+str(h))
    print(str(objnonow)+"check")
    print(objnohex)
    print(newlinehex)
    print(xlochex)
    print(ylochex)
    print(zlochex)
    append=""
    if os.path.exists(curnotefpc) and objno2>=0:
        with open(curnotefpc,"rb") as f:
            content=f.read()
            cihx=str(binascii.hexlify(content).decode(\'utf-8\'))
            mo1=re.search(regexnote1,cihx)
            mo2=re.compile(regexnote1)
            if mo2.search(cihx):
                print("found")
                objno2=int(mo1.group(2), 16)
                objno2+=1
                prefixhex=""
                if objno2<=2:
                    print("found")
                    totalobjhex=str(format(objno2,\'x\')).zfill(2)
                    print(totalobjhex)
                    replace1 = re.sub(regexnote1, mo1.group(1)+totalobjhex, cihx)
                    ##append=replace1+newlinehex+secondobjhex+objscalehex+picnamehex+xpixshex+ypixshex+"01"
                    append=replace1+hexc
                if objno2>2 and objno2<128:
                    print("found2")
                    totalobjhex=str(format(objno2,\'x\')).zfill(2)
                    print(totalobjhex)
                    replace1 = re.sub(regexnote1, mo1.group(1)+totalobjhex, cihx)
                    append=replace1+hexc
                if objno2==128:
                    print("found3")
                    prefix=194;
                    prefixhex=format(prefix,\'x\')
                    print(prefixhex)
                    totalobjhex=str(format(objno2,\'x\')).zfill(2)
                    print(totalobjhex)
                    replace1 = re.sub(regexnote1, mo1.group(1)+prefixhex+totalobjhex, cihx)
                    append=replace1+hexc
                if objno2>128:
                    print("found4")
                    mo1=re.search(regexnote2,cihx)
                    mo2=re.compile(regexnote2)
                    if mo2.search(cihx):
                        print("found5")
                        objno2=int(mo1.group(3), 16)
                        objno2+=1
                        ##prefix=int((objno2-128)/64);
                        ##prefix=mo1.group(2)
                        prefix=int(mo1.group(2), 16)
                        ##prefix=194+prefix;
                        prefix=prefix+int((objno2-128)/64);
                        #if (objno2<192):
                            #prefix=int((objno2-128)/64);
                            #prefix=194+prefix;
                        #if (objno2>=192):
                            #prefix=int((objno2-192)/64);
                            #prefix=195+prefix;
                        prefixhex=format(prefix,\'x\')
                        print(prefixhex)
                        if (objno2<192):
                            totalobjhex=str(format(objno2,\'x\')).zfill(2)
                        if (objno2>=192):
                            totalobjhex=str(format((128+int((objno2-192)%64)),\'x\')).zfill(2)
                        print(totalobjhex)
                        replace1 = re.sub(regexnote2, mo1.group(1)+prefixhex+totalobjhex, cihx)
                        append=replace1+hexc
    if append:
        appendtext(curnotefpc,append,"wb")
    return objno2,curattachdirpc

def appendnewnote(newdir1,curindexpc,curindexoldpc):
    global replace1, replace2
    replace1=""
    replace2=""
    with open(curindexpc, \'rb\') as f:
        print("checkingindexcur")
        content = f.read()
        cihx=str(binascii.hexlify(content).decode(\'utf-8\'))
        regexc1=re.compile(regexindex1)
        if regexc1.search(cihx):
            mo1= re.search(regexindex1,cihx)
            p1d=(int(mo1.group(3), 16))+1
            p1dhex="%0.4X" % p1d
            regexr1=mo1.group(1)+mo1.group(2)+p1dhex+mo1.group(4)
            replace1 = re.sub(regexindex1, regexr1, cihx)
        else:
            pass
        difftime=getdateinhex()
        newdir1hex=convasciitohex(newdir1,1)
        newfolderhex1="011A"+newdir1hex+"00" + \\
                        "00" + \\
                        "04" + \\
                        "00" + \\
                        "00" + \\
                        "01" + difftime + "FFFFFF" + "0000" + \\
                        "01" + difftime + "FFFFFF" + "0000" + \\
                        "001A" + newdir1hex + \\
                        "00" + "1123236E6F7465732F2323756E66696C6564" + "05" + \\
                        "00"+ \\
                        "000000" + \\
                        "000000" + \\
                        "000000" + \\
                        "01" + difftime + "FFFFFF" + "0000" + \\
                        "01" + difftime + "FFFFFF"
        regexc2=re.compile(regexindex2)
        if regexc2.search(replace1):
            mo2 = re.search(regexindex2,replace1)
            regexr2=mo2.group(1)+mo2.group(2)+newfolderhex1+mo2.group(3)+mo2.group(4)
            replace2 = re.sub(regexindex2, regexr2, replace1)
        appendtext(curindexpc,replace2,"wb")
        print("donecheckingindexcur")
    return True






#####libocvfinal
import cv2
import numpy as np
a=1000
def convertrest(imgdir,imgname,afterimg,a,ocvtype):
    ##a=0
    print(imgname)
    #time.sleep(3600)
    if ocvtype==2 or ocvtype==21:
        image = cv2.imread(imgdir+os.path.sep+imgname)
    if ocvtype==1 or ocvtype==3:
        image = cv2.imread(imgdir+os.path.sep+imgname)
    imgw,imgh=imgsize(imgdir+os.path.sep+imgname)
    timgh=0.10*imgw
    bimgh=0.90*imgw
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
    _, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours
    # for each contour found, draw a rectangle around it on original image
    print(contours)
    for contour in contours:
        a-=1
        # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)
        # discard areas that are too large
        img=image[y-5:y+h+5, x-5:x+w+5]
        if h>10 and w>10 and y>timgh and y<bimgh:
            ##cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
            img=image[y-5:y+h+5, x-5:x+w+5]
            cv2.imwrite(imgdir+os.path.sep+str(a)+"t2"+imgname, img)
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), -1)
    # write original image with added contours to disk
    cv2.imwrite(imgdir+os.path.sep+"contouredc2"+afterimg, image)
    #ocv1/3
    ##converttext(dir_path,"13.jpg",1000)
    #ocv2
    ##converttext(dir_path,"conv0003.jpg",1000)

def converttext(imgdir,imgname,afterimg,a,ocvtype,colour,testing):
    large=cv2.imread(imgdir+os.path.sep+imgname)
    imgw,imgh=imgsize(imgdir+os.path.sep+imgname)
    timgh=0.10*imgw
    bimgh=0.90*imgw
    print(imgdir+os.path.sep+imgname+" "+str(imgw)+","+str(imgh))
    if ocvtype==1 or ocvtype==2 or ocvtype==4 or ocvtype==5:
        rgb=large
        rgb=cv2.pyrDown(large)
    if ocvtype==3:
        rgb=cv2.pyrDown(large)
    if ocvtype==21:
        rgb=cv2.pyrUp(large)
        rgb=cv2.pyrUp(rgb)
    rgb2=rgb.copy()
    small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    #cv2.imwrite(imgdir+os.path.sep+\'grab1.png\',connected)
    # using RETR_EXTERNAL instead of RETR_CCOMP
    _, contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    mask = np.zeros(bw.shape, dtype=np.uint8)
    #print(contours)
    for idx in range(len(contours)):

        x, y, w, h = cv2.boundingRect(contours[idx])
        mask[y:y+h, x:x+w] = 0
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
        if ocvtype==1 or ocvtype==3 :
            if r > 0.45 and w > 100 and h > 10 and y>timgh and y<bimgh:
                a-=1
                ##img = rgb[y:y+h-1, x:x+w-1]
                img=rgb[y-5:y+h+5, x-5:x+w+5]
                cv2.imwrite(imgdir+os.path.sep+str(a)+"t1"+imgname, img)
                cv2.rectangle(rgb, (x, y), (x+w, y+h), (255, 255, 255), -1)
        elif ocvtype==2 or ocvtype==21:
            if r > 0.45 and w > 25 and h > 10:
                a-=1
                ##img = rgb[y+15:y+h-15, x+15:x+w-15]
                img=rgb[y:y+h, x:x+w]
                if ocvtype==2:
                    cv2.imwrite(imgdir+os.path.sep+str(a)+"t1"+imgname, img)
                elif ocvtype==21:
                    cv2.rectangle(rgb, (x-3, y-3), (x+w+3, y+h+3), (255, 255, 255), -1)
                cv2.rectangle(rgb, (x, y), (x+w, y+h), (255, 255, 255), -1)
                converttext(imgdir, str(a)+"t1"+imgname+".jpg","2"+afterimg+".jpg",a,4,"neutral",testing)
        elif ocvtype==4:
            if r > 0.45 and w > 25 and h > 10:
                a-=1
                ##img = rgb[y:y+h-1, x:x+w-1]
                img=rgb[y-5:y+h+5, x-5:x+w+5]
                cv2.imwrite(imgdir+os.path.sep+str(a)+"t3"+imgname, img)
                cv2.rectangle(rgb, (x, y), (x+w, y+h), (255, 255, 255), -1)
        elif ocvtype==5:
            if w > 25 and h > 10 and y>timgh and y<bimgh:
                a-=1
                ##img = rgb[y:y+h-1, x:x+w-1]
                img=rgb[y-5:y+h+5, x-5:x+w+5]
                cv2.imwrite(imgdir+os.path.sep+str(a)+"t3"+imgname, img)
                cv2.rectangle(rgb, (x, y), (x+w, y+h), (255, 255, 255), -1)

        if testing and y>timgh and y<bimgh:
            #img0=rgb[y-5:y+h+5, x-5:x+w+5]
            #cv2.imwrite(imgdir+os.path.sep+str(a)+"t0qc"+imgname, img0)
            #cv2.rectangle(rgb2, (x, y), (x+w, y+h), (255, 255, 255), -1)
            #print("testing")
            pass
    if ocvtype==1 or ocvtype==3:
        ##rgb = cv2.pyrUp(rgb)
        cv2.imwrite(imgdir+os.path.sep+afterimg, rgb)
        #convertrest(imgdir,"contouredc"+imgname,afterimg,a,ocvtype)
        #converttext(imgdir,"contouredc"+imgname,"contouredc2"+afterimg,a,5,"neutral",testing)
    if ocvtype==4:
        ##rgb = cv2.pyrUp(rgb)
        cv2.imwrite(imgdir+os.path.sep+afterimg, rgb)
        convertrest(imgdir,"contouredc"+imgname,afterimg,a,ocvtype)
    if ocvtype==5:
        cv2.imwrite(imgdir+os.path.sep+afterimg, rgb)
#    cv2.imwrite(imgdir+os.path.sep+afterimg+".jpg", img)
    if testing:
        #cv2.imwrite(imgdir+os.path.sep+"mask"+afterimg, mask)
        #cv2.imwrite(imgdir+os.path.sep+"rect2"+afterimg, rgb2)
        print("testing")
        pass
def convertcolour(imgdir,imgname,afterimg,colour,size):
    a=1000
    idx=0
    # Convert BGR to HSV
    frame=cv2.imread(imgdir+os.path.sep+imgname)
    if size=="down":
        frame=cv2.pyrDown(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if colour=="red":
        lowerr = np.array([110,50,50])
        upperr = np.array([130,255,255])
        mask = cv2.inRange(hsv, lowerr, upperr)
    elif colour=="green":
        lowerg=np.array([33,80,40])
        upperg=np.array([102,255,255])
        mask = cv2.inRange(hsv, lowerg, upperg)
    elif colour=="blue":
        lowerb = np.array([110,50,50])
        upperb = np.array([130,255,255])
        mask = cv2.inRange(hsv,lowerb,upperb)
    #cv2.imwrite(imgdir+os.path.sep+\'grabblue.png\', mask)

    kernel = np.ones((5,5),\'int\')
    dilated = cv2.dilate(mask,kernel)
    ##cv2.imwrite(imgdir+os.path.sep+\'grabblue1.png\',dilated)
    #res = cv2.bitwise_and(frame,frame,mask=mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    connected = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    ##cv2.imwrite(imgdir+os.path.sep+\'grabblue2.png\',connected)

    #_,thrshed = cv2.threshold(cv2.cvtColor(connected,cv2.COLOR_BGR2GRAY),3,255,cv2.THRESH_BINARY)
    #_,contours,hier = cv2.findContours(thrshed,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    _, contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #print(contours)
    for idx in range(len(contours)):
        a-=1
        x, y, w, h = cv2.boundingRect(contours[idx])
        mask[y:y+h, x:x+w] = 0
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
        if r > 0.45 and w > 50 and h > 10:
            a-=1
            img=frame[y-5:y+h+5, x-5:x+w+5]
            cv2.imwrite(imgdir+os.path.sep+str(a)+"t1blue"+imgname, img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), -1)
    cv2.imwrite(imgdir+os.path.sep+afterimg, frame)

def pushnewdir1toand(newdir1,curindexpc,curindexoldpc):
    curanddevice=checkadbdevices()
    #nulldevice="error: device \'(null)\' not found"
    deviceconnected="device"
    if deviceconnected in curanddevice:
        copydir(fnnotesdirpc+os.path.sep+newdir1,fnnotesdirand)
        appendnewnote(newdir1,curindexpc,curindexoldpc)
    return True
def runpdftonote(convpdfdirpc,pdfdir,pdfname,pagestart,pageend,ocvtype,continuenote,testing):
    print("startpdftonote")
    column=1
    if not continuenote:
        if os.path.exists(curnotelocpc):
            os.remove(curnotelocpc)
    CN=checknotz(curnotelocpc)
    newdir1=CN[0]
    objno2=CN[1]
    pageend=pageend+1
    if noconversion:
        print("noconv")
        a=0
        b=objno2
        for i in range(pagestart,pageend) :
            a+=1
            print("Page"+str(i))
            imgname=convertpdf2jpg(pdfdir,pdfname,quality,i,outputdir)
            if a==10 or i==(pageend-1):
                convertjpg2note(outputdir,column,newdir1,objno2)
                a=0
                column+=1
            print(imgname)
    if not noconversion:
        for i in range(pagestart,pageend) :
            a=1000
            ##i-=1
            imgname=convertpdf2jpg(pdfdir,pdfname,quality,i,convpdfdirpc)
            print(str(i)+" "+imgname)
            if testing:
                pdfconvimg=convpdfdirpc+os.path.sep+"contouredc"+imgname+".jpg"
                pdfdir0img=dir0+os.path.sep+"contouredc"+imgname+".jpg"
                converttext(convpdfdirpc,imgname+".jpg","contouredc"+imgname+".jpg",1000,1,"neutral",testing)
                a-=1
                column+=1
            if not testing:
                straight=True
                if not straight:
                    pdfconvimg=convpdfdirpc+os.path.sep+"contouredc"+imgname+".jpg"
                    pdfdir0img=dir0+os.path.sep+"contouredc"+imgname+".jpg"
                    #convertcolour(convpdfdirpc,imgname+".jpg","contouredc"+imgname+".jpg","green","down")
                    convertcolour(convpdfdirpc,imgname+".jpg","contouredc"+imgname+".jpg","green","")
                    subprocess.call("mv "+pdfconvimg+" "+pdfdir0img,shell=True)
                    objno2=convertjpg2note(convpdfdirpc,2,newdir1,1)

                    shutil.rmtree(convpdfdirpc)
                    checkdir(convpdfdirpc,"")
                    subprocess.call("mv "+pdfdir0img+" "+pdfconvimg,shell=True)
                    convertcolour(convpdfdirpc,"contouredc"+imgname+".jpg","contouredc"+imgname+".jpg","blue","")
                    subprocess.call("mv "+pdfconvimg+" "+pdfdir0img,shell=True)
                    objno2=convertjpg2note(convpdfdirpc,1,newdir1,objno2)

                    shutil.rmtree(convpdfdirpc)
                    checkdir(convpdfdirpc,"")
                    subprocess.call("mv "+pdfdir0img+" "+pdfconvimg,shell=True)
                    converttext(convpdfdirpc,"contouredc"+imgname+".jpg","contouredc"+imgname+".jpg",1000,1,"neutral","")
                    subprocess.call("mv "+pdfconvimg+" "+pdfdir0img,shell=True)
                    objno2=convertjpg2note(convpdfdirpc,2,newdir1,objno2)

                if straight:
                    #shutil.rmtree(convpdfdirpc)
                    #checkdir(convpdfdirpc,"")
                    #subprocess.call("mv "+pdfdir0img+" "+pdfconvimg,shell=True)
                    converttext(convpdfdirpc,imgname+".jpg","contouredc"+imgname+".jpg",1000,1,"neutral","")
                    #subprocess.call("mv "+pdfconvimg+" "+pdfdir0img,shell=True)
                    objno2=convertjpg2note(convpdfdirpc,column,newdir1,objno2)

                ###subprocess.call("cp "+convpdfdirpc+os.path.sep+imgname+".jpg "+pdfdir+os.path.sep+"attach/00.jpg",shell=True)
                ###subprocess.call("cp "+convpdfdirpc+os.path.sep+imgname+".jpg "+pdfdir+os.path.sep+"attach",shell=True)
                a-=1
                column+=1
    if args.pdfmdir :
        relevant_path=args.pdfmdir
        included_extensions = [\'pdf\']
        pdf_names = [fn for fn in os.listdir(relevant_path)
                      if any(fn.endswith(ext) for ext in included_extensions)]
        print(len(pdf_names))
        for i in range(0,len(pdf_names)):
            print(pdf_names[i])
            subprocess.call("python3 "+pdftonotedir+" -pdir \\""+relevant_path+"\\" -p \\""+pdf_names[i]+"\\" -d 100 -t 1 -nc 1" ,shell=True)
def runshowpdf(convpdfdirpc,pdfdir,pdfname,pagestart,pageend,ocvtype,continuenote):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    convpdfdirpc1=convpdfdirpc+os.path.sep+pdfname
    if not os.path.exists(convpdfdirpc1):
        os.makedirs(convpdfdirpc1)
    imgname=convertpdf2jpg(pdfdir,pdfname,quality,pagestart,convpdfdirpc1)
    imgdir=convpdfdirpc+os.path.sep+pdfname+os.path.sep+imgname+".jpg"
    print(imgdir)
    img=mpimg.imread(imgdir)
    imgplot=plt.imshow(img)
    #countarea
    plt.show()
    image = PIL.Image.open(open(imgdir, \'rb\'))
    #image.show()
    return True

#https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
#import tkinter as tk
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    if __name__ == "__main__":
        rootimgv = tk.Tk()
        #aMainApplication(root).pack(side="top", fill="both", expand=True)
        rootimgv.mainloop()
def prevpage(pdfdir,page):
    page+=1
    showpdf()
    return True
def nextpage(pdfdir,page):
    page+=1
    showpdf()
    return True
def detecttouch():
    return True
def progresswhitelist():
    return True
def whitelistarea(xpos,ypos,wimg,himg):
    return True
def progresspage():
    return True

def convertpdf2jpg(pdfdir,pdfname,quality,page,convpdfdirpc):
    ##for i in range(int(pagestart),int(pageend)):
    #ppmcommand2="convert -verbose -density "+str(quality)+" -trim "+pdfdir+os.path.sep+pdfname+"["+str(page)+"] -quality 100 -flatten -sharpen 0x1.0 "+convpdfdirpc+os.path.sep+convpname
    pdfpage=subprocess.getoutput("pdfinfo \\""+pdfdir+os.path.sep+pdfname+"\\" | grep Pages: | awk \'{print $2}\'")
    pagez=str(page).zfill(4)
    convpname="conv"+pagez
    ppmcommand="pdftoppm \\""+pdfdir+os.path.sep+pdfname+"\\" \\""+convpdfdirpc+os.path.sep+convpname+"\\" -jpeg -f "+str(page)+" -singlefile"
    #ppmcommand="pdftoppm \\""+pdfdir+os.path.sep+pdfname+"\\" \\""+convpdfdirpc+os.path.sep+convpname+"\\" -png -f "+str(page)+" -singlefile"
    print(ppmcommand)
    print(convpname)
    subprocess.call(ppmcommand,shell=True)
    imgdir=convpdfdirpc+os.path.sep+convpname+".jpg"
    while True:
        if os.path.exists(imgdir):
            print(imgdir)
            break
    return convpname
def convertpdf2jpg2(pdfdir,pdfname,quality,page,convpdfdirpc,ver):
        ##for i in range(int(pagestart),int(pageend)):
        #ppmcommand2="convert -verbose -density "+str(quality)+" -trim "+pdfdir+os.path.sep+pdfname+"["+str(page)+"] -quality 100 -flatten -sharpen 0x1.0 "+convpdfdirpc+os.path.sep+convpname
        ossep=os.path.sep
        if not os.path.exists(convpdfdirpc):
                os.makedirs(convpdfdirpc)
        if sys.platform in [\'linux\', \'linux2\']:
                pdfinfocommand="pdfinfo"
                pdftoppmcommand="pdftoppm"
                pdfpage=subprocess.getoutput(pdfinfocommand+" \\""+pdfdir+os.path.sep+pdfname+"\\" | grep Pages: | awk \'{print $2}\'")
                pdfpage=int(pdfpage)
        if sys.platform in [\'Windows\', \'win32\', \'cygwin\']:
                userid=subprocess.getoutput("echo %USERNAME%")
                userhomedir=subprocess.getoutput("echo %USERPROFILE%")
                popplerver="poppler-0.51"
                popplerdir="C:\\\\Users\\\\"+userid+"\\\\Downloads\\\\"+popplerver+"_x86\\\\"+popplerver+"\\\\bin"
                pdfinfocommand=popplerdir+"\\\\pdfinfo.exe"
                pdftoppmcommand=popplerdir+"\\\\pdftoppm.exe"
                if ver=="wsl":
                        pdfdir0=conwindirtovwsldir(pdfdir)
                        convpdfdirpc0=conwindirtovwsldir(convpdfdirpc)
                        print("convertpdf2jpginwsl="+pdfdir)
                        ##pdfpage=subprocess.getoutput("wsl pdfinfo \\""+pdfdir0+"/"+pdfname+"\\" | grep Pages: | awk \'{print $2}\'")
                        #ppmcommand="wsl pdftoppm \\""+pdfdir0+"/"+pdfname+"\\" \\""+convpdfdirpc0+"/"+convpname+"\\" -jpeg -f "+str(page)+" -singlefile"
                        imgdir=convpdfdirpc+os.path.sep+convpname+".jpg"
                pdfpage0=subprocess.getoutput(pdfinfocommand+" \\""+pdfdir+os.path.sep+pdfname+"\\"")
                #print("pp0="+pdfpage0)
                #https://stackoverflow.com/questions/15422144/how-to-read-a-long-multiline-string-line-by-line-in-python
                for line in pdfpage0.splitlines():
                        #print(line)
                        #lineResult = libLAPFF.parseLine(line)
                        lineResult=line
                        pdfpage1=lineResult
                        #print("pp1="+pdfpage1)
                        if re.search(r"Pages:",str(line)):
                                pdfpage1=line
                                print("pp1="+pdfpage1)
                                pdfpage2 = re.sub(r"(Pages:)([ ])*", \'\', pdfpage1)
                                print("pp2="+pdfpage2)
                                pdfpage=int(pdfpage2)
        print("totalp="+str(pdfpage))
        if page<0:
                page=1
        if page<=pdfpage:
                pagez=str(page).zfill(4)
        if page>pdfpage:
                pagez=str(pdfpage).zfill(4)
        convpname="conv"+pagez
        img0=convpdfdirpc+os.path.sep+convpname
        imgdir=img0+".jpg"
        if not os.path.exists(imgdir):
                ppmcommand=pdftoppmcommand+" \\""+pdfdir+os.path.sep+pdfname+"\\" \\""+img0+"\\" -jpeg -f "+str(page)+" -singlefile"
                #ppmcommand=pdftoppmcommand+" \\""+pdfdir+os.path.sep+pdfname+"\\" \\""+img0+"\\" -png -f "+str(page)+" -singlefile"
                print(ppmcommand)
                subprocess.call(ppmcommand,shell=True)
                #time.sleep(5)
        while True:
                if os.path.exists(imgdir):
                        print(imgdir)
                        break
        return imgdir

def conwindirtovwsldir(windir):
    checkdir="C:\\\\Windows"
    wsldir=""
    #if os.path.exists(checkdir):
        #userid=subprocess.getoutput("awk -F: \'!/root/ && /(\\/bin\\/bash)/ {print $1}\' /etc/passwd")
        #userid=subprocess.getoutput("echo \\"%USERNAME%\\"")
    print("wd="+windir)
    wsldir=re.sub(r"C:","/mnt/c",windir)
    wsldir=re.sub(r"\\\\","/",wsldir)
    print("ad="+wsldir)
    return wsldir

def convertjpg2note(folderlocation,column,newdir1,objno2):
    print("runengine")
    objno2re=objno2
    allfnpicdir=os.listdir(folderlocation)
    for i in range(0,len(allfnpicdir)):
        Time=strftime("%Y%m%d%H%M%S")
        objno2rez=str(objno2re).zfill(2)
        picname=Time+\'abcdefghijklm\'+objno2rez+\'.jpg\'
        print(picname)
        if objno2re>=0:
            picdir=folderlocation+ os.path.sep +  allfnpicdir[i]
            picdirnew=folderlocation + os.path.sep + picname
            print(picdir)
            subprocess.call("cp \\""+picdir+"\\" \\""+picdirnew+"\\"", shell=True)
            os.remove(picdir)
            subprocess.call("cp \\""+picdirnew+"\\" \\""+curattachdirpc+"\\"", shell=True)
            attachfnanddir=fnnotesdirandint+os.path.sep+newdir1+".notz/attach"
            print(attachfnanddir)
            w, h=imgsize(picdirnew)
            appendnewpic(w,h,picname,newdir1,objno2re,"nearlatest")
            runadbcommand("adb push -p \\""+picdirnew+"\\" \\""+attachfnanddir+"\\"")
            objno2re+=1
        runadbcommand("adb push \\""+curnotefpc+"\\" \\""+curnotzand+"\\"")
    return objno2re

def setvarconvpdf():
    global ocvtype,noconversion
    testing=False
    continuenote=False
    showpdf=False
    if args.testing:
        testing=True
    if args.continuenote :
        continuenote=True
    if args.pdfdir:
        pdfdir=args.pdfdir
    else:
        pdfdir=dir0
        #print("Slide=100")
        #print("Tbook=300")
        #print("Work=300/Adobe")
    if args.pdfname:
        shutil.rmtree(convpdfdirpc)
        checkdir(convpdfdirpc,"")
        pdfname=args.pdfname
        if args.density :
            quality=int(args.density)
        if args.pagestart :
            pagestart=int(args.pagestart)
        if args.pageend :
            pageend=int(args.pageend)
            pageend=pageend
        else:
            pdfpage=subprocess.getoutput("pdfinfo \\""+pdfdir+os.path.sep+pdfname+"\\" | grep Pages: | awk \'{print $2}\'")
            pageend=int(pdfpage)
        if args.type:
            ocvtype=int(args.type)
        if args.noconversion=="1":
            noconversion=True
        print("PDFDir="+pdfdir+os.path.sep+pdfname+" Page="+str(pagestart)+" to "+str(pageend))
        print("ocvt"+str(ocvtype))
        if args.showpdf:
            runshowpdf(convpdfdirpc,pdfdir,pdfname,pagestart,pageend,ocvtype,continuenote)
        if not args.showpdf:
            if not testing:
                runpdftonote(convpdfdirpc,pdfdir,pdfname,pagestart,pageend,ocvtype,continuenote,"")
            if testing:
                continuenote=False
                runpdftonote(convpdfdirpc,pdfdir,pdfname,pagestart,pageend,ocvtype,continuenote,testing)
    return True
args = parse_args()
setvarconvpdf()
#convertcolour(convpdfdirpc,imgname+".jpg","green")
#convertcolour("/home/user/Pictures","Screenshot from 2018-07-05 20-04-46.png","green")
'