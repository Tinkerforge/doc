#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_io4 import IO4

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    io = IO4(UID) # Create device object
    ipcon.add_device(io) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Set pin 1 to output low
    io.set_configuration(1 << 1, 'o', False)

    # Set pin 2 and 3 to output high
    io.set_configuration((1 << 2) | (1 << 3), 'o', True)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
