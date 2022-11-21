---
title: RPI Setup
description: RPI Setup
---

# RPI Setup

```bash
#!/bin/bash
## https://stackoverflow.com/questions/51047700/48address-already-in-use-ah00072-make-sock-could-not-bind-to-address-80
sudo lsof -i:80

sudo netstat -ltnp | grep ':80'
```

https://www.slintel.com/tech/web-and-application-servers/apachehttpserver-vs-lighttpd
https://www.lighttpd.net/

https://linuxize.com/post/how-to-install-apache-on-raspberry-pi/


https://github.com/RaspAP/raspap-webgui

