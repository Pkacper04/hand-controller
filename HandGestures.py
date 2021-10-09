import HandDetector
from pyautogui import size
from threading import Thread
from SecondModeController import Second_Mode
from FirstModeController import First_Mode
from ThirdModeController import Third_Mode
from MathematicalFunctions import wait,readCameraDystans,dys





class HandGesture:
    def __init__(self):
        self.fMode = First_Mode()
        self.sMode = Second_Mode()
        self.tMode = Third_Mode()

    def Control(self):
        number = 0

        self.fingers = HandDetector.main([0,4, 8, 12, 16, 20])

        width, height = size()

        p1 = Thread(target=wait,args=(2,))
        p1.start()

        while (self.fingers):
            Hand = self.fingers.__next__()
            Thumb = self.fingers.__next__()
            FirstFinger = self.fingers.__next__()
            SecondFinger = self.fingers.__next__()
            ThirdFinger = self.fingers.__next__()
            Pinky = self.fingers.__next__()


            cameraDys = readCameraDystans(Thumb, Pinky)


            if dys(Thumb,Pinky) < 40 and p1.is_alive() == False:
                p1 = Thread(target=wait,args=(2,))
                p1.start()
                number += 1
                if number >= 4:
                    number = 0

            if number == 1:
                self.fMode.mouse_movement(FirstFinger, width, height)
                self.fMode.left_mouse_click(Hand,FirstFinger, SecondFinger)
                self.fMode.right_mouse_click(Hand,SecondFinger, ThirdFinger)
                self.fMode.ScrollDown(Hand, FirstFinger, cameraDys)
                self.fMode.ScrollUp(FirstFinger,SecondFinger, cameraDys)
            elif number == 2:
                self.sMode.Control_functions(Hand,Thumb,FirstFinger,SecondFinger,cameraDys)
            elif number == 3:
                self.tMode.Stop_Video(Thumb,Pinky)
                self.tMode.Go_Further(Hand)








f = HandGesture()
f.Control()


























