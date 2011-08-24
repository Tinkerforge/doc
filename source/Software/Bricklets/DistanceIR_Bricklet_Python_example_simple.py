#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_distance_ir import DistanceIR

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    dist = DistanceIR(UID) # Create device object
    ipcon.add_device(dist) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get current distance (unit is mm)
    distance = dist.get_distance()

    print('Distance: ' + str(distance/10.0) + ' cm')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
