import keyboard
import time
from directKeys import PressKey, ReleaseKey, W, A, S, D, SPACE

def main():
    stop = True
    while True:
        while (stop):
            if keyboard.is_pressed("q"):
                 print("exit")
                 return
            if keyboard.is_pressed("p"):
                 print("You Started")
                 stop = False

        PressKey(W)
        time.sleep(0.1)
        ReleaseKey(W)
        
        PressKey(D)
        time.sleep(0.1)
        ReleaseKey(D)

        if keyboard.is_pressed("p"):
                 print("You Stoped")
                 time.sleep(1)
                 if keyboard.is_pressed("q"):
                    print("exit")
                    return
                 stop = True

main()