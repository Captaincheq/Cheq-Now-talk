from cv2 import cv2
import numpy as np

img = cv2.imread("frank.jpg")

a = cv2.blur(img, (10,10))
g = cv2.GaussianBlur(img, (5,5), 0)
m = cv2.medianBlur(img, 5)

cv2.imshow("o",img)
cv2.imshow("a",a)
cv2.imshow("g",g)
cv2.imshow("m", m)

cv2.waitKey(0)
cv2.destroyAllWindows()
