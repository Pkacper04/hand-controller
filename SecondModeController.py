import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from threading import Thread
from MathematicalFunctions import wait,Degree,dys


class SecondControl:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))


    def setMasterVolume(self,var):
        self.volume.SetMasterVolumeLevelScalar((var/100), None)


    def setScreenBrightness(self,var):
        sbc.set_brightness(var)

class Second_Mode:
    def __init__(self):
        self.functions = SecondControl()
        self.Volumecon = Thread(target=wait, args=(4,))
        self.Brightnesscon = Thread(target=wait, args=(4,))
        self.start_point = 0
        self.number = 0
        self.wait = Thread(target=wait, args=(2,))
        self.wait.start()

    def Control_functions(self,Hand,point,vpoint,bpoint,cameraDys):
        change_pos = Degree(vpoint,bpoint,Hand)

        if change_pos < 6 and self.Volumecon.is_alive() == False and self.Brightnesscon.is_alive() == False:
            self.number += 1
            if self.number > 3:
                self.number = 0

        print(self.number)

        if self.number==1 or self.Volumecon.is_alive():
            if self.start_point == 0:
                self.Volumecon = Thread(target=wait, args=(4,))
                self.Volumecon.start()
            self.Volume_Change(dys(point,vpoint),cameraDys)
            self.number = 2

        elif self.number==3 or self.Brightnesscon.is_alive():
            if self.start_point == 0:
                self.Brightnesscon = Thread(target=wait, args=(4,))
                self.Brightnesscon.start()
            self.Brightenss_Change(dys(point,bpoint),cameraDys)
            self.number = 0

        else:
            self.start_point = 0


    def Volume_Change(self,position,cameraDys):
        if position <= 120 and position >= 20 and round(position)%5 == 0:
            self.functions.setMasterVolume(round(position)-20)
        if abs(self.start_point - position) > 8 :
            self.start_point = position
            self.Volumecon = Thread(target=wait, args=(4,))
            self.Volumecon.start()



    def Brightenss_Change(self,position,cameraDys):
        print("dziala")
        if position <= 120 and position >= 20 and round(position)%5 == 0:
            self.functions.setScreenBrightness(round(position)-20)
        if abs(self.start_point - position) > 8:
            self.start_point = position
            self.Brightnesscon = Thread(target=wait, args=(4,))
            self.Brightnesscon.start()




