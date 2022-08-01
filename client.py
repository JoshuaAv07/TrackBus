import serial
import requests
import time

ser = serial.Serial('COM4', 9600, timeout=1)
get = requests.get("https://track-bus-nevsoft.herokuapp.com/routes", headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
})

routes = get.json()
#print(route)
#print(routes[0])
while True:    

    raw_data = ser.readline()
    if raw_data:
        try:
            sen=str(raw_data).split("'")
            sen = sen[1].split('\\')
            s = sen[0]
            for i in routes:
                if i['bus_id'] == s:
                    data = {
                        'stop_id': 1,
                        'bus_name': i['bus_name'],
                        'bus_id': s
                    }
            req = requests.post("https://track-bus-nevsoft.herokuapp.com/signals", json=data)
            
            value = data['bus_id']
            print(f"{req.text} tarjeta: {value}") 
        except Exception as e:
            print(e)

    time.sleep(1)