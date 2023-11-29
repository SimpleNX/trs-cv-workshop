import cv2 as cv
import numpy as np

image = np.zeros((500,500,3),0,np.uint8)

sa=0
#Works
#Half and Half, after one rotation white circle and then after a black circle and repeats
while(True):
    cv.ellipse(image, (250,250),(100,100), 0, sa, sa+5, [255,255,255],25)
    sa+=5
    cv.ellipse(image, (250,250),(100,100), 0, sa-5,sa, [0,0,0],25)
    cv.imshow("Loading", image)
    #Homeowork
    if(sa>355):
        cv.ellipse()
    if cv.waitKey(10) & 0xFF==27:
        break
cv.destroyAllWindows()