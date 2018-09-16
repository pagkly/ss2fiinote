import cv2
import numpy as np
def everyletter(imgdir):
    img = cv.imread(imgdir,0)
    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5,5), np.uint8)
 
    # The first parameter is the original image,
    # kernel is the matrix with which image is 
    # convolved and third parameter is the number 
    # of iterations, which will determine how much 
    # you want to erode/dilate a given image. 
    img_erosion = cv2.erode(img, kernel, iterations=1)
    #img_dilation = cv2.dilate(img, kernel, iterations=1)
    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

imgdir=""
everyletter(imgdir)
##detect contourarea<50
##pick that coordinate
## for f in smallcd: dr
#cv2.drawContours(img, contours, -1, (0,255,0), 3)
#if coordinate in range():
#    x1+scx1,y1+scy1
#    scx2,x2,scy2,y2
