import threading
import camera
import cv2
from ai import AI
from arduino import ArduinoInterface
import time

camera_dict = dict()

def main():
    #camera_thread = threading.Thread(target=camera.main, args=[])
    #camera_thread.run()
    arduino = ArduinoInterface()
    ai = AI()

    for _ in range(100):
        move = ai.get_move()
        arduino.write(move)
        time.sleep(0.1)
        arduino.read()
    
    arduino.close()

if __name__ == "__main__":
    main()
