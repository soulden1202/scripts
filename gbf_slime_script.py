import cv2
import pyautogui
from time import sleep
import pyscreeze
import keyboard
import random



def main():
    pyautogui.PAUSE = 0 


    ok_template = cv2.imread("imgs/ok_test.png", cv2.IMREAD_UNCHANGED)
    ok_template_gray = cv2.cvtColor(ok_template, cv2.COLOR_RGB2GRAY)
    arrow_template = cv2.imread("imgs/arrow.png", cv2.IMREAD_UNCHANGED)
    pa_template = cv2.imread("imgs/play_again.png", cv2.IMREAD_UNCHANGED)
    pa_template_gray = cv2.cvtColor(pa_template, cv2.COLOR_RGB2GRAY)
    fa_template = cv2.imread("imgs/fa.png", cv2.IMREAD_UNCHANGED)
    fa_template_gray = cv2.cvtColor(fa_template, cv2.COLOR_RGB2GRAY)
    kagu_template = cv2.imread("imgs/kagu.png", cv2.IMREAD_UNCHANGED)
    kagu_template_gray = cv2.cvtColor(kagu_template, cv2.COLOR_RGB2GRAY)

    x,y,w,h = 1439,91,481,882 
    start = True
    
    # pyautogui.screenshot("rawimgs/img.png",(x,y,w,h))
    # raw_2 = cv2.imread("rawimgs/img.png")
    # raw_2_gray = cv2.cvtColor(raw_2 , cv2.COLOR_RGB2GRAY)
    # ok= cv2.matchTemplate(raw_2_gray,ok_template_gray, cv2.TM_CCOEFF_NORMED)
    
    # ok_res = cv2.minMaxLoc(ok)
    # print(ok_res)
    
    # cv2.imshow("ok",ok)
    # cv2.waitKey()
    picked_sum = False

    while start:
        isFa = isKagu=  isOk = isArrow= isPa = False
        pyautogui.screenshot("rawimgs/img.png",(x,y,w,h))
        raw_2 = cv2.imread("rawimgs/img.png")
        raw_2_gray = cv2.cvtColor(raw_2 , cv2.COLOR_RGB2GRAY)
        fa =  cv2.matchTemplate(raw_2_gray, fa_template_gray, cv2.TM_CCOEFF_NORMED) 
        pa =  cv2.matchTemplate(raw_2_gray, pa_template_gray, cv2.TM_CCOEFF_NORMED)
        ka = cv2.matchTemplate(raw_2_gray, kagu_template_gray, cv2.TM_CCOEFF_NORMED)
        ok= cv2.matchTemplate(raw_2_gray,ok_template_gray, cv2.TM_CCOEFF_NORMED)
        
        fa_res =cv2.minMaxLoc(fa)
        pa_res = cv2.minMaxLoc(pa)
        ka_res = cv2.minMaxLoc(ka)
        ok_res = cv2.minMaxLoc(ok)
        
        
        temp_array = [pa_res[1], fa_res[1], ka_res[1], ok_res[1]]
        

        print(temp_array)
        
        
        min_val, max_val , min_loc, max_loc = 0,0,0,0
        
        if max(temp_array) == fa_res[1]:
            isFa= True 
            min_val, max_val , min_loc, max_loc = fa_res
            
        elif max(temp_array) == pa_res[1]:
            isPa =True
            min_val, max_val , min_loc, max_loc = pa_res
        elif max(temp_array) == ka_res[1]:
            if picked_sum:
                isOk = True
                min_val, max_val , min_loc, max_loc = ok_res
                picked_sum= False
                
            else:
                isKagu =True
                min_val, max_val , min_loc, max_loc = ka_res
        elif max(temp_array) == ok_res[1]:
            isOk =True
            min_val, max_val , min_loc, max_loc = ok_res        
        if isFa and max_val >= 0.56:
            print("is Fa")
            pyautogui.click(max_loc[0]+x + random.random() + random.randint(1,2), max_loc[1]+y+ random.random() + random.randint(1,2))
            sleep(random.randint(30,35) + random.random())
            print("resume")
        elif isPa and max_val >= 0.9:
            print("is PA")
            pyautogui.click(max_loc[0]+x+20 + random.random() + random.randint(1,2), max_loc[1]+y+20+ random.random() + random.randint(1,2))
            sleep(random.randint(1,5) + random.random())
            print(max_val)
            print("resume")
        elif isKagu and max_val >= 0.9:
            print("is Kagu")
            pyautogui.click(max_loc[0]+x + random.random() + random.randint(1,2), max_loc[1]+y+ random.random() + random.randint(1,2))
            sleep(random.randint(1,5) + random.random())
            picked_sum =True
            
            print(max_val)
            print("resume")  
        elif isOk and max_val >= 0.5:
            print("is ok")
            pyautogui.click(max_loc[0]+x+ random.random() + random.randint(1,2), max_loc[1]+y+ random.random() + random.randint(1,2))
            sleep(random.randint(1,5) + random.random())
            print(max_val)
            print("resume")          
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
        


if __name__ == "__main__":     
        main()  # Already an admin here.