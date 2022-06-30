from flask import Flask, request

app = Flask('__main__')

device = {
    "code": "12312414",
    "descrip": "Temp, sensor",
    "value": 67
}

#Save an user
@app.route('/users', methods=['POST'])
def save_users():
    user = request.json
    print(user)
    return user

#Get devices
@app.route('/devices', methods=['GET'])
def go_home():
    print(device)
    return device

# Save a device
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device, 201

@app.route('/sensor', methods=['POST'])
def save_sensor():
    device = request.json
    print(device)
    ''' Pythonic form '''
    with open('devices.dat', 'a') as f:
        f.write(str(device +'\n'))
        ''' For normal languages
        f = open('devices.dat', 'a')
        f.write(str(device))
        f.close()
        '''

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')