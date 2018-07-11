from tkinter import *
from PIL import Image, ImageTk

rootimgv = Tk()
#https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
#https://www.sourcecodester.com/tutorials/python/12128/python-simple-image-viewer.html
#================================METHODS========================================

def perccolor():
	#https://stackoverflow.com/questions/43167867/color-percentage-in-image-python-opencv-using-histogram
	import numpy as np
	import cv2
	img = cv2.imread('J9MbW.jpg')
	brown = [145, 80, 40]  # RGB
	diff = 20
	boundaries = [([brown[2]-diff, brown[1]-diff, brown[0]-diff],
	               [brown[2]+diff, brown[1]+diff, brown[0]+diff])]
	# in order BGR as opencv represents images as numpy arrays in reverse order
	for (lower, upper) in boundaries:
	    lower = np.array(lower, dtype=np.uint8)
	    upper = np.array(upper, dtype=np.uint8)
	    mask = cv2.inRange(img, lower, upper)
	    output = cv2.bitwise_and(img, img, mask=mask)

	    ratio_brown = cv2.countNonZero(mask)/(img.size/3)
	    print('brown pixel percentage:', np.round(ratio_brown*100, 2))

	    cv2.imshow("images", np.hstack([img, output]))
	    cv2.waitKey(0)
def gettkinterxypos(eventorigin):
      global x,y
      x = eventorigin.x
      y = eventorigin.y
	  ###bindkeyboardandmouse
	  	###http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
		##Example:http://www.java2s.com/Code/Python/Event/MouseeventsonaframeMouseclickedposition.htm
		##https://www.daniweb.com/programming/software-development/threads/364829/mouse-position-tkinter
		##class:https://stackoverflow.com/questions/3288047/how-do-i-get-mouse-position-relative-to-the-parent-widget-in-tkinter
	  #https://www.reddit.com/r/learnpython/comments/gwrig/questions_about_getting_mouse_coordinates_in/
	  #https://bytes.com/topic/python/answers/888796-how-get-x-coordinate-image
	  #https://stackoverflow.com/questions/38428593/getting-the-absolute-position-of-cursor-in-tkinter
	  #https://www.quora.com/In-Python-using-Tkinter-how-can-I-get-the-mouse-position-on-the-screen
	  #print root.winfo_pointerxy()
      print(x,y)
def DisplayImage(event=None):
	import os,subprocess
	userhomedir=subprocess.getoutput("echo %USERPROFILE%")
	dir0=os.path.dirname(os.path.realpath(__file__))
	convpdfdirpc=dir0+os.path.sep+"ConvertedPDF"
	imgdir=convpdfdirpc+os.path.sep+"29.pdf"+os.path.sep+"conv0001.jpg"
	print(imgdir)
	rootimgv.title("Simple Image Viewer/Viewer")
	load = Image.open(imgdir)
	imgw, imgh = load.size
	if sys.platform in ['linux', 'linux2'] :
		screenw = rootimgv.winfo_screenwidth()
		screenh = rootimgv.winfo_screenheight()
	if sys.platform in ['Windows', 'win32', 'cygwin']:
		from win32api import GetSystemMetrics
		screenw=GetSystemMetrics(0)
		screenh=GetSystemMetrics(1)
	showimgw=int((screenh/imgh)*imgw)
	showimgh=int(screenh)
	x = (screenw/2) - (showimgw/2)
	y = (screenh/2) - (showimgh/2)
	rootimgv.geometry("%dx%d+%d+%d" % (showimgw, showimgh, x,y))
	rootimgv.resizable(1, 1)
	load = load.resize((showimgw, showimgh), Image.ANTIALIAS)
	render = ImageTk.PhotoImage(load)
	panel = Label(rootimgv, image=render)
	panel.image=render
	panel.bind("<Button 1>",gettkinterxypos)
	panel.pack(fill=BOTH, expand=YES)

#https://stackoverflow.com/questions/5436810/adding-zooming-in-and-out-with-a-tkinter-canvas-widget
class GUI:
    def __init__(self, root):
        # ... omitted rest of initialization code
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        self.scale = 1.0
        self.orig_img = Image.open(File)
        self.img = None
        self.img_id = None
        # draw the initial image at 1x scale
        self.redraw()

        # ... rest of init, bind buttons, pack frame

    def zoom(self,event):
        if event.num == 4:
            self.scale *= 2
        elif event.num == 5:
            self.scale *= 0.5
        self.redraw(event.x, event.y)

    def redraw(self, x=0, y=0):
        if self.img_id:
            self.canvas.delete(self.img_id)
        iw, ih = self.orig_img.size
        size = int(iw * self.scale), int(ih * self.scale)
        self.img = ImageTk.PhotoImage(self.orig_img.resize(size))
        self.img_id = self.canvas.create_image(x, y, image=self.img)

        # tell the canvas to scale up/down the vector objects as well
        self.canvas.scale(ALL, x, y, self.scale, self.scale)

if __name__ == "__main__":
	DisplayImage()
	rootimgv.mainloop()
