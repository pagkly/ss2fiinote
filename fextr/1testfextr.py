#!/usr/bin/env python3
"""
ph3fn="pyhook-1.6.1-cp35-cp35m-win32.whl"
ph3downdir="\\$ph3fn"
ph3downlink="https://files.pythonhosted.org/packages/00/36/c08af743a671d94da7fe10ac2d078624f3efc09273ffae7b18601a8414fe/PyHook3-1.6.1-cp35-win32.whl"
curl -o "$ph3fn" "$ph3downlink"
"""
import os, sys, threading
import _thread
from FN33andlib import *
from functools import partial

dir0 = os.path.dirname(os.path.realpath(__file__))
textclick=0
pause=0
is_recording=0
linuxpc=1
def Default():
    textclick=0
    pause=0
    is_recording=0
Default()
def checkdep():
    deplist=["pyautogui pyuserinput"]
    deplist.split()
    if sys.platform in ['linux', 'linux2']:
        callpip="pip3"
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        callpip="pip"
    for f in deplist:
        subprocess.call(callpip+" install "+str(f),shell=True)
#checkdep()
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

import win32api, win32con
import win32com.client as comclt
wsh=comclt.Dispatch("WScript.Shell")
"""
wsh.AppActivate("Notepad") # select another application
wsh.AppActivate("%USERPROFILE%\\Documents\\Docs\\Automate\\FiiNoteWINE\\FiiNote.exe")
focusprog("FiiNote")
"""
