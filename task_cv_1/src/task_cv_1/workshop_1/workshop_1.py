import cv2 as cv
import numpy as np

SKY_COLOR =  (25, 25, 40)
GROUND_COLOR = (30, 50, 35)
BUILDING_COLOR = (90, 90, 100)
WINDOW_OFF_COLOR = (20, 20, 30)
WINDOW_ON_COLOR = (255, 220, 120)

HEIGHT = 700
WIDTH = 600
ROW_COUNT = 6
COL_COUNT = 5

img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

def genWindow(i, j):
    return (int(HEIGHT*0.1)+i*70+20, int(HEIGHT*0.1)+i*70+70, int(WIDTH*0.2)+j*75+15, int(WIDTH*0.2)+j*75+45)

def draw(img):
    #Sky
    img[:] = SKY_COLOR

    #Ground
    img[int(HEIGHT*0.8):HEIGHT, :] = GROUND_COLOR

    #Building
    img[int(HEIGHT*0.1):int(HEIGHT*0.85), int(WIDTH*0.15):int(WIDTH*0.85)] = BUILDING_COLOR

    #Windows
    windows = []
    for x in range(6):
        for y in range(5):
            windows.append(genWindow(x, y))
            img[windows[-1][0]:windows[-1][1], windows[-1][2]:windows[-1][3]] = WINDOW_OFF_COLOR

    #Picked Windows
    picked_windows = np.random.choice(COL_COUNT*ROW_COUNT, 4)

    for idx in picked_windows:
        (x0, x1, y0, y1) = windows[idx] 
        img[x0:x1, y0:y1] = WINDOW_ON_COLOR

    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

while True:
    draw(img)    
    cv.imshow("Building", img)
    if cv.waitKey(1000) == 27:
        break

cv.destroyAllWindows()