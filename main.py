from camera import Camera
import cv2
from arduino import ArduinoInterface
import time
from collections import deque
import numpy as np
import time
import keyboard
from simulation import Simulation
from time import sleep

def main():
    camera = Camera(settings=dict())
    # arduino = ArduinoInterface()
    sim = Simulation(camera.width, camera.height, camera=camera, draw=True)

    while camera.is_on:
        striker_vel = sim.run()
        print('Striker vel: ',striker_vel)

        #arduino.write('{} {}'.format(striker_vel.x, striker_vel.y))
        #arduino.read()
        sleep(0.01)
    #arduino.close()

if __name__ == "__main__":
    print("Starting camera...")
    main()
