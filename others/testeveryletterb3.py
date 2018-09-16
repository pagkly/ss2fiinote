#b'blob 8019\x00
import os
import cv2
import cv2 as cv
import numpy as np
from operator import itemgetter
dir0=os.path.dirname(os.path.realpath(__file__))
def everyletter(imgdir):
    #https://stackoverflow.com/questions/30506126/open-cv-error-215-scn-3-scn-4-in-function-cvtcolor
    img = cv.imread(imgdir,0)
    imgc = cv.imread(imgdir)
    #imgc=cv2.copyMakeBorder(img,0,0,0,0,cv2.BORDER_REPLICATE)
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((2,1), np.uint8)
    
    #hsv = cv2.cvtColor(imgc, cv2.COLOR_BGR2HSV)
    #lowerb = np.array([0,0,0])
    #upperb = np.array([180, 255, 80])
    #blackmask = cv2.inRange(hsv,lowerb,upperb)
    #cv2.imshow(\'HSV\', hsv)
    #cv2.imshow(\'MASK\', blackmask)
    #cv2.waitKey(0)

    ret, thresh = cv2.threshold(img, 127, 255, cv.THRESH_BINARY)
    img_erosion=cv2.erode(thresh, kernel, iterations=1)
    #cv2.imshow(\'BW\', thresh)
    cv2.imshow(\'IE\', img_erosion)
    cv2.waitKey(0)
 
    # The first parameter is the original image,
    # kernel is the matrix with which image is 
    # convolved and third parameter is the number 
    # of iterations, which will determine how much 
    # you want to erode/dilate a given image.
    im2, contours, hierarchy = cv2.findContours(img_erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)
    #cv2.drawContours(imgc, contours, -1, (0,255,0), 3)
    listofcd=[]
    for contour in contours:
        [x,y,w,h] = cv2.boundingRect(contour)
        listofcd.append([x,y,w,h])
    #print(listofcd)
    ##listofcd=sorted(listofcd, key=itemgetter(1,0))
    #for c in listofcd:
    #    for i in listofcd:
    #        if c[0] in range(i[0],i[0]+5) and c[1] in range(c[1]-20,c[1]+10) and c!=i:
    #            listofcd.remove(i)
    #            #print(i)
    countrect=0
    for i in range(0,len(listofcd)):
        [x,y,w,h]=listofcd[i]
        if i+1!=len(listofcd):
            [xafter,yafter,wafter,hafter]=listofcd[i+1]
            if w<9 and h<9 and w>3 and h>3:
                #and w in range(h-2,h+2):
                a=0
                for i in range(0,len(listofcd)):
                    [xcheck,ycheck,wcheck,hcheck]=listofcd[i]
                    #if [xcheck,ycheck,wcheck,hcheck] != [x,y,w,h] and not ycheck in range(y-100,y+50) and not xcheck in range(x+1,x+150):
                    if [xcheck,ycheck,wcheck,hcheck] != [x,y,w,h]:
                        if xcheck in range(x-1,x+10) and ycheck in range(y-5,y+10):
                            a+=1
                            #print(str(a))
                            break
                if a==0:
                    countrect+=1
                    cv2.rectangle(imgc, (x, y), (x+w, y+h), (0, 255, 0), 1)
                if a>=1:
                    pass
    cv2.imshow(\'Contoured\', imgc)
    cv2.imwrite(dir0+os.path.sep+"after.jpg",imgc)
    #cv2.waitKey(0)
    print(str(countrect))
def everyletter3(imgdir):
    src = cv2.imread(imgdir, 0)
    binary_map = (src > 0).astype(np.uint8)
    connectivity = 4 # or whatever you prefer
    output = cv2.connectedComponentsWithStats(binary_map, connectivity, cv2.CV_32S)
    cv2.imshow(\'Contoured\', output)
    cv2.waitKey(0)
    
def everyletter5(imgdir):
    img = cv2.imread(imgdir)
    (h, w) = img.shape[:2]
    #height, width, channels = img.shape
    image_size = h*w
    mser = cv2.MSER_create()
    mser.setMaxArea(int(image_size/2))
    mser.setMinArea(10)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting to GrayScale
    _, bw = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    regions, rects = mser.detectRegions(bw)

    # With the rects you can e.g. crop the letters
    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
    cv2.imshow(\'Contoured\', img)
    cv2.waitKey(0)
def everyletter10(imgdir):
    #method = cv2.cv.CV_TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(dir0+os.path.sep+"noteqs.jpg")
    large_image = cv2.imread(imgdir)

    result = cv2.matchTemplate(small_image, large_image, cv2.TM_SQDIFF_NORMED)
    print(result)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]
    
    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Display the original image with the rectangle around the match.
    cv2.imshow(\'output\',large_image)

    # The image is only displayed if we call this
    cv2.waitKey(0)

def everyletter11(imgdir):
    #method = cv2.TM_SQDIFF_NORMED
    # Read the images from the file
    small_image = cv2.imread(dir0+os.path.sep+"noteqs.jpg")
    large_image = cv2.imread(imgdir)
    result=cv2.matchTemplate(small_image, large_image, cv2.TM_SQDIFF_NORMED)
    ret,result=cv2.threshold(result, 0.7, 1., cv2.THRESH_BINARY);
    #ret, thresh = cv2.threshold(img, 127, 255, cv.THRESH_BINARY)
    resb=result.convertTo(resb, cv2.CV_8U, 255);
    contours=findContours(resb, contours, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE);
    for i in range(0,len(contours)):
        #Mat1b mask(result.rows, result.cols, uchar(0));
        cv2.drawContours(mask, contours, i, (255), cv2.CV_FILLED);
        #mn,_,mnLoc,_=cv2.minMaxLoc(result, NULL, &max_val, NULL, &max_point, mask);
        mn,_,mnLoc,_=cv2.minMaxLoc(result);
        MPx,MPy = mnLoc
        trows,tcols = small_image.shape[:2]
        cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows), (0,255,0), 2);
    # Display the original image with the rectangle around the match.
    cv2.imshow(\'output\',large_image)

    # The image is only displayed if we call this
    cv2.waitKey(0)
def everyletter000(imgdir):
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    large_image=imgdir
    notefsimgdir=dir0+os.path.sep+"notefs.jpg"
    notecmimgdir=dir0+os.path.sep+"notecm.jpg"
    noteqsimgdir=dir0+os.path.sep+"noteqs.jpg"
    img_rgb = cv2.imread(large_image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    clist=[]
    #FS
    template = cv2.imread(notefsimgdir,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        clist.append([pt[0],pt[1],pt[0] + w, pt[1] + h])
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #CM
    template = cv2.imread(notecmimgdir,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        clist.append([pt[0],pt[1],pt[0] + w, pt[1] + h])
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #QS
    template = cv2.imread(noteqsimgdir,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        clist.append([pt[0],pt[1],pt[0] + w, pt[1] + h])
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #print(clist)
    for c in clist:
        for i in clist:
            if c[0] in range(i[0]-5,i[0]+5) and c!=i:
                clist.remove(i)
                print(i)
    for c in clist:           
        cv2.rectangle(img_rgb, (c[0],c[1]),(c[2],c[3]), (0,0,255), 2)

    #cv2.imwrite(\'res.png\',img_rgb)
    cv2.imshow(\'output\',img_rgb)
    cv2.waitKey(0)
    
    
imgdir=dir0+os.path.sep+"20180808185431abcdefghijklm74.jpg"
print(imgdir)
everyletter(imgdir)
##detect contourarea<50
##pick that coordinate
## for f in smallcd: dr
#cv2.drawContours(img, contours, -1, (0,255,0), 3)
#if coordinate in range():
#    x1+scx1,y1+scy1
#    scx2,x2,scy2,y2
'