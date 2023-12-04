#cv2.SimpleBlobDetector(src,minThres,maxThres,thresStep)
#Thres max and min is the range of area to find the circle or blob.
#cv2.drawKeypoints(inimg,keypoints,outimg,color,flag)
#Drawing Circle around the blob detected.

import cv2 as cv
import numpy as np

img = cv.imread("bubbles.png", 0)

#Blob Function takes input as dictionaries.
#More like its a class, defining objects and assign values to attributes of the object.
para = cv.SimpleBlobDetector_Params()

para.minThreshold = 10
para.maxThreshold = 100
para.minArea = 200
para.filterByArea = True

detector = cv.SimpleBlobDetector_create(para)

keypoint = detector.detect(img)

image_with_keypoint = cv.drawKeypoints(img, keypoint, np.array([]), (255,0,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow("image", image_with_keypoint)
cv.waitKey(0)
cv.destroyAllWindows()