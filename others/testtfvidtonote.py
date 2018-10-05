import sys
import argparse
import os, shutil, datetime, time
import re

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      count = count + 1

def startextraction(pathIn, pathOut):
    if os.path.exists(pathOut):
        print("dir exists")
        #exit()
        datenow=datetime.datetime.now()
        print(datenow)
        datenow=re.sub(" ","_",datenow)
        shutil.move(pathOut, pathOut+"old"+datenow)
        os.makedirs(pathOut)
    elif not os.path.exists(pathOut):
        os.makedirs(pathOut)
    extractImages(pathIn, pathOut)
if __name__=="__main__":
    print("starting")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    #args.pathIn="C:\\Users\\user\\Documents\\GitHub\\DocsSem2\\SEM0218\\MAST10005\\MASTLC2\\MAST10005_20180917.mp4"
    args.pathOut="C:\\Users\\user\\Documents\\GitHub\\DocsSem2\\SEM0218\\MAST10005\\MASTLC2"
    args.pathIn="C:\\Users\\user\\Documents\\GitHub\\DocsSem2\\SEM0218\\MAST10005\\MASTLC2"
    if ".mp4" in args.pathIn:
        startextraction(args.pathIn, args.pathOut)
    else:
        mp4lst=[f for f in os.listdir(args.pathIn) if ".mp4" in f]
        print(mp4lst)
        for f in mp4lst:
            curmp4dir=os.path.join(args.pathIn, f)
            destmp4dir=os.path.join(args.pathOut, re.sub(".mp4","",f))
            print(curmp4dir, destmp4dir)
            #time.sleep(3600)
            startextraction(curmp4dir, destmp4dir)
            
            
