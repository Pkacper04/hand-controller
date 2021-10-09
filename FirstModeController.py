from threading import Thread
from MathematicalFunctions import wait,Degree,dys
from autopy import mouse
from pyautogui import press,click

class First_Mode:
    def __init__(self):
        self.controlFunction = Thread(target=wait, args=(0.1,))
        self.controlFunction.start()

    def mouse_movement(self, position, width, height):
        x = int(abs(float(position[1]) - 580) * (width / 580))
        y = int(float(position[2]) * (height / 420))
        try:
            mouse.move(x, y)
        except:
            pass

    def left_mouse_click(self, Hand, FirstFinger, SecondFinger):
        degree = Degree(FirstFinger, SecondFinger, Hand)

        if degree <= 6 and self.controlFunction.is_alive() == False:
            self.controlFunction = Thread(target=wait, args=(0.5,))
            self.controlFunction.start()
            mouse.click()

    def right_mouse_click(self, Hand, SecondFinger, ThirdFinger):
        degree = Degree(SecondFinger, ThirdFinger, Hand)

        if degree < 6 and self.controlFunction.is_alive() == False:
            self.controlFunction = Thread(target=wait, args=(0.5,))
            self.controlFunction.start()
            click(button="RIGHT")

    def ScrollDown(self, Hand, FirstFinger, cameraDys):
        position = dys(Hand, FirstFinger)
        position = position + ((cameraDys - 470) / 6)

        if position < 90 and self.controlFunction.is_alive() == False:
            self.controlFunction = Thread(target=wait, args=(0.8,))
            self.controlFunction.start()
            press("pgdn")

    def ScrollUp(self, FirstFinger, SecondFinger, cameraDys):
        position = dys(FirstFinger, SecondFinger)
        position = position + ((cameraDys - 470) / 1.14)

        if position > 170 and self.controlFunction.is_alive() == False:
            self.controlFunction = Thread(target=wait, args=(0.8,))
            self.controlFunction.start()
            press("pgup")