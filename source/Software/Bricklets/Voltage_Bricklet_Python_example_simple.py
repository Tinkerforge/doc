#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "ABC" # Change to your UID

from ip_connection import IPConnection
from bricklet_voltage import Voltage

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    v = Voltage(UID) # Create device object
    ipcon.add_device(v) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get current voltage (unit is mV)
    voltage = v.get_voltage()

    print('Voltage: ' + str(voltage/1000.0) + ' V')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
