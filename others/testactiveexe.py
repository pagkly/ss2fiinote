import psutil, win32process, win32gui, time
def active_window_process_name():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow()) #This produces a list of PIDs active window relates to
    #print(psutil.Process(pid[-1]).name()) #pid[-1] is the most likely to survive last longer
    return psutil.Process(pid[-1]).name()


time.sleep(3) #click on a window you like and wait 3 seconds 
active_window_process_name()
