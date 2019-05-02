from camera import Camera
import cv2
from ai import AI
from arduino import ArduinoInterface
import time
from collections import deque
import numpy as np
import time

def main():
    camera = Camera(settings=dict())
    arduino = ArduinoInterface()
    ai = AI(camera)

    while camera.is_on:
        move = ai.get_move()
        arduino.write(str(move[0]) + " " + str(move[1]))
    arduino.close()

if __name__ == "__main__":
    print("Starting camera...")
    main()
