#We read a image and then use canny to detect edge and then use hough transformations to get the points/
#Then we extract the points out of the lines or edges.
#And then we plot the a line with the given points.
#First Try works for black and white images only.

import cv2 as cv
import numpy as np

v1 = cv.VideoCapture("test_video.mp4")

def func(x):
    pass

cv.namedWindow("trackbar")
low=cv.createTrackbar("Low", "trackbar", 0, 255, func) 
high=cv.createTrackbar("High", "trackbar", 0, 255, func)

while True:
    low = cv.getTrackbarPos("Low", "trackbar")
    high = cv.getTrackbarPos("High","trackbar")

    _,img = v1.read()
    cv.imshow("Original", img)
    gray_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray_img, low, high)
    lines=cv.HoughLinesP(canny,1000,np.pi/180,150,200,100,150)

    for i in range(0, len(lines)):
        x1, y1, x2, y2 = lines[i][0]
        cv.line(canny,(x1,y1),(x2,y2),[0,255,255],3,cv.LINE_AA)

    cv.imshow("Detected", canny)
    k=cv.waitKey(1)
    if k==ord("q"):
        break
cv.destroyAllWindows()