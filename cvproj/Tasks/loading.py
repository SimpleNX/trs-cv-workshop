import cv2 as cv
import numpy as np

image = np.zeros((500, 500, 3), np.uint8)

sa = 0
sa1 = 0
sa2 = 0

flag = 0

#Works
#Half and Half, after one rotation white circle and then after a black circle and repeats

while True:

    if flag == 0 and sa < 360:
        cv.ellipse(image, (250, 250), (100, 100), 0, sa, sa+5, [255, 255, 255], 25)
        sa += 5
        cv.imshow("Loading", image)
        cv.ellipse(image, (250, 250), (100, 100), 0, sa-5, sa, [0, 0, 0], 25)

    elif flag == 0 and sa >= 360:
        flag = 1
        cv.ellipse(image, (250, 250), (100, 100), 0, sa1, sa1+5, [255, 255, 255], 25)
        sa1 += 5
        cv.imshow("Loading", image)

    elif flag == 1 and sa1 >= 360:
        flag = 2
        cv.ellipse(image, (250,250), (100, 100), 0, sa2, sa2+5, [0, 0, 0], 25)
        sa2 += 5
        cv.imshow("Loading", image)

    elif flag == 2:
        flag = 0
        sa = 0
        sa1 = 0
        sa2 = 0

    k = cv.waitKey(1)
    if k == ord('q'):
        break

cv.destroyAllWindows()