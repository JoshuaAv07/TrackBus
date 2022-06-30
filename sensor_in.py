import serial
import time

ser = serial.Serial('...', 9600, timeout=1)

while True:
    raw_data = ser.readline()
    data = float(raw_data[0])
    print(data)
    time.sleep() 

ser.close()