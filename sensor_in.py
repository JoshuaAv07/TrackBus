import serial
import time

ser = serial.Serial('COM4', 9600, timeout=1)

class Sensor:
    def sensor_sign():
        while True:
            
            raw_data = ser.readline()
            sen=str(raw_data).split("'")
            sen = sen[1].split('\\')
            s = sen[0]
            #time.sleep() 

ser.close()