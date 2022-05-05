import cv2 as cv
import numpy as np

imagename = "man.png"
img = cv.imread(imagename, cv.IMREAD_GRAYSCALE)

#a
for i in range(256):
    for j in range(256):
        img[i][j] = img[i][j]//4
cv.imshow("a", img)

#b 
img = cv.imread(imagename, cv.IMREAD_GRAYSCALE)
for i in range(256):
    for j in range(256):
        if img[i][j]<=128:
            img[i][j] = img[i][j]//2

cv.imshow("b", img)
cv.waitKey(0)
