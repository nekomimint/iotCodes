import gpiozero as GPIO
import time


BOTON_UP = GPIO.Button(26)
BOTON_LEFT = GPIO.Button(25)
BOTON_RIGHT = GPIO.Button(19)
BOTON_DOWN = GPIO.Button(13)
try:
    while True:
        time.sleep(0.4)
        if BOTON_UP.is_active:
            print("Arriba")
        if BOTON_DOWN.is_active:
            print("Abajo")
        if BOTON_LEFT.is_active:
            print("Izquierda")
        if BOTON_RIGHT.is_active:
            print("Derecha")
except KeyboardInterrupt:
    print("Se finalizo la prueba")