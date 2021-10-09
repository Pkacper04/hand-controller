from math import sqrt, pow
from threading import Thread
from MathematicalFunctions import wait
from pyautogui import press

class Third_Mode:
    def __init__(self):
        self.p2 = Thread(target=wait, args=(2,))
        self.p2.start()

    def Stop_Video(self, Thumb, Pinky):
        dys = sqrt(pow(abs(Thumb[1] - Pinky[1]), 2) + pow(abs(Thumb[2] - Pinky[2]), 2))
        print(dys)
        if dys > 270 and self.p2.is_alive() == False:
            press("space")

            self.p2 = Thread(target=wait, args=(2,))
            self.p2.start()

    def Go_Further(self, Hand):
        dys1 = Hand[1]
        p2 = Thread(target=wait, args=(2,))
        p2.start()