# Importing the modules 
import cv2 
import numpy as np 

# Reading the image 
image = cv2.imread('image.jpg') 

# Applying the filter
#HEre the pixel value is replaced with the median value of the neighbourhood pixels
#The values in the kernel would be greater than 2.
medianBlur = cv2.medianBlur(image, 9) #Value till 9.

# Showing the image 
cv2.imshow('Original', image) 
cv2.imshow('Median blur', medianBlur) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 
