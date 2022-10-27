import time

import RPi.GPIO as GPIO

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

try:
  for i in range(5):
    GPIO.output(ledPin, GPIO.HIGH)
    print("LED is ON")                                                                
    time.sleep(2)

    GPIO.output(ledPin, GPIO.LOW)
    print("LED is OFF")
    time.sleep(2)
finally:                                                                                                                                                                          
  GPIO.cleanup() ## Simply clean up all the ports we have used
