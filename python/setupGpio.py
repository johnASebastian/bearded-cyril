import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
zones = [11,7,16,10]
for pin in zones:
	GPIO.setup(pin, GPIO.OUT)

