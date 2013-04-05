
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starter Kit: Weather Station</a> / Using C to write to LCD 20x4 Bricklet

.. |ENUMERATION_TYPE_CONNECTED| replace:: ``IPCON_ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``IPCON_ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``cb_illuminance``
.. |cb_humidity| replace:: ``cb_humidity``
.. |cb_air_pressure| replace:: ``cb_air_pressure``

.. include:: CToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_c_to_lcd:

Using C to write to LCD 20x4 Bricklet
=====================================

.. include:: CToLCD.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: CToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Discover Bricks and Bricklets
-------------------------------------

|step1_start_off|

.. code-block:: c

    #define HOST "localhost"
    #define PORT 4223

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: c

    typedef struct {
        IPConnection ipcon;
    } WeatherStation;

    int main() {
        WeatherStation ws;
        ipcon_create(&ws.ipcon);
        ipcon_connect(&ws.ipcon, HOST, PORT);

        ipcon_register_callback(&ws.ipcon,
                                IPCON_CALLBACK_ENUMERATE,
                                (void *)cb_enumerate,
                                (void *)&ws);
        ipcon_register_callback(&ws.ipcon,
                                IPCON_CALLBACK_CONNECTED,
                                (void *)cb_connected,
                                (void *)&ws);

        ipcon_enumerate(&ws.ipcon);
        return 0;
    }

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: c

    void cb_connected(uint8_t connected_reason, void *user_data) {
        WeatherStation *ws = (WeatherStation *)user_data;

        if(connected_reason == IPCON_CONNECT_REASON_AUTO_RECONNECT) {
            ipcon_enumerate(&ws->ipcon);
        }
    }

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: c

    typedef struct {
        IPConnection ipcon;
    } WeatherStation;

    void cb_connected(uint8_t connected_reason, void *user_data) {
        WeatherStation *ws = (WeatherStation *)user_data;

        if(connected_reason == IPCON_CONNECT_REASON_AUTO_RECONNECT) {
            ipcon_enumerate(&ws->ipcon);
        }
    }

    int main() {
        WeatherStation ws;
        ipcon_create(&ws.ipcon);
        ipcon_connect(&ws.ipcon, HOST, PORT);

        ipcon_register_callback(&ws.ipcon,
                                IPCON_CALLBACK_ENUMERATE,
                                (void *)cb_enumerate,
                                (void *)&ws);
        ipcon_register_callback(&ws.ipcon,
                                IPCON_CALLBACK_CONNECTED,
                                (void *)cb_connected,
                                (void *)&ws);

        ipcon_enumerate(&ws.ipcon);
        return 0;
    }


