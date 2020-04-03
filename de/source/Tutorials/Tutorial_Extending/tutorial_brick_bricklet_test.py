#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID_DC = "XXYYZZ" # Change to the UID of your DC Brick
UID_POTI = "XYZ" # Change to the UID of your Rotary Poti Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_dc import BrickDC
from tinkerforge.bricklet_rotary_poti import BrickletRotaryPoti

dc = None

# Callback function for position callback (parameter has range -150 to 150)
def cb_position(position):
    velocity = 32767 // 2 * position // 150 # Velocity: -32767/32767

    print('Set Position/Velocity: ' + str(position) + '/' + str(velocity))

    dc.set_velocity(velocity)

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection

    dc = BrickDC(UID_DC, ipcon) # Create DC brick device object
    poti = BrickletRotaryPoti(UID_POTI, ipcon) # Create rotary poti device object

    ipcon.connect(HOST, PORT) # Connect to brickd

    poti.set_position_callback_period(50) # set callback period to 50ms
    poti.register_callback(poti.CALLBACK_POSITION, cb_position)

    dc.enable() # Enable motor power
    dc.set_acceleration(0xFFFF) # Full acceleration

    input('Press Enter to exit\n') # Use raw_input() in Python 2

    # Stop motor before disabling motor power
    dc.set_acceleration(16384) # Fast decceleration (50 %/s) for stopping
    dc.set_velocity(0) # Request motor stop
    time.sleep(2) # Wait for motor to actually stop: velocity (100 %) / decceleration (50 %/s) = 2 s
    dc.disable() # Disable motor power

    ipcon.disconnect()
