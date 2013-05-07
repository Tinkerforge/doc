
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starter Kit: Weather Station</a> / Using Ruby to write to LCD 20x4 Bricklet

.. |ref_CALLBACK_ENUMERATE| replace:: :rb:attr:`::CALLBACK_ENUMERATE <IPConnection::CALLBACK_ENUMERATE>`
.. |ref_CALLBACK_CONNECTED| replace:: :rb:attr:`::CALLBACK_CONNECTED <IPConnection::CALLBACK_CONNECTED>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :rb:func:`#enumerate <IPConnection#enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``CALLBACK_ILLUMINANCE``
.. |cb_humidity| replace:: ``CALLBACK_HUMIDITY``
.. |cb_air_pressure| replace:: ``CALLBACK_AIR_PRESSURE``

.. include:: RubyToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_ruby_to_lcd:

Using Ruby to write to LCD 20x4 Bricklet
========================================

.. include:: RubyCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: RubyToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Discover Bricks and Bricklets
-------------------------------------

|step1_start_off|

.. code-block:: ruby

    HOST = 'localhost'
    PORT = 4223

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: ruby

    ipcon = IPConnection.new
    ipcon.connect HOST, PORT

    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, connected_uid, position,
                                                                  hardware_version, firmware_version,
                                                                  device_identifier, enumeration_type|
    end

    ipcon.register_callback(IPConnection::CALLBACK_CONNECTED) do |connected_reason|
    end

    ipcon.enumerate

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: ruby

    ipcon.register_callback(IPConnection::CALLBACK_CONNECTED) do |connected_reason|
      if connected_reason == IPConnection::CONNECT_REASON_AUTO_RECONNECT
        ipcon.enumerate
      end
    end

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: ruby

    HOST = 'localhost'
    PORT = 4223

    ipcon = IPConnection.new
    ipcon.connect HOST, PORT

    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, connected_uid, position,
                                                                  hardware_version, firmware_version,
                                                                  device_identifier, enumeration_type|
    end

    ipcon.register_callback(IPConnection::CALLBACK_CONNECTED) do |connected_reason|
      if connected_reason == IPConnection::CONNECT_REASON_AUTO_RECONNECT
        ipcon.enumerate
      end
    end

    ipcon.enumerate


Step 2: Initialize Bricklets on Enumeration
-------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: ruby

    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, connected_uid, position,
                                                                  hardware_version, firmware_version,
                                                                  device_identifier, enumeration_type|
      if enumeration_type == IPConnection::ENUMERATION_TYPE_CONNECTED or
         enumeration_type == IPConnection::ENUMERATION_TYPE_AVAILABLE

|step2_lcd_config|

.. code-block:: ruby

    if device_identifier == BrickletLCD20x4::DEVICE_IDENTIFIER
      lcd = BrickletLCD20x4.new uid, ipcon
      lcd.clear_display
      lcd.backlight_on

|step2_other_config1|

.. code-block:: ruby

    elsif device_identifier == BrickletAmbientLight::DEVICE_IDENTIFIER
      ambient_light = BrickletAmbientLight.new uid, ipcon
      ambient_light.set_illuminance_callback_period 1000
      ambient_light.register_callback(BrickletAmbientLight::CALLBACK_ILLUMINANCE) do |illuminance|
      end
    elsif device_identifier == BrickletHumidity::DEVICE_IDENTIFIER
      humidity = BrickletHumidity.new uid, ipcon
      humidity.set_humidity_callback_period 1000
      humidity.register_callback(BrickletHumidity::CALLBACK_HUMIDITY) do |humidity|
      end
    elsif device_identifier == BrickletBarometer::DEVICE_IDENTIFIER
      barometer = BrickletBarometer.new uid, ipcon
      barometer.set_air_pressure_callback_period 1000
      barometer.register_callback(BrickletBarometer::CALLBACK_AIR_PRESSURE) do |air_pressure|
      end
    end

|step2_other_config2|

|step2_put_together|

.. code-block:: ruby

    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, connected_uid, position,
                                                                  hardware_version, firmware_version,
                                                                  device_identifier, enumeration_type|
      if enumeration_type == IPConnection::ENUMERATION_TYPE_CONNECTED or
         enumeration_type == IPConnection::ENUMERATION_TYPE_AVAILABLE
        if device_identifier == BrickletLCD20x4::DEVICE_IDENTIFIER
          lcd = BrickletLCD20x4.new uid, ipcon
          lcd.clear_display
          lcd.backlight_on
        elsif device_identifier == BrickletAmbientLight::DEVICE_IDENTIFIER
          ambient_light = BrickletAmbientLight.new uid, ipcon
          ambient_light.set_illuminance_callback_period 1000
          ambient_light.register_callback(BrickletAmbientLight::CALLBACK_ILLUMINANCE) do |illuminance|
          end
        elsif device_identifier == BrickletHumidity::DEVICE_IDENTIFIER
          humidity = BrickletHumidity.new uid, ipcon
          humidity.set_humidity_callback_period 1000
          humidity.register_callback(BrickletHumidity::CALLBACK_HUMIDITY) do |humidity|
          end
        elsif device_identifier == BrickletBarometer::DEVICE_IDENTIFIER
          barometer = BrickletBarometer.new uid, ipcon
          barometer.set_air_pressure_callback_period 1000
          barometer.register_callback(BrickletBarometer::CALLBACK_AIR_PRESSURE) do |air_pressure|
          end
        end
      end
    end


