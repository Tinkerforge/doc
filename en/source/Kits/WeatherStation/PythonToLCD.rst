.. _starter_kit_weather_station_python_to_lcd:

Using Python to write to LCD 20x4 Bricklet
==========================================

For this project we are assuming, that you have a Python environment set up 
and that you have a rudimentary understanding of the Python language.

If you are totally new to either Python itself or to Python in the context of 
Tinkerforge, you should start :ref:`here <TODO>`.

Goals
-----

We are setting the following goals for this project:

* Temperature, ambient light, humidity and air pressure should be shown
  on the LCD20x4 Bricklet,
* the measured values should be updated automatically when they change and
* the measured values should be formated to be easily readable.

Since this project will likely run 24/7, we will also make sure
that the application is as robust towards external influences as possible.
The application should still work when

* Bricklets are exchanged (i.e. we don't rely on UIDs),
* Brick Daemon isn't running or is restarted,
* WIFI Extension is out of range or
* Weather Station is restarted (power loss or accidental USB removal).

In the following we will show step-by-step how this can be achieved.

Step 1: Discover Bricks and Bricklets
-------------------------------------

To start off, we need to define where our program should connect to::

    HOST = "localhost"
    PORT = 4223

If the WIFI Extension is used or if the Brick Daemon is
running on a different PC, you have to exchange "localhost" with the
IP or hostname of the WIFI Extension or PC.

When the program is first initialized, we need to register the enumerate
and connected calllbacks and trigger a first enumerate::

	def __init__(self):
		self.ipcon = IPConnection()
		self.ipcon.connect(WeatherStation.HOST, WeatherStation.PORT)

		self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, 
									 self.cb_enumerate)
		self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED, 
									 self.cb_connected)

		self.ipcon.enumerate()


In the connected callback we need to trigger the enumerate again, if
the reason is an auto reconnect::

	def cb_connected(self, connected_reason):
		if connected_reason == IPConnection.CONNECT_REASON_AUTO_RECONNECT:
			self.ipcon.enumerate()

An auto reconnect means, that the connection to the WIFI Extension or to the
Brick Daemon was lost and could subsequently be established again. In this
case the Bricklets may have lost their configurations and we have to
reconfigure them. Since the configuration is done during the
enumeration process (see below), we have to trigger another enumeration.

Step 1 put together::

    class WeatherStation:
        HOST = "localhost"
        PORT = 4223

        def __init__(self):
            self.ipcon = IPConnection()
            self.ipcon.connect(WeatherStation.HOST, WeatherStation.PORT)

            self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, 
                                         self.cb_enumerate)
            self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED, 
                                         self.cb_connected)

            self.ipcon.enumerate()

        def cb_connected(self, connected_reason):
            if connected_reason == IPConnection.CONNECT_REASON_AUTO_RECONNECT:
                self.ipcon.enumerate()


Step 2: Initialize Bricklets on enumeration
-------------------------------------------

During the enumeration we want to configure all of the weather measuring
Bricklets. Doing this during the enumeration ensures that Bricklets get
reconfigured if they were disconnected or there was a power loss.

