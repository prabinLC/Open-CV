import cv2 as cv
import numpy as np
img = cv.imread("Photos\cat.png")

# cv.imshow("cat",img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

cannyedge = cv.Canny(blur,175,300)
cv.imshow("canny",cannyedge)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("blank",blank)


res, thres = cv.threshold(gray,150,200, cv.THRESH_BINARY)
cv.imshow("thress",thres)
print(thres)
contours, _ = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank,contours,-1,(0,0,255),1) 
cv.imshow("blank can",blank)

print(f'{len(contours)} many countours')
cv.waitKey(0)