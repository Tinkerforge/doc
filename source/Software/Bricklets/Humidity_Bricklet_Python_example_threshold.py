#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_humidity import Humidity

# Callback for humidity outside of 30 to 60 %RH
def cb_reached(humidity):
    if humidity < 30:
        print('Humidity too low: ' + str(humidity/10.0) + ' %RH')
    if humidity > 60:
        print('Humidity too high ' + str(humidity/10.0) + ' %RH')

    print('Recommended humiditiy for human comfort is 30 to 60 %RH.')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    h = Humidity(UID) # Create device object
    ipcon.add_device(h) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    h.set_debounce_period(10000)

    # Register threshold reached callback to function cb_reached
    h.register_callback(h.CALLBACK_HUMIDITY_REACHED, cb_reached)

    # Configure threshold for "outside of 30 to 60 %RH" (unit is %RH/10)
    h.set_humidity_callback_threshold('o', 30*10, 60*10)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
