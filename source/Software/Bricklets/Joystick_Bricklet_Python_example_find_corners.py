#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "abcd" # Change to your UID

from ip_connection import IPConnection
from bricklet_joystick import Joystick

# Callback for x and y position outside of -99, 99
def cb_reached(x, y):
    if x == 100 and y == 100:
        print('Top Right')
    elif x == -100 and y == 100:
        print('Top Left')
    elif x == -100 and y == -100:
        print('Bottom Left')
    elif x == 100 and y == -100:
        print('Bottom Right')
    else:
        # This can't happen, the threshold is configured to:
        # "outside of -99, 99"
        print('Error')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    js = Joystick(UID) # Create device object
    ipcon.add_device(js) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Get threshold callbacks with a debounce time of 0.2 seconds (200ms)
    js.set_debounce_period(200)

    # Register threshold reached callback to function cb_reached
    js.register_callback(js.CALLBACK_POSITION_REACHED, cb_reached)

    # Configure threshold for "x and y value outside of -99 and 99"
    js.set_position_callback_threshold('o', -99, 99, -99, 99)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
