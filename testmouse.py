from pynput.mouse import Button, Controller
import win32com.client as comclt
import time
import win32gui
import win32gui, win32con
import os
w=win32gui
wingui=w.GetWindowText(w.GetForegroundWindow())
wsh=comclt.Dispatch("WScript.Shell")
def windowEnumerationHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
def focusprog(appname):
            results = []
            top_windows = []
            win32gui.EnumWindows(windowEnumerationHandler, top_windows)
            for i in top_windows:
                if appname in i[1].lower():
                    print (i)
                    win32gui.ShowWindow(i[0],win32con.SW_MAXIMIZE)
                    win32gui.SetForegroundWindow(i[0])
                    j=os.getpid()
                    print(j)
                    break
#focusprog("Notes")
#time.sleep(3)
#wsh.SendKeys("%{TAB}{TAB}{TAB}")
time.sleep(5)
#wsh.SendKeys("%{TAB}")
#time.sleep(3)
#wsh.SendKeys("%{TAB}")
#wsh.SendKeys("%{TAB}")
mouse = Controller()
print ("Current position: " + str(mouse.position))
#mouse.position = (100, 200)
#mouse.move(200, 100)
#mouse.press(Button.left)
#mouse.release(Button.left)
#mouse.click(Button.right, 1)
#mouse.click(Button.left, 1)
# Scroll up two steps
mouse.scroll(0, 20)
# Scroll right five steps
#mouse.scroll(5, 0)


