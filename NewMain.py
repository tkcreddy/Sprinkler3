from com.aak.modules.config.configread import configread
import traceback
import time
import RPi.GPIO as GPIO

def Main():
    try:
        x = configread()
        y = x.GPIO(1)
        print("", y)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(y, GPIO.OUT)
        time.sleep(10)

    except Exception as ex:
        traceback.print_exc()
    finally:
        GPIO.cleanup() #this ensures a clean exit


Main()