---
layout: post
title:  "Raspberry Pi WPA-EAP Wifi Connection"
author: mangalbhaskar, Shivam
categories: [ IoT, Raspberry Pi ]
image: assets/images/rpi-3-b-gpio.jpg
featured: true
comments: true
---



1. Create Hash Password
    ```bash
    echo -n "plaintext_password_here" | iconv -t utf16le | openssl md4
    ```
2. Add WPA network details to `/etc/wpa_supplicant/wpa_supplicant.conf` file.
    ```bash
    sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
    ```
3. Add wifi network details (and modify as per comment)
    ```bash
    ## replace:
    ## ssid__name with the wifi SSID
    ## user__name with the wifi username
    ## the_hash with the hash password
    network={
      ssid="ssid__name"
      priority=1
      proto=RSN
      key_mgmt=WPA-EAP
      pairwise=CCMP
      auth_alg=OPEN
      eap=PEAP
      identity="user__name"
      password=hash:the_hash
      phase1="peaplabel=0"
      phase2="auth=MSCHAPV2"
    }
    ```
4. Reconfigure WLAN interface
    ```bash
    ## reconfigure; you should get OK as an output
    wpa_cli -i wlan0 reconfigure
    ```


## Troubleshooting
> work in progress


```bash
ifconfig wlan0
sudo iwlist wlan0 scan
```

```bash
# https://raspberrypi.stackexchange.com/a/123889
sudo killall wpa_supplicant
sudo wpa_supplicant -i wlan0 -D wext -c /etc/wpa_supplicant/wpa_supplicant.conf -B
wpa_cli -i wlan0 reconfigure
```


## References

* [Gist - github wifi LAN](https://gist.github.com/pdp7/d2711b5ff1fbb000240bd8337b859412)
* [wireless-security-guide-introduction-to-leap-authentication](https://resources.infosecinstitute.com/topic/wireless-security-guide-introduction-to-leap-authentication/)
* [connect-raspberry-pi-peap-mschap-v2-wifi](https://blog.iamlevi.net/2017/01/connect-raspberry-pi-peap-mschap-v2-wifi/)
* [setup-wifi-on-raspberry-pi](https://www.maketecheasier.com/setup-wifi-on-raspberry-pi/)
* [multiple-wpa_supplicant-networks/](https://hemstreet.io/raspberry-pi-multiple-wpa_supplicant-networks/)
