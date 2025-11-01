import cv2 as cv
import numpy as np

img = cv.imread("Photos/nepal.png")

cv.imshow("nepal",img)
average = cv.blur(img,(3,3))
gaus = cv.GaussianBlur(img,(3,3),0)
meadian = cv.medianBlur(img,3)
bilateral = cv.bilateralFilter(img,15,35,35)
cv.imshow("average",average)
cv.imshow("gaus",gaus)
cv.imshow("meadian",meadian)
cv.imshow("bilateral",bilateral)

cv.waitKey(0)