import cv2 as cv
import numpy as np

img = cv.imread("task3.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (5, 5), 0)
img = cv.Canny(img, 50, 150)

cv.imshow("Processed Image", img)
cv.waitKey(0)
cv.destroyAllWindows()