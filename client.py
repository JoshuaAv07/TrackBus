from http import client
from iiot_device import Sensor
import json
import time


# Creación de un objeto de la clase HTTPConnection
_conn = client.HTTPConnection(host='localhost', port=5000)

# Creación de un objeto de la clase Sensor
s = Sensor()

# Pa'a formar el JSON que se va al servidor
h = {'Content-type': 'application/json'}

while True:

    data = {
        'id' : 1,
        'name' : 'Temp_Sensor',
        'value' : s.get_random_number()
    }

    json_data = json.dumps(data)

    # Enviar los datos al servidor
    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close()

    
    val = data['value']

    if type(val) == int:
        print(f"It is a number {val}" )
        if val < 15:
            print(val, "es menor a 15")
        else: 
            print(val, "es igual o mayor a 15") 

    elif type(val) == float:
        print(f"It is not an int {val}" )
        val = int(val)
        print(f"Now it is {val}" )
    else:
        print(f"It is not a number {val}")
        if (val == True):
            val = 1
            print(f"Now it is {val}")
        
        elif (val == False):
            val = 0
            print(f"Now it is {val}")

        else:
            pass

    time.sleep(.5)