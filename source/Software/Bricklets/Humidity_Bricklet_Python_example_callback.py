#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_humidity import Humidity

# Callback function for humidity callback (parameter has unit %RH/10)
def cb_humidity(rh):
    print('Relative Humidity: ' + str(rh/10.0) + ' %RH')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    h = Humidity(UID) # Create device object
    ipcon.add_device(h) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Set Period for rh callback to 1s (1000ms)
    # Note: The callback is only called every second if the 
    #       humidity has changed since the last call!
    h.set_humidity_callback_period(1000)

    # Register humidity callback to function cb_humidity
    h.register_callback(h.CALLBACK_HUMIDITY, cb_humidity)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