The configurations should be performed on first startup 
(ENUMERATION_TYPE_CONNECTED) as well as whenever the enumeration is triggered
externaly by us (ENUMERATION_TYPE_AVAILABLE)::

    def cb_enumerate(self, 
                     uid, connected_uid, position, hardware_version, 
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:

The LCD20x4 configuration is simple, we want the current text cleared and
we want the backlight on::

	if device_identifier == LCD20x4.DEVICE_IDENTIFIER:
		self.lcd = LCD20x4(uid, self.ipcon)
		self.lcd.clear_display()
		self.lcd.backlight_on()

We configure the Ambient Light, Humidity and Barometer Bricklet to
return their respective measurments continuously with a period of
1000ms (1s)::

	elif device_identifier == AmbientLight.DEVICE_IDENTIFIER:
		self.al = AmbientLight(uid, self.ipcon)
		self.al.set_illuminance_callback_period(1000)
		self.al.register_callback(self.al.CALLBACK_ILLUMINANCE, 
								  self.cb_illuminance)
	elif device_identifier == Humidity.DEVICE_IDENTIFIER:
		self.hum = Humidity(uid, self.ipcon)
		self.hum.set_humidity_callback_period(1000)
		self.hum.register_callback(self.hum.CALLBACK_HUMIDITY, 
								   self.cb_humidity)
	elif device_identifier == Barometer.DEVICE_IDENTIFIER:
		self.baro = Barometer(uid, self.ipcon)
		self.baro.set_air_pressure_callback_period(1000)
		self.baro.register_callback(self.baro.CALLBACK_AIR_PRESSURE,
									self.cb_air_pressure)

This means that the Bricklets will call the cb_illuminance, cb_humidity
and cb_air_pressure functions whenever the value has changed, but
with a maximum period of 1000ms.

Step 2 put together::

    def cb_enumerate(self, 
                     uid, connected_uid, position, hardware_version, 
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:
            if device_identifier == LCD20x4.DEVICE_IDENTIFIER:
                self.lcd = LCD20x4(uid, self.ipcon)
                self.lcd.clear_display()
                self.lcd.backlight_on()
            elif device_identifier == AmbientLight.DEVICE_IDENTIFIER:
                self.al = AmbientLight(uid, self.ipcon)
                self.al.set_illuminance_callback_period(1000)
                self.al.register_callback(self.al.CALLBACK_ILLUMINANCE, 
                                          self.cb_illuminance)
            elif device_identifier == Humidity.DEVICE_IDENTIFIER:
                self.hum = Humidity(uid, self.ipcon)
                self.hum.set_humidity_callback_period(1000)
                self.hum.register_callback(self.hum.CALLBACK_HUMIDITY, 
                                           self.cb_humidity)
            elif device_identifier == Barometer.DEVICE_IDENTIFIER:
                self.baro = Barometer(uid, self.ipcon)
                self.baro.set_air_pressure_callback_period(1000)
                self.baro.register_callback(self.baro.CALLBACK_AIR_PRESSURE,
                                            self.cb_air_pressure)


Step 3: Show measurements on display
------------------------------------

We want a neat arrangement of the measurements on the display, such as::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

The decimal marks and the units should be below each other. To achieve this
we use two characters for the unit, two decimal places and crop the name
to use the maximum characters that are left::

    def fmt(self, value, pre, post=2):
        v2, v1 = math.modf(value)
        v1 = str(int(v1))
        v2 = str(int(v2 * 10**post))

        num_space = (pre - len(v1))
        num_zero = (post - len(v2))

        return ' '*num_space + v1 + '.' + v2 + '0'*num_zero

The code above receives a floating point value, extracts the digits before
and after the decimal place and formats it according to the given pre
and post spaces. For the pre spaces we use the digits before the
decimal point and fill the rest with space. For the post spaces we fill
with zeros.

Now we can simply format the values of the callbacks with the fmt function
and write them to the display, one value per line::

    def cb_illuminance(self, illuminance):
		text = 'Illuminanc %s lx' % self.fmt(illuminance/10.0, 3)
		self.lcd.write_line(0, 0, text)

    def cb_humidity(self, humidity):
		text = 'Humidity %s %%' % self.fmt(humidity/10.0, 5)
		self.lcd.write_line(1, 0, text)
 
    def cb_air_pressure(self, air_pressure):
		text = 'Air Press %s mb' % self.fmt(air_pressure/1000.0, 4)
		self.lcd.write_line(2, 0, text)

We are still missing the temperature. The Barometer Bricklet can
measure temperature, but it doesn't have a callback for it. As a
simple workaround we can retrieve the temperature in the cb_air_pressure
callback::

    def cb_air_pressure(self, air_pressure):
		text = 'Air Press %s mb' % self.fmt(air_pressure/1000.0, 4)
		self.lcd.write_line(2, 0, text)

		fmt_text = self.fmt(self.baro.get_chip_temperature()/100.0, 2)
		# \xDF == ° on LCD20x4 charset
		text = 'Temperature %s \xDFC' % fmt_text
		self.lcd.write_line(3, 0, text)

Step 3 put together::

    def fmt(self, value, pre, post=2):
        v2, v1 = math.modf(value)
        v1 = str(int(v1))
        v2 = str(int(v2 * 10**post))

        num_space = (pre - len(v1))
        num_zero = (post - len(v2))

        return ' '*num_space + v1 + '.' + v2 + '0'*num_zero

    def cb_illuminance(self, illuminance):
		text = 'Illuminanc %s lx' % self.fmt(illuminance/10.0, 3)
		self.lcd.write_line(0, 0, text)

    def cb_humidity(self, humidity):
		text = 'Humidity %s %%' % self.fmt(humidity/10.0, 5)
		self.lcd.write_line(1, 0, text)
 
    def cb_air_pressure(self, air_pressure):
		text = 'Air Press %s mb' % self.fmt(air_pressure/1000.0, 4)
		self.lcd.write_line(2, 0, text)

		fmt_text = self.fmt(self.baro.get_chip_temperature()/100.0, 2)
		# \xDF == ° on LCD20x4 charset
		text = 'Temperature %s \xDFC' % fmt_text
		self.lcd.write_line(3, 0, text)

Thats it. If we would copy these three steps together in one file and
execute it, we would have a working Weather Station!

There are some obvious ways to make the output better.
The name could be cropped according to the exact space that is available
(dependent on the number of digits of the measured value). Also, to
read the temperature in the humidity callback is suboptimal. If the
humidity doesn't change, we won't update the temperature. It would be better
to read the temperature in a different thread in an endless loop with a
one second sleep after each read. But we want to keep this code as simple
as possible.

However, we do not meet all of our goals yet. The program is not yet
robust enough. What happens if can't connect on startup? What happens if
the enumerate after an auto reconnect doesn't work?

What we need is error handling!

Step 4: Error handling and Logging
----------------------------------

On startup, we need to try to connect until the connection works::

    while True:
        try:
            self.ipcon.connect(WeatherStation.HOST, WeatherStation.PORT)
            break
        except Error as e:
            log.error('Connection Error: ' + str(e.description))
            time.sleep(1)
        except socket.error as e:
            log.error('Socket error: ' + str(e))
            time.sleep(1)

and we need to try enumerating until the message goes through::

    while True:
        try:
            self.ipcon.enumerate()
            break
        except Error as e:
            log.error('Enumerate Error: ' + str(e.description))
            time.sleep(1)

With these changes it is now possible to first start the program and 
connect the Weather Station afterwards.

We also need to make sure, that we only write to the lcd if it is
already initialized::

    def cb_illuminance(self, illuminance):
        if self.lcd is not None:
            text = 'Helligkeit %s  lx' % self.fmt(illuminance/10.0, 3, 1)
            self.lcd.write_line(0, 0, text)
            log.info('Write to line 0: ' + text)

and that we have to deal with errors during the initialization::

    if device_identifier == LCD20x4.DEVICE_IDENTIFIER:
        try:
            self.lcd = LCD20x4(uid, self.ipcon)
            self.lcd.clear_display()
            self.lcd.backlight_on()
            log.info('LCD20x4 initialized')
        except Error as e:
            log.error('LCD20x4 init failed: ' + str(e.description))
            self.lcd = None

Additionally we added some logging. With the logging we can later find out
what exactly caused a problem, when the Weather Station failed for some
time period.

For example, if we connect to the Weather Station via WIFI and we have
regular auto reconnects, it likely means that the WIFI connection is not
very stable.

.. _starter_kit_weather_station_python_to_lcd_step_5:

Step 5: Everything put together
-------------------------------

Thats it! We are already done with our Weather Station and all of the
goals should be met.

Now all of the above put together (:ref:`download <todo>`)::

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	import socket
	import sys
	import time
	import math
	import logging as log
	log.basicConfig(level=log.INFO)

	from tinkerforge.ip_connection import IPConnection
	from tinkerforge.ip_connection import Error
	from tinkerforge.brick_master import Master
	from tinkerforge.bricklet_lcd_20x4 import LCD20x4
	from tinkerforge.bricklet_ambient_light import AmbientLight
	from tinkerforge.bricklet_humidity import Humidity
	from tinkerforge.bricklet_barometer import Barometer

	class WeatherStation:
		HOST = "localhost"
		PORT = 4223

		ipcon = None
		lcd = None
		al = None
		hum = None
		baro = None

		def __init__(self):
			self.ipcon = IPConnection()
			while True:
				try:
					self.ipcon.connect(WeatherStation.HOST, WeatherStation.PORT)
					break
				except Error as e:
					log.error('Connection Error: ' + str(e.description))
					time.sleep(1)
				except socket.error as e:
					log.error('Socket error: ' + str(e))
					time.sleep(1)

			self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, 
										 self.cb_enumerate)
			self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED, 
										 self.cb_connected)

			while True:
				try:
					self.ipcon.enumerate()
					break
				except Error as e:
					log.error('Enumerate Error: ' + str(e.description))
					time.sleep(1)

		# Format value to fit on LCD with given pre and post digits
		def fmt(self, value, pre, post=2):
			v2, v1 = math.modf(value)
			v1 = str(int(v1))
			v2 = str(int(v2 * 10**post))

			num_space = (pre - len(v1))
			num_zero = (post - len(v2))

			return ' '*num_space + v1 + '.' + v2 + '0'*num_zero

		def cb_illuminance(self, illuminance):
			if self.lcd is not None:
				text = 'Illuminanc %s lx' % self.fmt(illuminance/10.0, 3)
				self.lcd.write_line(0, 0, text)
				log.info('Write to line 0: ' + text)

		def cb_humidity(self, humidity):
			if self.lcd is not None:
				text = 'Humidity %s %%' % self.fmt(humidity/10.0, 5)
				self.lcd.write_line(1, 0, text)
				log.info('Write to line 1: ' + text)
	 
		def cb_air_pressure(self, air_pressure):
			if self.lcd is not None:
				text = 'Air Press %s mb' % self.fmt(air_pressure/1000.0, 4)
				self.lcd.write_line(2, 0, text)
				log.info('Write to line 2: ' + text)

				fmt_text = self.fmt(self.baro.get_chip_temperature()/100.0, 2)
				# \xDF == ° on LCD20x4 charset
				text = 'Temperature %s \xDFC' % fmt_text
				self.lcd.write_line(3, 0, text)
				log.info('Write to line 3: ' + text.replace('\xDF', '°'))

		def cb_enumerate(self, 
						 uid, connected_uid, position, hardware_version, 
						 firmware_version, device_identifier, enumeration_type):
			if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
			   enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:
				if device_identifier == LCD20x4.DEVICE_IDENTIFIER:
					try:
						self.lcd = LCD20x4(uid, self.ipcon)
						self.lcd.clear_display()
						self.lcd.backlight_on()
						log.info('LCD20x4 initialized')
					except Error as e:
						log.error('LCD20x4 init failed: ' + str(e.description))
						self.lcd = None
				elif device_identifier == AmbientLight.DEVICE_IDENTIFIER:
					try:
						self.al = AmbientLight(uid, self.ipcon)
						self.al.set_illuminance_callback_period(1000)
						self.al.register_callback(self.al.CALLBACK_ILLUMINANCE, 
												  self.cb_illuminance)
						log.info('AmbientLight initialized')
					except Error as e:
						log.error('AmbientLight init failed: ' + str(e.description))
						self.al = None
				elif device_identifier == Humidity.DEVICE_IDENTIFIER:
					try:
						self.hum = Humidity(uid, self.ipcon)
						self.hum.set_humidity_callback_period(1000)
						self.hum.register_callback(self.hum.CALLBACK_HUMIDITY, 
												   self.cb_humidity)
						log.info('Humidity initialized')
					except Error as e:
						log.error('Humidity init failed: ' + str(e.description))
						self.hum = None
				elif device_identifier == Barometer.DEVICE_IDENTIFIER:
					try:
						self.baro = Barometer(uid, self.ipcon)
						self.baro.set_air_pressure_callback_period(1000)
						self.baro.register_callback(self.baro.CALLBACK_AIR_PRESSURE,
													self.cb_air_pressure)
						log.info('Barometer initialized')
					except Error as e:
						log.error('Barometer init failed: ' + str(e.description))
						self.baro = None

		def cb_connected(self, connected_reason):
			if connected_reason == IPConnection.CONNECT_REASON_AUTO_RECONNECT:
				while True:
					try:
						self.ipcon.enumerate()
						break
					except Error as e:
						log.error('Enumerate Error: ' + str(e.description))
						time.sleep(1)

	if __name__ == "__main__":
		log.info('Weather Station: Start')

		weather_station = WeatherStation()

		if sys.version_info < (3, 0):
			input = raw_input # Compatibility for Python 2.x
		input('Press key to exit\n')

		if weather_station.ipcon != None:
			weather_station.ipcon.disconnect()

		log.info('Weather Station: End')
