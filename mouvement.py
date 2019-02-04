import RPi.GPIO as GPIO
import time

# Initialisation de notre GPIO 17 pour recevoir un signal
# Contrairement à nos LEDs avec lesquelles on envoyait un signal
broche=17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(broche, GPIO.IN)

currentstate = 0
previousstate = 0

# Boucle infini jusqu'à CTRL-C
while True:
    # Lecture du capteur
    currentstate = GPIO.input(broche)
		 # Si le capteur est déclenché
    if currentstate == 1 and previousstate == 0:
        print("    Mouvement détecté !")
        # En enregistrer l'état
        previousstate = 1
    # Si le capteur est s'est stabilisé
    elif currentstate == 0 and previousstate == 1:
        print("    Prêt")
        previousstate = 0
    # On attends 10ms
    time.sleep(0.01)
