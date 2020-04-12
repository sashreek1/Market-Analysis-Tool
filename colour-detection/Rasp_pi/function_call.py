import Final_pi
import cv2

ls={}
val=0
while 1:
    val=Final_pi.GetValues(ls)
    print(ls)
    if val==27:
        break;
cv2.destroyAllWindows()
