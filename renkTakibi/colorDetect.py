import cv2
import numpy as np


class GreenDetector:
    def __init__(self):
        # Create mask for orange color
        self.lowGreen = np.array([45, 100, 50])
        self.highGreen = np.array([75, 255, 255])

    def detect(self, frame):
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks with color ranges
        mask = cv2.inRange(hsv_img, self.lowGreen, self.highGreen)

        # Find Contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        box = (0, 0, 0, 0)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            box = (x, y, x + w, y + h)
            break
        x, y, x2, y2 = box
        cx = int((x + x2) / 2)
        cy = int((y + y2) / 2)    
        return cx,cy

class BlueDetector:
    def __init__(self):
        # Create mask for blue color
        self.lowBlue = np.array([100, 150, 0])
        self.highBlue = np.array([140, 255, 255])

    def detect(self, frame):
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks with color ranges
        mask = cv2.inRange(hsv_img, self.lowBlue, self.highBlue)

        # Find Contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        box = (0, 0, 0, 0)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            box = (x, y, x + w, y + h)
            break
        x, y, x2, y2 = box
        cx = int((x + x2) / 2)
        cy = int((y + y2) / 2) 

        return cx,cy