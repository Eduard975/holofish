import keyboard
import time
from PIL import ImageGrab 
from directKeys import PressKey, ReleaseKey, W, A, S, D, SPACE
#pyautogui.press('Any key combination')

blue   = (52,144,246)
l_blue  = (75,187,247)
yellow = (245,197,67)
red    = (225,50,50)
green  = (45,235,43)
purple = (174,49,208)

def main():
    has_pressed = False
    do_save = False
    i = 0
    stop = True

    while True:
        #time.sleep(0.1)
        px = ImageGrab.grab(bbox=(1100, 700, 1200, 800))
        # you might need to edit this manually
        #px.save('m.png')

        while (stop):
            if keyboard.is_pressed("q"):
                 print("exit")
                 return(0)
            if keyboard.is_pressed("p"):
                 print("You Started")
                 time.sleep(0.1)
                 stop = False

        for y in range(0, 100, 1):
            for x in range(0, 100, 1):
                color = px.getpixel(xy=[x, y])
                #print(color)
                if color == blue:
                    PressKey(S)
                    time.sleep(0.1)
                    ReleaseKey(S)
                    has_pressed = True

                    if(do_save):
                        px.save('a' + str(i) +'.png')
                        i+=1
                        print("You pressed s"+ str(i))
                    break
                if color == yellow:
                    PressKey(A)
                    time.sleep(0.1)
                    ReleaseKey(A)
                    has_pressed = True

                    if(do_save):
                        px.save('a' + str(i) +'.png')
                        i+=1
                        print("You pressed a"+ str(i))
                    break
                if color == red:
                    PressKey(W)
                    time.sleep(0.1)
                    ReleaseKey(W)
                    has_pressed = True

                    if(do_save):
                        px.save('a' + str(i) +'.png')
                        i+=1
                        print("You pressed w"+ str(i))
                    break
                if color == green:
                    PressKey(D)
                    time.sleep(0.1)
                    ReleaseKey(D)
                    has_pressed = True

                    if(do_save):
                        px.save('a' + str(i) +'.png')
                        i+=1
                        print("You pressed d"+ str(i))
                    break
                if color == purple:
                    PressKey(SPACE)
                    time.sleep(0.1)
                    ReleaseKey(SPACE)
                    has_pressed = True
                    if(do_save):
                        px.save('a' + str(i) +'.png')
                        i+=1
                        print("You pressed space" + str(i))
                    break
                if color == l_blue:
                    PressKey(SPACE)
                    time.sleep(0.5)
                    ReleaseKey(SPACE)

                    time.sleep(1)

                    PressKey(SPACE)
                    time.sleep(0.5)
                    ReleaseKey(SPACE)
                    has_pressed = True

                    if(do_save):
                        px.save('a' + str(i) +'.png')
                        i+=1
                        print("You pressed space" + str(i))

                    break
            if(has_pressed):
                has_pressed = False
                break

        if keyboard.is_pressed("p"):
             print("You Stoped")
             time.sleep(1)
             stop = True
        if keyboard.is_pressed("q"):
            print("exit")
            return(0)

main()