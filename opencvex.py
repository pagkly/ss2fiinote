from imutils import perspective
from imutils import contours
import numpy as np
import imutils

def capturecam0():
    # Webcamera no 0 is used to capture the frames
    cap = cv2.VideoCapture(0)
    # This drives the program into an infinite loop.
    while(1):       
        # Captures the live stream frame-by-frame
        _, frame = cap.read() 
        # Converts images from BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # This displays the frame, mask 
    # and res which we created in 3 separate windows.
        k = cv2.waitKey(5) &amp; 0xFF
        if k == 27:
            break
    # Destroys all of the HighGUI windows.
    cv2.destroyAllWindows() 
    # release the captured frame
    cap.release()
 def convertblue(imgdir,imgname):
    img=cv2.imread(imgdir+os.path.sep+imgname)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([110,50,50])
    upper_red = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # The bitwise and of the frame and mask is done so 
    # that only the blue coloured objects are highlighted 
    # and stored in res
    res = cv2.bitwise_and(img, img, mask= mask)
    cv2.imwrite(imgdir+os.path.sep+'grabblue.png', res)
    return True
#convertblue("/home/user/Pictures","Screenshot from 2018-07-05 20-04-46.png")

def order_points_old(pts):
    # initialize a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # return the ordered coordinates
    return rect
def convertblue3(imgdir,imgname):
    #https://www.pyimagesearch.com/2016/03/21/ordering-coordinates-clockwise-with-python-and-opencv/
    a=1000
    # load our input image, convert it to grayscale, and blur it slightly
    image = cv2.imread(imgdir+os.path.sep+imgname)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    # sort the contours from left-to-right and initialize the bounding box
    # point colors
    (cnts, _) = contours.sort_contours(cnts)
    colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))
    # loop over the contours individually
    for (i, c) in enumerate(cnts):
        if cv2.contourArea(c)<100:
            continue
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
        # show the original coordinates
        print("Object #{}:".format(i + 1))
        print(box)
        # in top-left, top-right, bottom-right, and bottom-left
        # order, then draw the outline of the rotated bounding
        # box
        rect = order_points_old(box)
        # check to see if the new method should be used for
        # ordering the coordinates
        ##if args["new"] > 0:
            ##rect = perspective.order_points(box)
        #show the re-ordered coordinates
        print(rect.astype("int"))
        print("")
        # loop over the original points and draw them
        for ((x, y), color) in zip(rect, colors):
            cv2.circle(image, (int(x), int(y)), 5, color, -1)
        cv2.putText(image, "Object #{}".format(i + 1),(int(rect[0][0] - 15), int(rect[0][1] - 15)),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
        a-=1
        cv2.imwrite(imgdir+os.path.sep+str(a)+"t1blue"+imgname, image)
