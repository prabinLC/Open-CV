import cv2 as cv
import numpy as np
img = cv.imread("Photos\cat.png")
vid = cv.VideoCapture("Videos\Dog.mp4")
blank = np.zeros((500,500,3),dtype='uint8')

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def draw(x):
    # cv.imshow("rand",x)
    cv.line(x,(200,200),(250,250),(255,255,0),thickness=2)
    # cv.imshow("line",x)
    # cv.circle(x,(x.shape[1]//2,x.shape[0]//2), 10,(255,255,0),thickness=2)
    cv.rectangle(x,(x.shape[1]//2,x.shape[0]//2), (10,10),(255,255,0),thickness=2)
    cv.putText(x,'hellow world',(0,255),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,0),2)
    
    resized =cv.resize(x,(200,200))
    cv.imshow("x",resized)
    # cv.imshow('circle',x)

# cv.imshow("cat",img)

draw(blank)

cv.waitKey(0)
# while True:
#     isTrue, frame = vid.read()
#     # cv.imshow("vid",frame)
#     frame_rescale = rescaleFrame(frame,0.2)
#     cv.imshow("vids",frame_rescale)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
    
# vid.release()
# cv.destroyAllWindows()


