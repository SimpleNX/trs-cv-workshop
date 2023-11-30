#We read a image and then use canny to detect edge and then use hough transformations to get the points/
#Then we extract the points out of the lines or edges.
#And then we plot the a line with the given points.
#First Try works for black and white images only.

import cv2 as cv
import numpy as np

v1 = cv.VideoCapture("test_video.mp4")

#Lane Detection frame by frame.

while True:
    _,img = v1.read()
    cv.imshow("Original", img)
    canny = cv.Canny(gray_img, 150, 250)
    lines=cv.HoughLinesP(canny,1,np.pi/180,150,minLineLength=50,maxLineGap=50)

    for i in range(0, len(lines)):
        x1, y1, x2, y2 = lines[i][0]
        cv.line(canny,(x1,y1),(x2,y2),[0,255,255],3,cv.LINE_AA)

    cv.imshow("Detected", canny)
    k=cv.waitKey(1)
    if k==ord("q"):
        break
cv.destroyAllWindows()