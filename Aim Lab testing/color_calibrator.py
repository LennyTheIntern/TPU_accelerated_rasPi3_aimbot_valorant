import cv2
import numpy as np

cap = cv2.VideoCapture(0)

hmin = 130
smin = 166
vmin = 0

hmax = 179
smax = 255
vmax = 255


def on_change_hmax(value):
    global hmax
    hmax = value
    print (hmax)
def on_change_smax(value):
    global smax
    smax = value
    print (smax)
def on_change_vmax(value):
    global vmax
    vmax = value
    print (vmax)


def on_change_hmin(value):
    global hmin
    hmin= value
    print (hmin)
def on_change_smin(value):
    global smin
    smin = value
    print (smin)
def on_change_vmin(value):
    global vmin
    vmin = value
    print (vmin)    



name_bars = 'trackbar window'
cv2.namedWindow('trackbar window',cv2.WINDOW_NORMAL)
cv2.createTrackbar("hue max",name_bars,179,179,on_change_hmax)
cv2.createTrackbar("sat max",name_bars,255,255,on_change_smax)
cv2.createTrackbar("val max",name_bars,255,255,on_change_vmax)
cv2.createTrackbar("hue min",name_bars,130,179,on_change_hmin)
cv2.createTrackbar("sat min",name_bars,166,255,on_change_smin)
cv2.createTrackbar("val min",name_bars,0,255,on_change_vmin)

while True:
    ret,img = cap.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 
    
    
    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])

    
    mask = cv2.inRange(hsv,lower,upper)
    #masked = cv2.bitwise_and(hsv,hsv,mask=mask)
    
    con= cv2.findContours(mask.copy(),
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
    
        
    if(len(con) > 0):
        i = 0
        for c in con:
            area = cv2.contourArea(c)
            
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            print('element:',i)
            print("x:",x)
    #cv2.imshow("result",img)
    #cv2.imshow("masked",masked)
    #trak bars for other stuff
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()