import jsoncfg
import os
class configread():

    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'PIN.cfg')
        self.config = jsoncfg.load_config(self.config_path)

    def GPIO(self,zone):
        self.zone = zone
        self.GPIO = self.config.zones[self.zone].GPIO()
        return self.GPIO

    def num_zones(self):
        self.num_zones = self.config.num_of_zones()
        return self.num_zones

    def list(self):
        self.gpiolist = {}
        self.numz=self.num_zones + 1
        for i in range(self.numz):
            if i != 0:
                self.gpiolist[i] = self.config.zones[i].GPIO()
        return self.gpiolist
