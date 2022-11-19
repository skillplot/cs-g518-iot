#!/bin/bash

topic=$1
[[ ! -z ${topic} ]] || topic="test"

for i in $(seq 1 1 10); do
  echo -e "$i: ${topic}\n";
  sleep 1;
  mosquitto_pub -d -t ${topic} -m "Namaste, World!" -p 1883;
done
