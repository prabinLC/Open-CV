import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def resize_live(width,height,video):
    video.set(3,width) 
    video.set(4,height)