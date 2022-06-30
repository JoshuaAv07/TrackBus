from random import randint

#Definición de la clase
class Sensor:

    #Constructor de la clase
    def __init__(self):
        pass

    def get_temp(self):
        return self._sensor['coretemp']

    #Simular la toma de algún valor de otro sensor
    def get_random_number(self):
        return randint(0, 50)