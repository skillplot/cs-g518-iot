#!/bin/bash

sudo service mosquitto start

## configure mosquitto
# sudo vi /etc/mosquitto/mosquitto.conf


# * Delete this line.
#     ```bash
#     include_dir /etc/mosquitto/conf.d
#     ```
# * Add the following lines to the bottom of the file.
#     ```bash
#     allow_anonymous false
#     password_file /etc/mosquitto/pwfile
#     listener 1883
#     ```

# sudo mosquitto_passwd -c /etc/mosquitto/pwfile <username>
