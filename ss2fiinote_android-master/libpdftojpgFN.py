import subprocess, sys, os, time
import shutil

def convertpdf2jpg(pdfdir,pdfname,quality,page,outputdir):
    ##converteddir=pdfdir+"/ConvertedPDF"
    converteddir=outputdir
    pdfpage=subprocess.getoutput("pdfinfo \""+pdfdir+"/"+pdfname+"\" | grep Pages: | awk '{print $2}'")
    ##for i in range(int(pagestart),int(pageend)):
    pagei=str(page).zfill(4)
    convpname="conv"+pagei
    print("pdftoppm \""+pdfdir+"/"+pdfname+"\" \""+converteddir+"/"+convpname+"\" -jpeg -f "+str(page)+" -singlefile")
    subprocess.call("pdftoppm \""+pdfdir+"/"+pdfname+"\" \""+converteddir+"/"+convpname+"\" -jpeg -f "+str(page)+" -singlefile",shell=True)
    #subprocess.call("convert -verbose -density "+str(quality)+" -trim "+pdfdir+"/"+pdfname+"["+str(page)+"] -quality 100 -flatten -sharpen 0x1.0 "+converteddir+"/"+convpname, shell=True)
    return (convpname)

#convertpdf2jpg(pdfdir,pdfname)
#runengine(str(0),str(0),converteddir)
