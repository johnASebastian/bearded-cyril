import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
for pin in range(2,26):
	GPIO.setup(x, GPIO.OUT)

	