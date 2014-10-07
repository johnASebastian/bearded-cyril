import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
zones = [11,7,16,10]
for pin in zones:
	GPIO.setup(pin, GPIO.OUT)

for pin in zones:
	GPIO.output(pin, TRUE)
	time.sleep(5)
	GPIO.output(pin, FALSE)
	

