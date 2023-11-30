import numpy as np
import cv2 
import keyboard as kb
img = np.full((500,500,3),0, dtype=np.uint8)

flag =0
t=0

cx=250
cy=250

#Making up Pacman
while True :
    img=np.full((500,500,3),0,dtype=np.uint8)
    cv2.ellipse(img,(cx,cy),(50,50),-135-t,135+t,[0,255,255],-1)
    if(t==0):
        t+=1
    if(t>=45):
        flag=1
    if(t<=0):
        flag=0
    if flag==1:
        t-=1
#If key is pressed then the direction of mouth changes to face that direction
#And the centre of the ellipse shifts by some move value.
#Then the whole animation of it moving along that direction continues until it detects another keypress.

    #if kb.is_Pressed('w'):

    cv2.imshow("img",img)
    cv2.waitKey(1)

#Using Keyboard Module to simulate the movements of PacMan
#Homework to simulate the function.