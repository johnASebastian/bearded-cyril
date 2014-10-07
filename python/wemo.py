from multiprocessing import Process

from ouimeaux.environment import Environment
from ouimeaux.signals import discovered, devicefound, receiver
from ouimeaux.signals import subscription, statechange

class Controller(object):

    def __init__(self, callback):
        self.callback = callback
        self.env = Environment(
            motion_callback=self.new_motion,
            with_cache=False)
        receiver(devicefound)(self.found)
        receiver(statechange)(self.state)

    def new_motion(self, motion):
        print "Found motion"
        print motion

    def start(self):
        print "Starting environment"
        self.env.start()
        print "Discover stuff"
        self.env.discover(5)
        print "Wait for stuff"
        self.env.wait()

    def found(self, **kwargs):
        print "Discovered"
        print kwargs

    def state(self, **kwargs):
        print "State Changed"
        print kwargs

if __name__ == "__main__":
    print "Create controller"
    ctrl = Controller(None)
    print "Starting controller"
    ctrl.start()
