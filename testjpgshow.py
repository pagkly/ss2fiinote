from tkinter import *
from PIL import Image, ImageTk

rootimgv = Tk()
rootimgv.title("Python: Simple Image Viewer")
width = 600
height = 300
screenw = rootimgv.winfo_screenwidth()
screenh = rootimgv.winfo_screenheight()
x = (screenw/2) - (width/2)
y = (screenh/2) - (height/2)
rootimgv.geometry("%dx%d+%d+%d" % (width, height, x, y))
rootimgv.resizable(0, 0)

#https://www.sourcecodester.com/tutorials/python/12128/python-simple-image-viewer.html
#================================METHODS========================================
def gettkinterxypos():
	return xpos,ypos
def getorigin(eventorigin):
      global x,y
      x = eventorigin.x
      y = eventorigin.y
      print(x,y)
def DisplayImage(event=None):
	import os,subprocess
	userhomedir=subprocess.getoutput("echo %USERPROFILE%")
	dir0=os.path.dirname(os.path.realpath(__file__))
	convpdfdirpc=dir0+os.path.sep+"ConvertedPDF"
	imgdir=convpdfdirpc+os.path.sep+"29.pdf"+os.path.sep+"conv0001.jpg"
	print(imgdir)

	Home = Toplevel()
	Home.title("Simple Image Viewer/Viewer")
	load = Image.open(imgdir)
	imgw, imgh = load.size
	if sys.platform in ['linux', 'linux2'] :
		screenw = root.winfo_screenwidth()
		screenh = root.winfo_screenheight()
	if sys.platform in ['Windows', 'win32', 'cygwin']:
		from win32api import GetSystemMetrics
		screenw=GetSystemMetrics(0)
		screenh=GetSystemMetrics(1)
	screenw = Home.winfo_screenwidth()
	screenh = Home.winfo_screenheight()
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
	panel.pack(fill=BOTH, expand=YES)
#================================FRAMES=========================================
Top = Frame(rootimgv, width=600, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(rootimgv, width=300, height=200, bd=1, relief=SOLID)
Mid.pack_propagate(0)
Mid.pack(pady=20)
#================================LABEL WIDGETS==================================
lbl_title = Label(Top, text="Python: Simple Image Viewer", width=600, font=("arial", 20))
lbl_title.pack(fill=X)
lbl_text = Label(Mid, text="flower.jpg", font=("arial", 20))
lbl_text.bind("<Button-1>", DisplayImage)
lbl_text.pack()


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
	rootimgv.mainloop()
	rootimgv.bind("<Button 1>",getorigin)
