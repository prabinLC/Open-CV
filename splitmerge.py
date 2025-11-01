import cv2 as cv
import numpy as np
import sys
import os

img = cv.imread("Photos/nepal.png")

if img is None:
    print("Error: Could not read the image. Please check the file path.")
    print(f"Attempted to load from: {os.path.abspath('Photos/nepal.png')}")
    sys.exit(1)

cv.imshow("nepal",img)

blank = np.zeros(img.shape[:2],dtype='uint8')
b,g,r = cv.split(img)

cv.imshow("blue",b)
cv.imshow("red",r)
cv.imshow("green",g)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

merged = cv.merge([b,g,r])
cv.imshow("merge",merged)

blue = cv.merge([b,blank,blank])
red = cv.merge([blank,blank,r])
green = cv.merge([blank,g,blank])
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)
cv.waitKey(0)