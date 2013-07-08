
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Rauchmelder mit Ruby auslesen

.. |ref_CALLBACK_ENUMERATE| replace:: :rb:attr:`::CALLBACK_ENUMERATE <IPConnection::CALLBACK_ENUMERATE>`
.. |ref_CALLBACK_CONNECTED| replace:: :rb:attr:`::CALLBACK_CONNECTED <IPConnection::CALLBACK_CONNECTED>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :rb:func:`#enumerate <IPConnection#enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_interrupt| replace:: ``CALLBACK_INTERRUPT``
.. |value_mask| replace:: ``value_mask``

.. include:: SmokeDetector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_hardware_hacking_smoke_detector_ruby:

Rauchmelder mit Ruby auslesen
=============================

.. include:: RubyCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro

.. include:: SmokeDetector.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Ziele
-----

.. include:: SmokeDetector.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Schritt 1: Bricks und Bricklets dynamisch erkennen
--------------------------------------------------

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


Schritt 2: Bricklets beim Enumerate initialisieren
--------------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: ruby

    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, connected_uid, position,
                                                                  hardware_version, firmware_version,
                                                                  device_identifier, enumeration_type|
      if enumeration_type == IPConnection::ENUMERATION_TYPE_CONNECTED or
         enumeration_type == IPConnection::ENUMERATION_TYPE_AVAILABLE

|step2_config|

.. code-block:: ruby

    if device_identifier == BrickletIndustrialDigitalIn4::DEVICE_IDENTIFIER
      idi4 = BrickletIndustrialDigitalIn4.new uid, ipcon
      idi4.set_debounce_period 10000
      idi4.set_interrupt 15
      idi4.register_callback(BrickletIndustrialDigitalIn4::CALLBACK_INTERRUPT) do |interrupt_mask, value_mask|
      end
    end

|step2_put_together|

.. code-block:: ruby

    ipcon.register_callback(IPConnection::CALLBACK_ENUMERATE) do |uid, connected_uid, position,
                                                                  hardware_version, firmware_version,
                                                                  device_identifier, enumeration_type|
      if enumeration_type == IPConnection::ENUMERATION_TYPE_CONNECTED or
         enumeration_type == IPConnection::ENUMERATION_TYPE_AVAILABLE
        if device_identifier == BrickletIndustrialDigitalIn4::DEVICE_IDENTIFIER
          idi4 = BrickletIndustrialDigitalIn4.new uid, ipcon
          idi4.set_debounce_period 10000
          idi4.set_interrupt 15
          idi4.register_callback(BrickletIndustrialDigitalIn4::CALLBACK_INTERRUPT) do |interrupt_mask, value_mask|
          end
        end
      end
    end


Schritt 3: Auf Alarmsignal reagieren
------------------------------------

|step3_intro|

.. code-block:: ruby

    idi4.register_callback(BrickletIndustrialDigitalIn4::CALLBACK_INTERRUPT) do |interrupt_mask, value_mask|
      if value_mask > 0
        puts 'Fire! Fire!'
      end
    end

|step3_complete|

|step3_suggestions|

|step3_robust1|

|step3_robust2|


Schritt 4: Fehlerbehandlung und Logging
---------------------------------------

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

    if device_identifier == BrickletIndustrialDigitalIn4::DEVICE_IDENTIFIER
      begin
        idi4 = BrickletIndustrialDigitalIn4.new uid, ipcon
        idi4.set_debounce_period 10000
        idi4.set_interrupt 15
        idi4.register_callback(BrickletIndustrialDigitalIn4::CALLBACK_INTERRUPT) do |interrupt_mask, value_mask|
          if value_mask > 0
            puts 'Fire! Fire!'
          end
        end
        puts 'Industrial Digital In 4 initialized'
      rescue Exception => e
        idi4 = nil
        puts 'Industrial Digital In 4 init failed: ' + e
      end
    end

|step4_logging1|

|step4_logging2|


Schritt 5: Alles zusammen
-------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.github.com/Tinkerforge/hardware-hacking/master/smoke_detector/ruby/smoke_detector.rb>`__):

.. literalinclude:: ../../../../../hardware-hacking/smoke_detector/ruby/smoke_detector.rb
 :language: ruby
 :tab-width: 4
