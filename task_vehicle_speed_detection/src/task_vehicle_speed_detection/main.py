import numpy as np
import cv2 as cv

class SpeedLine:
    def __init__(self, x1, x2, y):
        self._x1 = x1
        self._x2 = x2
        self._y = y

    def is_crossed(self, cx, prev_y, cur_y):
        if (prev_y < self._y) != (cur_y < self._y):
            return True
        return False

class Vehicle:
    pass
        

class SpeedDetector:
    pass
        