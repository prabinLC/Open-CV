import cv2 as cv
from rescale import *

img = cv.imread("Photos\cat.png")
cv.imshow("cat",img)
cv.waitKey(0)

video = cv.VideoCapture("Videos\Dog.mp4")
while True:
    isTrue, frame = video.read()

    frame_resized = rescaleFrame(frame, scale=0.2)
    frame_resized = resize_live(2,2,frame)
    # cv.imshow('Video',frame)
    cv.imshow("rescale",frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()

