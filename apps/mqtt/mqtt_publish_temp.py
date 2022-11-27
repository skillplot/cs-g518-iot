import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
print("connecting to broker",mqttBroker)
client.connect(mqttBroker)

while True:
   randNumber = uniform(20.0, 21.0)
   info=client.publish("TEMPERATURE",randNumber)
#   print(info.is_published())
   print("published " + str(randNumber) + " to topic TEMPERATURE")
   time.sleep(5)