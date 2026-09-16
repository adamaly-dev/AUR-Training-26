import cv2 as cv
import numpy as np

img = cv.imread("task3.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (5, 5), 0)
img = cv.Canny(img, 50, 150)

contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

freq = {"Triangle": 0, "Square": 0, "Rectangle": 0, "Circle": 0}

new_img = cv.imread("task3.jpg")

for contour in contours:
    area = cv.contourArea(contour)
    if area < 200:
        continue

    perimeter = cv.arcLength(contour, True)
    points = cv.approxPolyDP(contour, 0.037 * perimeter, True)

    new_img = cv.drawContours(new_img, [points], 0, (0, 255, 0), 2)

    M = cv.moments(points)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    txt = ""

    if len(points) == 3:
        txt = "Triangle"
    
        freq["Triangle"] += 1
    elif len(points) == 4:
        x, y, h, w = cv.boundingRect(points)
        # print(x, y, h , w)
        # print(w/h)
        if 0.97 < w/h < 1.03:
            txt = "Square"
            freq["Square"] += 1
        else:
            txt = "Rectangle"
            freq["Rectangle"] += 1
    else:
        txt = "Circle"
        freq["Circle"] += 1
    cv.putText(new_img, txt, (cx-50, cy), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

for key, value in freq.items():
    print(f"{key}: {value}")

cv.imshow("Canny Edges", img)
cv.imshow("Processed Image", new_img)
cv.waitKey(0)
cv.destroyAllWindows()