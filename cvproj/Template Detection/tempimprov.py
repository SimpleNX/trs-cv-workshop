#Improved Version of Template Matching
#A range of matches can be used to detect similiar objects.
import cv2 as cv
import numpy as np

#Reading the image and the template
image = cv.imread("plane.jpg",cv.IMREAD_COLOR)
template = cv.imread("template.jpg", cv.IMREAD_COLOR)

w,h = template.shape#Getting the shape of the template so as to form the detection rectangle.
#Matching the template and the target image
tempmat = cv.matchTemplate(image, template,cv.TM_SQDIFF_NORMED)

#Finding the max and min val coordinates.
n,x, nl, xl = cv.minMaxLoc(tempmat)

#Defining the threshold after which an object is determined as similiar to the template.
threshold = 0.6
loc = np.where(result>=threshold)
#print(loc)

#Printing the coordinates which pass the threshold:
for pt in zip(*loc[::-1]):
    #print(pt)
    cv.rectangle(image, pt, (pt[0]+w,pt[1]+h), [255,255,255],2)
#Drawing the required detection rectangle over the image
#cv.rectangle(image, nl,[nl[0]+w,nl[1]+h] ,[255,255,255],2)
cv.imshow("Detected Template", image)

if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()