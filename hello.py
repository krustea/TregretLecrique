from flask import Flask
app = Flask(__name__)

class Led:
    def __init__(self, numero_broche, couleur):
        self.numero_broche = numero_broche
        self.couleur = couleur

    def on(self, numero_broche):
        return GPIO.output(numero_broche, GPIO.HIGH)

    def off(self, numero_broche):
        return GPIO.output(numero_broche, GPIO.LOW)

led1= Led('14', 'rouge')
led2= Led('15', "bleu")

from flask import render_template
@app.route('/on/')
def hello():
    return render_template('on.html')

import RPi.GPIO as GPIO
import time

#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#initialisation de la broche en mode "sortie"
#⚠️ Le nombre passé en paramètre correspond au numéro de GPIO et non au numéro de la broche.
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)



@app.route('/on/')
@app.route('/on/<nbr>')
def on(nbr):
    if nbr == '1':
        led1.on
    elif nbr == '2':
        led2.on
    return render_template('on.html', nbr=nbr)

@app.route('/off/')
@app.route('/off/<nbr>')
def off(nbr):
    if nbr == '1':
        led1.off
    elif nbr == '2':
        led2.off
    return render_template('on.html', nbr=nbr)
