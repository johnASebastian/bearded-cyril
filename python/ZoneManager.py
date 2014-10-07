import RPi.GPIO as GPIO
import time

class ZoneManager(object):
	zones = [11,7,16,10]
	
	def setupZones(self):
		GPIO.setmode(GPIO.BOARD)
		for pin in self.zones:
			GPIO.setup(pin, GPIO.OUT)

	def turnZoneOn(self, zoneNumber):
		GPIO.output(self.zones[zoneNumber], True)

	def turnZoneOff(self, zoneNumber):
		GPIO.output(self.zones[zoneNumber], False)



