import subprocess, sys, os
import shutil
import re
import binascii
import time
import math
import tkinter as tk
from libFN33and import checknotz
from PIL import Image
import pyscreenshot
from time import gmtime,strftime

dir_path = os.path.dirname(os.path.realpath(__file__))

if sys.platform in ['linux', 'linux2'] or sys.platform in ['Windows', 'win32', 'cygwin']:
    #fnsavedirpc="/home/user/Documents/Docs/Tech/Automate/FiiNote/Save/@pagkly/notes/"
    if sys.platform in ['linux', 'linux2']:
        dirand="/run/user/1000/gvfs"
        dirand2=os.listdir(dirand)
        fnsavedirand=dirand+"/"+dirand2[0]+"/Internal shared storage/fiinote/notes/"
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        dirand="Z:\\"
        fnsavedirand=dirand+"fiinote\\notes\\"
        
    fnnotespdir=fnsavedirand
    print(fnnotespdir)
    indexcur = fnnotespdir+'index.nti'
    indexold = fnnotespdir+'indexold.nti'
    indexcure= "/home/user/indexedit.nti"
notef=""

def removefile(dirname):
    if os.path.exists(dirname):
        subprocess.call("rm -f "+dirname+" ;", shell=True)

def runengine(folderlocation,column,newdir1,objno2):
        curnotedir=dir_path+os.path.sep+"andimages.txt"
        print("runengine")
        print("runengine2")
        a=objno2
        allfnpicdir=os.listdir(folderlocation)
        for i in range(0,len(allfnpicdir)):
            Time=strftime("%Y%m%d%H%M%S")
            az=str(a).zfill(2)
            picname=Time+'abcdefghijklm'+az+'.jpg'
            print(picname)
            ##if a==0 :
                ##CN=checknotz(curnotedir)
                ##newdir1=CN[0]
                ##objno2=CN[1]
                ##a=objno2
                ##newdir1="AOWNLPC00000"+Time
                ##curnotz=fnnotespdir+newdir1+".notz"
                ##curnotef=fnnotespdir+newdir1+".notz"+os.path.sep+newdir1+".note"
                ##curpicdir=fnnotespdir+newdir1+".notz"+os.path.sep+"attach"
                ##a+=1
            if a>=0:
                source=folderlocation
                print(folderlocation + os.path.sep +  allfnpicdir[i])
                subprocess.call("cp \""+folderlocation + os.path.sep +  allfnpicdir[i]+"\" \""+folderlocation + os.path.sep + picname+"\"", shell=True)
                os.remove(folderlocation+os.path.sep +allfnpicdir[i])
                imgdir=folderlocation+os.path.sep+picname
                ##andfndir=fnnotespdir+os.path.sep
                andfndir="/storage/emulated/0/fiinote/notes/"
                attachfnanddir=andfndir+newdir1+".notz/attach"
                print(attachfnanddir)
                im = Image.open(imgdir)
                w, h = im.size
                appendnewpic2(w,h,picname,newdir1,a,column)
                subprocess.call("adb push -p \""+imgdir+"\" \""+attachfnanddir+"\"",shell=True)
                a+=1
            andfndir="/storage/emulated/0/fiinote/notes/"
            curnotz=andfndir+newdir1+".notz"
            curnotef=dir_path+os.path.sep+"ConvertedPDF"+os.path.sep+newdir1+".note"
            subprocess.call("adb push \""+curnotef+"\" \""+curnotz+"\"",shell=True)
            ##if a>=30:
            ##    a=0
            ##a<30 and 
                
