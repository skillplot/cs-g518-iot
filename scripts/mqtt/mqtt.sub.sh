#!/bin/bash

## Copyright (c) 2021 mangalbhaskar. All Rights Reserved.
##__author__ = 'mangalbhaskar'
###----------------------------------------------------------
## MQTT
#
## The mosquitto_pub command will publish to a topic
# -d debug mode; so all messages and activity will be output on the screen
# -u username
# -P password
# -t topic name we want to publish to
# -q Quality Of Service (QoS); 0 or 1 or 2
# -h hostname
# -p port
# -m message
#
## publish a message to the "test" topic
## mosquitto_pub -d -u username -P password -t test -m "Hello, World!" -q 0
#
## References:
## https://mosquitto.org/documentation/migrating-to-2-0/
###----------------------------------------------------------

topic=$1
[[ ! -z ${topic} ]] || topic="test"

mosquitto_sub -d -t ${topic} -p 1883


topic=$1
qos=$2

[[ ! -z ${topic} ]] || topic="test"
[[ ! -z ${qos} ]] || qos=0

username=pi
password=pi12345
host=localhost
port=1883
# mosquitto_sub -d -t ${topic} -p 1883
mosquitto_sub -d -t ${topic} -h ${host} -p ${port} -q ${qos};
