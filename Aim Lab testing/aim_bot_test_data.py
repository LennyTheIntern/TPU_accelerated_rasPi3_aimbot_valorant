import cv2
import numpy as np
import serial
from time import sleep
from smbus import SMBus
addr = 0x8
bus = SMBus(1)
numb = 11234



#ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
cap = cv2.VideoCapture(0)

#center of the screen
center_x = 318
center_y = 238

#HSV mins for color detection
hmin = 130
smin = 166
vmin = 0
#HSV max for color detection 
hmax = 179
smax = 255
vmax = 255

#these should just be replaced for getpos
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

click_flag = False

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
        smallest_distance = 10000
        x_min = 0
        y_min = 0
        for c in con:
            area = cv2.contourArea(c)
            
            if(area > 25):
                i += 1
                (x,y,w,h) = cv2.boundingRect(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                #print('element:',i)

                
                # there might be a faster aproximation function
                temp_distance = np.sqrt(((x-center_x + (w >> 1))**2) + ((y- center_y+ (h >> 1))**2))
                #(temp_distance)
                if(temp_distance < smallest_distance):
                    smallest_distance = temp_distance
                    if(temp_distance < 40):
                        click_flag = True
                        
                    x_min = x - center_x + (w >> 1)
                    y_min = y - center_y + (h >> 1)
        if(click_flag):
            try:
                bus.write_byte(addr,0xA0A0 >> 0)
                bus.write_byte(addr,0xA0A0 >> 8)
                bus.write_byte(addr,0xA0A0 >> 0)
                bus.write_byte(addr,0xA0A0 >> 8)
            except:
                print("click failed")
            click_flag = False
        if(y_min != 0 or x_min != 0):
            y_min = y_min >> 2 if y_min < 127 else 10;
            x_min = x_min >> 2 if x_min < 127 else 10;
            try:
                bus.write_byte(addr,x_min >> 0)
                bus.write_byte(addr,x_min >> 8)
                bus.write_byte(addr,y_min >> 0)
                bus.write_byte(addr,y_min >> 8)
            except:
                print("lost a mouse move")
            #sleep(.05)
        #print("x:",x_min)
        #print("y:",y_min) 

    #cv2.imshow("result",img)
    #cv2.imshow("masked",masked)
    #trak bars for other stuff
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()