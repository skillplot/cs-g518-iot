---
title: DHT 11 Sensor
description: DHT 11 Sensor
---

1. Latest upgradation:

	```bash
	sudo apt update
	sudo apt full-upgrade
	sudo apt install python3-pip
	sudo pip3 install --upgrade setuptools
	sudo reboot
	```

2. install and run a script developed by Adafruit :

	```bash
	sudo pip3 install --upgrade adafruit-python-shell
	wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
	sudo python3 raspi-blinka.py
	```

3. Install the CircuitPython-DHT Library

	```bash
	pip3 install adafruit-circuitpython-dht
	sudo apt-get install libgpiod2
	```