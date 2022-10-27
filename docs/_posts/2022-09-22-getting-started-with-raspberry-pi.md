---
layout: post
title:  "Getting Started With Raspberry Pi"
author: mangalbhaskar
categories: [ IoT, Raspberry Pi ]
image: assets/images/getting-started-with-raspberry-pi-1.png
featured: true
comments: true
---


## Overview

1. Installing OS in Raspberry Pi
2. Installing through headless system (Enabling Wifi and SSH)
3. Remote access through your laptop

The following steps are required to be performed to complete above all tasks.

1. Install Raspberry Pi Imager in your desktop or laptop
2. Insert the Micro SD Card into Card Reader.
3. Inject the Card reader into laptop and format it.
4. Install the OS into Micro SD Card using Imager.
5. Install Putty into your laptop.
6. Connect Raspberry Pi through Putty.
7. Use Remote Desktop Connect (windows application) for remote connection
8. Surf the web browser through laptop


## Install RPI Image on the SD Card

```bash
sudo snap install rpi-imager
```
* configure settings
    * hostname
    * username/password
    * enable ssh
    * wifi SSID, password
    * disable telemetry
* write the rpi image to SD card; verify the image


## Connect to RPI over SSH

```bash
ip a
## nmap - Network exploration tool and security / port scanner
nmap 192.168.0.*
ssh pi@192.168.0.104
```

## Configure RPI for GUI

```bash
raspinfo
#
raspi-config
```

* Interface Options => VNC => enable the service => Finish => Reboot required
* Download & Install VNC viewer on Laptop


## References


The detailed instructions to perform the above tasks can be found in the following web link.

* [Raspberrypi Getting Started](https://www.raspberrypi.org/documentation/computers/getting-started.html)
* [Raspberrypi Documentation](https://www.raspberrypi.com/documentation/)
* [Download & Install VNC viewer on Laptop](https://www.realvnc.com/en/connect/download/viewer/#)
