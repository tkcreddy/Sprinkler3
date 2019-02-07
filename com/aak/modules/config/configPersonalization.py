import jsoncfg
import os
class Configpersonalization():

    def __init__(self):
        BASE_PATH = '../config'
        self.personalize_config_file = os.path.join(BASE_PATH, 'Personal_config.cfg')
        self.config = jsoncfg.load_config(self.personalize_config_file)


    def GPIO(self,zone):
        self.zone = zone
        self.GPIO = self.config.zones[self.zone].GPIO()
        return self.GPIO

    def zip(self):
        self.zip = self.config.zip()
        return self.zip

    def country(self):
        self.country = self.config.country()
        return self.country

    def owm_appid(self):
        self.owm_appid = self.config.owm_appid()
        return self.owm_appid

    def list(self):
        self.gpiolist = {}
        self.numz=self.num_zones + 1
        for i in range(self.numz):
            if i != 0:
                self.gpiolist[i] = self.config.zones[i].GPIO()
        return self.gpiolist
