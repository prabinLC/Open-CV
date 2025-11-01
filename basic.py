import cv2 as cv

img = cv.imread("Photos\cat.png")

# cv.imshow("show", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

canny = cv.Canny(blur, 100,20)



cv.imshow("canny edges",canny)
dialated = cv.dilate(canny, (7,7),iterations=3)
cv.imshow("dialated edges",dialated)


eroded = cv.erode(dialated,(3,3), iterations=1)
cv.imshow("eroded edges",eroded)

resized = cv.resize(img,(200,200))
cv.imshow('lol',resized)

crope = img[50:200,200:400]
cv.imshow("crop",crope)

cv.waitKey(0)