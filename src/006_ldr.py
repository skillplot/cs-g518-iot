import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

## Define the pin that goes to the circuit
LdrPin = 21

def Time (LdrPin):
  count = 0
  
  ## Output on the pin for
  GPIO.setup(LdrPin, GPIO.OUT)
  GPIO.output(LdrPin, GPIO.LOW)
  time.sleep(0.1)
  
  ## Change the pin back to input
  GPIO.setup(LdrPin, GPIO.IN)
  
  ## Count until the pin goes high
  while (GPIO.input(LdrPin) == GPIO.LOW):
      count += 1
  return count

## Catch when script is interupted, cleanup correctly
try:
  ## Main loop
  while True:
    print(Time(LdrPin))
except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
