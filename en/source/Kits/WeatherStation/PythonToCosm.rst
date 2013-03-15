.. _starter_kit_weather_station_cosm:

Using Python to upload weather measurements to Cosm
===================================================

For this project we are assuming, that you have a Python environment set up 
and that you have a rudimentary understanding of the Python language.

If you are totally new to either Python itself or to Python in the context of 
Tinkerforge, you should start :ref:`here <TODO>`.

Goals
-----

We are setting the following goals for this project:

* The weather measurements should be calculated and shown on the LCD20x4 Bricklet, as in the :ref:`Write environment measurements to LCD project <starter_kit_weather_station_python_to_lcd>`. 
* The measurments should additionally be stored and uploaded to Cosm in 5 minute intervals.

In the following we will show step-by-step how this can be achieved.

Step 1: Create and configure Cosm account
-----------------------------------------

To use Cosm, we first have to create a Cosm account. 
Got to `http://www.cosm.com <http://www.cosm.com>`__ and sign up.

Click on "+ Device/Feed" and as type choose "Something Else". 
Choose "push data to Cosm", a title and tags and create the feed.

In the feed we have to add datastreams for our weather measurements:

.. image:: /Images/Kits/weather_station_cosm_datastreams.jpg
   :scale: 50 %
   :alt: Cosm datastream configuration
   :align: center
   :target: ../../_images/Kits/weather_station_cosm_datastreams.jpg

The streams got the IDs AirPressure, AmbientLight, Humidity and Temperature.
Later we will need these IDs to upload measurements.

Step 2: Understanding Cosm protocol
-----------------------------------

A quick search in the Cosm API documentation reveals that we can update
a datastream by `just sending a small json package <https://cosm.com/docs/v2/datastream/update.html>`__.

The given example is::

 {
  "current_value":"294",
  "max_value":"697.0",
  "min_value":"0.0",
  "id":"1"
 }

which can be send via HTTP PUT to "http://api.cosm.com/v2/feeds/<ID>". The
API key is put in the header of the HTTP request and the return consists of
an HTTP header only.

This seems quite straight forward. To not spam Cosm, we should limit the uploading
interval to once every 5 minutes. This means, that we need to store the
measurements and determine the corresponding
min and max values for each interval.

Step 3: Storing measurements
----------------------------

To start off, we create a simple value storage. To identify the
values, we use the ID that was configured in the Cosm account as
the Datastream ID::

    class Cosm:
        def __init__(self):
            self.items = {}

        def put(self, identifier, value):
            try:
                _, min_value, max_value = self.items[identifier]
                if value < min_value:
                    min_value = value
                if value > max_value:
                    max_value = value
                self.items[identifier] = (value, min_value, max_value)
            except:
                self.items[identifier] = (value, value, value)

We retrieve the old value, min_value and max_value, calculate the new
min/max and update it. If there aren't any values stored for a given
identifier, we catch the occuring exception and add the identifier
as a new key to the dict.

The Weather Station code itself we can base on the code from the
:ref:`Write environment measurements to LCD project <starter_kit_weather_station_python_to_lcd_step_5>`

We just have to use the put function whenever a new measurement arrives::

    class WeatherStation:
        # [...]
        def __init__(self):
            # [...]
            self.cosm = Cosm()
            # [...]

        # [...]
        def cb_illuminance(self, illuminance):
            if self.lcd is not None:
                text = 'Illuminanc %s lx' % self.fmt(illuminance/10.0, 3)
                self.lcd.write_line(0, 0, text)

                # Here we add illuminance to cosm with ID "AmbientLight"
                self.cosm.put('AmbientLight', illuminance/10.0) 
                log.info('Write to line 0: ' + text)
        # [...]

This has to be added for the other measurments accordingly.

Step 4: Uploading measurements
------------------------------

To upload our measurements we first have to define all of the names, urls, 
keys and so on::

    class Cosm:
        HOST = 'api.cosm.com'
        AGENT = "Tinkerforge cosm 1.0"
        FEED = '105813.json'
        API_KEY = 'WtXx2m6ItNZyFYoQyr5qnoN1GsOSAKxPMGdIaXRLYzY5ND0g'
     
        def __init__(self):
            self.items = {}
            self.headers = {
                "Content-Type"  : "application/x-www-form-urlencoded",
                "X-ApiKey"      : Cosm.API_KEY,
                "User-Agent"    : Cosm.AGENT,
            }
            self.params = "/v2/feeds/" + str(Cosm.FEED)
            threading.Thread(target=self.upload).start()

You have to exchange the FEED and API_KEY values by your own Cosm
feed and key. Everything else is practically copied from the
Cosm documentation.

