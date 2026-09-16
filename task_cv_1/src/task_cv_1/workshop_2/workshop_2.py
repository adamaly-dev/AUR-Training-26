import cv2 as cv
import numpy as np

# Orange to Red
# Red to Green
# Green to Orange

LOW_ORANGE = (5, 100, 100)
HIGH_ORANGE = (25, 255, 255)
LOW_RED = (0, 100, 100)
HIGH_RED = (10, 255, 255)
LOW_GREEN = (35, 80, 80)
HIGH_GREEN = (90, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (0, 165, 255)

img = cv.imread("task2.jpg")
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask_orange = cv.inRange(img_hsv, LOW_ORANGE, HIGH_ORANGE)
mask_red = cv.inRange(img_hsv, LOW_RED, HIGH_RED)
mask_green = cv.inRange(img_hsv, LOW_GREEN, HIGH_GREEN)

img[mask_red > 0] = GREEN
img[mask_orange > 0] = RED
img[mask_green > 0] = ORANGE

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()