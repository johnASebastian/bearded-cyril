import RPi.GPIO as GPIO
import time

class ZoneManager(object):
	zones = [11,7,16,10]

	def __init__ (self):
		GPIO.setmode(GPIO.BOARD)
		for pin in zones:
			GPIO.setup(pin, GPIO.OUT)

	def turnZoneOn(self, zoneNumber):
		GPIO.output(self.zone[zoneNumber], TRUE)

	def turnZoneOff(self, zoneNumber):
		GPIO.output(self.zone[zoneNumebr], FALSE)



