
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Readout Smoke Detectors using Ruby

.. |ref_CALLBACK_ENUMERATE| replace:: :rb:attr:`::CALLBACK_ENUMERATE <IPConnection::CALLBACK_ENUMERATE>`
.. |ref_CALLBACK_CONNECTED| replace:: :rb:attr:`::CALLBACK_CONNECTED <IPConnection::CALLBACK_CONNECTED>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :rb:func:`#enumerate <IPConnection#enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_voltage_reached| replace:: ``CALLBACK_VOLTAGE_REACHED``

.. include:: SmokeDetector_Ruby.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_ruby:

Read out Smoke Detectors using Ruby
===================================

.. include:: RubyCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector_Ruby.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: SmokeDetector_Ruby.substitutions
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


Step 2: Initialize Bricklet on Enumeration
------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: ruby

    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, connected_uid, position,
                                                                  hardware_version, firmware_version,
                                                                  device_identifier, enumeration_type|
      if enumeration_type == IPConnection::ENUMERATION_TYPE_CONNECTED or
         enumeration_type == IPConnection::ENUMERATION_TYPE_AVAILABLE

|step2_config1|

.. code-block:: ruby

    if device_identifier == BrickletAnalogIn::DEVICE_IDENTIFIER
      analog_in = BrickletAnalogIn.new uid, ipcon
      analog_in.set_range 1
      analog_in.set_debounce_period 10000
      analog_in.set_voltage_callback_threshold '>', 1200, 0
      analog_in.register_callback(BrickletAnalogIn::CALLBACK_VOLTAGE_REACHED) do |voltage|
      end
    end

|step2_config2|

|step2_config3|

|step2_put_together|

.. code-block:: ruby

    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, connected_uid, position,
                                                                  hardware_version, firmware_version,
                                                                  device_identifier, enumeration_type|
      if enumeration_type == IPConnection::ENUMERATION_TYPE_CONNECTED or
         enumeration_type == IPConnection::ENUMERATION_TYPE_AVAILABLE
        if device_identifier == BrickletAnalogIn::DEVICE_IDENTIFIER
          analog_in = BrickletAnalogIn.new uid, ipcon
          analog_in.set_range 1
          analog_in.set_debounce_period 10000
          analog_in.set_voltage_callback_threshold '>', 1200, 0
          analog_in.register_callback(BrickletAnalogIn::CALLBACK_VOLTAGE_REACHED) do |voltage|
          end
        end
      end
    end


Step 3: Handle the alarm signal
-------------------------------

|step3_intro|

.. code-block:: ruby

    analog_in.register_callback(BrickletAnalogIn::CALLBACK_VOLTAGE_REACHED) do |voltage|
      puts 'Fire! Fire!'
    end

|step3_complete|

|step3_suggestions|

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

|step4_initialization|

.. code-block:: ruby

    if device_identifier == BrickletAnalogIn::DEVICE_IDENTIFIER
      begin
        analog_in = BrickletAnalogIn.new uid, ipcon
        analog_in.set_range 1
        analog_in.set_debounce_period 10000
        analog_in.set_voltage_callback_threshold '>', 1200, 0
        analog_in.register_callback(BrickletAnalogIn::CALLBACK_VOLTAGE_REACHED) do |voltage|
          puts 'Fire! Fire!'
        end
        puts 'Analog In initialized'
      rescue Exception => e
        analog_in = nil
        puts 'Analog In init failed: ' + e
      end
    end

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/ruby/smoke_detector.rb>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/ruby/smoke_detector.rb
 :language: ruby
 :tab-width: 4
