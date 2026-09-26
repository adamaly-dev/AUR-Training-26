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
    DISTANCE:float = 9.144
    
    def __init__(self, id):
        self.id = id
        self.prev_y = 0
        self.cross_1 = None
        self.cross_2 = None

    def update(self, cx, cy, now, line_a, line_b):
        if line_a.is_crossed(cx, self.prev_y, cy):
            self.cross_1 = now
        if line_b.is_crossed(cx, self.prev_y, cy):
            self.cross_2 = now
        self.prev_y = cy

    def get_speed(self):
        if self.cross_1 == None or self.cross_2 == None:
            return None
        return self.DISTANCE/(self.cross_2-self.cross_1)
        
        

class SpeedDetector:
    pass