import cv2
import numpy as np
img = np.full((500,500,3), 255, dtype =np.uint8)#Image using numpy
#img[200:300, 200:300]=[255,0,0]
'''cv2.circle(img, (250,250), 40, [255,0,255], 4)#Circle
cv2.imshow("img", img)
cv2.waitKey(0)'''

#Animation to square bouncing in vertical direction.

steps =10
h=200
w=200
flag=0

while True:
    if flag==0:
        cv2.rectangle(img,[w,h],[w+100,h+100],[0,0,0], -1)
        h+=steps
        cv2.rectangle(img, [w,h], [w+100,h+100], [255,0,0],-1)
        cv2.imshow("img", img)
        if (h+100)>=500:
            flag=1
    if flag==1:
        cv2.rectangle(img,[w,h],[w+100,h+100],[0,0,0], -1)
        h-=steps
        cv2.rectangle(img, [w,h], [w+100,h+100], [255,0,0],-1)
        cv2.imshow("img", img)
        if (h)<=0:
            flag=0
    if cv.waitKey(0) & 0xFF==ord('q'):
        break
    cv2.imshow("img", img)
    #cv2.waitKey(1)