#import the Python GPIO library and time library
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#need to name input and output pins
#TRIG as output pin or transmitter (which triggers the sensor)
#ECHO as input pin or receiver (which reads the return pulse signal from the sensor)
TRIG = 23
ECHO = 24

print("Distance Measurement In Progress")

#set two GPIO pins as input and output pins
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, GPIO.LOW)
print("Waiting For Sensor To Settle")
time.sleep(2)

#to obtain the echo response, we are setting out TRIG pin high for 10 microseconds and then setting it low again
GPIO.output(TRIG, GPIO.HIGH) #triggering the sensor
time.sleep(0.00001) #for 10 microseconds
GPIO.output(TRIG, GPIO.LOW)

#sensor sets ECHO pin to high for the time it takes for the pulse to go and come back
#so we need to measure the amount of time that the ECHO pin stays high
#time.time() function will record the latest timestamp for a given condition
while GPIO.input(ECHO)==0: #ECHO pin goes from low to high, and we’re recording the low condition using the time.time() function
  pulse_start = time.time() #then the recorded timestamp will be the latest time at which that pin was low

#Once a signal is received, the value changes from low (0) to high (1), and the signal will remain high for the duration of the echo pulse
#so we also need the last high timestamp for ECHO
while GPIO.input(ECHO)==1:
  pulse_end = time.time()

#now calculate the difference between the two recorded timestamps
pulse_duration = pulse_end - pulse_start
print("Pulse Duration:",pulse_duration,"seconds")
#speed = distance / time; speed of sound at sea level = 343m/s
distance = pulse_duration * 17150
print("Distance:",distance,"cm")

#clean GPIO pins to ensure that all inputs and outputs are reset
GPIO.cleanup()
