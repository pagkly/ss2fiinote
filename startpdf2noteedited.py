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
    parser.add_argument(
        "-pdir",
        "--pdfmdir",
        help="Loc of PDFs. Example: -pdir /home/user"
    )
    return parser.parse_args()

args = parse_args()

def testing() :
    return True

def setvarargs():
    noconversion=False
    quality=100
    pagestart=1
    if args.pdfdir:
        pdfdir=args.pdfdir
    else:
        pdfdir=dir_path
        print("Slide=100")
        print("Tbook=300")
        print("Work=300/Adobe")
    if not noconversion:
        pdfdir=dir_path

    convertedpdfdir=pdfdir+os.path.sep+"ConvertedPDF"
    ocvjpgdir=pdfdir+os.path.sep+"attach"
    curnotedir=pdfdir+os.path.sep+"andimages.txt"
    outputdir=pdfdir+os.path.sep+"attach"
    print(pdfdir)
    print(dir_path)
    ##sys.exit()


    if args.pdfname:
        pdfname=args.pdfname
        if args.density :
            quality=int(args.density)
        if args.pagestart :
            pagestart=int(args.pagestart)
        if args.pageend :
            pageend=int(args.pageend)
            pageend=pageend
        else :
            pdfpage=subprocess.getoutput("pdfinfo \""+pdfdir+"/"+pdfname+"\" | grep Pages: | awk '{print $2}'")
            pageend=int(pdfpage)
    if int(args.type)==1:
        from libOCVFinal import converttext
    elif int(args.type)==2:
        from libOCVFinal2 import converttext
    elif int(args.type)==3:
        from libOCVFinal3 import converttext
    else:
        pass
    print("t"+int(args.type))
    if int(args.noconversion)==1:
        noconversion=True
    return True


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
        imgname=convertpdf2jpg(pdfdir,pdfname,quality,i,convertedpdfdir)
        print(i+" "+imgname)
        converttext(convertedpdfdir,imgname+".jpg",a)
        subprocess.call("cp "+convertedpdfdir+os.path.sep+imgname+".jpg "+pdfdir+os.path.sep+"attach/00.jpg",shell=True)
        ##subprocess.call("cp "+convertedpdfdir+os.path.sep+imgname+".jpg "+pdfdir+os.path.sep+"attach",shell=True)
        runengine(pdfdir+os.path.sep+"attach",column,newdir1,objno2)
        a-=1
        column+=1



if args.pdfmdir :
    relevant_path=args.pdfmdir
    included_extensions = ['pdf']
    pdf_names = [fn for fn in os.listdir(relevant_path)
                      if any(fn.endswith(ext) for ext in included_extensions)]
    print(len(pdf_names))

    for i in range(0,len(pdf_names)):
        print(pdf_names[i])
        ##sys.exit()
        subprocess.call("python3 ~/Documents/Docs/Tech/Automate/FN35AOCV/startpdf2note.py -pdir \""+relevant_path+"\" -p \""+pdf_names[i]+"\" -d 100 -t 1 -nc 1" ,shell=True)
