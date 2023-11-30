#For Template matching
#cv2.matchTemplate(image, template, method)
'''Methods:
    TM_SQDIFF
    TM_SQDIFF_NORMED
    CCORR
    CCOEFF'''
#If the sqdiff between the template and the image is zero at a square region of the image, that is where we have detected the template.
#cv2.minMaxLoc()
'''It returns the max value and the coordinate of the top left corner of this rectangle.
Same with the minimum'''
'''template.jpg, plane.jpg'''
import cv2 as cv
import numpy as np

#Reading the image and the template
image = cv.imread("plane.jpg",cv.IMREAD_COLOR)
template = cv.imread("template.jpg", cv.IMREAD_COLOR)

w,h = template.shape#Getting the shape of the template so as to form the detection rectangle.
#Matching the template and the target image
tempmat = cv.matchTemplate(image, template,cv.TM_SQDIFF)

#Finding the max and min val coordinates.
n,x, nl, xl = cv.minMaxLoc(tempmat)

#Drawing the required detection rectangle over the image
cv.rectangle(image, nl,[nl[0]+w,nl[1]+h] ,[255,255,255],2)
cv.imshow("Detected Template", image)

if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()

#Drawbacks
#It works for only 100% matching image and template.
