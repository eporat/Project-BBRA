import numpy as np
import cv2
from threading import Thread
import time
from collections import deque
import sys
import threading
import colorsys

class Circle:
    def __init__(self, x, y):
        self.pos = np.array([x,y])
        self.vel = np.array([0,0])

    def set_vel(self, vel):
        self.vel = vel

    def set_pos(self, pos):
        self.pos = pos

class Camera:
    def __init__(self, *, settings):
        self.cap = cv2.VideoCapture(0)
        self.frame = None
        self.dtime = 0
        self.start = 0

        self.dpos = deque(maxlen=6)
        self.dtimes = deque(maxlen=6)

        self.puck = Circle(0, 0)
        self.player = Circle(0, 0)

        self.is_on = True

        for setting in settings:
            self.cap.set(setting, settings.setting)

        self.thread = threading.Thread(target=self.run_camera, args=[])
        self.thread.start()

    def read_from_cam(self):
        while self.is_on:
            _, self.frame = self.cap.read()
            self.dtime = time.time() - self.start
            self.dtimes.append(self.dtime)
            self.start = time.time()
        return

    def run_camera(self):
        cv2.namedWindow('Sliders', cv2.WINDOW_AUTOSIZE)
        cv2.createTrackbar('Hue Puck', 'Sliders', 140, 180, nothing)
        cv2.createTrackbar('Sensitivity Puck', 'Sliders', 2, 10, nothing)
        cv2.createTrackbar('Hue Player', 'Sliders', 140, 180, nothing)
        cv2.createTrackbar('Sensitivity Player', 'Sliders', 2, 10, nothing)

        #cap.set(cv2.CAP_PROP_FPS, 120)
        #cap.set(3, 320)
        #cap.set(4, 240)
        t = Thread(target=self.read_from_cam, args=[])
        t.start()

        while True:
            if self.frame is not None:
                canvas = self.frame.copy()
                canvas = cv2.blur(canvas, (5,5))
                hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
                puck_hue = cv2.getTrackbarPos('Hue Puck', 'Sliders')
                puck_center = detect_circles(hsv, puck_hue, 50, 255, 50, 255, cv2.getTrackbarPos('Sensitivity Puck', 'Sliders'))
                player_hue = cv2.getTrackbarPos('Hue Player', 'Sliders')
                player_center = detect_circles(hsv, player_hue, 50, 255, 50, 255, cv2.getTrackbarPos('Sensitivity Player', 'Sliders'))

                if puck_center is not None:
                    #self.dpos.append(np.array(new_center) - self.puck.pos)
                    self.puck.pos = puck_center
                if player_center is not None:
                    self.player.pos = player_center
                    #self.pos = sum(self.dpos / self.dtimes)

                puck_r, puck_g, puck_b = colorsys.hsv_to_rgb(puck_hue / 180.0, 1.0, 1.0)
                player_r, player_g, player_b = colorsys.hsv_to_rgb(player_hue / 180.0, 1.0, 1.0)
                print(puck_r, puck_g, puck_b)

                cv2.circle(self.frame, puck_center, 20, (puck_b * 256, puck_g * 256, puck_r * 256))
                cv2.circle(self.frame, player_center, 20, (player_b * 256, player_g * 256, player_r * 256))

                cv2.imshow('frame', self.frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        self.is_on = False
        return


def detect_circles(hsv, hue, sLow, sHigh, vLow, vHigh, sensitivity):
    mask1 = cv2.inRange(hsv, np.array([hue - sensitivity, sLow, vLow]), \
        np.array([hue + sensitivity, sHigh, vHigh]))
    mask2 = cv2.inRange(hsv, np.array([179 - hue - sensitivity, sLow, vLow]), \
        np.array([179 - hue + sensitivity, sHigh, vHigh]))

    mask = cv2.bitwise_or(mask1, mask2)
    cv2.imshow('mask', mask)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not contours:
        return

    blob = max(contours, key=lambda el: cv2.contourArea(el))

    M = cv2.moments(blob)
    if M["m00"] == 0:
        return
    center = int(M["m10"] / M["m00"]) , int(M["m01"]/M["m00"])

    return center


def nothing(x):
    pass
