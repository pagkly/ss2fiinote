#https://matthew-brett.github.io/curious-git/reading_git_objects.html
import zlib  # A compression / decompression library
#filename = 'working/git_example/.git/objects/e2/7bb34b0807ebf1b91bb66a4c147430cde4f08f'
import time, os, subprocess
notepadppdir="C:\\Program Files\\Notepad++\\Notepad++.exe"
while True:
    folder=input("Folder : ")
    fcount=0
    folderdir='C:\\Users\\SP3\\Documents\\GitHub\\FN35OCVbside\\.git\\objects\\'+folder
    filelist=os.listdir(folderdir)

    """
    for f in filelist:
    #print(str(fcount)+". "f)
    #fcount+=1
    
    """
    for file in filelist:
        altfolderdir="C:\\Users\\SP3\\Documents\\GitHub\\FN35OCVbside\\decodegitobj\\"+folder
        if not os.path.exists(altfolderdir):
            os.makedirs(altfolderdir)
        newftext=altfolderdir+"\\"+file+"code.txt"
        filedir='C:\\Users\\SP3\\Documents\\GitHub\\FN35OCVbside\\.git\\objects\\'+folder+os.path.sep+file
        fsize=str(os.path.getsize(filedir))
        #print(file)
        print(fsize)
        if not os.path.exists(newftext) and not "code.txt" in file and (os.path.getsize(filedir)<100000):
            print(file)
            compressed_contents = open(filedir, 'rb').read()
            decompressed_contents = zlib.decompress(compressed_contents)
            
            f=open(newftext,"w")
            f.write(str(decompressed_contents))
            f.close()
            subprocess.call('"'+notepadppdir+'"'+" "+newftext, shell=True)
            #subprocess.call("taskkill /F /IM Notepad++.exe /T",shell=True)
    #subprocess.call('"'+notepadppdir+'"'+" "+newftext, shell=True)
    ##file=input("Filenm : ")
    #fnname=input("Folder+FN : ")
   
"""
from hashlib import sha1  # SHA1 hash algorithm
hash_value = sha1(decompressed_contents).hexdigest()
hash_value
"""

"""
#from Tkinter import *

from tkinter import *
from tkinter import Tk
import tkinter as tk

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()
"""
