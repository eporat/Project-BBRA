import numpy as np
import cv2
from threading import Thread
import time
from main import camera_dict

frame = None
cap = None
start = 0

def read_from_cam():
    global frame, start
    while True:
        _, frame = cap.read()

def main():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 120)
    cap.set(3, 320)
    cap.set(4, 240)
    t = Thread(target=read_from_cam, args=[])
    t.start()

    while True:
        if frame is not None:
            canvas = frame.copy()
            canvas = cv2.blur(canvas, (5,5))
            hsv = cv2.cvtColor(canvas, cv2.COLOR_BGR2HSV)
            center = detect_circles(hsv, 0, 100, 255, 100, 255, 5)
            camera_dict.center = center

    cv2.destroyAllWindows()

def detect_circles(hsv, hue, sLow, sHigh, vLow, vHigh, sensitivity):
    mask1 = cv2.inRange(hsv, np.array([hue - sensitivity, sLow, vLow]), \
        np.array([hue + sensitivity, sHigh, vHigh]))
    mask2 = cv2.inRange(hsv, np.array([179 - hue - sensitivity, sLow, vLow]), \
        np.array([179 - hue + sensitivity, sHigh, vHigh]))

    mask = cv2.bitwise_or(mask1, mask2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not contours:
        return

    blob = max(contours, key=lambda el: cv2.contourArea(el))

    M = cv2.moments(blob)
    if M["m00"] == 0:
        return
    center = int(M["m10"] / M["m00"]) , int(M["m01"]/M["m00"])

    return center
