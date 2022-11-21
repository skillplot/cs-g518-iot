#import the Python GPIO library and time library
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pin = 21
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
	if GPIO.input(pin):
		print("Touch is detected")
		
	else:
		print("Touch is not detected")
	time.sleep(1)
