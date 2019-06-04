import smbus2
import bme280
import time
import alertlib

def calibrate(numb):
    bus = smbus2.SMBus(numb)
    return bme280.load_calibration_params(bus, 0x76)

def get_data(numb,calibration):
    bus = smbus2.SMBus(numb)
    return bme280.sample(bus, 0x76, calibration)

def print_data(data):
    print("Reading sensor on i2c bus 3 at time %f" % data.timestamp)
    print "Temperature : %.2f" %data.temperature
    print "Pressure : %.2f hPa " %data.pressure+"\n"

calibration3 = calibrate(3)
calibration4 = calibrate(4)

while True:
    inside_sensor = get_data(3,calibration3)
    outside_sensor = get_data(4,calibration4)
    if inside_sensor.pressure/outside_sensor.pressure > 1.1:
        print "warning"
        alert = alertlib.Alert("The pressure sensors are out of sync!")
        alert.send_to_email("zandrews22@gmail.com --summary Pressure sensors")
    time.sleep(60)
    

