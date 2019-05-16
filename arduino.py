import serial

class ArduinoInterface:
    def __init__(self):
        self.arduino = serial.Serial('COM4', 115200, timeout=0.1)

    def write(self, msg):
        self.arduino.write((str(msg)).encode())

    def read(self):
        try:
            data = self.arduino.readline().decode("utf-8")
            print(data)
        except:
            print("Something went wrong")

    def close(self):
        self.arduino.close()
