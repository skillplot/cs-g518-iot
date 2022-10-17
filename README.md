# Readme

* [docs](docs/index.md)


## Getting Started

1. Clone the repo and configure it
    ```bash
    git clone https://github.com/skillplot/cs-g518-iot.git
    git config user.name <user_name>
    git config user.email <user_email>
    git config -l
    ```
2. To add new/updates changes
    ```bash
    git status
    ## put add all the changes
    git add -A
    ## example to add particular file
    git add README.md
    git status
    git commit -m'put some details on the changes'
    git push
    git status
    ```


## Lab Sessions

* Lab-1
    * [Button](src/001_button.py)
    * [Single Led](src/002_single_led.py)
    * [Multiple Led](src/003_multiple_led.py)
* Lab-2
    * [Touch Sensor](src/004_touch_sensor.py)
    * [Ultrasonic Sensor](src/004_ultrasonic_sensor.py)
* Lab-3
    * [Servo Motor](src/005_servo_motor.py)
    * [LDR](src/006_ldr.py)

