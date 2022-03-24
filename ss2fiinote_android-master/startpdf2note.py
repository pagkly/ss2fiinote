##pdf-jpg conversion
##jpg OpenCV detection
##jpg to note on Android
import os
import time
import shutil
import subprocess
import argparse
import sys

from libFN33and import checknotz
from libjpgtonoteandFN import runengine
from libpdftojpgFN import convertpdf2jpg

dir_path = os.path.dirname(os.path.realpath(__file__))

def removefile(dirname):
    if os.path.exists(dirname):
        subprocess.call("rm -f "+dirname+" ;", shell=True)
        
def checkdir(dirname):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
        os.mkdir(dirname)
    else:
        os.mkdir(dirname)
    return True


def parse_args():
    # Create the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-pdir",
        "--pdfdir",
        help="Loc of PDF. Example: -pdir /home/"
    )
    parser.add_argument(
        "-p",
        "--pdfname",
        help="Name of PDF. Example: -p ABC.pdf"
    )
    parser.add_argument(
        "-ps",
        "--pagestart",
        help="Starting Page. Example: -ps 1"
    )
    parser.add_argument(
        "-pe",
        "--pageend",
        help="End Page. Example: -pe 6"
    )
    parser.add_argument(
        "-d",
        "--density",
        help="DPI. Example: -d 100"
    )
    parser.add_argument(
        "-t",
        "--type",
        help="OCV Type. Example: -t 1"
    )
    parser.add_argument(
        "-nc",
        "--noconversion",
        help="OCV Type. Example: -nc 1"
    )
    return parser.parse_args()


args = parse_args()

if args.pdfdir:
    pdfdir=args.pdfdir
    convertedpdfdir=pdfdir+os.path.sep+"ConvertedPDF"
    ocvjpgdir=pdfdir+os.path.sep+"attach"
    curnotedir=pdfdir+os.path.sep+"andimages.txt"
    outputdir=pdfdir+os.path.sep+"attach"
else:
    convertedpdfdir=dir_path+os.path.sep+"ConvertedPDF"
    ocvjpgdir=dir_path+os.path.sep+"attach"
    curnotedir=dir_path+os.path.sep+"andimages.txt"
    outputdir=dir_path+os.path.sep+"attach"
    print("Slide=100")
    print("Tbook=300")
    print("Work=300/Adobe")
    pdfdir=dir_path
print(pdfdir)
print(dir_path)
##sys.exit()

if args.pdfname:
    pdfname=args.pdfname
    if args.density :
        quality=int(args.density)
    else :
        quality=100
    if args.pagestart :
        pagestart=int(args.pagestart)
    else:
        pagestart=1
    if args.pageend :
        pageend=int(args.pageend)
        pageend=pageend
    else :
        pdfpage=subprocess.getoutput("pdfinfo \""+pdfdir+"/"+pdfname+"\" | grep Pages: | awk '{print $2}'")
        pageend=int(pdfpage)

if int(args.type)==1:
    from libOCVFinal import converttext
    print("t1")
elif int(args.type)==2:
    from libOCVFinal2 import converttext
    print("t2")
elif int(args.type)==3:
    from libOCVFinal3 import converttext
    print("t3")
else:
    pass

if int(args.noconversion)==1:
    noconversion=True
else:
    noconversion=False


column=1
checkdir(convertedpdfdir)
removefile(curnotedir)
CN=checknotz(curnotedir)
newdir1=CN[0]
objno2=CN[1]
pageend=pageend+1
if noconversion:
    print("no Conv")
    checkdir(ocvjpgdir)
    a=0
    b=objno2
    for i in range(pagestart,pageend) :
        a+=1
        print("Page"+str(i))
        imgname=convertpdf2jpg(pdfdir,pdfname,quality,i,outputdir)
        if a==10 or i==(pageend-1):
            runengine(outputdir,column,newdir1,objno2)
            a=0
            column+=1
            checkdir(ocvjpgdir)
        print(imgname)
        
        
            
if not noconversion:
    for i in range(pagestart,pageend) :
        checkdir(ocvjpgdir)
        a=1000
        ##i-=1
        print(i)
        convertedpdfdir=dir_path+os.path.sep+"ConvertedPDF"
        imgname=convertpdf2jpg(pdfdir,pdfname,quality,i,convertedpdfdir)
        print(imgname)
        converttext(convertedpdfdir,imgname+".jpg",a)
        subprocess.call("cp "+convertedpdfdir+os.path.sep+imgname+".jpg "+pdfdir+os.path.sep+"attach/00.jpg",shell=True)
        ##subprocess.call("cp "+convertedpdfdir+os.path.sep+imgname+".jpg "+pdfdir+os.path.sep+"attach",shell=True)
        runengine(pdfdir+os.path.sep+"attach",column,newdir1,objno2)
        a-=1
        column+=1

