#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_temperature import Temperature

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    t = Temperature(UID) # Create device object
    ipcon.add_device(t) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get current temperature (unit is °C/100)
    temperature = t.get_temperature()/100.0

    print('Temperature: ' + str(temperature) + ' °C')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
