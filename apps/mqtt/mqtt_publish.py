import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("first")
print("connecting to broker",mqttBroker)
client.connect(mqttBroker)

while True:
    info = client.publish("firstcode", "hello")
    print(info.is_published())
    print("Just published " +"hello "+ "to topic firstcode")
    time.sleep(5)
