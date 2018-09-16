#ad\3aa3551
#b'blob 7225\x00
import math
def h2d(hexstring):
    return ("decno("+str(hexstring)+")="+str(int(hexstring, 16)) )
#https://codebeautify.org/hex-decimal-converter#
def d2h(decno):
    return ("hexstring("+str(decno)+")="+format(decno,"x"))
#https://codebeautify.org/decimal-hex-converter#

patternpic=r\'(01 c8 8a)(.{54})(.{32})(.{3})(.{3})(.{3})(.{3})(.{54})(03 03)(.{153,})\'
patternpicwxhex=r\'(01 [cC]8 8[aA].)(.{18})(.{18})(.{18})(.{18})(.{18})(.{18})(.{18})(.{18})(.{18})(03.)(0.{8,11})(0.{8,11})(0.{8,11})(0.{8,11})(.*)(67.)\'
patternpicpython=r\'(01[cC]88[aA])(.{12})(.{12})(.{12})(.{12})(.{12})(.{12})(.{12})(.{12})(.{12})(03)(0.{5,7})(0.{5,7})(0.{5,7})(0.{5,7})(.*)(67.)\'
#(01[cC]88[aA])(.{12})(.{12})(.{12})(.{12})(.{12})(.{12})(.{12})(.{12})(.{12})(03)(0.{5,7})(0.{5,7})(0.{5,7})(0.{5,7})
#(01[cC]88[aA]){0,1}(.{12}){0,1}(.{12}){0,1}(.{12}){0,1}(.{12}){0,1}(.{12}){0,1}(.{12}){0,1}(.{12}){0,1}(.{12}){0,1}(.{12}){0,1}(03){0,1}(0.{5,7})(0.{5,7})(0.{5,7})(0.{5,7})
replacewith=r\'\
$1\
$2\
$3\
$4\
\
$5\
$6\
$7\
\
$8\
$9\
$10\
\
$11\
$12\
$13\
$14\
$15\
\
$16\
$17\'
#\
\
$1\
$2\
$3\
$4\
\
$5\
$6\
$7\
\
$8\
$9\
$10\
\
$11\
$12\
$13\
$14\
$15\
\
$16\
$17
regexindex1=r\'(01)(.{8})(.{4})(011a)\'
patternpic=r\'(010ac480c391c391c391(?!.*010ac480c391c391c391))(.*?)(01c88a)(.{36})(.{28})(.{2})(.{2})(.{2})(.{2})(.{36})(0303)(.{102,})\'
patternpicx=r\'(010ac480c391c391c391(?!.*010ac480c391c391c391))(.*?)(01c88a)(.{28})(.{2})(.{2})(.{2})(.{2})(.{36})(.{36})(0303)(.{102,})\'
regexindex2=r\'(1123236e6f7465732f2323756e66696c6564(?!.*1123236e6f7465732f2323756e66696c6564))(.*?)(00\\d\\d\\d\\d00\\d\\d)(2323)\'
regexnote1=r\'(0302010201)(.{2})(.{2}){0,1}\'
regexnote2=r\'(0302010201)(.{2})(.{2})(0a){0,1}\'
regexnote1v2=r\'(.{1570})(0201)(.{2})(0a)\'
def parser(fnnotedir):
    filetext=open(fnnotedir,"r")
    with open(fnnotedir, \'r\') as f:
        content = f.read()
        replace1 = re.sub(regexnote1, mo1.group(1)+totalobjhex, cihx)
    parsedtext=open(fnnotedir,"w+")
    parsedtext.append("")
    filetext.close()
    subprocess.call("notepad ",shell=True)
    return True
print(h2d("E2"))
#exit()
print(h2d("BF"))
print(h2d("37"))
print(h2d("937"))
print(h2d("F4"))
print(h2d("BA"))
print(h2d("93"))
print(h2d("80"))
print(d2h(192))
print(h2d("E7"))
print(h2d("B9"))
print(h2d("E0"))
print(h2d("E8"))
print(404/64)
#exit()
#LAST VAL-1
def picscaling(w,h):
            orix="03 E2 93 B9"
            oriy="03 E2 93 B9"
            if w>h:
                realscaling=15
                ##orix="03 E2 8C AE"
                ##oriy="03 E2 A8 92"
                realscaling=35
            if w<h:
                realscaling=80
                realscaling=30
                realscaling=17
                #h,w=w,h
                #orix="02 E2 8F 9E"
                #oriy="02 E3 92 AD"
            print(orix)
            print(oriy)
            orixlist=orix.split()
            defxvallist=[]
            for f in orixlist:
                val=int(f, 16)
                defxvallist.append(val)
            defxpresuffix,defxsuffix,defxscalequot,defxscalerem=defxvallist
                
            oriylist=oriy.split()
            defyvallist=[]
            for f in oriylist:
                val=int(f, 16)
                defyvallist.append(val)
            defypresuffix,defysuffix,defyscalequot,defyscalerem=defyvallist
            #print(defxpresuffix,defxsuffix,defxscalequot,defxscalerem)
            #print(defypresuffix,defysuffix,defyscalequot,defyscalerem)
            
            scaledw=(realscaling*w)
            
            initw=scaledw-(192-defxscalequot)
            
            xscalequotadd=int((scaledw-(192-defxscalequot))/(192-128))
            xscalequotint=defxscalequot+xscalequotadd
            xscalerem=int((scaledw-(192-defxscalequot))%(192-128))
            if scaledw<=0:
                xscalequotadd=0
                xscalerem=defxscalerem
            xscaleremint=128+xscalerem
            
            xsuffixadd=int((xscalequotint-128)/(192-128))
            xsuffixrem=int((xscalequotint-128)%(192-128))
            xsuffixint=defxsuffix+xsuffixadd
            xscalequotint=128+xsuffixrem
            #xpresuffix=(02=2,)
            xpresuffixadd=int((xsuffixint-defxsuffix)/(232-224))
            xpresuffixrem=int((xsuffixint-defxsuffix)%(232-224))

            defxpresuffix+=1
            xpresuffixint=defxpresuffix+xpresuffixadd
            if xpresuffixint>3:
                defxsuffix=defxsuffix-2
                xpresuffixint=defxpresuffix+xpresuffixadd
                xsuffixint=defxsuffix+xpresuffixrem
            if xpresuffixint==3:
                if xsuffixint>231:
                    xpresuffixint=defxpresuffix+1
                    xsuffixint=(defxsuffix-2)+(xsuffixint-232)
            
            
            xpresuffixhex=format(xpresuffixint,\'x\').zfill(2)
            xsuffixhex=format(xsuffixint,\'x\').zfill(2)
            xscalequothex=format(xscalequotint,\'x\').zfill(2)
            xscaleremhex=format(xscaleremint,\'x\').zfill(2)
            print(xpresuffixhex,xsuffixhex,xscalequothex,xscaleremhex)
            xscalehexs=xpresuffixhex+xsuffixhex+xscalequothex+xscaleremhex;

            #([ =+(#,-])(x) #$1y
            #scaledw #scaledh
            #defx #defy
            scaledh=realscaling*h;

            #yscalequot=(80=128,BF=191)
            #yscalerem=(B9=183,BF=191)
            initw=scaledh-(192-defyscalequot)
            yscalequotadd=int((scaledh-(192-defyscalequot))/(192-128))
            yscalequotint=defyscalequot+yscalequotadd
            yscalerem=int((scaledh-(192-defyscalequot))%(192-128))
            if scaledh<=0:
                yscalequotadd=0
                yscalerem=defyscalerem
            yscaleremint=128+yscalerem
            
            ysuffixadd=int((yscalequotint-128)/(192-128))
            ysuffixrem=int((yscalequotint-128)%(192-128))
            ysuffixint=defysuffix+ysuffixadd
            yscalequotint=128+ysuffixrem
            #ypresuffix=(02=2,)
            ypresuffixadd=int((ysuffixint-defysuffix)/(232-224))
            ypresuffixrem=int((ysuffixint-defysuffix)%(232-224))
            
            ypresuffixint=defypresuffix+ypresuffixadd
            if ypresuffixint>3:
                defysuffix=defysuffix-2
                ypresuffixint=defypresuffix+ypresuffixadd
                ysuffixint=defysuffix+ypresuffixrem
            if ypresuffixint==3:
                if ysuffixint>231:
                    ypresuffixint=defypresuffix+1
                    ysuffixint=(defysuffix-2)+(ysuffixint-232)
            
            ypresuffixhex=format(ypresuffixint,\'x\').zfill(2)
            ysuffixhex=format(ysuffixint,\'x\').zfill(2)
            yscalequothex=format(yscalequotint,\'x\').zfill(2)
            yscaleremhex=format(yscaleremint,\'x\').zfill(2)
            print(ypresuffixhex,ysuffixhex,yscalequothex,yscaleremhex)
            yscalehexs=ypresuffixhex+ysuffixhex+yscalequothex+yscaleremhex;

            print("orix="+orix)
            print("oriy="+oriy)
            print("finalx="+str(xscalehexs))
            print("finaly="+str(yscalehexs))
            return True
print(picscaling(1755,1240))
print(picscaling(1275,1500))
print(picscaling(97,48))
print(picscaling(418,73))
print(picscaling(404,22))
    
'