import tkinter as tk
import os,sys
import time
import psutil
import win32gui
from win32api import GetSystemMetrics
import win32com.client as comclt
import win32gui, win32con
def spawntrans():
    global roottrans
    root = tk.Tk()
    roottrans=tk.Toplevel()
    if sys.platform in ['linux', 'linux2'] :
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        w=GetSystemMetrics(0)
        h=GetSystemMetrics(1)
    #roottrans.attributes('-alpha', 0.3)
    roottrans.wm_attributes('-alpha',0.05,'-topmost',1)
    roottrans.geometry('%dx%d+%d+%d' % (w, h, 0,0))
    roottrans.resizable(False, False)
    roottrans.update_idletasks()
    roottrans.overrideredirect(True)
    roottrans.mainloop()

spawntrans()
