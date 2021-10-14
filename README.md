# mpu6050

A Python module for accessing the MPU-6050 digital accelerometer and gyroscope on a Raspberry Pi.


## Installation

```sh
cd Downloads/  
git clone https://github.com/everylumi/mpu6050.git
cd mpu6050/  
sudo python3 setup.py install #Python3  
sudo python setup.py install #Python2
```

## Usage

First, ensure the device is available on the i2c bus:

```
$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- 5a -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

Within Python, the device can be used like this:

```python
from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)

while True:
    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    temp = sensor.get_temp()

    print("Accelerometer data")
    print("x: " + str(accel_data['x']))
    print("y: " + str(accel_data['y']))
    print("z: " + str(accel_data['z']))

    print("Gyroscope data")
    print("x: " + str(gyro_data['x']))
    print("y: " + str(gyro_data['y']))
    print("z: " + str(gyro_data['z']))

    print("Temp: " + str(temp) + " C")
    sleep(0.5)
```

## License

This project is licensed under the terms of the MIT license.










Example
-------

Assuming that the address of your MPU-6050 is 0x68, you can read read accelerometer data like this:

::

    >>> from mpu6050 import mpu6050

    >>> sensor = mpu6050(0x68)

    >>> accelerometer_data = sensor.get_accel_data()

Dependencies
------------

Either the ``python-smbus`` or ``python3-smbus`` package, according to your
Python version.

Installation
------------

There are two ways of installing this package: via PyPi or via the git repository.
Installing from the git repository insures that you have the absolute latest
version installed, but this can be prone to bugs.

1. install the python-smbus package
::

    sudo apt install python3-smbus

2a. Install this package from PyPi repository
::

    pip install mpu6050-raspberrypi

Or:

2b. Clone the repository and run setup.py
::
    
    git clone https://github.com/Tijndagamer/mpu6050.git
    python setup.py install

Issues & Bugs
-------------

Please report any issues or bugs here:

    https://github.com/Tijndagamer/mpu6050/issues


License
-------

::

    Copyright (c) 2015, 2016, 2017, 2018 Martijn (MrTijn) and contributors
    Licensed under the MIT License. For more information, see ``LICENSE``.
