import Final_pi
import cv2

def detect_colour(form_func, countvar):
    ls={'blue': 0, 'red': 0,'green': 0, 'orange': 0,'yellow': 0}
    ls_prev= {'blue': 0, 'red': 0,'green': 0, 'orange': 0,'yellow': 0}
    val=0
    i = 0
    while 1:
        print(i)
        print("prev : ", ls_prev)
        val,ls=Final_pi.GetValues()
        print("ls : ",ls)
        if ls == ls_prev or i==0:
            print("no change")
            if val==27:
                break;
            if i == 1:
                ls_prev = ls
        elif ls!= ls_prev:
            print("change")
            ls_prev = ls
            countvar.update(ls)
            form_func()
        ls_prev = ls
        i+=1

    cv2.destroyAllWindows()
