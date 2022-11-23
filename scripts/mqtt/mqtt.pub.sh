#!/bin/bash


## The mosquitto_pub command will publish to a topic
# -d debug mode; so all messages and activity will be output on the screen
# -u username
# -P password
# -t topic name we want to publish to

## publish a message to the "test" topic
## mosquitto_pub -d -u username -P password -t test -m "Hello, World!"


topic=$1
[[ ! -z ${topic} ]] || topic="test"

for i in $(seq 1 1 10); do
  echo -e "$i: ${topic}\n";
  sleep 1;
  mosquitto_pub -d -t ${topic} -m "Namaste, World!" -p 1883;
done
