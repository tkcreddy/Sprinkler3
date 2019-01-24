import jsoncfg
class configread():

    def __init__(self):
        self.config = jsoncfg.load_config('PIN.cfg')

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



