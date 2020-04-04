# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import cv2
import numpy as np
# initialize the camera and grab a reference to the raw camera capture
resx,resy=640,480
camera = PiCamera()
camera.resolution = (resx,resy)
camera.framerate = 40
rawCapture = PiRGBArray(camera, size=(resx,resy))
# allow the camera to warmup
time.sleep(0.1)


#initialization
c_blue=c_red=c_green=c_orange=c_yellow=0
area_low=resx*resy/100
area_high=20000

# capture frames from the camera
for img in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    frame = img.array
    
    #_,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX

    #blue
    low_blue=np.array([85,121,86])
    high_blue=np.array([119,255,255])
    mask1=cv2.inRange(hsv,low_blue,high_blue)
    blur1=cv2.GaussianBlur(mask1,(15,15),0)
    contours1,_=cv2.findContours(blur1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    c_blue=0 #reset the values for count of blue object
    for contour1 in contours1:
        area1=cv2.contourArea(contour1)
        
        if (area1>area_low and area1<area_high):
            approx = cv2.approxPolyDP(contour1, 0.009 * cv2.arcLength(contour1, True), True) 
            n=approx.ravel()
            x=n[0]
            y=n[1]
            c_blue+=1
            cv2.drawContours(frame,[approx],0,(255,0,0),3)
            cv2.putText(frame,str(c_blue),(x,y), font, 2,(255,0,0),2,cv2.LINE_AA)
    cv2.putText(frame,'B='+str(c_blue),(50,50), font, 1,(255,0,0),2,cv2.LINE_AA)
    

    #Red
    low_red=np.array([131,92,83])
    high_red=np.array([179,255,255])
    mask2=cv2.inRange(hsv,low_red,high_red)
    blur2=cv2.GaussianBlur(mask2,(15,15),0)
    contours2,_=cv2.findContours(blur2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    c_red=0
    
    for contour2 in contours2:
        area2=cv2.contourArea(contour2)
        
        if (area2>area_low and area2<area_high):
            approx = cv2.approxPolyDP(contour2, 0.009 * cv2.arcLength(contour2, True), True) 
            n=approx.ravel()
            x=n[0]
            y=n[1]
            c_red+=1
            cv2.drawContours(frame,[approx],0,(0,0,255),3)
            cv2.putText(frame,str(c_red),(x,y), font, 2,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame,'R='+str(c_red),(50,80), font, 1,(0,0,255),2,cv2.LINE_AA)
    
   
    #Green
        
    low_green=np.array([61,89,121])
    high_green=np.array([87,255,255])
    mask3=cv2.inRange(hsv,low_green,high_green)
    blur3=cv2.GaussianBlur(mask3,(15,15),0)
    contours3,_=cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    c_green=0
    
    for contour3 in contours3:
        area3=cv2.contourArea(contour3)

        if (area3>area_low and area3<area_high):
            approx = cv2.approxPolyDP(contour3, 0.009 * cv2.arcLength(contour3, True), True) 
            n=approx.ravel()
            x=n[0]
            y=n[1]
            c_green+=1
            cv2.drawContours(frame,[approx],-1,(0,255,0),3)
            cv2.putText(frame,str(c_green),(x,y), font, 2,(0,255,0),2,cv2.LINE_AA)       
    cv2.putText(frame,'G='+str(c_green),(50,110), font, 1,(0,255,0),2,cv2.LINE_AA)
   
    #orange
    
    low_or=np.array([0,89,99])
    high_or=np.array([11,188,201])
    mask4=cv2.inRange(hsv,low_or,high_or)
    blur4=cv2.GaussianBlur(mask4,(15,15),0)
    contours4,_=cv2.findContours(blur4,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    c_orange=0
    for contour4 in contours4:
        area4=cv2.contourArea(contour4)

        if (area4>area_low and area4<area_high):
            approx = cv2.approxPolyDP(contour4, 0.009 * cv2.arcLength(contour4, True), True) 
            n=approx.ravel()
            x=n[0]
            y=n[1]
            c_orange+=1
            cv2.drawContours(frame,[approx],-1,(0,140,255),3)
            cv2.putText(frame,str(c_orange),(x,y), font, 2,(0,140,255),2,cv2.LINE_AA)       
    cv2.putText(frame,'O='+str(c_orange),(50,140), font, 1,(0,140,255),2,cv2.LINE_AA)
   
    #yellow
    
    low_ye=np.array([30,61,103])
    high_ye=np.array([61,255,255])
    mask5=cv2.inRange(hsv,low_ye,high_ye)
    blur5=cv2.GaussianBlur(mask5,(15,15),0)
    contours5,_=cv2.findContours(blur5,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    c_yellow=0
    
    for contour5 in contours5:
        area5=cv2.contourArea(contour5)

        if (area5>area_low and area5<area_high):
            approx = cv2.approxPolyDP(contour5, 0.009 * cv2.arcLength(contour5, True), True) 
            n=approx.ravel()
            x=n[0]
            y=n[1]
            c_yellow+=1
            cv2.drawContours(frame,[approx],-1,(0,215,255),3)
            cv2.putText(frame,str(c_yellow),(x,y), font, 2,(0,215,255),2,cv2.LINE_AA)       
    cv2.putText(frame,'Y='+str(c_yellow),(50,170), font, 1,(0,215,255),2,cv2.LINE_AA)
   

    cv2.imshow("frame",frame)
    
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    if cv2.waitKey(1)==27:#press esc to exit
        break;

cv2.destroyAllWindows()
