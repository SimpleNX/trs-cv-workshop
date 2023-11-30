import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)#Reading video from the webcam

while True:
    _,img = vid.read()#Reading frame by frame images from the video
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)#Converting the image to grayscale to work for contour.
#Detecting the edges via canny detection.
    canny=cv.Canny(img_gray,30,300)
#Unpacking the contours
    contours, heirarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#Drawing the contours on the image.
    cv.drawContours(img_gray, contours,-1,(255,0,0),3)
    cv.drawContours(img, contours,-1,(255,0,0),3)
#Showing the contoured images.
    cv.imshow("Contoured Original", img)
    cv.imshow("Contoured Grayscale", img_gray)

    k = cv.waitKey(1)
    if k==ord('q'):
        break
cv.destroyAllWindows()