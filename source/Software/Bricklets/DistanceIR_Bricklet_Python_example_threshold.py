#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_distance_ir import DistanceIR

# Callback for distance smaller than 20cm
def cb_reached(distance):
    print('Distance is smaller than 20cm: ' + str(distance/10.0) + ' cm')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    dist = DistanceIR(UID) # Create device object
    ipcon.add_device(dist) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get threshold callbacks with a debounce time of 1 second (1000ms)
    dist.set_debounce_period(1000)

    # Register threshold reached callback to function cb_reached
    dist.register_callback(dist.CALLBACK_DISTANCE_REACHED, cb_reached)

    # Configure threshold for "smaller than 20cm" (unit is mm)
    dist.set_distance_callback_threshold('<', 200, 0)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
