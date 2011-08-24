#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
MASTER_UID = "aySDPZAhvvd"

from ip_connection import IPConnection
from brick_master import Master

import time

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT)
    master = Master(MASTER_UID)
    ipcon.add_device(master)

    print("Calibrate 1")
    time.sleep(2)
    ipcon.adc_calibrate(master, 'd')

    print("Calibrate 2")
    time.sleep(2)
    ipcon.adc_calibrate(master, 'd')

    time.sleep(2)
    print("Offset, Gain: ", ipcon.get_adc_calibration(master))
    ipcon.destroy()
