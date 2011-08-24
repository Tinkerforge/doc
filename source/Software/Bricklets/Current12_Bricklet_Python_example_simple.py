#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "ABCD" # Change to your UID

from ip_connection import IPConnection
from bricklet_current12 import Current12

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    c = Current12(UID) # Create device object
    ipcon.add_device(c) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get current current (unit is mA)
    current = c.get_current()

    print('Current: ' + str(current/1000.0) + ' A')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
