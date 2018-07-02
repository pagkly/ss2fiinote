import os
import shutil
import subprocess
import cv2
import numpy as np

a=1000
dir_path = os.path.dirname(os.path.realpath(__file__))
convertedpdfdir=dir_path+"/ConvertedPDF"
ocvjpgdir=dir_path+"/attach"

def converttext(imgdir,imgname, a):
    large = cv2.imread(imgdir+os.path.sep+imgname)
    print(imgdir+os.path.sep+imgname)
    rgb = cv2.pyrUp(large)
    rgb = cv2.pyrUp(rgb)
    ##P/L
    ##rgb=large
    small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    # using RETR_EXTERNAL instead of RETR_CCOMP
    _, contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    mask = np.zeros(bw.shape, dtype=np.uint8)

    for idx in range(len(contours)):
        a-=1
        x, y, w, h = cv2.boundingRect(contours[idx])
        mask[y:y+h, x:x+w] = 0
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
        if r > 0.45 and w > 25 and h > 10:
            ##img = rgb[y+15:y+h-15, x+15:x+w-15]
            img=rgb[y:y+h, x:x+w]
            cv2.imwrite(ocvjpgdir+os.path.sep+str(a)+"t1"+imgname, img)
            cv2.rectangle(rgb, (x-3, y-3), (x+w+3, y+h+3), (255, 255, 255), -1)
            converttext2(ocvjpgdir, str(a)+"t1"+imgname, a)


def converttext2(imgdir,imgname, a):
    large = cv2.imread(ocvjpgdir+os.path.sep+imgname)
    ##rgb = cv2.pyrUp(large)
    ##P/L
    rgb=large
    small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    # using RETR_EXTERNAL instead of RETR_CCOMP
    _, contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    mask = np.zeros(bw.shape, dtype=np.uint8)

    for idx in range(len(contours)):
        a-=1
        x, y, w, h = cv2.boundingRect(contours[idx])
        mask[y:y+h, x:x+w] = 0
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
        if r > 0.45 and w > 25 and h > 10:
            ##img = rgb[y:y+h-1, x:x+w-1]
            img=rgb[y-5:y+h+5, x-5:x+w+5]
            cv2.imwrite(ocvjpgdir+os.path.sep+str(a)+"t3"+imgname, img)
            cv2.rectangle(rgb, (x, y), (x+w, y+h), (255, 255, 255), -1)

    #cv2.imshow('rects', rgb)
    ##rgb = cv2.pyrUp(rgb)
    cv2.imwrite(ocvjpgdir+os.path.sep+'contoured1'+imgname, rgb)
    convertrest(imgname, a)

def convertrest(imgname, a):
    ##a=0
    image = cv2.imread(ocvjpgdir+os.path.sep+'contoured1'+imgname)
    ##image=img
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
    _, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours
    # for each contour found, draw a rectangle around it on original image
    for contour in contours:
        a-=1
        # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)
        # discard areas that are too large
        if h>700 and w>700:
            continue
        # discard areas that are too small
        if h<40 or w<40:
            continue
        else:
            # draw rectangle around contour on original image
            #im=pyscreenshot.grab(bbox=(x,y,x+w,y+h),childprocess=False)
            ##cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
            ##img = image[y:y+h, x:x+w]
            img=image[y-5:y+h+5, x-5:x+w+5]
            cv2.imwrite(ocvjpgdir+os.path.sep+str(a)+"t2"+imgname, img) 
            #img.save(str(x)+'test.jpg')
    # write original image with added contours to disk  
    cv2.imwrite(ocvjpgdir+os.path.sep+"contoured2"+imgname, image) 


#checkdir(convertedpdfdir)
#checkdir(ocvjpgdir)
##converttext(dir_path,"conv0003.jpg",1000)



