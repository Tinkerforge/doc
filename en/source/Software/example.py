#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223

from tinkerforge.ip_connection import IPConnection

# Print incoming enumeration
def cb_enumerate(uid, connected_uid, position, hardware_version, firmware_version, device_identifier, enumeration_type):
    print("uid:               " + uid)
    print("enumeration_type:  " + str(enumeration_type))
    if enumeration_type == IPConnection.ENUMERATION_TYPE_DISCONNECTED:
        return

    print("connected_uid:     " + connected_uid)
    print("position:          " + position)
    print("hardware_version:  " + str(hardware_version))
    print("firmware_version:  " + str(firmware_version))
    print("device_identifier: " + str(device_identifier))

if __name__ == "__main__":
    # Create connection and connect to brickd
    ipcon = IPConnection()
    ipcon.connect(HOST, PORT)

    # Register Enumerate Callback
    ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, cb_enumerate)

    raw_input('Press key to exit\n') # Use input() in Python 3
