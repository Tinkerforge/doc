#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_ambient_light import AmbientLight

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    al = AmbientLight(UID) # Create device object
    ipcon.add_device(al) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get current illuminance (unit is Lux/10)
    illuminance = al.get_illuminance()/10.0

    print('Illuminance: ' + str(illuminance) + ' Lux')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
