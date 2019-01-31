import RPi.GPIO as GPIO
class Led:
    def __init__(self, numero_broche):
        self.numero_broche = numero_broche
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(numero_broche, GPIO.OUT)

    def on(self, numero_broche):
        return GPIO.output(numero_broche, GPIO.HIGH)

    def off(self, numero_broche):
        return GPIO.output(numero_broche, GPIO.LOW)

led1= Led('14')
led2= Led('15')
