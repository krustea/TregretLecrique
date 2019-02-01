import RPi.GPIO as GPIO
class Led2:
    def __init__(self, Celsius):
        self.Celsius = Celsius
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        
    def led2_Celsius(self):
        if (self.Celsius < 15):
            GPIO.output(18, GPIO.HIGH)
        elif (self.Celsius > 30):
            GPIO.output(24, GPIO.HIGH)
            
