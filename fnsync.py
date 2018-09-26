import os, sys
import time
import subprocess
import re
pcdir="C:\\Users\\SP3\\AppData\\Roaming\\FiiNote\\@pagkly\\notes"
pcdir2="C:\\Users\\SP3\\Documents\\GitHub\\FNnotes\\@pagkly\\notes"
if sys.platform in ['linux', 'linux2']:
    tabletdir="/media/tablet/fiinote/notes"
if sys.platform in ['Windows', 'win32', 'cygwin']:
    tabletdir="Z:\\fiinote\\notes"

tabletdirlst=os.listdir(tabletdir)
pcdirlst=os.listdir(pcdir)
newdirlst=[dirname for dirname in list(set(pcdirlst)-set(tabletdirlst)) if ".notz" in dirname ]
newdirlst.append("index.nti")
#print(newdirlst)
if os.path.exists(tabletdir):
    print(newdirlst)
else:
    print("nopathexists")
    exit()
    
#copy pc newdir+index.nti
for newdir in newdirlst:
    sourcedir=pcdir+os.path.sep+newdir
    destinationdir=tabletdir+os.path.sep+newdir
    #+" /COPYALL /E"
    subprocess.call("robocopy "+sourcedir+" "+destinationdir+" /s /e /copyall",shell=True)
    pass

"""
#copy pc index.nti
pcurindexdir=pcdir+os.path.sep+"index.nti"
tcurindexdir=tabletdir+os.path.sep+"index.nti"
toldindexdir=tabletdir+os.path.sep+"indexold.nti"
if os.path.exists(toldindexdir) : os.remove(toldindexdir)
if os.path.exists(tcurindexdir) : os.remove(tcurindexdir)
subprocess.call("copy "+pcurindexdir+" "+tcurindexdir,shell=True)
"""

#copy pc .note
newtabletdirlst=[eachdir for eachdir in os.listdir(tabletdir) if ".notz" in eachdir]
#print(newtabletdirlst)
for tnotzdir in newtabletdirlst:
    print("")
    print(tnotzdir)
    pcnotzdir=pcdir+os.path.sep+tnotzdir
    tabnotzdir=tabletdir+os.path.sep+tnotzdir
    
    pcimgdir=pcnotzdir+os.path.sep+"attach"
    tabimgdir=tabnotzdir+os.path.sep+"attach"
    #time.sleep(3600)
    if os.path.exists(tabimgdir):
        print(len(os.listdir(pcimgdir)))
        newimglst=list(set(os.listdir(pcimgdir))-set(os.listdir(tabimgdir)))
        #print(newimglst)
        for imgname in newimglst:
            print(imgname)
            subprocess.call("copy "+pcimgdir+os.path.sep+imgname+" "+tabimgdir+os.path.sep+imgname,shell=True)
    else:
        if os.path.exists(pcimgdir):
            print("tabdirnotexist;copy "+str(len(os.listdir(pcimgdir))))
            subprocess.call("robocopy "+pcimgdir+" "+tabimgdir+" /s /e /copyall",shell=True)
            pass
        
    notedir=re.sub(".notz",".note",tnotzdir)
    sourcedir=pcnotzdir+os.path.sep+notedir
    destdir=tabnotzdir+os.path.sep+notedir
    #and os.path.getmtime(sourcedir)!=os.path.getmtime(destdir)
    if os.path.getsize(sourcedir)!=os.path.getsize(destdir):
        if os.path.exists(destdir):
            print("copy .note")
            os.remove(destdir)
        subprocess.call("copy "+sourcedir+" "+destdir,shell=True)

    pcthumb=pcnotzdir+os.path.sep+"thumbnail.jpg"
    tabthumb=tabnotzdir+os.path.sep+"thumbnail.jpg"
    if not os.path.exists(tabthumb) and os.path.exists(pcthumb):
        print("copy thumbnail.jpg")
        subprocess.call("copy "+pcthumb+" "+tabthumb,shell=True)
    if not os.path.exists(tabthumb) and not os.path.exists(pcthumb) and os.path.exists(tabimgdir):
        if len(os.listdir(tabimgdir))>0:
            print("copy thumbnail.jpg from pcimgdir")
            subprocess.call("copy "+tabimgdir+os.path.sep+os.listdir(tabimgdir)[1]+" "+tabthumb,shell=True)
