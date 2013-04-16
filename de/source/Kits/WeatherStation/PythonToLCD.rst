
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Mit Python auf das LCD 20x4 Bricklet schreiben

.. |ref_CALLBACK_ENUMERATE| replace:: :py:attr:`CALLBACK_ENUMERATE <IPConnection.CALLBACK_ENUMERATE>`
.. |ref_CALLBACK_CONNECTED| replace:: :py:attr:`CALLBACK_CONNECTED <IPConnection.CALLBACK_CONNECTED>`
.. |callback| replace:: Callback
.. |ref_enumerate| replace:: :py:func:`enumerate <IPConnection.enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``cb_illuminance``
.. |cb_humidity| replace:: ``cb_humidity``
.. |cb_air_pressure| replace:: ``cb_air_pressure``

.. include:: PythonToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_python_to_lcd:

Mit Python auf das LCD 20x4 Bricklet schreiben
==============================================

.. include:: PythonCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

.. include:: PythonToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Bricks und Bricklets dynamisch erkennen
--------------------------------------------------

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


Schritt 2: Bricklets beim Enumerate initialisieren
--------------------------------------------------

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


Schritt 3: Messwerte auf dem Display anzeigen
---------------------------------------------

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: python

    text = '%6.2f' % value

|step3_printf|

.. code-block:: python

    def cb_illuminance(self, illuminance):
        text = 'Illuminanc %6.2f lx' % (illuminance/10.0)
        self.lcd.write_line(0, 0, text)

    def cb_humidity(self, humidity):
        text = 'Humidity   %6.2f %%' % (humidity/10.0)
        self.lcd.write_line(1, 0, text)

    def cb_air_pressure(self, air_pressure):
        text = 'Air Press %7.2f mb' % (air_pressure/1000.0)
        self.lcd.write_line(2, 0, text)

|step3_temperature|

.. code-block:: python

    def cb_air_pressure(self, air_pressure):
        text = 'Air Press %7.2f mb' % (air_pressure/1000.0)
        self.lcd.write_line(2, 0, text)

        # \xDF == ° on LCD 20x4 charset
        text = 'Temperature %5.2f \xDFC' % (self.baro.get_chip_temperature()/100.0)
        self.lcd.write_line(3, 0, text)

|step3_put_together|

.. code-block:: python

    def cb_illuminance(self, illuminance):
        text = 'Illuminanc %6.2f lx' % (illuminance/10.0)
        self.lcd.write_line(0, 0, text)

    def cb_humidity(self, humidity):
        text = 'Humidity   %6.2f %%' % (humidity/10.0)
        self.lcd.write_line(1, 0, text)

    def cb_air_pressure(self, air_pressure):
        text = 'Air Press %7.2f mb' % (air_pressure/1000.0)
        self.lcd.write_line(2, 0, text)

        # \xDF == ° on LCD 20x4 charset
        text = 'Temperature %5.2f \xDFC' % (self.baro.get_chip_temperature()/100.0)
        self.lcd.write_line(3, 0, text)

|step3_complete|

|step3_suggestions1| |step3_suggestions2_common|

|step3_robust1|

|step3_robust2|


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

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
            text = 'Illuminanc %6.2f lx' % (illuminance/10.0)
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


.. _starter_kit_weather_station_python_to_lcd_step_5:

Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/python/weather_station.py>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/python/weather_station.py
 :language: python
 :tab-width: 4
