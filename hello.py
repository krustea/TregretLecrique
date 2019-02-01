from led import Led
from led2 import Led2
from temperature import TemperatureSensor

from flask import Flask
app = Flask(__name__)

from flask import render_template
degcel= TemperatureSensor()
led2= Led2()


@app.route('/on/')
def hello():
    return render_template('on.html')

@app.route('/led/<on_off>')
def led(on_off):
    if on_off == 'on' or on_off == 'off':
        led1.status = on_off
        led1.led_status()
    elif on_off == 'blink':
        led1.blink()
    return render_template('on.html')

@app.route('/temp/<Celsius>')
def tempC(Celsius):
    Celsius = degcel.degreeCelsius()
    led2 = led2.led2_Celsius()
    return render_template('degree.html', Celsius = Celsius)

