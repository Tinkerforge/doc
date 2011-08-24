#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
JOYSTICK_UID = "bastian"

from ip_connection import IPConnection
from bricklet_joystick import Joystick
import time

def callback_enumerate(uid, stack_id, name, is_new):
    print("{0}: {1} {2} {3}".format(name, uid, stack_id, is_new))

def callback_position(pos):
    print("pos: {0}".format(pos))

def callback_analog(ana):
    print("ana: {0}".format(ana))

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT)
    ipcon.enumerate(callback_enumerate)

    joystick = Joystick(JOYSTICK_UID)
    ipcon.add_device(joystick)

    while True:
        print joystick.is_pressed()
        time.sleep(1)

    raw_input()
    ipcon.destroy()
