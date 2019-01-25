from com.aak.modules.config.configread import configread

import RPi.GPIO as GPIO

x = configread()
y = x.GPIO(1)
print("", y)
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(y, GPIO.OUT)