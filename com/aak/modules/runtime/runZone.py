from com.aak.modules.config.configRead import Configread
import traceback
import time
import RPi.GPIO as GPIO

class Runzonejob():

    def __init__(self, zone, num_secs):
        self.zone = int(zone)
        self.num_secs = int(num_secs)

        try:
            getconfig = Configread()
            gpioid = getconfig.GPIO(self.zone)
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.cleanup()
            print("Zone {} job kicked off".format(self.zone))
            GPIO.setup(gpioid, GPIO.OUT)
            time.sleep(self.num_secs)
            print("Zone {} job done".format(self.zone))

        except Exception as ex:
            traceback.print_exc()
        finally:
            GPIO.cleanup()  # this ensures a clean exit

