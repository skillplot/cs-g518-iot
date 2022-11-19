#!/bin/bash

topic=$1
[[ ! -z ${topic} ]] || topic="test"

mosquitto_sub -d -t ${topic} -p 1883
