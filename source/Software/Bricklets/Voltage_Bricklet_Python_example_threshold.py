#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "ABC" # Change to your UID

from ip_connection import IPConnection
from bricklet_voltage import Voltage

# Callback for voltage smaller than 5V
def cb_reached(voltage):
    print('Voltage dropped below 5V: ' + str(voltage/1000.0))

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    v = Voltage(UID) # Create device object
    ipcon.add_device(v) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    v.set_debounce_period(10000)

    # Register threshold reached callback to function cb_reached
    v.register_callback(v.CALLBACK_VOLTAGE_REACHED, cb_reached)

    # Configure threshold for "smaller than 5V" (unit is mV)
    v.set_voltage_callback_threshold('<', 5*1000, 0)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
