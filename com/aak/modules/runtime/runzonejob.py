from com.aak.modules.config.configread import configread
import traceback
import time
import RPi.GPIO as GPIO


class Runzonejob():

    def __init__(self, zone, num_secs):
        self.zone = zone
        self.num_secs = num_secs

    def runjob(self):
        try:
            getconfig = configread()
            gpioid = getconfig.GPIO(self.zone)
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.cleanup()
            GPIO.setup(gpioid, GPIO.OUT)
            time.sleep(self.num_secs)

        except Exception as ex:
            traceback.print_exc()
        finally:
            GPIO.cleanup()  # this ensures a clean exit

