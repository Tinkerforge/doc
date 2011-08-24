#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "abcde" # Change to your UID

from ip_connection import IPConnection
from bricklet_temperature_ir import TemperatureIR

# Callback functions for object/ambient temperature callbacks 
# (parameters have unit °C/10)
def cb_object(temperature):
    print('Object Temperature: ' + str(temperature/10.0) + ' °C')

def cb_ambient(temperature):
    print('Ambient Temperature: ' + str(temperature/10.0) + ' °C')

if __name__ == "__main__":
    ipcon = IPConnection(HOST, PORT) # Create ip connection to brickd

    tir = TemperatureIR(UID) # Create device object
    ipcon.add_device(tir) # Add device to ip connection
    # Don't use device before it is added to a connection

    # Set Period for temperature callbacks to 1s (1000ms)
    # Note: The callbacks are only called every second if the 
    #       value has changed since the last call!
    tir.set_object_temperature_callback_period(1000)
    tir.set_ambient_temperature_callback_period(1000)

    # Register object temperature callback to function cb_object
    tir.register_callback(tir.CALLBACK_OBJECT_TEMPERATURE, cb_object)
    # Register ambient temperature callback to function cb_ambient
    tir.register_callback(tir.CALLBACK_AMBIENT_TEMPERATURE, cb_ambient)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.destroy()
