import ZoneManager 
import sys
import time
#import wemo
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
	zm = ZoneManager.ZoneManager()
	#Start up Weemo thing
#	wemo(self)
	#pass instance of this
	while(True):
		time.sleep(1)
		print "sleep"
		time.sleep(1)
		zm.turnZoneOn(0)
		zm.turnZoneOn(1)
		time.sleep(1)
		zm.turnZoneOn(2)
		zm.turnZoneOn(3)
		time.sleep(1)
		zm.turnZoneOff(0)
		zm.turnZoneOff(1)
		time.sleep(1)
		zm.turnZoneOff(2)
		zm.turnZoneOff(3)



if __name__ == "__main__":
    main()
