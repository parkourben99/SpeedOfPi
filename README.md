# SpeedOfPi 

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/parkourben99/SpeedOfPi/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/parkourben99/SpeedOfPi/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/parkourben99/SpeedOfPi/badges/build.png?b=master)](https://scrutinizer-ci.com/g/parkourben99/SpeedOfPi/build-status/master)

Required:
- Raspberry Pi running [raspbian](https://www.raspberrypi.org/downloads/raspbian/)
- PCF8574 8-bit I2C I/O Expander
- 60 x Leds & Buttons

The first step is to enable i2c via raspi-config: `sudo raspi-config`, select advance menu, select i2c, then enable it.
Make sure you are upto date `sudo apt-get update`.
Next install smbus which will control the i2c, `sudo apt-get install python3-smbus`.