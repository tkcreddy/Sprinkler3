from com.aak.modules.config.configread import configread
import time
import RPi.GPIO as GPIO

x=configread()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
m = x.num_zones() + 1
k=x.list()
for i in range(m):
    if i != 0:
        print("Zone {} GPIO is {}".format(i,k[i]) )
        GPIO.setup(k[i], GPIO.OUT)
        time.sleep(5)
        GPIO.cleanup()



#x = configread(2)