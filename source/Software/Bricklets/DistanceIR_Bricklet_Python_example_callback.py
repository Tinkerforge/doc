#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_distance_ir import DistanceIR

# Callback function for distance callback (parameter has unit mm)
def cb_distance(distance):
    print('Distance: ' + str(distance/10.0) + ' cm')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    dist = DistanceIR(UID) # Create device object
    ipcon.add_device(dist) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Set Period for distance callback to 0.2s (200ms)
    # Note: The callback is only called every 200ms if the 
    #       distance has changed since the last call!
    dist.set_distance_callback_period(200)

    # Register distance callback to function cb_distance
    dist.register_callback(dist.CALLBACK_DISTANCE, cb_distance)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