To make uploads in equidistant 5 minute intervals, we are starting the
upload function in a thread::

    def upload(self):
        while True:
            time.sleep(5*60) # Upload data every 5min
            if len(self.items) == 0:
                continue

            stream_items = []
            for identifier, value in self.items.items():
                stream_items.append({'id': identifier, 
                                     'current_value': value[0], 
                                     'min_value': value[1], 
                                     'max_value': value[2]})
     
            data = {
              'version' : '1.0.0',
              'datastreams': stream_items,
            }
            self.items = {}
            body = json.dumps(data)

            http = httplib.HTTPSConnection(Cosm.HOST)
            http.request('PUT', self.params, body, self.headers)
            response = http.getresponse()
            http.close()

            if response.status != 200:
                log.error('Could not upload to cosm -> ' + 
                          str(response.status) + ': ' + response.reason)

Here we take the data that was gathered, package it in the json format and
send a HTTP PUT request with the data and the header that was defined in
__init__. We also parse the response code and log it if something went wrong.

Step 5: Everything put together
-------------------------------

We are done! There is of course still room for improvement. For example the
uploading and adding of data could be protected by a mutex to ensure that we
don't add data while it is uploaded and thus remove the newly added data
after the uploading finished.

But if you put everything of the above together, you have a working 
Weather Station that uploads the weather measurements to Cosm
(:ref:`download <todo>`)::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import socket
    import sys
    import time
    import math
    import logging as log
    import httplib
    import json
    import threading
    log.basicConfig(level=log.INFO)

    from tinkerforge.ip_connection import IPConnection
    from tinkerforge.ip_connection import Error
    from tinkerforge.brick_master import Master
    from tinkerforge.bricklet_lcd_20x4 import LCD20x4
    from tinkerforge.bricklet_ambient_light import AmbientLight
    from tinkerforge.bricklet_humidity import Humidity
    from tinkerforge.bricklet_barometer import Barometer

    class Cosm:
        HOST = 'api.cosm.com'
        AGENT = "Tinkerforge cosm 1.0"
        FEED = '105813.json'
        API_KEY = 'WtXx2m6ItNZyFYoQyR5qnoN1GsOSAKxPMGdIaXRLYzY5ND0g'
     
        def __init__(self):
            self.items = {}
            self.headers = {
                "Content-Type"  : "application/x-www-form-urlencoded",
                "X-ApiKey"      : Cosm.API_KEY,
                "User-Agent"    : Cosm.AGENT,
            }
            self.params = "/v2/feeds/" + str(Cosm.FEED)
            threading.Thread(target=self.upload).start()

        def put(self, identifier, value):
            try:
                _, min_value, max_value = self.items[identifier]
                if value < min_value:
                    min_value = value
                if value > max_value:
                    max_value = value
                self.items[identifier] = (value, min_value, max_value)
            except:
                self.items[identifier] = (value, value, value)

        def upload(self):
            while True:
                time.sleep(5*60) # Upload data every 5min
                if len(self.items) == 0:
                    continue

                stream_items = []
                for identifier, value in self.items.items():
                    stream_items.append({'id': identifier, 
                                         'current_value': value[0], 
                                         'min_value': value[1], 
                                         'max_value': value[2]})
         
                data = {
                  'version' : '1.0.0',
                  'datastreams': stream_items,
                }
                self.items = {}
                body = json.dumps(data)

                http = httplib.HTTPSConnection(Cosm.HOST)
                http.request('PUT', self.params, body, self.headers)
                response = http.getresponse()
                http.close()

                if response.status != 200:
                    log.error('Could not upload to cosm -> ' + 
                              str(response.status) + ': ' + response.reason)

    class WeatherStation:
        HOST = "localhost"
        PORT = 4223

        ipcon = None
        lcd = None
        al = None
        hum = None
        baro = None

        def __init__(self):
            self.cosm = Cosm()
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
                self.cosm.put('AmbientLight', illuminance/10.0)
                log.info('Write to line 0: ' + text)

        def cb_humidity(self, humidity):
            if self.lcd is not None:
                text = 'Humidity %s %%' % self.fmt(humidity/10.0, 5)
                self.lcd.write_line(1, 0, text)
                self.cosm.put('Humidity', humidity/10.0)
                log.info('Write to line 1: ' + text)
     
        def cb_air_pressure(self, air_pressure):
            if self.lcd is not None:
                text = 'Air Press %s mb' % self.fmt(air_pressure/1000.0, 4)
                self.lcd.write_line(2, 0, text)
                self.cosm.put('AirPressure', air_pressure/1000.0)
                log.info('Write to line 2: ' + text)

                temperature = self.baro.get_chip_temperature()/100.0
                fmt_text = self.fmt(temperature, 2)
                # \xDF == ° on LCD20x4 charset
                text = 'Temperature %s \xDFC' % fmt_text
                self.lcd.write_line(3, 0, text)
                self.cosm.put('Temperature', temperature)
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
            raw_input('Press key to exit\n') # Use input() in Python 3
        else:
            input('Press key to exit\n') # Use input() in Python 3

        if weather_station.ipcon != None:
            weather_station.ipcon.disconnect()

        log.info('Weather Station: End')
