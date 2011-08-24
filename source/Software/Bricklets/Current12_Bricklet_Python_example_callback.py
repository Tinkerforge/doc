#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "ABCD" # Change to your UID

from ip_connection import IPConnection
from bricklet_current12 import Current12

# Callback function for current callback (parameter has unit mA)
def cb_current(current):
    print('Current: ' + str(current/1000.0) + ' A')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    c = Current12(UID) # Create device object
    ipcon.add_device(c) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Set Period for current callback to 1s (1000ms)
    # Note: The callback is only called every second if the 
    #       current has changed since the last call!
    c.set_current_callback_period(1000)

    # Register current callback to function cb_current
    c.register_callback(c.CALLBACK_CURRENT, cb_current)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
