# Importing the modules 
import cv2 
import numpy as np 

# Reading the image 
image = cv2.imread('image.jpg') 

# Applying the filter 
#Mean filtering using a n*n kernel
averageBlur = cv2.blur(image, (5, 5)) 

# Showing the image 
cv2.imshow('Original', image) 
cv2.imshow('Average blur', averageBlur) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 
