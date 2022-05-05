import cv2 as cv
import numpy as np

imagename="man.png"
img = cv.imread(imagename, cv.IMREAD_GRAYSCALE)

#msb 1
img = cv.imread(imagename, cv.IMREAD_GRAYSCALE)
for i in range(256):
    for j in range(256):
        if (img[i][j]>>0)%2 == 1:
            img[i][j]=255
        else:
            img[i][j]=0
cv.imshow("msb",img)

#5
img = cv.imread(imagename, cv.IMREAD_GRAYSCALE)
for i in range(256):
    for j in range(256):
        if (img[i][j]>>4)%2 == 1:
            img[i][j]=255
        else:
            img[i][j]=0
cv.imshow("5",img)

# lsb 8
img = cv.imread(imagename, cv.IMREAD_GRAYSCALE)
for i in range(256):
    for j in range(256):
        if (img[i][j]>>7)%2==1:
            img[i][j]=255
        else:
            img[i][j]=0
cv.imshow("lsb",img)
cv.waitKey(0)
