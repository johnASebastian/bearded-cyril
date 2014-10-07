import ZoneManager 
import sys
import time
import wemo
from sys import argv

def motion_detected(state,zone):
	print zone;
	if state:
		ZoneManager.turnZoneOn(zone)
	else:
		ZoneManager.turnZoneOff(zone)

def main():
	f = open(sys.argv[1],"r")
	contents = f.read()
	f.close()
	print contents
	#Start up the api
	#Start up Zonemaonager
	ZoneManager()
	#Start up Weemo thing
	wemo(self)
	#pass instance of this
	while(True):
		time.sleep(1)
		print "sleep"
		time.sleep(1)
		ZoneManager.turnZoneOn(0)
		ZoneManager.turnZoneOn(1)
		time.sleep(1)
		ZoneManager.turnZoneOn(2)
		ZoneManager.turnZoneOn(3)
		time.sleep(1)
		ZoneManager.turnZoneOff(0)
		ZoneManager.turnZoneOff(1)
		time.sleep(1)
		ZoneManager.turnZoneOff(2)
		ZoneManager.turnZoneOff(3)



if __name__ == "__main__":
    main()
