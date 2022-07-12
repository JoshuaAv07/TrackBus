import serial
import requests
import time

ser = serial.Serial('COM4', 9600, timeout=1)

while True:    

    raw_data = ser.readline()
    if raw_data:
        try:
            sen=str(raw_data).split("'")
            sen = sen[1].split('\\')
            s = sen[0]
            data = {
                'stop_id': 1,
                'bus_name': 'Dale Up',
                'bus_id': s
            }
            req = requests.post("https://track-bus-nevsoft.herokuapp.com/signals", json=data)
            
            value = data['bus_id']
            print(f"{req.text} tarjeta: {value}") 
        except Exception as e:
            print(e)

    time.sleep(1)