import ZoneManager 
import sys
import time
import wemo
import datetime
from datetime import datetime
from sys import argv

class Scheduler(object):
	def __init__(self, zm):
		self.zm = zm
		self.zones = [{'blocked':False, 'on':False}, {'blocked':False,'on':False},
				{'blocked':False, 'on':False}, {'blocked':False, 'on':False}] 

	def motion_detected(self, state, zoneId):
		print 'motion detected in zone ', zoneId, 'active? ', state;
		zone = self.zones[zoneId]
		zone['blocked'] = state
		print 'after changing, blocked is', zone['blocked']
		print 'after changing, on is', zone['on']
		if state:
			print 'iffing'
			self.zm.turnZoneOff(zoneId)
		else:
			print 'elsing', 'on', zone['on']
			# if zone['on']:
			# 	print 'iffing 2'
			self.zm.turnZoneOn(zoneId)
		print 'zone ', zoneId,'status', zone['blocked']

	def zone_start(self, zoneId):
		zone = self.zones[zoneId]
		zone['on'] = True
		print 'attempting to start ', zoneId, 'blocked? ', zone['blocked'], 'on?', zone['on']
		if not zone['blocked']:
			self.zm.turnZoneOn(zoneId)
		print 'after turning on, on is', self.zones[zoneId]['on']
		self.zones[zoneId] = zone

	def zone_stop(self, zone):
		print 'stopping'
		temp = self.zones[zone]
		temp['on'] = False
		self.zm.turnZoneOff(zone)
		
def main():
	#f = open(sys.argv[1],"r")
	#contents = f.read()
	#f.close()
	#print contents
	#Start up the api
	#Start up Zonemaonager
	zm = ZoneManager.ZoneManager()
	#Start up Weemo thing
	runner = Scheduler(zm)
	wemo.Controller(runner).start()
	#pass instance of this
	runner.zone_start(0)
	runner.zone_start(1)
	time.sleep(1)
	runner.zone_start(2)
	runner.zone_start(3)
	while(True):
		time.sleep(1)
#		print "sleep"
#		time.sleep(1)
#		runner.zone_start(0)
#		runner.zone_start(1)
#		time.sleep(1)
#		runner.zone_start(2)
#		runner.zone_start(3)
#		time.sleep(1)
#		runner.zone_stop(0)
#		runner.zone_stop(1)
#		time.sleep(1)
#		runner.zone_stop(2)
#		runner.zone_stop(3)



if __name__ == "__main__":
    main()
