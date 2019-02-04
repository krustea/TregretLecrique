import RPi.GPIO as GPIO
import time

# Initialisation des GPIOs

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Numéro de la broche que nous allons utiliser pour lire 
# les données
broche=27

def read_light():
    lightCount = 0 #intitialisation de la variable de lumière
    GPIO.setup(broche, GPIO.OUT)
    GPIO.output(broche, GPIO.LOW)
    time.sleep(0.1) # on draine la charge du condensateur
    GPIO.setup(broche, GPIO.IN)
    #Tant que la broche lit ‘off’ on incrémente notre variable
    while (GPIO.input(broche) == GPIO.LOW):
        lightCount += 1
    return lightCount

# Boucle infini jusqu'à CTRL-C
while True:
    print(read_light())
    time.sleep(1)
