import numpy as np
import cv2 as cv
from ultralytics import YOLO

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
        self.prev_y = -1
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
        return self.DISTANCE/(self.cross_2-self.cross_1)*3.6
        
        

class SpeedDetector:
    AX1:int = 70
    AX2:int = 230
    AY:int = 90
    BX1:int = 15
    BX2:int = 225
    BY:int = 125

    def __init__(self, model_path:str, video_path:str):
        self.vid = cv.VideoCapture(video_path)
        self.model = YOLO(model_path)
        self.line_a = SpeedLine(self.AX1, self.AX2, self.AY)
        self.line_b = SpeedLine(self.BX1, self.BX2, self.BY)
        self.fps = self.vid.get(cv.CAP_PROP_FPS)
        self.width = int(self.vid.get(cv.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vid.get(cv.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv.VideoWriter("new_vid.avi", fourcc, float(self.fps), (self.width, self.height))
        self.vehicles:list[Vehicle] = []

    def run(self):
        current_time = 0.0
        while True:
            success, frame = self.vid.read()
            current_time += 1.0 / self.fps
            if success:        
                self.track_frame(frame, current_time)
            else:
                break

        self.vid.release()
        self.video_writer.release()

    def track_frame(self, frame, current_time):
        results = self.model.track(frame, persist=True, tracker='bytetrack.yaml', conf=0.4)
        boxes = results[0].boxes
        new_frame = frame.copy()
        if boxes.id is not None:
            for (x1, y1, x2, y2), track_id in zip(boxes.xyxy.int().tolist(), boxes.id.int().tolist()):
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                while track_id > len(self.vehicles):
                    self.vehicles.append(Vehicle(len(self.vehicles)))
                self.vehicles[track_id-1].update(cx, cy, current_time, self.line_a, self.line_b)

                color = (0, 255, 0)
                if self.vehicles[track_id-1].cross_2 != None:
                    color = (0, 0, 255)
                cv.rectangle(new_frame, (x1, y1), (x2, y2), color, thickness=1, lineType=cv.LINE_8)

        self.video_writer.write(new_frame)
        
        
