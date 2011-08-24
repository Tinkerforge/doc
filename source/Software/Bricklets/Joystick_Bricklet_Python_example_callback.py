#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "abcd" # Change to your UID

from ip_connection import IPConnection
from bricklet_joystick import Joystick

# Callback function for pressed and released events 
def cb_pressed():
    print('Pressed')

def cb_released():
    print('Released')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    js = Joystick(UID) # Create device object
    ipcon.add_device(js) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Register callbacks for pressed and released events
    js.register_callback(js.CALLBACK_PRESSED, cb_pressed)
    js.register_callback(js.CALLBACK_RELEASED, cb_released)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
