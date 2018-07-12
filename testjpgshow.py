import os,subprocess
from tkinter import *
from PIL import Image, ImageTk
userhomedir=subprocess.getoutput("echo %USERPROFILE%")
dir0=os.path.dirname(os.path.realpath(__file__))
convpdfdirpc=dir0+os.path.sep+"ConvertedPDF"
rootimgv = Tk()
width = 600
height = 300
screen_width = rootimgv.winfo_screenwidth()
screen_height = rootimgv.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
rootimgv.geometry("%dx%d+%d+%d" % (width, height, x, y))
rootimgv.resizable(0, 0)
#https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
#https://www.sourcecodester.com/tutorials/python/12128/python-simple-image-viewer.html
#================================METHODS========================================
def prevpage():
	return True
def nextpage():
	return True
def whitelistpagearea(page,x,y):
	import cv2
	return True
def progresspage(page):
	return True
def progresspagewhitelist():
	return True
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

from FN33andlib import conwindirtovwsldir,convertpdf2jpg2
def DisplayImage(pdfdir,pdfname,*args,**kwargs):
	#imgdir=convpdfdirpc+os.path.sep+"29.pdf"+os.path.sep+"conv0001.jpg"
	#imgdir=convertpdf2jpginwsl(pdfdir,pdfname,120,1,convpdfdirpc+os.path.sep+pdfname)
	imgdir=convertpdf2jpg2(pdfdir,pdfname,120,1,convpdfdirpc+os.path.sep+pdfname,"")
	print(imgdir)
	Home = Toplevel()
	Home.title("Simple Image Viewer/Viewer")
	load = Image.open(imgdir)
	imgw, imgh = load.size
	if sys.platform in ['linux', 'linux2'] :
		screenw = Home.winfo_screenwidth()
		screenh = Home.winfo_screenheight()
	if sys.platform in ['Windows', 'win32', 'cygwin']:
		from win32api import GetSystemMetrics
		screenw=GetSystemMetrics(0)
		screenh=GetSystemMetrics(1)
	showimgw=int((screenh/imgh)*imgw)
	showimgh=int(screenh)
	x = (screenw/2) - (showimgw/2)
	y = (screenh/2) - (showimgh/2)
	Home.geometry("%dx%d+%d+%d" % (showimgw, showimgh, x,y))
	Home.resizable(1, 1)
	load = load.resize((showimgw, showimgh), Image.ANTIALIAS)
	render = ImageTk.PhotoImage(load)
	panel = Label(Home, image=render)
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


#================================FRAMES=========================================
mfwidth=500
mfheight=200
Top = Frame(rootimgv, width=mfwidth, bd=1, relief=SOLID)
Top.pack(side=TOP)

Mid = Frame(rootimgv, width=mfwidth, height=mfheight, bd=1, relief=SOLID)
Mid.pack_propagate(0)
Mid.pack(pady=20)
#https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
def listfilesext(dir,ext):
	allfilesdir=[]
	allfilesname=[]
	allfilesfulldir=[]
	for file in os.listdir(dir):
		if file.endswith(ext):
			#and os.path.isfile(os.path.join(dir, file))
			#os.path.isdir("bob")
			allfilesdir.append(dir)
			allfilesname.append(file)
			allfilesfulldir.append(os.path.join(dir, file))
	print(allfilesfulldir)
	return allfilesdir,allfilesname,allfilesfulldir

#https://stackoverflow.com/questions/10927234/setting-the-position-on-a-button-in-python
#https://stackoverflow.com/questions/10865116/python-tkinter-creating-buttons-in-for-loop-passing-command-arguments
def placebutton(allfilesdir,allfilesname,allfilesfulldir):
	from functools import partial
	x=len(allfilesfulldir)
	value=int(x)
	bwidth=500
	bheight=25
	lbl_title = Label(Top, text="Python: Simple Image Viewer", width=mfwidth, font=("arial", 20))
	lbl_title.pack(fill=X)
	for i in range(value):
		print(allfilesdir[i])
		print(allfilesname[i])
		#b=Button(Mid,text=allfilesfulldir[i],command=lambda: DisplayImage(allfilesdir[i],allfilesname[i]))
		b=Button(Mid,text=allfilesfulldir[i],command=partial(DisplayImage,allfilesdir[i],allfilesname[i]))
		b.place(x=mfwidth/2-bwidth/2, y=i*30, width=bwidth, height=bheight)


if __name__ == "__main__":
	#DisplayImage()
	allfilesdir,allfilesname,allfilesfulldir=listfilesext(dir0,".pdf")
	placebutton(allfilesdir,allfilesname,allfilesfulldir)
	rootimgv.mainloop()
