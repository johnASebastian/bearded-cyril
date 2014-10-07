from multiprocessing import Process

from ouimeaux.environment import Environment
from ouimeaux.signals import discovered, devicefound, receiver
from ouimeaux.signals import subscription, statechange

class Controller(object):

    mappings = {
        "zone1": 0,
        "zone2": 1,
        "zone3": 2,
        "zone4": 3
    }

    def __init__(self, callback):
        self.callback = callback
        self.env = Environment(with_cache=False)
        receiver(statechange)(self.state)

    def start(self):
        print "Starting environment"
        self.env.start()
        print "Discover stuff"
        self.env.discover(5)
        print "Wait for stuff"
        self.env.wait()

    def state(self, sender=None, state=None, **kwargs):
        zone = self.mappings.get(sender.name)
        if zone == None:
            return
        self.callback.motion_detected(bool(state), zone)

if __name__ == "__main__":
    class Tmp(object):
        def motion_detected(self, state, zone):
            print "Zone {} motion = {}".format(zone, state)

    print "Create controller"
    ctrl = Controller(Tmp())
    print "Starting controller"
    ctrl.start()
