from http import client
from socket import timeout
import json
import time
import serial

#Creacion de un objeto de la clase HHTPConnetion
_conn = client.HTTPConnection('localhost', port=5000)

#Creacion de un objeto de la clase Sensor

ser = serial.Serial('COM4', 9600, timeout=1)
  
h = {'Content-type': 'application/json'}  

while True:
    count = 0
    count += 1
    raw_data = ser.readline()
    sen=str(raw_data).split("'")
    #sen = (data[1])[28:32:1].split(".")
    sen = sen[1].split('\\')
    s = sen[0]
    data = {
        'id': count,
        'name': 'Dale Up',
        'value': s
    }
    json_data = json.dumps(str(data))

    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close()


    value = data['value']
    print("Tarjeta: ", value)
        
    #time.sleep(.5)