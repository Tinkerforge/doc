#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from ip_connection import IPConnection
from bricklet_lcd_16x2 import LCD16x2

# Callback functions for button status
def cb_pressed(i):
    print('Pressed: ' + str(i))

def cb_released(i):
    print('Released: ' + str(i))

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    lcd = LCD16x2(UID) # Create device object
    ipcon.add_device(lcd) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Register button status callbacks to cb_pressed and cb_released
    lcd.register_callback(lcd.CALLBACK_BUTTON_PRESSED, cb_pressed)
    lcd.register_callback(lcd.CALLBACK_BUTTON_RELEASED, cb_released)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
