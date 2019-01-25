from com.aak.modules.config.configread import configread
import RPi.GPIO as GPIO

x=configread()
y=x.GPIO(8)
print("", y)
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(y, GPIO.OUT)

m = x.num_zones() + 1
k=x.list()
for i in range(m):
    if i != 0:
        print("Zone {} GPIO is {}".format(i,k[i]) )


#x = configread(2)