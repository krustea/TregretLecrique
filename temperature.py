# Imports
import os
import glob
import time



class TemperatureSensor:
    def __init__(self):
        os.system('modprobe w1-gpio')  # Allume le module 1wire
        os.system('modprobe w1-therm')  # Allume le module Temperature
        self.device_file = '/sys/bus/w1/devices/28-01131a4f0da1/w1_slave'

    def read_temp_raw(self):
        f = open(self.device_file, 'r')  # Ouvre le dichier
        lines = f.readlines()  # Returns the text
        f.close()
        return lines

    def degreeCelsius(self):
        lines = self.read_temp_raw()  # Lit le fichier de température
        # Tant que la première ligne ne vaut pas 'YES', on attend 0,2s
        # On relis ensuite le fichier
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        # On cherche le '=' dans la seconde ligne du fichier
        equals_pos = lines[1].find('t=')
        # Si le '=' est trouvé, on converti ce qu'il y a après le '=' en degrées celcius
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    def fahrenheit(self):
        temp_c = self.degreeCelsius()
        tfah = (temp_c * 1.8) +32
        return tfah

temperatureEnCelsius = TemperatureSensor()
print("La température en degrée est de ",temperatureEnCelsius.degreeCelsius())
print("La température en fahrenheit est de ",temperatureEnCelsius.fahrenheit())

