---
title: MQTT
description: MQTT
---


# MQTT
> Message Queuing Telemetry Transport

https://en.wikipedia.org/wiki/MQTT
https://zuli.io/how-to-install-and-configure-mqtt-on-a-raspberry-pi

* MQTT, or Message Queue Telemetry Transport, is a lightweight publish/subscribe messaging protocol frequently used in IoT applications.
* The protocol runs over TCP/IP and is designed to be platform-agnostic
* It is a machine-to-machine communication protocol that uses message multiplexing to transmit data over long distances.

* The publish/subscribe model is used to implement the MQTT messaging protocol, which is lightweight and dynamic in IoT.
    * In the publish and subscribe principle, a topic is required to publish somewhere else so that subscribers see it, and this is why the publish and subscribe principle is used.
    * A broker connects subscribers and publishers in an effort to facilitate communication between them
    * The publisher can publish its message on a topic and the subscriber can listen to it.
    * The broker is only required to use the same network if the topics are distributed throughout the network.

* It can provide real-time and dependable messaging services for Internet of Things (IoT) devices in a fraction of the time and bandwidth required by traditional messaging services.
* MQTT is a protocol that is widely used in the Internet of Things, mobile internet, and in other fields such as electricity. 

Messages can be sent and received by any device using MQTT, and we can communicate with other devices in the network
the broker receives all messages from publishers (who publish on this server) and sends specific messages to subscribers (devices that view the sensor data published by the publisher)


## Node Red MQTT Broker

A MQTT Broker that Is Implemented In Node.js
The use of the MQTT open messaging protocol makes it simple for network clients with limited bandwidth to distribute telemetry data.

You can use MQTT-in and MQTT-out nodes without using the Mosquitto environment
It is used as a MQTT broker in Node.js.
Node is responsible for implementing this MQTT broker. There are no requirements for a Mosquitto-like environment to use because you can use MQTT-in and MQTT-out nodes.



## Exercises

* use the Raspberry Pi as a communication device to send a message from one device to another
* create a Raspberry Pi MQTT Broker for your Raspberry Pi
* use the pubsub library and ESP8266 to send data from our Raspberry Pi MCU to our MQTT server


## Mosquitto MQTT Broker and Client

The recommended method is to use the Mosquitto package from the official repositories. Install MQTT broker and MQTT client. There are many different clients available, but we recommend using `MQTT.fx`
MQTT.fx installed, open it and click on the “Connect” button. In the “Host” field, enter the IP address of your Raspberry Pi. The default port is 1883, so you can leave that field blank.


### Installation and Configuration

* Install `mosquitto` broker and `mosquitto-clients` client packages.
    ```bash
    sudo apt -y update
    sudo apt -y install mosquitto
    sudo apt -y install mosquitto-clients
    ```
* Configure the broker. The mosquitto broker's configuration file is located at `/etc/mosquitto/mosquitto.conf`. Open and edit this file. To configure MQTT broker to be authenticated.
    ```bash
    sudo vi /etc/mosquitto/mosquitto.conf
    ```
* Delete this line.
    ```bash
    include_dir /etc/mosquitto/conf.d
    ```
* Add the following lines to the bottom of the file.
    ```bash
    allow_anonymous false
    password_file /etc/mosquitto/pwfile
    listener 1883
    ```
    * anyone connecting to our broker need to provide username and password
    * mosquitto to listen for messages on port number `1883`
    * If you don't want the broker to require a username and password, don't include the first two lines that we added.
*  tell mosquitto what the username and password are. Replace `<username>` with the username that you would like. Then enter the password you would like when prompted.  When editing the configuration file, you specified a different `password_file` path, replace the path below with the one you used
    ```bash
    sudo mosquitto_passwd -c /etc/mosquitto/pwfile <username>
    ```
* Reboot RPi
    ```bash
    sudo reboot
    ```
* Start the broker
    ```bash
    sudo service mosquitto start
    ```

## References

* https://www.instructables.com/How-to-Use-MQTT-With-the-Raspberry-Pi-and-ESP8266/