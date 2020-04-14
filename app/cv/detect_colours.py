import cv.detect_colour_func as detect_colour_func
import cv2
import cv.bought as bought

def detect_colour(form_func, countvar):
    ls={'blue': 0,'green': 0, 'orange': 0,'yellow': 0}
    ls_prev= {'blue': 0,'green': 0, 'orange': 0,'yellow': 0}
    val=0
    i = 0
    bought.bought = []
    while True:

        print(i)
        print("prev : ", ls_prev)
        val,ls=detect_colour_func.GetValues()
        print("ls : ",ls)
        
        if ls == ls_prev or i==0:
            print("no change")
            if val==27:
                break;
            if i == 1:
                ls_prev = ls
                
        elif ls!= ls_prev:
            print("change")
            countvar.update(ls)
            for i in ls:
                print("checking for change in : ",i)
                print(ls[i],ls_prev[i])
                if ls[i] != ls_prev[i]:
                    num = abs(ls[i]-ls_prev[i])
                    print("difference : ", num)
                    for j in range(num):
                        print("appending to bought list", i)
                        bought.bought.append(i)
                        
            print("bought : ",bought.bought)
            

            ls_prev = ls
            form_func()

        ls_prev = ls
        i+=1
    
    cv2.destroyAllWindows()
