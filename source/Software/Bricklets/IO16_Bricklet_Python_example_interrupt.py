#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_io16 import IO16

# Callback function for interrupts
def cb_interrupt(port, interrupt_mask, value_mask):
    print('Interrupt on port: ' + port)
    print('Interrupt by: ' + str(bin(interrupt_mask)))
    print('Value: ' + str(bin(value_mask)))

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    io = IO16(UID) # Create device object
    ipcon.add_device(io) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Enable interrupt on pin 2 of port a 
    io.set_port_interrupt('a', 1 << 2)

    # Register callback for interrupts
    io.register_callback(io.CALLBACK_INTERRUPT, cb_interrupt)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
