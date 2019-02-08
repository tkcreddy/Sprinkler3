import jsoncfg
import os
class Configread():

    def __init__(self):
        BASE_PATH = '../config'
        self.config_path = os.path.join(BASE_PATH,'CONFIG.cfg')
        self.config = jsoncfg.load_config(self.config_path)

    def GPIO(self,zone):
        self.zone = zone
        self.GPIO = self.config.zones[self.zone].GPIO()
        return self.GPIO

    def num_zones(self):
        self.num_zones = self.config.num_of_zones()
        return self.num_zones

    def db_loc(self):
        self.db_loc = self.config.db()
        return self.db_loc

    def num_programs(self):
        self.num_programs = self.config.num_of_progams()
        return self.num_programs


    def list(self):
        self.gpiolist = {}
        self.numz=self.num_zones + 1
        for i in range(self.numz):
            if i != 0:
                self.gpiolist[i] = self.config.zones[i].GPIO()
        return self.gpiolist
