import numpy as np
import cv2 
import keyboard as kb
img = np.full((500,500,3),0, dtype=np.uint8)

flag =0
t=0
#Making up Pacman
while True :
    img=np.full((500,500,3),0,dtype=np.uint8)
    cv2.ellipse(img,(250,250),(50,50),-135-s,135+s,[0,255,255],-1)
    if(t==0):
        t+=1
    if(t>=45):
        flag=1
    if(t<=0):
        flag=0
    if flag==1:
        t-=1
    cv2.imshow("img",img)
    cv2.waitKey(1)

#Using Keyboard Module to simulate the movements of PacMan
#Homework to simulate the function.