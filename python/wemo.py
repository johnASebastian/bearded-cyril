from multiprocessing import Process
from threading import Timer

from ouimeaux.environment import Environment
from ouimeaux.signals import discovered, devicefound, receiver
from ouimeaux.signals import subscription, statechange

class Zone(object):

    def __init__(self, num, callback):
        self.num = num
        self.motion = False
        self.event = None
        self.callback = callback

    def trigger(self, motion):
        if self.event:
            self.event = None
        self.motion = motion
        self.callback.motion_detected(motion, self.num)

    def schedule(self):
        if self.event != None:
            return
        print "Schedule event zone {}".format(self.num)
        self.event = Timer(30, self.trigger, (False,))
        self.event.start()

    def cancel(self):
        print "Cancel event"
        if self.event != None:
            self.event.cancel()
        self.event = None


class Controller(object):

    def __init__(self, callback):
        self.callback = callback
        self.motion = False
        self.env = Environment(with_cache=False)
        self.event = None
        receiver(statechange)(self.state)
        self.mappings = {
            "zone1": Zone(0, callback),
            "zone2": Zone(1, callback),
            "zone3": Zone(2, callback),
            "zone4": Zone(3, callback)
        }


    def start(self):
        print "Starting environment"
        self.env.start()
        print "Discover stuff"
        self.env.discover(5)
        print "Wait for stuff"
        Process(target=self.env.wait).start()

    def state(self, sender=None, state=None, **kwargs):
        motion = bool(state)
        print "Got state change {} {}".format(sender.name, motion)
        zone = self.mappings.get(sender.name)

        if zone == None:
            return

        if motion:
            zone.cancel()

        if zone.motion and not motion:
            zone.schedule()

        if not zone.motion and motion:
            zone.trigger(motion)

if __name__ == "__main__":
    class Tmp(object):
        def motion_detected(self, state, zone):
            print "ZONE {} MOTION = {}".format(zone, state)

    print "Create controller"
    ctrl = Controller(Tmp())
    print "Starting controller"
    ctrl.start()
