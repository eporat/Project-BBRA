import numpy as np
import cv2
from threading import Thread
import time
from collections import deque
import sys
import threading
import colorsys
from vector2d import Vector2D

class Camera:
    def __init__(self, *, settings):
        self.previous_mask = None
        self.current_mask = None
        self.cap = cv2.VideoCapture(0)
        self.width = int(self.cap.get(3))
        self.height = int(self.cap.get(4))
        self.frame = None
        self.dtime = 0
        self.start = 0
        self.kernel_size = 4
        self.kernel = np.ones((self.kernel_size, self.kernel_size))
        self.puck = {'pos': Vector2D(1, 1)}
        self.striker = {'pos': Vector2D(1, 1)}
        self.table = {'min_x': 0, 'min_y': 0, 'max_x': 0, 'max_y': 0}
        self.is_on = True

        for setting in settings:
            self.cap.set(setting, settings.setting)

        self.thread = threading.Thread(target=self.run_camera, args=[])
        self.thread.start()

    def read_from_cam(self):
        while self.is_on:
            _, self.frame = self.cap.read()
        return

    def run_camera(self):
        cv2.namedWindow('Sliders', cv2.WINDOW_AUTOSIZE)
        cv2.createTrackbar('Hue Puck', 'Sliders', 140, 180, nothing)
        cv2.createTrackbar('Sensitivity Puck', 'Sliders', 2, 10, nothing)
        cv2.createTrackbar('Hue Striker', 'Sliders', 140, 180, nothing)
        cv2.createTrackbar('Sensitivity Striker', 'Sliders', 2, 10, nothing)
        cv2.createTrackbar('Hue Table', 'Sliders', 140, 180, nothing)
        cv2.createTrackbar('Sensitivity Table', 'Sliders', 2, 10, nothing)

        t = Thread(target=self.read_from_cam, args=[])
        t.start()

        while True:
            if self.frame is not None:
                self.canvas = self.frame.copy()
                # canvas = cv2.blur(canvas, (10,10))
                hsv = cv2.cvtColor(self.canvas, cv2.COLOR_BGR2HSV)

                table_hue = cv2.getTrackbarPos('Hue Table', 'Sliders')
                table_sensitivity = cv2.getTrackbarPos('Sensitivity Table', 'Sliders')
                #puck_center = self.detect_circle(hsv, puck_hue, 50, 255, 50, 255, puck_sensitivity)
                striker_hue = cv2.getTrackbarPos('Hue Striker', 'Sliders')
                striker_sensitivity = cv2.getTrackbarPos('Sensitivity Striker', 'Sliders')
                striker_center = self.detect_circle(hsv, striker_hue, 50, 255, 50, 255, striker_sensitivity, 'striker mask')

                puck_hue = cv2.getTrackbarPos('Hue Puck', 'Sliders')
                puck_sensitivity = cv2.getTrackbarPos('Sensitivity Puck', 'Sliders')
                puck_center = self.detect_circle(hsv, puck_hue, 50, 255, 50, 255, puck_sensitivity, 'puck mask')

                if puck_center is not None:
                    self.puck['pos'] = Vector2D(puck_center[0], puck_center[1])
                    s = Vector2D(0,0)


                if striker_center is not None:
                    self.striker['pos'] = Vector2D(striker_center[0], striker_center[1])
                    s = Vector2D(0,0)

                self.detect_table(hsv, table_hue, 50, 255, 50, 255, table_sensitivity)

                puck_r, puck_g, puck_b = colorsys.hsv_to_rgb(puck_hue / 180.0, 1.0, 1.0)
                striker_r, striker_g, striker_b = colorsys.hsv_to_rgb(striker_hue / 180.0, 1.0, 1.0)

                cv2.circle(self.canvas, puck_center, 20, (puck_b * 256, puck_g * 256, puck_r * 256))
                cv2.circle(self.canvas, striker_center, 20, (striker_b * 256, striker_g * 256, striker_r * 256))

                cv2.imshow('canvas', self.canvas)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        self.is_on = False
        return


    def detect_circle(self, hsv, hue, sLow, sHigh, vLow, vHigh, sensitivity, name):
        mask = self.calculate_mask(hsv, hue, sLow, sHigh, vLow, vHigh, sensitivity)
        cv2.imshow(name, mask)
        return detect_circle_center(mask)

    def detect_table(self, hsv, hue, sLow, sHigh, vLow, vHigh, sensitivity):
        mask = self.calculate_mask(hsv, hue, sLow, sHigh, vLow, vHigh, sensitivity)
        cv2.imshow('table mask', mask)
        _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if not contours:
            return

        contour = max(contours, key=lambda el: cv2.contourArea(el))
        if contour is not None:
            x,y,w,h = cv2.boundingRect(contour)
            self.table['min_x'] = x
            self.table['min_y'] = y
            self.table['max_x'] = x + w
            self.table['max_y'] = y + h
            cv2.rectangle(self.canvas, (x, y), (x+w, y+h), (0,255,0))
        #
        # for cnt in contours:
        #     if 3 <= len(cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)) <= 10:
        cv2.drawContours(self.canvas, [contour], 0, 255, -1)

    def calculate_mask(self, hsv, hue, sLow, sHigh, vLow, vHigh, sensitivity):
        mask1 = cv2.inRange(hsv, np.array([hue - sensitivity, sLow, vLow]), \
            np.array([hue + sensitivity, sHigh, vHigh]))
        mask2 = cv2.inRange(hsv, np.array([179 - hue - sensitivity, sLow, vLow]), \
            np.array([179 - hue + sensitivity, sHigh, vHigh]))

        mask = cv2.bitwise_or(mask1, mask2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, self.kernel)

        return mask

def detect_polygon_center(mask, min, max):
    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not contours:
        return

    blobs = sorted(contours, key=lambda el: cv2.contourArea(el), reverse=True)

    for blob in blobs:
        if min <= len(cv2.approxPolyDP(blob, 0.01 * cv2.arcLength(blob, True), True)) <= max:
            M = cv2.moments(blob)
            if M["m00"] == 0:
                return
            center = int(M["m10"] / M["m00"]) , int(M["m01"]/M["m00"])
            return center

def detect_circle_center(mask):
    return detect_polygon_center(mask, 1, float("inf"))



def nothing(x):
    pass
