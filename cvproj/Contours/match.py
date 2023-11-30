import cv2 

img1 = cv2.imread('gorilla.png')
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

_,binary_img1 = cv2.threshold(gray_img1, 50, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("tiger1",binary_img1)

img2 = cv2.imread('tiger2.jpg')
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

_,binary_img2 = cv2.threshold(gray_img2, 50, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("tiger2",binary_img2)

contour1, hierarchy = cv2.findContours(binary_img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour2, hierarchy = cv2.findContours(binary_img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cont_diff = cv2.matchShapes(contour1[0], contour2[0], cv2.CONTOURS_MATCH_I1, 0)
print(cont_diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
