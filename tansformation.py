import cv2 as cv
import numpy as np
img = cv.imread("Photos\cat.png")

cv.imshow("name",img)


def translate (img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

transforms = translate(img,100,100)

# cv.imshow("tanslated",transforms)


def rotated(img,angle,point=None):
    dimension = img.shape[:2 ]

    if point is None:
        point = (img.shape[1]//2,img.shape[1]//2)

    rotMatrix = cv.getRotationMatrix2D(point,angle,2)
    return cv.warpAffine(img,rotMatrix,dimension)

# r_t = rotated(img, 45)
# cv.imshow('dsfdsf',r_t)
# r_t1 = rotated(r_t, 45)
# cv.imshow('dsfdsf1',r_t1)
# res = cv.resize(img,(200,200),interpolation=cv.INTER_CUBIC)
# cv.imshow('s',res)

flip0 = cv.flip(img,0)
cv.imshow('flip0',flip0)
flip1 = cv.flip(img,1)
cv.imshow('flip1',flip1)
flip_1 = cv.flip(img,-1)
cv.imshow('flip_1',flip_1)

cv.waitKey(0)