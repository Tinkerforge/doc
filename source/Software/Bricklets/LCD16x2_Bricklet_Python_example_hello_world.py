#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_lcd_16x2 import LCD16x2

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    lcd = LCD16x2(UID) # Create device object
    ipcon.add_device(lcd) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Turn backlight on
    lcd.backlight_on()

    # Write "Hello World"
    lcd.write_line(0, 0, 'Hello World')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
