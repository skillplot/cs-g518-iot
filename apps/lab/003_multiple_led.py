import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

try:
  for i in range(2):
    print("Iteration",i)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)

    GPIO.output(17,True)
    print("1st Led is ON")
    time.sleep(3)
    GPIO.output(17,False)
    print("1st Led is OFF")
    time.sleep(3)

    GPIO.output(18,True)
    print("2nd Led is ON")
    time.sleep(3)
    GPIO.output(18,False)
    print("2nd Led is OFF")
    time.sleep(3)

    GPIO.output(22,True)
    print("3rd Led is ON")
    time.sleep(3)
    GPIO.output(22,False)
    print("3rd Led is OFF")
    time.sleep(3)
finally:
    GPIO.cleanup() ## Simply clean up all the ports we have used
