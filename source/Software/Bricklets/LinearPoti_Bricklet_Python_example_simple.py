#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "abc" # Change to your UID

from ip_connection import IPConnection
from bricklet_linear_poti import LinearPoti

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    poti = LinearPoti(UID) # Create device object
    ipcon.add_device(poti) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get current position of poti (return value has range 0-100)
    position = poti.get_position()

    print('Position: ' + str(position))

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
