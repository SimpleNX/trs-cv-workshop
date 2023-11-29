#We read a image and then use canny to detect edge and then use hough transformations to get the points/
#Then we extract the points out of the lines or edges.
#And then we plot the a line with the given points.
import cv2 as cv
import numpy as np

vi = cv.VideoCapture("test_video.mp4")
while True:
    _,img = vi.read()
    gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray,50,200,None,3)
    lines = cv.HoughLinesP(canny, 1000, np.pi/180,50,None,50,10)
    for i in range(0,len(lines)):
        l = lines[i][0]
        cv.line(vi, (l[0],l[1]),(l[2],l[3]),[0,255,255],3,cv.LINE_AA)
    cv.imshow("Original",vi)
    cv.imshow("Detected",canny)
    k=cv.waitKey(1)
    if k==ord('q'):
        break
cv.destroyAllWindows()