from numpy import degrees,arccos
from math import sqrt, pow
import time

def Degree(Point1, Point2, Point3):
    dys = sqrt(pow(abs(Point1[1] - Point2[1]), 2) + pow(abs(Point1[2] - Point2[2]), 2))
    dys1 = sqrt(pow(abs(Point1[1] - Point3[1]), 2) + pow(abs(Point1[2] - Point3[2]), 2))
    dys2 = sqrt(pow(abs(Point2[1] - Point3[1]), 2) + pow(abs(Point2[2] - Point3[2]), 2))
    cos = (pow(dys1, 2) + pow(dys2, 2) - pow(dys, 2)) / (2 * dys2 * dys1)
    return degrees(arccos(cos))


def wait(waitTime):
    time.sleep(waitTime)

def dys(Point1,Point2):
    return sqrt(pow((Point1[1] - Point2[1]), 2) + pow(Point1[2] - Point2[2], 2))


def readCameraDystans(Point1, Point2):
    cameraDys = (640 - (max(Point1[1], Point2[1]) - min(Point1[1], Point2[1])))
    return cameraDys
