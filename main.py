from camera import Camera
import cv2
from ai import AI
from arduino import ArduinoInterface
import time
from collections import deque
import numpy as np
import time
import keyboard

def main():
    camera = Camera(settings=dict())
    arduino = ArduinoInterface()
    # ai = AI(camera)

    while camera.is_on:
        print(camera.puck.vel)
        if camera.puck.vel[0] > 3:
            arduino.write(1)

        elif camera.puck.vel[0] < -3:
            arduino.write(0)
        arduino.read()
    arduino.close()

if __name__ == "__main__":
    print("Starting camera...")
    main()
