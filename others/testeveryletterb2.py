#92\\a4c5b02359
#b'blob 11981\x00
import os
import cv2
import cv2 as cv
import numpy as np
from operator import itemgetter
dir0=os.path.dirname(os.path.realpath(__file__))        
def everyletter0(imgdir):
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
    #kernel = np.ones((1,1), np.uint8)
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
def everyletter_connectedcomp(imgdir):
    src = cv2.imread(imgdir, 0)
    binary_map = (src > 0).astype(np.uint8)
    connectivity = 4 # or whatever you prefer
    output = cv2.connectedComponentsWithStats(binary_map, connectivity, cv2.CV_32S)
    cv2.imshow(\'Contoured\', output)
    cv2.waitKey(0)
def everyletter(imgdir,ocvtype):
    imgori = cv2.imread(imgdir)
    img=imgori.copy()
    (imgh, imgw) = img.shape[:2]
    image_size = imgh*imgw
    mser = cv2.MSER_create()
    mser.setMaxArea(int(image_size/2))
    mser.setMinArea(10)

    #dtext
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting to GrayScale
    _, bw = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow("",bw)
    cv2.waitKey(0)

    if imgh>imgw:
        kernelcd = np.ones((5,20), np.uint8)
        if "math" in ocvtype:
            kernelcd = np.ones((5,30), np.uint8)
    if imgw>imgh:
        kernelcd = np.ones((5,20), np.uint8)
    bwcd=cv2.erode(bw, kernelcd, iterations=1)
    regions, rects = mser.detectRegions(bwcd)
    imgcd=imgori.copy()
    listcd=[]
    for (x, y, w, h) in rects:
        if w>10 and h>10:
            listcd.append([x,y,w,h])
            cv2.rectangle(imgcd, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
    #cv2.imshow(\'cd\', imgcd)
    #cv2.waitKey(0)
        
    kernel = np.ones((3,1), np.uint8)
    bw=cv2.erode(bw, kernel, iterations=1)
    #ret, bw = cv2.connectedComponents(bw)
    regions, rects = mser.detectRegions(bw)
    # With the rects you can e.g. crop the letters
    for (x, y, w, h) in rects:
        if w<7 and h<7:
            #cv2.rectangle(img, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
            pass
        #cv2.rectangle(img, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
        #cv2.rectangle(img, (x-1, y-1), (x+w+1, y+h+1), color=(255, 255, 255), thickness=-1)
        else:
            cv2.rectangle(img, (x, y), (x+w, y+h), color=(255, 255, 255), thickness=-1)
            pass
    listcdoc=[]
    def cdoc(mat):
        mask=mat
        im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        imgb=imgori.copy()
        for contour in contours:
            [x,y,w,h] = cv2.boundingRect(contour)
            cd=[x,y,w,h]
            print(cd)
            if h<(50/100*imgh) and w>(1/100*imgw) and h>(1/100*imgh):
                listcdoc.append([x,y,w,h])
                cv2.rectangle(imgb, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
        #cv2.imshow(\'mb\', imgb)
        #cv2.waitKey(0)
    imgf=imgori.copy()
    if imgh>imgw:
        kernelcd = np.ones((5,5), np.uint8)
    if imgw>imgh:
        kernelcd = np.ones((5,20), np.uint8)
    imgfe=cv2.erode(imgf, kernel, iterations=1)
    #cv2.imshow(\'my\', imgfe)
    #cv2.waitKey(0)
    hsv = cv2.cvtColor(imgfe, cv2.COLOR_BGR2HSV)
    #cv2.imshow(\'my\', hsv)
    #cv2.waitKey(0)
    #filteryellow
    lowery = np.array([20,100,100])
    uppery = np.array([30,255,255])
    masky = cv2.inRange(hsv, lowery, uppery)
    #cv2.imshow(\'my\', masky)
    #filterred
    lowerr = np.array([160,100,100])
    upperr = np.array([179,255,255])
    maskr = cv2.inRange(hsv, lowerr, upperr)
    ret, thresh = cv2.threshold(maskr, 120.0, 255.0, cv2.THRESH_BINARY_INV)
    kernelcd = np.ones((10,30), np.uint8)
    maskr=cv2.erode(thresh, kernelcd, iterations=1)
    cdoc(maskr)
    #filtergreen
    lowerg=np.array([33,80,40])
    upperg=np.array([102,255,255])
    maskg = cv2.inRange(hsv, lowerg, upperg)
    #filterblue
    lowerb = np.array([78,158,124])
    upperb=np.array([138,255,255])
    maskb = cv2.inRange(hsv,lowerb,upperb)
    ret, thresh = cv2.threshold(maskb, 120.0, 255.0, cv2.THRESH_BINARY_INV)
    kernelcd = np.ones((5,18), np.uint8)
    maskb=cv2.erode(thresh, kernelcd, iterations=1)
    cdoc(maskb)
        
    img1=img.copy()
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 120.0, 255.0, cv2.THRESH_BINARY)
    #cv2.imshow(\'BW\', thresh)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    listcdsign=[]
    for contour in contours:
        [x,y,w,h] = cv2.boundingRect(contour)
        if w>3 or h>3:
            listcdsign.append([x,y,w,h])
            cv2.rectangle(img1, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
    print(listcdsign)
    print(str(len(listcd)))
    print(str(len(listcdsign)))
    cv2.imshow("",img1)
    cv2.waitKey(0)
    if not "math" in ocvtype:
        for i in listcdsign:
            [xsign,ysign,wsign,hsign]=i
            for c in listcd:
                [xcheck,ycheck,wcheck,hcheck]=c
                if xsign in range(xcheck,xcheck+wcheck) and ysign in range(ycheck,ycheck+hcheck):
                    #print("remove")
                    listcd.remove(c)
                    print(c)
                    listcd.append([xcheck,ycheck,(xsign+wsign)-xcheck,hcheck])
                    listcd.append([(xsign+wsign),ycheck,wcheck-((xsign+wsign)-xcheck),hcheck])
                    break
    listcd=sorted(listcd, key=itemgetter(1,0))
    for i in listcd:
        [xsign,ysign,wsign,hsign]=i
        for c in listcd:
            [xcheck,ycheck,wcheck,hcheck]=c
            if xcheck in range(xsign,xsign+wsign) and ycheck in range(ysign,ysign+hsign) and i!=c:
                listcd.remove(c)
            
    #for i in listcdoc:
    #    [xsign,ysign,wsign,hsign]=i
    #    for c in listcd:
    #        [xcheck,ycheck,wcheck,hcheck]=c
    #        if xsign in range(xcheck,xcheck+wcheck) and ysign in range(ycheck,ycheck+hcheck):
                #if (hcheck)/(hsign)>2:
                #    listcd.remove(c)
                #    print(c)
                #    listcd.append([xcheck,ycheck,wcheck,(ysign+hsign)-ycheck])
                #    listcd.append([xcheck,(ysign+hsign),wcheck,hcheck-((ysign+hsign)-ycheck)])
                #else:
                    #print("remove")
     #               listcd.remove(c)
     #               print(c)
     #               listcd.append([xcheck,ycheck,(xsign+wsign)-xcheck,hcheck])
     #               listcd.append([(xsign+wsign),ycheck,wcheck-((xsign+wsign)-xcheck),hcheck])
     #               break
    imgfinal=imgori.copy()
    withcolour=True
    if withcolour:
        for cd in listcdoc:
            [x,y,w,h] = cd
            if w>20:
                #cropthisimg
                cv2.rectangle(imgfinal, (x, y), (x+w, y+h), color=(255, 255, 255), thickness=-1)
                pass
    for cd in listcd:
        [x,y,w,h] = cd
        if w>20:
            #cropthisimg
            cv2.rectangle(imgfinal, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
            pass
    cv2.imwrite("savedmser2.jpg",imgfinal)
    cv2.imshow(\'Contoured\', imgfinal)
    
    
def everyletter_matchtcomp(imgdir):
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
imgdir="20180813194632abcdefghijklm72.jpg"
imgdir2=dir0+os.path.sep+"savedmser.jpg"
imgdir3="conv1000.jpg"
print(imgdir)
everyletter(imgdir,"")
#everyletter0(imgdir2)
##detect contourarea<50
##pick that coordinate
## for f in smallcd: dr
#cv2.drawContours(img, contours, -1, (0,255,0), 3)
#if coordinate in range():
#    x1+scx1,y1+scy1
#    scx2,x2,scy2,y2
'