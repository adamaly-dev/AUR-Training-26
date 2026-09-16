import cv2 as cv
import numpy as np

class PolygonTracker:
    LOWER_BLUE = np.array([100, 50, 50])
    UPPER_BLUE = np.array([130, 255, 255])
    LOWER_RED1 = np.array([0, 50, 50])
    UPPER_RED1 = np.array([10, 255, 255])
    LOWER_RED2 = np.array([170, 50, 50])
    UPPER_RED2 = np.array([180, 255, 255])

    def __init__(self, url):
        self.vid = cv.VideoCapture(url)
        self.blue_square = 0
        self.red_circle = 0
        self.prev_frame = [0, 0]
        self.fps = self.vid.get(cv.CAP_PROP_FPS)
        self.width = int(self.vid.get(cv.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vid.get(cv.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv.VideoWriter("new_vid.avi", fourcc, float(self.fps), (self.width, self.height))

    def get_red_mask(self, frame):
        mask1 = cv.inRange(frame, self.LOWER_RED1, self.UPPER_RED1)
        mask2 = cv.inRange(frame, self.LOWER_RED2, self.UPPER_RED2)

        red_mask = cv.bitwise_or(mask1, mask2)
        return red_mask

    def get_blue_mask(self, frame):
        mask = cv.inRange(frame, self.LOWER_BLUE, self.UPPER_BLUE)
        return mask

    def control(self):
        while True:
            success, frame = self.vid.read()
            if success:
                frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                self.detect(frame)
            else:
                break

        self.vid.release()
        self.video_writer.release()

    def detect(self, frame):
        blurred = cv.medianBlur(frame, 3)
        red_mask = self.get_red_mask(blurred)
        blue_mask = self.get_blue_mask(blurred)

        current_blue_square = 0
        current_red_circle = 0

        i = 0

        for mask in [red_mask, blue_mask]:
            contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                area = cv.contourArea(contour)
                if area < 200:
                    continue

                perimeter = cv.arcLength(contour, True)
                points = cv.approxPolyDP(contour, 0.02 * perimeter, True)
                
                if (i == 0) and (len(points) > 6):
                    current_red_circle += 1
                elif (i == 1) and (len(points) == 4):
                    current_blue_square += 1
            i += 1

        if current_blue_square > self.prev_frame[0]:
            self.blue_square += current_blue_square-self.prev_frame[0]
        if current_red_circle > self.prev_frame[1]:
            self.red_circle += current_red_circle-self.prev_frame[1]

        self.prev_frame = [current_blue_square, current_red_circle]

        self.draw(frame)

    def draw(self, frame):
        new_frame = frame.copy()                

        new_frame = cv.cvtColor(new_frame, cv.COLOR_HSV2BGR)

        cv.putText(new_frame, f"Blue Squares: {self.blue_square}", (5, self.height-5), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        cv.putText(new_frame, f"Red Circles: {self.red_circle}", (5, self.height-55), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

        self.video_writer.write(new_frame)


def main():
    tracker = PolygonTracker("video.mp4")
    tracker.control()


main()


# In __init__, get video and store the video in the class as a property
#
# In control method, iterate over frames and 
# call a function to detect all polygons in the current picture
#
# In detect method, get all polygons
#
# In draw method, update counter on top left of frame
#
