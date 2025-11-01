import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("blnak",blank)
# print(blank)
# cv.line(blank,(200,200),(300,300),)
# blank[100:200,200:400] = 0,255,0
# cv.imshow("green",blank)
# print(blank)



cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
print('the ' , blank)
# cv.imshow('rectangle',blank)s



cv.line(blank,(0,0),(500,500),(255,0,0),thickness=2)
# cv.imshow('line',blank)s

cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),49,(255,255,0),-1)
# cv.imshow("circle",blank)s
cv.putText(blank,'hi this is test img',(0,255),cv.FONT_HERSHEY_SIMPLEX,2.0,(255,0,0),2)
cv.imshow("writing",blank)
cv.waitKey(0)



#import the image