Step 3: Show measurements on display
------------------------------------

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: ruby

    text = "%6.2f" % value

|step3_printf|

.. code-block:: ruby

    ambient_light.register_callback(BrickletAmbientLight::CALLBACK_ILLUMINANCE) do |illuminance|
      text = 'Illuminanc %6.2f lx' % (illuminance/10.0)
      lcd.write_line 0, 0, text
    end

    humidity.register_callback(BrickletHumidity::CALLBACK_HUMIDITY) do |humidity|
      text = 'Humidity   %6.2f %%' % (humidity/10.0)
      lcd.write_line 1, 0, text
    end

    barometer.register_callback(BrickletBarometer::CALLBACK_AIR_PRESSURE) do |air_pressure|
      text = 'Air Press %7.2f mb' % (air_pressure/1000.0)
      lcd.write_line 2, 0, text
    end

|step3_temperature|

.. code-block:: ruby

    barometer.register_callback(BrickletBarometer::CALLBACK_AIR_PRESSURE) do |air_pressure|
      text = 'Air Press %7.2f mb' % (air_pressure/1000.0)
      lcd.write_line 2, 0, text

      temperature = barometer.get_chip_temperature
      text = 'Temperature %5.2f %sC' % [(temperature/100.0), 0xDF.chr]
      lcd.write_line 3, 0, text
    end

|step3_put_together|

.. code-block:: ruby

    ambient_light.register_callback(BrickletAmbientLight::CALLBACK_ILLUMINANCE) do |illuminance|
      text = 'Illuminanc %6.2f lx' % (illuminance/10.0)
      lcd.write_line 0, 0, text
    end

    humidity.register_callback(BrickletHumidity::CALLBACK_HUMIDITY) do |humidity|
      text = 'Humidity   %6.2f %%' % (humidity/10.0)
      lcd.write_line 1, 0, text
    end

    barometer.register_callback(BrickletBarometer::CALLBACK_AIR_PRESSURE) do |air_pressure|
      text = 'Air Press %7.2f mb' % (air_pressure/1000.0)
      lcd.write_line 2, 0, text

      temperature = barometer.get_chip_temperature
      # 0xDF == ° on LCD 20x4 charset
      text = 'Temperature %5.2f %sC' % [(temperature/100.0), 0xDF.chr]
      lcd.write_line 3, 0, text
    end

|step3_complete|

|step3_suggestions1| |step3_suggestions2_common|

|step3_robust1|

|step3_robust2|


Step 4: Error handling and Logging
----------------------------------

|step4_intro1|

.. code-block:: ruby

    while true
      begin
        ipcon.connect HOST, PORT
        break
      rescue Exception => e
        puts 'Connection Error: ' + e
        sleep 1
      end
    end

|step4_intro2|

.. code-block:: ruby

    while true
      begin
        ipcon.enumerate
        break
      rescue Exception => e
        puts 'Enumerate Error: ' + e
        sleep 1
      end
    end

|step4_connect_afterwards|

|step4_lcd_initialized1|

.. code-block:: ruby

    ambient_light.register_callback(BrickletAmbientLight::CALLBACK_ILLUMINANCE) do |illuminance|
      if lcd != nil
        text = 'Illuminanc %6.2f lx' % (illuminance/10.0)
        lcd.write_line 0, 0, text
        puts "Write to line 0: #{text}"
      end
    end

|step4_lcd_initialized2|

.. code-block:: ruby

  if device_identifier == BrickletAmbientLight::DEVICE_IDENTIFIER
    begin
      ambient_light = BrickletAmbientLight.new uid, ipcon
      ambient_light.set_illuminance_callback_period 1000
      ambient_light.register_callback(BrickletAmbientLight::CALLBACK_ILLUMINANCE) do |illuminance|
      end
      puts 'Ambient Light initialized'
    rescue Exception => e
      ambient_light = nil
      puts 'Ambient Light init failed: ' + e
    end
  end

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/weather-station/master/write_to_lcd/ruby/weather_station.rb>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/ruby/weather_station.rb
 :language: ruby
 :tab-width: 4
