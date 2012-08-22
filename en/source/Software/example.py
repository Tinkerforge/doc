#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223

from tinkerforge.ip_connection import IPConnection

def cb_enumerate(uid, name, stack_id, is_new):
    if is_new:
        print("New device:")
    else:
        print("Removed device:")

    print(" Name:     " + name)
    print(" UID:      " + uid)
    print(" Stack ID: " + str(stack_id))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create IP connection to brickd
    ipcon.enumerate(cb_enumerate) # Enumerate Bricks and Bricklets

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
