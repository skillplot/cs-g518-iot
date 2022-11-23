---
layout: post
title:  "MQTT Installation"
author: mangalbhaskar
categories: [ MQTT, IoT, Raspberry Pi ]
featured: true
comments: true
---


# MQTT Installation


* Install `mosquitto` broker and `mosquitto-clients` client packages.
    ```bash
    sudo apt -y update
    sudo apt -y install mosquitto
    sudo apt -y install mosquitto-clients
    ```


## Configuration

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

* [How-to-Use-MQTT-With-the-Raspberry-Pi-and-ESP8266](https://www.instructables.com/How-to-Use-MQTT-With-the-Raspberry-Pi-and-ESP8266/)