def appendnewpic2(w,h,picname,newdir1,objno2,column):
    objno2=int(objno2)
    column=int(column)
    print("number"+str(objno2))
    print("column"+str(column))
    curnotef=dir_path+os.path.sep+"ConvertedPDF"+os.path.sep+newdir1+".note"
    newlinehex="0AC480C391C391C39101";
    secondobjhex="C88A";
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
    
    posxhex=format(posx, 'x')
    prefixposxhex=format(prefixposx, 'x')
    xlochex="E5A5AA"+\
             "E5AB81"+\
             "E5A5A9"+\
             "E19E81"+\
             "E5A5"+prefixposxhex+\
             posxhex+"9E81"
    w=int(w)
    h=int(h)
    objno2c1=int(objno2/14);
    ##if (objno2c1==0):
    ##    prefixposy=169
    ##elif (objno2c1>0):
    ##    prefixposy=169+objno2c1
    ##if (objno2c1<32):
    ##    prefixposy=169
    ##elif (objno2c1>=32):
    ##    prefixposy=int(objno2c1/34)+169
    ##objno2c1=int(objno2);
    ##if (objno2c1<32):
    ##    prefixposyhex="A9"
    ##elif (objno2c1>=32):
    ##    prefixposy=int(objno2c1/34)+169
    ##    prefixposyhex=format(math.trunc(prefixposy), 'x')
    if (objno2c1==0):
        prefixposyhex="A9"
    elif (objno2c1>0):
        prefixposy=int(objno2c1)+169
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
    print(newlinehex)
    print(xlochex)
    print(ylochex)
    print(zlochex)
    if os.path.exists(curnotef) and objno2>=1:
        with open(curnotef,"rb") as f:
            content=f.read()
            cihx=str(binascii.hexlify(content).decode('utf-8'))
            regex_number=r'(0302010201)(.{2})'
            mo1=re.search(regex_number,cihx)
            mo2=re.compile(regex_number)
            if mo2.search(cihx):
                print("found")
                objno2=int(mo1.group(2), 16)
                objno2+=1
                prefixhex=""
                if objno2==2:
                    print("found")
                    totalobjhex=str(format(objno2,'x')).zfill(2)
                    print(totalobjhex)
                    replace1 = re.sub(regex_number, mo1.group(1)+totalobjhex, cihx)
                    ##append=replace1+newlinehex+secondobjhex+objscalehex+picnamehex+xpixshex+ypixshex+"01"
                    append=replace1+hexc
                    appendcurnotef(curnotef,append)
                if objno2>2 and objno2<128:
                    print("found2")
                    totalobjhex=str(format(objno2,'x')).zfill(2)
                    print(totalobjhex)
                    replace1 = re.sub(regex_number, mo1.group(1)+totalobjhex, cihx)
                    append=replace1+hexc
                    appendcurnotef(curnotef,append)
                if objno2==128:
                    print("found3")
                    prefix=194;
                    prefixhex=format(prefix,'x')
                    print(prefixhex)
                    totalobjhex=str(format(objno2,'x')).zfill(2)
                    print(totalobjhex)
                    replace1 = re.sub(regex_number, mo1.group(1)+prefixhex+totalobjhex, cihx)
                    append=replace1+hexc
                    appendcurnotef(curnotef,append)
                if objno2>128:
                    print("found4")
                    regex_number=r'(0302010201)(.{2})(.{2})'
                    mo1=re.search(regex_number,cihx)
                    mo2=re.compile(regex_number)
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
                        prefixhex=format(prefix,'x')
                        print(prefixhex)
                        if (objno2<192):
                            totalobjhex=str(format(objno2,'x')).zfill(2)
                        if (objno2>=192):
                            totalobjhex=str(format((128+int((objno2-192)%64)),'x')).zfill(2)
                        print(totalobjhex)
                        replace1 = re.sub(regex_number, mo1.group(1)+prefixhex+totalobjhex, cihx)
                        append=replace1+hexc
                        appendcurnotef(curnotef,append)
                        
                        
    return objno2

def appendcurnotef(curnotef,append):
    with open(curnotef,"wb") as fout:
        append=bytes(bytearray.fromhex(append))
        fout.write(append)
        fout.close()