Step 2: Initialize Bricklets on Enumeration
-------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: c

    void cb_enumerate(const char *uid, const char *connected_uid,
                      char position, uint8_t hardware_version[3],
                      uint8_t firmware_version[3], uint16_t device_identifier,
                      uint8_t enumeration_type, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;

        if(enumeration_type == IPCON_ENUMERATION_TYPE_CONNECTED ||
           enumeration_type == IPCON_ENUMERATION_TYPE_AVAILABLE) {

|step2_lcd_config|

.. code-block:: c

    if(device_identifier == LCD_20X4_DEVICE_IDENTIFIER) {
        lcd_20x4_create(&ws->lcd, uid, &ws->ipcon);
        lcd_20x4_clear_display(&ws->lcd);
        lcd_20x4_backlight_on(&ws->lcd);
    }

|step2_other_config1|

.. code-block:: c

      else if(device_identifier == AMBIENT_LIGHT_DEVICE_IDENTIFIER) {
        ambient_light_create(&ws->ambient_light, uid, &ws->ipcon);
        ambient_light_set_illuminance_callback_period(&ws->ambient_light, 1000);
        ambient_light_register_callback(&ws->ambient_light,
                                        AMBIENT_LIGHT_CALLBACK_ILLUMINANCE,
                                        (void *)cb_illuminance,
                                        (void *)ws);
    } else if(device_identifier == HUMIDITY_DEVICE_IDENTIFIER) {
        humidity_create(&ws->humidity, uid, &ws->ipcon);
        humidity_set_humidity_callback_period(&ws->humidity, 1000);
        humidity_register_callback(&ws->humidity,
                                   HUMIDITY_CALLBACK_HUMIDITY,
                                   (void *)cb_humidity,
                                   (void *)ws);
    } else if(device_identifier == BAROMETER_DEVICE_IDENTIFIER) {
        barometer_create(&ws->barometer, uid, &ws->ipcon);
        barometer_set_air_pressure_callback_period(&ws->barometer, 1000);
        barometer_register_callback(&ws->barometer,
                                    BAROMETER_CALLBACK_AIR_PRESSURE,
                                    (void *)cb_air_pressure,
                                    (void *)ws);
    }

|step2_other_config2|

|step2_put_together|

.. code-block:: c

    if(enumeration_type == IPCON_ENUMERATION_TYPE_CONNECTED ||
       enumeration_type == IPCON_ENUMERATION_TYPE_AVAILABLE) {
        if(device_identifier == LCD_20X4_DEVICE_IDENTIFIER) {
            lcd_20x4_create(&ws->lcd, uid, &ws->ipcon);
            lcd_20x4_clear_display(&ws->lcd);
            lcd_20x4_backlight_on(&ws->lcd);
        } else if(device_identifier == AMBIENT_LIGHT_DEVICE_IDENTIFIER) {
            ambient_light_create(&ws->ambient_light, uid, &ws->ipcon);
            ambient_light_set_illuminance_callback_period(&ws->ambient_light, 1000);
            ambient_light_register_callback(&ws->ambient_light,
                                            AMBIENT_LIGHT_CALLBACK_ILLUMINANCE,
                                            (void *)cb_illuminance,
                                            (void *)ws);
        } else if(device_identifier == HUMIDITY_DEVICE_IDENTIFIER) {
            humidity_create(&ws->humidity, uid, &ws->ipcon);
            humidity_set_humidity_callback_period(&ws->humidity, 1000);
            humidity_register_callback(&ws->humidity,
                                       HUMIDITY_CALLBACK_HUMIDITY,
                                       (void *)cb_humidity,
                                       (void *)ws);
        } else if(device_identifier == BAROMETER_DEVICE_IDENTIFIER) {
            barometer_create(&ws->barometer, uid, &ws->ipcon);
            barometer_set_air_pressure_callback_period(&ws->barometer, 1000);
            barometer_register_callback(&ws->barometer,
                                        BAROMETER_CALLBACK_AIR_PRESSURE,
                                        (void *)cb_air_pressure,
                                        (void *)ws);
        }
    }


Step 3: Show measurements on display
------------------------------------

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: c

    sprintf(text, "%6.2f", value);

|step3_printf|

.. code-block:: c

    void cb_illuminance(uint16_t illuminance, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;
        char text[30] = {'\0'};

        sprintf(text, "Illuminanc %6.2f lx", illuminance/10.0);
        lcd_20x4_write_line(&ws->lcd, 0, 0, text);
    }

    void cb_humidity(uint16_t humidity, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;
        char text[30] = {'\0'};

        sprintf(text, "Humidity   %6.2f %%", humidity/10.0);
        lcd_20x4_write_line(&ws->lcd, 1, 0, text);
    }

    void cb_air_pressure(int32_t air_pressure, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;
        char text[30] = {'\0'};

        sprintf(text, "Air Press %7.2f mb", air_pressure/1000.0);
        lcd_20x4_write_line(&ws->lcd, 2, 0, text);
    }

|step3_temperature|

.. code-block:: c

    void cb_air_pressure(int32_t air_pressure, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;
        char text[30] = {'\0'};

        sprintf(text, "Air Press %7.2f mb", air_pressure/1000.0);
        lcd_20x4_write_line(&ws->lcd, 2, 0, text);

        int16_t temperature;
        barometer_get_chip_temperature(&ws->barometer, &temperature);

        memset(text, '\0', sizeof(text));
        sprintf(text, "Temperature %5.2f %cC", temperature/100.0, 0xDF);
        lcd_20x4_write_line(&ws->lcd, 3, 0, text);
    }

|step3_put_together|

.. code-block:: c

    void cb_illuminance(uint16_t illuminance, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;
        char text[30] = {'\0'};

        sprintf(text, "Illuminanc %6.2f lx", illuminance/10.0);
        lcd_20x4_write_line(&ws->lcd, 0, 0, text);
    }

    void cb_humidity(uint16_t humidity, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;
        char text[30] = {'\0'};

        sprintf(text, "Humidity   %6.2f %%", humidity/10.0);
        lcd_20x4_write_line(&ws->lcd, 1, 0, text);
    }

    void cb_air_pressure(int32_t air_pressure, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;
        char text[30] = {'\0'};

        sprintf(text, "Air Press %7.2f mb", air_pressure/1000.0);
        lcd_20x4_write_line(&ws->lcd, 2, 0, text);

        int16_t temperature;
        barometer_get_chip_temperature(&ws->barometer, &temperature);

        memset(text, '\0', 30);
        sprintf(text, "Temperature %5.2f %cC", temperature/100.0, 0xDF);
        lcd_20x4_write_line(&ws->lcd, 3, 0, text);
    }

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Step 4: Error handling and Logging
----------------------------------

|step4_intro1|

.. code-block:: c

    while(true) {
        int rc = ipcon_connect(&ws.ipcon, HOST, PORT);
        if(rc < 0) {
            fprintf(stderr, "Could not connect to brickd: %d\n", rc);
            // TODO: sleep 1s
            continue;
        }
        break;
    }

|step4_intro2|

.. code-block:: c

    while(true) {
        int rc = ipcon_enumerate(&ws.ipcon);
        if(rc < 0) {
            fprintf(stderr, "Could not enumerate: %d\n", rc);
            // TODO: sleep 1s
            continue;
        }
        break;
    }

|step4_connect_afterwards|

|step4_lcd_initialized1|

.. code-block:: c

    void cb_illuminance(uint16_t illuminance, void *user_data) {
        WeatherStation *ws = (WeatherStation*)user_data;

        if(ws->lcd_created) {
            char text[30] = {'\0'};
            sprintf(text, "Illuminanc %6.2f lx", illuminance/10.0);
            lcd_20x4_write_line(&ws->lcd, 0, 0, text);
            printf("Write to line 0: %s\n", text);
        }
    }

.. FIXME |step4_lcd_initialized2|

.. FIXME code-block:: python

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

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/c/weather_station.c>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/c/weather_station.c
 :language: c
 :linenos:
 :tab-width: 4
