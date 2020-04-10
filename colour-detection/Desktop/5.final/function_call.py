import Final
import cv2

ls={} # required dictionary 
while(1) :        
    val=Final.GetValues(ls)
    print (ls)
    if val==27: #press esc to break the loop
        break

cv2.destroyAllWindows()
