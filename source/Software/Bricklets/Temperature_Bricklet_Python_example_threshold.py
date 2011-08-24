#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_temperature import Temperature

# Callback for temperature greater than 30 °C
def cb_reached(temperature):
    print('We have ' + str(temperature/100.0) + ' °C.')
    print('It is too hot, we need air conditioning!')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    t = Temperature(UID) # Create device object
    ipcon.add_device(t) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    t.set_debounce_period(10000)

    # Register threshold reached callback to function cb_reached
    t.register_callback(t.CALLBACK_TEMPERATURE_REACHED, cb_reached)

    # Configure threshold for "greater than 30 °C" (unit is °C/100)
    t.set_temperature_callback_threshold('>', 30*100, 0)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
