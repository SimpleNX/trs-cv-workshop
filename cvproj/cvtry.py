import cv2
image = cv2.imread("image.png", cv2.IMREAD_COLOR)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()