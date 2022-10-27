---
layout: post
title:  "Getting Started With Raspberry Pi"
author: mangalbhaskar
categories: [ IoT, Raspberry Pi ]
image: assets/images/getting-started-with-raspberry-pi-1.png
featured: true
comments: true
---


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
raspi-config
```

* Interface Options => VNC => enable the service => Finish => Reboot required
* Download & Install VNC viewer on Laptop


## References

* [Download & Install VNC viewer on Laptop](https://www.realvnc.com/en/connect/download/viewer/#)
* [Raspberrypi Documentation](https://www.raspberrypi.com/documentation/)
