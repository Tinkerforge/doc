#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "aySDPqVAkmw" # Change to your UID

from ip_connection import IPConnection
from brick_servo import Servo

servo = Servo(UID) # Create device object

# Use position reached callback to swing back and forth
def cb_reached(servo_num, position):
    if position == 9000:
        print('Position: 90°, going to -90°')
        servo.set_position(servo_num, -9000)
    elif position == -9000:
        print('Position: -90°, going to 90°')
        servo.set_position(servo_num, 9000)
    else:
        print('Error') # Can only happen if another program sets position

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd
    ipcon.add_device(servo) # Add device to ip connection
    # Don't use device before it is added to a connection


    # Register "position reached callback" to cb_reached
    # cb_reached will be called every time a position set with
    # set_position is reached
    servo.register_callback(servo.CALLBACK_POSITION_REACHED, cb_reached)

    # Set velocity to 100°/s. This has to be smaller or equal to 
    # maximum velocity of the servo, otherwise cb_reached will be
    # called too early
    servo.set_velocity(0, 10000) 
    servo.set_position(0, 9000)
    servo.enable(0)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
