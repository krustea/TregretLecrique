import RPi.GPIO as GPIO
class Led2:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        
    def led2_Celsius(self, Celsius):
        if (Celsius < 15):
            GPIO.output(18, GPIO.HIGH)
        elif(Celsius >= 15 and Celsius <= 30):
            GPIO.output(18, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
        elif (Celsius > 30):
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            
