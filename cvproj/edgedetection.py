import cv2
import numpy as np

vid=cv2.VideoCapture(0)

def func(x):
    pass

cv2.namedWindow("trackbar")
low=cv2.createTrackbar("Low", "trackbar", 0, 255, func) 
# (trackbar_name, window name, min_valueOfTrackbar, max_valueOfTrackbar, func)
high=cv2.createTrackbar("High", "trackbar", 0, 255, func)
# (trackbar_name, window name, min_valueOfTrackbar, max_valueOfTrackbar, func)

while True:
    low=cv2.getTrackbarPos("Low", "trackbar") # trackbar_name, window name
    high=cv2.getTrackbarPos("High", "trackbar") # trackbar_name, window name

    _,img = vid.read()
    cv2.imshow("img",img)
    gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = (5,5)
    blur = cv2.blur(gray_img, kernel)
    #two more parameters aperture_size, L2Gradient
    canny = cv2.Canny(gray_img, low, high) # canny(img, low, high) low=(0,255) high=(0,255)
    cv2.imshow("canny",canny)

    k=cv2.waitKey(1)
    if k==ord("q"):
        break

cv2.destroyAllWindows()