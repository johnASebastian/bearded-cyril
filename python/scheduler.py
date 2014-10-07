#import ZoneManager 
import sys
import time
from sys import argv

def motion_detected(zone):
	print zone;
	ZoneManager.turnOnZone(zone)

def main():
	f = open(sys.argv[1],"r")
	contents = f.read()
	f.close()
	print contents
	#Start up the api
	#Start up Weemo thing
	#pass instance of this
	while(True):
		time.sleep(1)
		print "sleep"


if __name__ == "__main__":
    main()
