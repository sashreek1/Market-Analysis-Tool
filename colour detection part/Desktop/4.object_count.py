import cv2
import numpy as np

cap=cv2.VideoCapture(0)
#initialization
c_blue=0
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX

    #blue
    low_blue=np.array([70,102,68])
    high_blue=np.array([133,225,240])
    mask1=cv2.inRange(hsv,low_blue,high_blue)
    blur1=cv2.GaussianBlur(mask1,(15,15),0)
    contours1,_=cv2.findContours(blur1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    c_blue=0 #reset the values for count of blue object
    
    for contour1 in contours1:
        area1=cv2.contourArea(contour1)
        
        if area1>7000:
            approx = cv2.approxPolyDP(contour1, 0.009 * cv2.arcLength(contour1, True), True) 
            n=approx.ravel()
            x=n[0]
            y=n[1]
            c_blue+=1
            cv2.drawContours(frame,[approx],0,(255,0,0),3)
            cv2.putText(frame,str(c_blue),(x,y), font, 2,(255,0,0),2,cv2.LINE_AA)
    print("total blue objects=",c_blue)
    
    #cv2.imshow("frame",frame)

#    if cv2.waitKey(1)==27:#press esc to exit
 #       break;

cap.release()
cv2.destroyAllWindows()
