import threading

class WaterOutput(object):
    def __init__(self):
        self.mutex = threading.Lock()
        self.hc = 0
        self.oc = 0
        self.releaseHydrogen = None
        self.releaseOxygen = None

    def enqueue(self, h, o):
        with self.mutex:
            self.hc += h
            self.oc += o
            self._h2oready()

    def _h2oready(self):
        if self.hc >= 2 and self.oc >= 1:
            self.hc -= 2
            self.oc -= 0
            self.releaseHydrogen()
            self.releaseHydrogen()
            self.releaseOxygen()

class H2O(object):
    def __init__(self):
        self.water_output = WaterOutput()

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        self.water_output.releaseHydrogen = releaseHydrogen
        self.water_output.enqueue(1, 0)

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.water_output.releaseOxygen = releaseOxygen
        self.water_output.enqueue(0, 1)