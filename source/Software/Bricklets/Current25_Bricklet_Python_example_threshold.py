#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "ABCD" # Change to your UID

from ip_connection import IPConnection
from bricklet_current25 import Current25

# Callback for current greater than 5A
def cb_reached(current):
    print('Current is greater than 5A: ' + str(current/1000.0))

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    c = Current25(UID) # Create device object
    ipcon.add_device(c) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    c.set_debounce_period(10000)

    # Register threshold reached callback to function cb_reached
    c.register_callback(c.CALLBACK_CURRENT_REACHED, cb_reached)

    # Configure threshold for "greater than 5A" (unit is mA)
    c.set_current_callback_threshold('>', 5*1000, 0)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
