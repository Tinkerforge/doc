
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starter Kit: Weather Station</a> / Using Visual Basic .NET to write to LCD 20x4 Bricklet

.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``IlluminanceCB``
.. |cb_humidity| replace:: ``HumidityCB``
.. |cb_air_pressure| replace:: ``AirPressureCB``

.. include:: VBNETToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_vbnet_to_lcd:

Using Visual Basic .NET to write to LCD 20x4 Bricklet
=====================================================

.. include:: VBNETToLCD.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: VBNETToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Discover Bricks and Bricklets
-------------------------------------

|step1_start_off|

.. code-block:: python

    HOST = "localhost"
    PORT = 4223

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: python

    def __init__(self):
        self.ipcon = IPConnection()
        self.ipcon.connect(WeatherStation.HOST, WeatherStation.PORT)

        self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE,
                                     self.cb_enumerate)
        self.ipcon.register_callback(IPConnection.CALLBACK_CONNECTED,
                                     self.cb_connected)

        self.ipcon.enumerate()

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: python

    def cb_connected(self, connected_reason):
        if connected_reason == IPConnection.CONNECT_REASON_AUTO_RECONNECT:
            self.ipcon.enumerate()

|step1_auto_reconnect_callback|

|step1_put_together|

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


Step 2: Initialize Bricklets on Enumeration
-------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: python

    def cb_enumerate(self, uid, connected_uid, position, hardware_version,
                     firmware_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_CONNECTED or \
           enumeration_type == IPConnection.ENUMERATION_TYPE_AVAILABLE:

|step2_lcd_config|

.. code-block:: python

            if device_identifier == LCD20x4.DEVICE_IDENTIFIER:
                self.lcd = LCD20x4(uid, self.ipcon)
                self.lcd.clear_display()
                self.lcd.backlight_on()

|step2_other_config1|

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

|step2_other_config2|

|step2_put_together|

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

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: vbnet

    Dim text As String = String.Format("{0,6:###.00}", value)

|step3_printf|

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

|step3_temperature|

.. code-block:: python

    def cb_air_pressure(self, air_pressure):
        text = 'Air Press %s mb' % self.fmt(air_pressure/1000.0, 4)
        self.lcd.write_line(2, 0, text)

        fmt_text = self.fmt(self.baro.get_chip_temperature()/100.0, 2)
        # \xDF == ° on LCD20x4 charset
        text = 'Temperature %s \xDFC' % fmt_text
        self.lcd.write_line(3, 0, text)

|step3_put_together|

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

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Step 4: Error handling and Logging
----------------------------------

|step4_intro1|

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

|step4_intro2|

.. code-block:: python

    while True:
        try:
            self.ipcon.enumerate()
            break
        except Error as e:
            log.error('Enumerate Error: ' + str(e.description))
            time.sleep(1)

|step4_connect_afterwards|

|step4_lcd_initialized1|

.. code-block:: python

    def cb_illuminance(self, illuminance):
        if self.lcd is not None:
            text = 'Helligkeit %s  lx' % self.fmt(illuminance/10.0, 3, 1)
            self.lcd.write_line(0, 0, text)
            log.info('Write to line 0: ' + text)

|step4_lcd_initialized2|

.. code-block:: python

    if device_identifier == AmbientLight.DEVICE_IDENTIFIER:
        try:
            self.al = AmbientLight(uid, self.ipcon)
            self.al.set_illuminance_callback_period(1000)
            self.al.register_callback(self.al.CALLBACK_ILLUMINANCE,
                                      self.cb_illuminance)
            log.info('AmbientLight initialized')
        except Error as e:
            log.error('AmbientLight init failed: ' + str(e.description))
            self.al = None

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/vbnet/WeatherStation.vb>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/vbnet/WeatherStation.vb
 :language: vbnet
 :linenos:
 :tab-width: 4
