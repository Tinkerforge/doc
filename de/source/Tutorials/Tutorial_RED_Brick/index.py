#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Temperature Bricklet 2.0

from flask import Flask       # Use Flask framework
application = Flask(__name__) # Function "application" is used by Apache/wsgi
app = application             # Use shortcut for routing

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature_v2 import BrickletTemperatureV2

PAGE = u"""
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<html>
 <head>
  <title>Temperature</title>
 </head>
 <body>
  <p>Temperature: {0} °C<p>
 </body>
</html>
"""

@app.route('/')
def index():
    ipcon = IPConnection() # Create IP connection
    t = BrickletTemperatureV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current temperature (unit is °C/100)
    temperature = t.get_temperature() / 100.0

    ipcon.disconnect()

    return PAGE.format(temperature)
