from http import client
import json
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
    if raw_data:
    
        sen=str(raw_data).split("'")
        sen = sen[1].split('\\')
        s = sen[0]
        data = {
            'stop_id': 1,
            'bus_name': 'Dale Up',
            'bus_id': s
        }
        
        json_data = json.dumps(str(data))

        _conn.request('POST', '/devices', json_data, headers=h)
        _conn.close() 
    
        value = data['bus_id']
        print("Tarjeta: ", value)