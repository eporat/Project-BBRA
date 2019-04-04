import threading
import camera
import cv2
from ai import AI
from arduino import ArduinoInterface
import time

camera_dict = dict()

def main():
    camera_thread = threading.Thread(target=camera.main, args=[])
    camera_thread.start()
    #arduino = ArduinoInterface()
    ai = AI()

    try:
        while True:
            move = ai.get_move()
            #arduino.write(move)
    except KeyboardInterrupt:
        print("Program done!")

    #arduino.close()

if __name__ == "__main__":
    main()
