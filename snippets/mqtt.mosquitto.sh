#!/bin/bash

sudo apt -y update
sudo apt -y install mosquitto
sudo apt -y install mosquitto-clients

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


## The mosquitto_sub command will subscribe to a topic
# -d debug mode; so all messages and activity will be output on the screen
# -u username
# -P password
# -t topic name we want to subscribe to

# mosquitto_sub -d -u username -P password -t test
# mosquitto_sub -d -t test

## publish a message to the "test" topic
## mosquitto_pub -d -u username -P password -t test -m "Hello, World!"


## pip install paho-mqtt

