import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("task_1.png")

normal_blur = cv.blur(img, (3, 3))
gaussian_blur = cv.GaussianBlur(img, (3, 3), 0)
median_blur = cv.medianBlur(img, 3)

normal_blur_tuned = cv.cvtColor(normal_blur, cv.COLOR_BGR2GRAY)
gaussian_blur_tuned = cv.cvtColor(gaussian_blur, cv.COLOR_BGR2GRAY)
median_blur_tuned = cv.cvtColor(median_blur, cv.COLOR_BGR2GRAY)

normal_blur_canny = cv.Canny(normal_blur_tuned, 50, 150)
gaussian_blur_canny = cv.Canny(gaussian_blur_tuned, 50, 150)
median_blur_canny = cv.Canny(median_blur_tuned, 50, 150)

fig, axes = plt.subplots(3, 3, figsize=(16, 16))
ax = axes.ravel()

for i in range(9):
    ax[i].axis("off")

ax[1].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
ax[1].set_title("Image")

ax[3].imshow(cv.cvtColor(normal_blur, cv.COLOR_BGR2RGB))
ax[3].set_title("Normal Blur")

ax[4].imshow(cv.cvtColor(gaussian_blur, cv.COLOR_BGR2RGB))
ax[4].set_title("Gaussian Blur")

ax[5].imshow(cv.cvtColor(median_blur, cv.COLOR_BGR2RGB))
ax[5].set_title("Median Blur")

ax[6].imshow(normal_blur_canny)
ax[6].set_title("Normal Blur Canny")

ax[7].imshow(gaussian_blur_canny)
ax[7].set_title("Gaussian Blur Canny")

ax[8].imshow(median_blur_canny)
ax[8].set_title("Median Blur Canny")

plt.show()

#running command
#QT_QPA_PLATFORM=wayland uv run python3 task_1.py