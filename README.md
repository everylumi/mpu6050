# mpu6050

A Python module for accessing the MPU-6050 digital accelerometer and gyroscope on a Raspberry Pi.


## Installation

```sh
cd ~/Downloads/ && sudo rm -rf mpu6050  
git clone https://github.com/everylumi/mpu6050.git
cd mpu6050/  
sudo python3 setup.py install #Python3  
sudo python setup.py install #Python2
```


## Uninstallation

```sh
sudo pip3 uninstall #Python3  
sudo pip uninstall #Python2
```

## Connection

VCC  -->   Raspberry Pi 3.3V  
GND  -->   Raspberry Pi GND  
SCL  -->   Raspberry Pi SCL  
SDA  -->   Raspberry Pi SDA  
AD0  -->   Raspberry Pi 3.3V, only for Slave connection
(I2C address: Master 0x68, Slave 0x69)


## Usage

First, ensure the device is available on the i2c bus:

```
$ sudo i2cdetect -y 1
# Master
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --

# Slave
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- 69 -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

Within Python, the device can be used like this:

```python
from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)   # Slave : 0x69

'''
Select Scale range
Accelerometer: ACCEL_RANGE_2G, ACCEL_RANGE_4G, ACCEL_RANGE_8G, ACCEL_RANGE_16G  
Gyroscope: GYRO_RANGE_250DEG, GYRO_RANGE_500DEG, GYRO_RANGE_1000DEG, GYRO_RANGE_2000DEG 
'''
#sensor.set_aceel_range(sensor.ACCEL_RANGE_2G)   #defalut: ACCEL_RANGE_2G
#sensor.set_gyro_range(sensor.GYRO_RANGE_250DEG) #defalut: AGYRO_RANGE_250DEG

while True:

    # Accelerometer data
    print("\nAccelerometer data")
    accel_data = sensor.get_accel_data()
    print(" x: " + str(accel_data['x']))
    print(" y: " + str(accel_data['y']))
    print(" z: " + str(accel_data['z']))
    
    # Accelerometer angle data
    accel_date_angle = sensor.get_accel_rotation()
    print(" - X_Rotation: ",round(accel_date_angle['y'],1), "\u00b0")
    print(" - Y_Rotation: ",round(accel_date_angle['x'],1), "\u00b0")
    print(" - Z_Rotation: ",round(accel_date_angle['z'],1), "\u00b0")

    # Gyroscope data, unit: degree/sec
    print("Gyroscope data")
    gyro_data = sensor.get_gyro_data()
    print(" x: " + str(gyro_data['x']))
    print(" y: " + str(gyro_data['y']))
    print(" z: " + str(gyro_data['z']))

    # Temperature
    temp = sensor.get_temp()
    print("Temp: ",round(temp,1), "\u00b0C")
 
    time.sleep(0.5)
```


## License

This project is licensed under the terms of the MIT license.
