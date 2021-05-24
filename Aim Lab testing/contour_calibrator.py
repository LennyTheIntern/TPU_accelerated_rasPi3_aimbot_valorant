import cv2
import numpy as np


def empty(c):
    pass
cap = cv2.VideoCapture(0)


cv2.namedWindow('trackbars')
#cv2,resizeWindow('trackbars',640,240)
cv2.createTrackbar('t1','trackbars',0,255,empty)
cv2.createTrackbar('t2','trackbars',0,255,empty)



while True:
    ret,img = cap.read()
    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGrey = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    
    
    t1 = cv2.getTrackbarPos('t1','trackbars')
    t2 = cv2.getTrackbarPos('t2','trackbars')
    imgCanny= cv2.Canny(imgGrey,t1,t2) 
    #cv2.imshow('img',img);
    #cv2.imshow('blur',imgBlur);
    cv2.imshow('grey',imgCanny);
    
    cv2.waitKey(1)