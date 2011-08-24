#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "aySDPZAhvvd" # Change to your UID

from ip_connection import IPConnection
from brick_master import Master

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brick

    master = Master(UID) # Create device object
    ipcon.add_device(master) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get voltage and current from stack (in mV/mA)
    voltage = master.get_stack_voltage()
    current = master.get_stack_current()

    print('Stack Voltage: ' + str(voltage/1000.0) + ' V')
    print('Stack Current: ' + str(current/1000.0) + ' A')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
