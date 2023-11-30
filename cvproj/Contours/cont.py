#cv2.findContours(image, contour_retrieval_mode, contour_approximation_method)
#Works
import cv2 as cv
import numpy as np

imgR = cv.imread("shapes.jpg", 1)
img = cv.cvtColor(imgR, cv.COLOR_BGR2GRAY)#Converts the image to grayscale image
#Making a frame to draw the detected contours.
#frame = np.full((500,500,3), 0, dtype = np.uint8)
#Using threshold functions to convert the image to binary
#ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
canny = cv.Canny(img, 30, 300)#Canny is used to detect the edges on the image
#Contour are used to find the contours and store.
contours, heirarchy= cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#Drawing the contours. by the help of the list of contours.
cv.drawContours(canny, contours, -1, (255,255,255), 3)
cv.drawContours(img, contours, -1, (255,255,255), 5)
cv.imshow("Contoured Image", canny)
cv.imshow("Contours on Original", img)
k= cv.waitKey(0)
if k==ord('q'):
    cv.destroyAllWindows()