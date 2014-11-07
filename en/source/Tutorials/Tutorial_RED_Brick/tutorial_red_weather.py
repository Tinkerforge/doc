#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID_LCD = "gTu" # Enter LCD UID here
UID_BAROMETER = "k6W" # Enter Barometer UID here
LOCATION = u"Stukenbrock" # Enter you city here

import pywapi
import types
from unidecode import unidecode
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_barometer import Barometer
from tinkerforge.bricklet_lcd_20x4 import LCD20x4

def cb_airpressure(airpressure):

    # get weather data from weather.com
    location_id = pywapi.get_location_ids(LOCATION).keys()[0]
    weather_com_result = pywapi.get_weather_from_weather_com(location_id)
    weather_com_conditions = "It is " + weather_com_result['current_conditions']['text'].lower()
    weather_com_temperature = u"" + weather_com_result['current_conditions']['temperature']

    # display general weather conditions
    lcd.write_line(0,0, weather_com_conditions)

    # display temperature status
    lcd.write_line(1,0, weather_com_temperature)
    lcd.write_line(1,len(weather_com_temperature)+1, chr(0xdf)) #°
    lcd.write_line(1,len(weather_com_temperature)+2, "C")

    # display measured airpressure
    airpressure_str = "%6.2f" % (airpressure/1000.0)
    lcd.write_line(2, 0, airpressure_str + " mbar")

    print "update lcd"


if __name__=="__main__":
    ipcon = IPConnection()
    baro = Barometer(UID_BAROMETER, ipcon)
    lcd = LCD20x4(UID_LCD, ipcon)

    ipcon.connect(HOST, PORT)

    baro.register_callback(baro.CALLBACK_AIR_PRESSURE, cb_airpressure)
    baro.set_air_pressure_callback_period(2000) # 2 seconds period
    lcd.backlight_on()
    lcd.clear_display()

    print "initialization complete"

    raw_input("Press key to exit\n")
    ipcon.disconnect()
