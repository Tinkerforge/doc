#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "2wx" # Change to your UID

from ip_connection import IPConnection
from bricklet_rotary_poti import RotaryPoti

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    poti = RotaryPoti(UID) # Create device object
    ipcon.add_device(poti) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get current position of poti (return value has range -150 to 150)
    position = poti.get_position()

    print('Position: ' + str(position))

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
