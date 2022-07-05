from http import client
from socket import timeout
import json
import time
import serial
#from sensor_in import Sensor

#Creacion de un objeto de la clase HHTPConnetion
_conn = client.HTTPConnection('localhost', port=5000)

#Creacion de un objeto de la clase Sensor

ser = serial.Serial('COM4', 9600, timeout=1)
  
#s = Sensor()
h = {'Content-type': 'application/json'}  

while True:
    
    raw_data = ser.readline()
    sen=str(raw_data).split("'")
    sen = sen[1].split('\\')
    s = sen[0]
    #sen = s.sensor_sign
    data = {
        'id': 1,
        'name': 'Dale Up',
        'value': s
    }
    json_data = json.dumps(str(data))

    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close()


    value = data['value']
    print("Tarjeta: ", value)
        
    #time.sleep(.5)