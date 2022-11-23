#!/bin/bash


## The mosquitto_sub command will subscribe to a topic
# -d debug mode; so all messages and activity will be output on the screen
# -u username
# -P password
# -t topic name we want to subscribe to

## mosquitto_sub -d -u username -P password -t test
## mosquitto_sub -d -t test

topic=$1
[[ ! -z ${topic} ]] || topic="test"

mosquitto_sub -d -t ${topic} -p 1883
