#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "abc" # Change to your UID

from ip_connection import IPConnection
from bricklet_linear_poti import LinearPoti

# Callback function for position callback (parameter has range 0-100)
def cb_position(position):
    print('Position: ' + str(position))

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    poti = LinearPoti(UID) # Create device object
    ipcon.add_device(poti) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Set Period for illuminance callback to 0.05s (50ms)
    # Note: The position callback is only called every 50ms if the 
    #       position has changed since the last call!
    poti.set_position_callback_period(50)

    # Register illuminance callback to function cb_position
    poti.register_callback(poti.CALLBACK_POSITION, cb_position)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
