
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starter Kit: Weather Station</a> / Using Python to write to LCD 20x4 Bricklet

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

To start off, we need to define where our program should connect to:

.. code-block:: python

    HOST = "localhost"
    PORT = 4223

If the WIFI Extension is used or if the Brick Daemon is
running on a different PC, you have to exchange "localhost" with the
IP address or hostname of the WIFI Extension or PC.

When the program is first initialized, we need to register the enumerate
and connected callbacks and trigger a first enumerate:

.. code-block:: python

    def __init__(self):
        self.ipcon = IPConnection()
        self.ipcon.connect(WeatherStation.HOST, WeatherStation.PORT)

        self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE,
                                     self.cb_enumerate)
        self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED,
                                     self.cb_connected)

        self.ipcon.enumerate()

The enumerate callback is triggered if a Brick gets connected over USB or if
the enumerate function is called. This allows to discover the Bricks and
Bricklets in a stack without knowing their types or UIDs beforehand.

The connected callback is triggered if the connection to the WIFI Extension or
to the Brick Daemon got established. In this callback we need to trigger the
enumerate again, if the reason is an auto reconnect:

.. code-block:: python

    def cb_connected(self, connected_reason):
        if connected_reason == IPConnection.CONNECT_REASON_AUTO_RECONNECT:
            self.ipcon.enumerate()

An auto reconnect means, that the connection to the WIFI Extension or to the
Brick Daemon was lost and could subsequently be established again. In this
case the Bricklets may have lost their configurations and we have to
reconfigure them. Since the configuration is done during the
enumeration process (see below), we have to trigger another enumeration.

Step 1 put together:

.. code-block:: python

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
(``ENUMERATION_TYPE_CONNECTED``) as well as whenever the enumeration is triggered
externaly by us (``ENUMERATION_TYPE_AVAILABLE``):

.. code-block:: python

    def cb_enumerate(self, uid, connected_uid, position, hardware_version,
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:

The LCD20x4 configuration is simple, we want the current text cleared and
we want the backlight on:

.. code-block:: python

            if device_identifier == LCD20x4.DEVICE_IDENTIFIER:
                self.lcd = LCD20x4(uid, self.ipcon)
                self.lcd.clear_display()
                self.lcd.backlight_on()

We configure the Ambient Light, Humidity and Barometer Bricklet to
return their respective measurements continuously with a period of
1000ms (1s):

.. code-block:: python

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

This means that the Bricklets will call the ``cb_illuminance``, ``cb_humidity``
and ``cb_air_pressure`` functions whenever the value has changed, but
with a maximum period of 1000ms.

Step 2 put together:

.. code-block:: python

    def cb_enumerate(self, uid, connected_uid, position, hardware_version,
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
to use the maximum characters that are left. That's why "Illuminanc" is missing
its final "e".

.. code-block:: python

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

Now we can simply format the values of the callbacks with the ``fmt`` function
and write them to the display, one value per line:

.. code-block:: python

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
simple workaround we can retrieve the temperature in the ``cb_air_pressure``
callback:

.. code-block:: python

    def cb_air_pressure(self, air_pressure):
        text = 'Air Press %s mb' % self.fmt(air_pressure/1000.0, 4)
        self.lcd.write_line(2, 0, text)

        fmt_text = self.fmt(self.baro.get_chip_temperature()/100.0, 2)
        # \xDF == ° on LCD20x4 charset
        text = 'Temperature %s \xDFC' % fmt_text
        self.lcd.write_line(3, 0, text)

Step 3 put together:

.. code-block:: python

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

That's it. If we would copy these three steps together in one file and
execute it, we would have a working Weather Station!

There are some obvious ways to make the output better.
The name could be cropped according to the exact space that is available
(depending on the number of digits of the measured value). Also,
reading the temperature in the air pressure callback is suboptimal. If the
air pressure doesn't change, we won't update the temperature. It would be better
to read the temperature in a different thread in an endless loop with a
one second sleep after each read. But we want to keep this code as simple
as possible.

However, we do not meet all of our goals yet. The program is not yet
robust enough. What happens if can't connect on startup? What happens if
the enumerate after an auto reconnect doesn't work?

What we need is error handling!

Step 4: Error handling and Logging
----------------------------------

On startup, we need to try to connect until the connection works:

.. code-block:: python

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

and we need to try enumerating until the message goes through:

.. code-block:: python

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
already initialized:

.. code-block:: python

    def cb_illuminance(self, illuminance):
        if self.lcd is not None:
            text = 'Helligkeit %s  lx' % self.fmt(illuminance/10.0, 3, 1)
            self.lcd.write_line(0, 0, text)
            log.info('Write to line 0: ' + text)

and that we have to deal with errors during the initialization:

.. code-block:: python

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

For example, if we connect to the Weather Station via Wi-Fi and we have
regular auto reconnects, it likely means that the Wi-Fi connection is not
very stable.

.. _starter_kit_weather_station_python_to_lcd_step_5:

Step 5: Everything put together
-------------------------------

That's it! We are already done with our Weather Station and all of the
goals should be met.

Now all of the above put together (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/python/weather.py>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/python/weather.py
 :language: python
 :linenos:
 :tab-width: 4
