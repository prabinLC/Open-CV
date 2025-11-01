import cv2 as  cv
import numpy as np
import matplotlib.pyplot as plt

    
img = cv.imread("Photos/cat.png")
cv.imshow("cat",img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("grey",gray)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("hsv",hsv)

lab = cv.cvtColor(img, cv.COLOR_LBGR2LAB)
cv.imshow("hsvs",lab)


lab = cv.cvtColor(img, cv.COLOR_LBGR2LAB)
cv.imshow("hsvs",lab)


rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("hsvss",rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)

