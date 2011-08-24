#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
DC_UID = "V"

from ip_connection import IPConnection
from brick_dc import DC

import time

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT)
    dc = DC(DC_UID)
    ipcon.add_device(dc)

    dc.enable()

    dc.set_acceleration(10000)

    dc.set_velocity(30000)
    time.sleep(3)

    dc.set_velocity(0)
    time.sleep(3)
    
    ipcon.destroy()
