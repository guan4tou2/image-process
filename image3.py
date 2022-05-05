import random
import cv2 as cv
import numpy as np
imagename="man.png"
img = cv.imread(imagename, cv.IMREAD_GRAYSCALE)

#128x128
for i in range(0,256,2):
    for j in range(0,256,2):
        img[i][j+1] = img[i+1][j] = img[i+1][j+1] = img[i][j]
cv.imshow("128x128",img)
# cv.waitKey(0)

#64x64
img = cv.imread(imagename, cv.IMREAD_GRAYSCALE)
for i in range(0,256,4):
    for j in range(0,256,4):
        x=random.randint(0,3)
        y=random.randint(0,3)
        px=img[i+x][j+y]
        for y in range(4):
            for z in range(4):
               img[i+y][j+z]=px
cv.imshow("64x64",img)
cv.waitKey(0)
