#/bin/bash

## Copyright (c) 2021 mangalbhaskar. All Rights Reserved.
##__author__ = 'mangalbhaskar'
###----------------------------------------------------------
## MQTT
#
## References:
## https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/
###----------------------------------------------------------


sudo apt -y update
sudo apt -y install mosquitto
sudo apt -y install mosquitto-clients

sudo systemctl enable mosquitto.service

mosquitto -v


# sudo vi /etc/mosquitto/mosquitto.conf

# sudo service mosquitto start

# * Delete this line.
#     ```bash
#     include_dir /etc/mosquitto/conf.d
#     ```
# * Add the following lines to the bottom of the file.
#     ```bash
#     allow_anonymous false
#     password_file /etc/mosquitto/pwfile
#     listener 1883
#     ```

# sudo mosquitto_passwd -c /etc/mosquitto/pwfile <username>
