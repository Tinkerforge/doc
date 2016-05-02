
:breadcrumbs: <a href="../index.html">Startseite</a> / <a href="../index.html#software">Software</a> / Brick MQTT Proxy

.. _brick_mqtt_proxy:

Brick MQTT Proxy
================

`MQTT <http://mqtt.org/>`__ ist ein Machine-to-Machine (M2M) und Internet der 
Dinge (IoT) Publish/Subscribe Nachrichten-Transport-Protokoll. Der Brick MQTT
Proxy erlaubt den Zugriff auf Bricks und Bricklets über MQTT. Er ist in Python
geschrieben und übersetzt Nachrichten zwischen dem 
:ref:`Tinkerforge TCP/IP Protocol (TFP) <llproto_tcpip>` und MQTT.

Setup und Benutzung
-------------------

Der Proxy ist ein Python-Skript und kann von seinem
`Brick MQTT Proxy GitHub Repository <https://github.com/Tinkerforge/brick-mqtt-proxy>`__
heruntergeladen werden.

Als Abhängigkeiten müssen nur die
:ref:`Tinkerforge Python API Bindings <api_bindings_python>` 
und `Eclipse Paho MQTT Python client library <https://pypi.python.org/pypi/paho-mqtt/1.1>`__
installiert werden. Unter Linux kann dies mit folgendem Befehl geschehen:

.. code-block:: bash

  sudo pip install tinkerforge paho-mqtt

Anschließend kann der Proxy mit folgender Zeile gestartet werden:

.. code-block:: bash

  python brick-mqtt-proxy.py

Um eine Liste der Kommandozeilen-Parameter für Host- und Porteinstellungen des
:ref:`Brick Daemon <brickd>` und des MQTT Broker, der Daten Updaterate und
einer möglichen Debugausgabe zu bekommen, muss folgende Zeile eingegeben werden:

.. code-block:: bash

  python brick-mqtt-proxy.py --help


Beispiele
^^^^^^^^^

In den folgenden Beispiel nutzen wir
`Mosquitto <http://mosquitto.org/documentation/>`__ als Broker und Client. 
Andere Broker und Clients können auf eine ähnliche Weise genutzt werden. Um 
Mosquitto unter Linux zu installieren kann folgende Zeile eingegeben werden:

.. code-block:: bash

  sudo apt-get install mosquitto mosquitto-clients

Anschließend startet man den Brick MQTT Proxy und führt eines der Beispiele aus.
Die Struktur ist :ref:`nachfolgend beschrieben <brick_mqtt_proxy_topics_and_payload_structure>`.
Denke daran die UID im Topic durch die des eigenen Bricklets auszutauschen.

.. code-block:: bash

  # Enummeriere alle verfügbaren Module
  mosquitto_sub -v -t tinkerforge/enumerate/available/#

  # Enummeriere alle verfügbaren Laser Range Finder Bricklets
  mosquitto_sub -v -t tinkerforge/enumerate/available/bricklet/laser_range_finder

  # Aktiviere den Laser
  mosquitto_pub -t tinkerforge/bricklet/laser_range_finder/vbM/enable_laser/set -m ''

  # Lese die gemessene Distanz
  mosquitto_sub -v -t tinkerforge/bricklet/laser_range_finder/vbM/distance

  # Enummeriere alle verfügbaren Analog Out 2.0 Bricklets
  mosquitto_sub -v -t tinkerforge/enumerate/available/bricklet/analog_out_v2

  # Lese die Eingangsspannung
  mosquitto_sub -v -t tinkerforge/bricklet/analog_out_v2/7xwQ9g/input_voltage

  # Lese die Ausgangsspannung
  mosquitto_sub -v -t tinkerforge/bricklet/analog_out_v2/7xwQ9g/output_voltage

  # Setze die Ausgangsspannung auf 2.5V
  mosquitto_pub -t tinkerforge/bricklet/analog_out_v2/7xwQ9g/input_voltage -m '{"voltage":2500}'


.. _brick_mqtt_proxy_topics_and_payload_structure:

Topic- und Payload-Struktur
---------------------------

Die Topics sind geteilt in Device (aktuell nur ``bricklet/``) und
``enumerate/`` Topics.

Devices
^^^^^^^

Der Proxy veröffentlicht (publishes) retained Messages von Messwert- und
Konfigurationsänderungen von unterstützen Devices mit dem folgenden Pattern:

.. code-block:: none

  tinkerforge/<prefix>/<uid>/<suffix>

Für ein Temperature Bricklet mit UID ``XYZ`` wird die Temperatur wie folgt
publishen:

.. code-block:: none

  tinkerforge/bricklet/temperature/XYZ/temperature

Messwert- Konfigurations-Information wird als JSON im folgenden Format
repräsentiert:

.. code-block:: json

  {
    "_timestamp": <timestamp>,
    "<key>": <value>
  }

Alle Nachrichten die der Proxy published enthalten einen UNIX
Zeitstempel, um das Alter der Information zur Verfügung zu stellen. Das Benennung
und die Bedeutung der Schlüssel-Wert-Paare ist gleichbedeutend mit der
Payload-Definition unseres :ref:`TCP/IP Protokolls <llproto_tcpip>`.
Alle Schlüssel-Wert-Paare, die vom Proxy hinzugefügt werden beginnen mit einem
Unterstrich um Namenskonflikte zu vermeiden. Als Beispiel wird die gemessene 
Temperatur eines Temperature Bricklets mit UID ``XYZ`` wie folgt gepublished:

.. code-block:: json

  {
    "_timestamp": 1440083842.785104,
    "temperature": 2343
  }

Topics die auf ``/set`` enden, ermöglichen die Konfiguration eines Devices zu 
ändern. Um zum Beispiel die Konfiguration eines Ambient Light Bricklet 2.0 mit
UID ``ABC`` zu ändern wird folgender JSON Payload:

.. code-block:: json

  {
    "illuminance_range": 1,
    "integration_time": 2
  }

unter folgenden Topic gepublished:

.. code-block:: none

  tinkerforge/bricklet/ambient_light_v2/ABC/configuration/set

Der Proxy parsed den Payload und ruft die dazugehörigen Konfigurations-Funktion
auf.

Hierbei entsprechen die Schlüssel-Wert-Paare wieder der Payload-Definition
unseres TCP/IP  Protokolls. Im Beispiel wird die Illuminance Range auf 32000Lux
und die  Integration Time auf 150ms gesetzt.

Enumerate
^^^^^^^^^

Es gibt drei verschiedene ``enumerate/`` Subtopics auf denen der Proxy
Ereignisse published:

* ``tinkerforge/enumerate/available/<device-topic-prefix>``: Wenn die Liste der
  verfügbaren Devices mit übereinstimmenden Topic-Prefix sich ändert wird eine
  retained Message mit der aktualisieren Liste aller nun verfügbaren Devices
  gepublished.
* ``tinkerforge/enumerate/connected/<device-topic-prefix>``: Wenn ein neues 
  Device mit übereinstimmenden Topic-Prefix verbunden wird, so wird eine
  Nachricht mit Informationen über dieses Device gepublished.
* ``tinkerforge/enumerate/disconnected/<device-topic-prefix>``: Wenn ein 
  bekanntes Device mit übereinstimmenden Topic-Prefix getrennt wird, so
  wird eine Nachricht mit Informationen über dieses Device gepublished.

Ein LCD 20x4 Bricklet, dass verbunden wird, wird auf folgenden Topic gepublished:

.. code-block:: none

  tinkerforge/enumerate/connected/bricklet/lcd_20x4

Zusätzlich wird die
retained Message auf ``tinkerforge/enumerate/available/bricklet/lcd_20x4``
aktualisiert. Die Device-Information wird für alle Subtopics in JSON in 
folgendem Format repräsentiert:

.. code-block:: json

  {
    "_timestamp": <timestamp>,
    "uid": "<uid>",
    "connected_uid": "<connected_uid>",
    "position": "<position>",
    "hardware_version": [<major>, <minor>, <release>],
    "firmware_version": [<major>, <minor>, <release>],
    "device_identifier": <device_identifier>
  }

Für ein Temperature Bricklet sieht dies zum Beispiel wie folgt aus:

.. code-block:: json

  {
    "_timestamp": 1440143404.176469,
    "uid": "se3",
    "connected_uid": "5VihSm",
    "position": "c",
    "hardware_version": [1, 1, 0],
    "firmware_version": [2, 0, 3],
    "device_identifier": 216
  }


Unterstützte Device Topics
--------------------------

Die nachfolgende Tabelle zeigt alle aktuell unterstützen Devices mit deren
Namen, Suffixen und Links. Die Links zeigen auf deren TCP/IP Protokoll
Dokumentation, aus der die Payload-Definition entnommen werden kann.

.. csv-table::
 :header: Device, Prefix, Suffix
 :delim: |
 :widths: 30, 30, 40

 :ref:`Accelerometer Bricklet <accelerometer_bricklet>`                         | bricklet/accelerometer               | :tcpip:func:`acceleration <BrickletAccelerometer.get_acceleration>`
                                                                                |                                      | :tcpip:func:`temperature <BrickletAccelerometer.get_temperature>`
                                                                                |                                      | :tcpip:func:`led_on <BrickletAccelerometer.is_led_on>`
                                                                                |                                      | :tcpip:func:`led_on/set <BrickletAccelerometer.led_on>`
                                                                                |                                      | :tcpip:func:`led_off/set <BrickletAccelerometer.led_off>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletAccelerometer.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletAccelerometer.set_configuration>`

 :ref:`Ambient Light Bricklet <ambient_light_bricklet>`                         | bricklet/ambient_light               | :tcpip:func:`illuminance <BrickletAmbientLight.get_illuminance>`

 :ref:`Ambient Light Bricklet 2.0 <ambient_light_v2_bricklet>`                  | bricklet/ambient_light_v2            | :tcpip:func:`illuminance <BrickletAmbientLightV2.get_illuminance>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletAmbientLightV2.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletAmbientLightV2.set_configuration>`

 :ref:`Analog In Bricklet <analog_in_bricklet>`                                 | bricklet/analog_in                   | :tcpip:func:`voltage <BrickletAnalogIn.get_voltage>`
                                                                                |                                      | :tcpip:func:`averaging <BrickletAnalogIn.get_averaging>`
                                                                                |                                      | :tcpip:func:`averaging/set <BrickletAnalogIn.set_averaging>`
                                                                                |                                      | :tcpip:func:`range <BrickletAnalogIn.get_range>`
                                                                                |                                      | :tcpip:func:`range/set <BrickletAnalogIn.set_range>`

 :ref:`Analog In Bricklet 2.0 <analog_in_v2_bricklet>`                          | bricklet/analog_in_v2                | :tcpip:func:`voltage <BrickletAnalogInV2.get_voltage>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletAnalogInV2.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletAnalogInV2.set_moving_average>`

 :ref:`Analog Out Bricklet <analog_out_bricklet>`                               | bricklet/analog_out                  | :tcpip:func:`voltage <BrickletAnalogOut.get_voltage>`
                                                                                |                                      | :tcpip:func:`voltage/set <BrickletAnalogOut.set_voltage>`
                                                                                |                                      | :tcpip:func:`mode <BrickletAnalogOut.get_mode>`
                                                                                |                                      | :tcpip:func:`mode/set <BrickletAnalogOut.set_mode>`

 :ref:`Analog Out Bricklet 2.0 <analog_out_v2_bricklet>`                        | bricklet/analog_out_v2               | :tcpip:func:`output_voltage <BrickletAnalogOutV2.get_output_voltage>`
                                                                                |                                      | :tcpip:func:`output_voltage/set <BrickletAnalogOutV2.set_output_voltage>`
                                                                                |                                      | :tcpip:func:`input_voltage <BrickletAnalogOutV2.get_input_voltage>`

 :ref:`Barometer Bricklet <barometer_bricklet>`                                 | bricklet/barometer                   | :tcpip:func:`air_pressure <BrickletBarometer.get_air_pressure>`
                                                                                |                                      | :tcpip:func:`altitude <BrickletBarometer.get_altitude>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletBarometer.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`reference_air_pressure <BrickletBarometer.get_reference_air_pressure>`
                                                                                |                                      | :tcpip:func:`reference_air_pressure/set <BrickletBarometer.set_reference_air_pressure>`
                                                                                |                                      | :tcpip:func:`averaging <BrickletBarometer.get_averaging>`
                                                                                |                                      | :tcpip:func:`averaging/set <BrickletBarometer.set_averaging>`

 :ref:`CO2 Bricklet <co2_bricklet>`                                             | bricklet/co2                         | :tcpip:func:`co2_concentration <BrickletCO2.get_co2_concentration>`

 :ref:`Current12 Bricklet <current12_bricklet>`                                 | bricklet/current12                   | :tcpip:func:`current <BrickletCurrent12.get_current>`
                                                                                |                                      | :tcpip:func:`over_current <BrickletCurrent12.is_over_current>`
                                                                                |                                      | :tcpip:func:`calibrate/set <BrickletCurrent12.calibrate>`

 :ref:`Current25 Bricklet <current25_bricklet>`                                 | bricklet/current25                   | :tcpip:func:`current <BrickletCurrent25.get_current>`
                                                                                |                                      | :tcpip:func:`over_current <BrickletCurrent25.is_over_current>`
                                                                                |                                      | :tcpip:func:`calibrate/set <BrickletCurrent25.calibrate>`

 :ref:`Distance IR Bricklet <distance_ir_bricklet>`                             | bricklet/distance_ir                 | :tcpip:func:`distance <BrickletDistanceIR.get_distance>`

 :ref:`Distance US Bricklet <distance_us_bricklet>`                             | bricklet/distance_us                 | :tcpip:func:`distance_value <BrickletDistanceUS.get_distance_value>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletDistanceUS.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletDistanceUS.set_moving_average>`

 :ref:`Dual Button Bricklet <dual_button_bricklet>`                             | bricklet/dual_button                 | :tcpip:func:`button_state <BrickletDualButton.get_button_state>`
                                                                                |                                      | :tcpip:func:`led_state <BrickletDualButton.get_led_state>`
                                                                                |                                      | :tcpip:func:`led_state/set <BrickletDualButton.set_led_state>`
                                                                                |                                      | :tcpip:func:`selected_led_state/set <BrickletDualButton.set_selected_led_state>`

 :ref:`Dual Relay Bricklet <dual_relay_bricklet>`                               | bricklet/dual_relay                  | :tcpip:func:`state <BrickletDualRelay.get_state>`
                                                                                |                                      | :tcpip:func:`state/set <BrickletDualRelay.set_state>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletDualRelay.set_monoflop>`
                                                                                |                                      | :tcpip:func:`selected_state/set <BrickletDualRelay.set_selected_state>`

 :ref:`Dust Detector Bricklet <dust_detector_bricklet>`                         | bricklet/dust_detector               | :tcpip:func:`dust_density <BrickletDustDetector.get_dust_density>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletDustDetector.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletDustDetector.set_moving_average>`

 :ref:`GPS Bricklet <gps_bricklet>`                                             | bricklet/gps                         | :tcpip:func:`status <BrickletGPS.get_status>`
                                                                                |                                      | :tcpip:func:`coordinates <BrickletGPS.get_coordinates>`
                                                                                |                                      | :tcpip:func:`altitude <BrickletGPS.get_altitude>`
                                                                                |                                      | :tcpip:func:`motion <BrickletGPS.get_motion>`
                                                                                |                                      | :tcpip:func:`date_time <BrickletGPS.get_date_time>`
                                                                                |                                      | :tcpip:func:`restart/set <BrickletGPS.restart>`

 :ref:`Hall Effect Bricklet <hall_effect_bricklet>`                             | bricklet/hall_effect                 | :tcpip:func:`value <BrickletHallEffect.get_value>`
                                                                                |                                      | :tcpip:func:`edge_count_config <BrickletHallEffect.get_edge_count_config>`
                                                                                |                                      | :tcpip:func:`edge_count_config/set <BrickletHallEffect.set_edge_count_config>`

 :ref:`Humidity Bricklet <humidity_bricklet>`                                   | bricklet/humidity                    | :tcpip:func:`humidity <BrickletHumidity.get_humidity>`

 :ref:`Industrial Analog Out Bricklet <industrial_analog_out_bricklet>`         | bricklet/industrial_analog_out       | :tcpip:func:`voltage <BrickletIndustrialAnalogOut.get_voltage>`
                                                                                |                                      | :tcpip:func:`voltage/set <BrickletIndustrialAnalogOut.set_voltage>`
                                                                                |                                      | :tcpip:func:`current <BrickletIndustrialAnalogOut.get_current>`
                                                                                |                                      | :tcpip:func:`current/set <BrickletIndustrialAnalogOut.set_current>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletIndustrialAnalogOut.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletIndustrialAnalogOut.set_configuration>`
                                                                                |                                      | :tcpip:func:`enabled <BrickletIndustrialAnalogOut.is_enabled>`
                                                                                |                                      | :tcpip:func:`enable/set <BrickletIndustrialAnalogOut.enable>`
                                                                                |                                      | :tcpip:func:`disable/set <BrickletIndustrialAnalogOut.disable>`

 :ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`     | bricklet/industrial_digital_in_4     | :tcpip:func:`value <BrickletIndustrialDigitalIn4.get_value>`
                                                                                |                                      | :tcpip:func:`edge_count_config/set <BrickletIndustrialDigitalIn4.set_edge_count_config>`
                                                                                |                                      | :tcpip:func:`available_for_group <BrickletIndustrialDigitalIn4.get_available_for_group>`
                                                                                |                                      | :tcpip:func:`group <BrickletIndustrialDigitalIn4.get_group>`
                                                                                |                                      | :tcpip:func:`group/set <BrickletIndustrialDigitalIn4.set_group>`

 :ref:`Industrial Digital Out 4 Bricklet <industrial_digital_in_4_bricklet>`    | bricklet/industrial_digital_out_4    | :tcpip:func:`value <BrickletIndustrialDigitalOut4.get_value>`
                                                                                |                                      | :tcpip:func:`value/set <BrickletIndustrialDigitalOut4.set_value>`
                                                                                |                                      | :tcpip:func:`selected_values/set <BrickletIndustrialDigitalOut4.set_selected_values>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletIndustrialDigitalOut4.set_monoflop>`
                                                                                |                                      | :tcpip:func:`available_for_group <BrickletIndustrialDigitalOut4.get_available_for_group>`
                                                                                |                                      | :tcpip:func:`group <BrickletIndustrialDigitalOut4.get_group>`
                                                                                |                                      | :tcpip:func:`group/set <BrickletIndustrialDigitalOut4.set_group>`

 :ref:`Industrial Dual 0-20mA Bricklet <industrial_dual_0_20ma_bricklet>`       | bricklet/industrial_dual_0_20ma      | :tcpip:func:`sample_rate <BrickletIndustrialDual020mA.get_sample_rate>`
                                                                                |                                      | :tcpip:func:`sample_rate/set <BrickletIndustrialDual020mA.set_sample_rate>`

 :ref:`Industrial Dual Analog In Bricklet <industrial_dual_analog_in_bricklet>` | bricklet/industrial_dual_analog_in   | :tcpip:func:`sample_rate <BrickletIndustrialDualAnalogIn.get_sample_rate>`
                                                                                |                                      | :tcpip:func:`sample_rate/set <BrickletIndustrialDualAnalogIn.set_sample_rate>`
                                                                                |                                      | :tcpip:func:`calibration <BrickletIndustrialDualAnalogIn.get_calibration>`
                                                                                |                                      | :tcpip:func:`calibration/set <BrickletIndustrialDualAnalogIn.set_calibration>`
                                                                                |                                      | :tcpip:func:`adc_values <BrickletIndustrialDualAnalogIn.get_adc_values>`

 :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`         | bricklet/industrial_quad_relay       | :tcpip:func:`value <BrickletIndustrialQuadRelay.get_value>`
                                                                                |                                      | :tcpip:func:`value/set <BrickletIndustrialQuadRelay.set_value>`
                                                                                |                                      | :tcpip:func:`selected_values/set <BrickletIndustrialQuadRelay.set_selected_values>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletIndustrialQuadRelay.set_monoflop>`
                                                                                |                                      | :tcpip:func:`available_for_group <BrickletIndustrialQuadRelay.get_available_for_group>`
                                                                                |                                      | :tcpip:func:`group <BrickletIndustrialQuadRelay.get_group>`
                                                                                |                                      | :tcpip:func:`group/set <BrickletIndustrialQuadRelay.set_group>`

 :ref:`IO-16 Bricklet <io16_bricklet>`                                          | bricklet/io16                        | :tcpip:func:`port/set <BrickletIO16.set_port>`
                                                                                |                                      | :tcpip:func:`port_configuration/set <BrickletIO16.set_port_configuration>`
                                                                                |                                      | :tcpip:func:`port_monoflop/set <BrickletIO16.set_port_monoflop>`
                                                                                |                                      | :tcpip:func:`selected_values/set <BrickletIO16.set_selected_values>`
                                                                                |                                      | :tcpip:func:`edge_count_config/set <BrickletIO16.set_edge_count_config>`

 :ref:`IO-4 Bricklet <io4_bricklet>`                                            | bricklet/io4                         | :tcpip:func:`value <BrickletIO4.get_value>`
                                                                                |                                      | :tcpip:func:`value/set <BrickletIO4.set_value>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletIO4.set_configuration>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletIO4.set_monoflop>`
                                                                                |                                      | :tcpip:func:`selected_values/set <BrickletIO4.set_selected_values>`
                                                                                |                                      | :tcpip:func:`edge_count_config/set <BrickletIO4.set_edge_count_config>`

 :ref:`Joystick Bricklet <joystick_bricklet>`                                   | bricklet/joystick                    | :tcpip:func:`position <BrickletJoystick.get_position>`
                                                                                |                                      | :tcpip:func:`pressed <BrickletJoystick.is_pressed>`
                                                                                |                                      | :tcpip:func:`calibrate/set <BrickletJoystick.calibrate>`

 :ref:`Laser Range Finder Bricklet <laser_range_finder_bricklet>`               | bricklet/laser_range_finder          | :tcpip:func:`distance <BrickletLaserRangeFinder.get_distance>`
                                                                                |                                      | :tcpip:func:`velocity <BrickletLaserRangeFinder.get_velocity>`
                                                                                |                                      | :tcpip:func:`mode <BrickletLaserRangeFinder.get_mode>`
                                                                                |                                      | :tcpip:func:`mode/set <BrickletLaserRangeFinder.set_mode>`
                                                                                |                                      | :tcpip:func:`laser_enabled <BrickletLaserRangeFinder.is_laser_enabled>`
                                                                                |                                      | :tcpip:func:`enable_laser/set <BrickletLaserRangeFinder.enable_laser>`
                                                                                |                                      | :tcpip:func:`disable_laser/set <BrickletLaserRangeFinder.disable_laser>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletLaserRangeFinder.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletLaserRangeFinder.set_moving_average>`

 :ref:`LCD 16x2 Bricklet <lcd_16x2_bricklet>`                                   | bricklet/lcd_16x2                    | :tcpip:func:`write_line/set <BrickletLCD16x2.write_line>`
                                                                                |                                      | :tcpip:func:`clear_display/set <BrickletLCD16x2.clear_display>`
                                                                                |                                      | :tcpip:func:`backlight_on <BrickletLCD16x2.is_backlight_on>`
                                                                                |                                      | :tcpip:func:`backlight_on/set <BrickletLCD16x2.backlight_on>`
                                                                                |                                      | :tcpip:func:`backlight_off/set <BrickletLCD16x2.backlight_off>`
                                                                                |                                      | :tcpip:func:`config <BrickletLCD16x2.get_config>`
                                                                                |                                      | :tcpip:func:`config/set <BrickletLCD16x2.set_config>`
                                                                                |                                      | :tcpip:func:`button_pressed <BrickletLCD16x2.is_button_pressed>`

 :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>`                                   | bricklet/lcd_20x4                    | :tcpip:func:`write_line/set <BrickletLCD20x4.write_line>`
                                                                                |                                      | :tcpip:func:`clear_display/set <BrickletLCD20x4.clear_display>`
                                                                                |                                      | :tcpip:func:`backlight_on <BrickletLCD20x4.is_backlight_on>`
                                                                                |                                      | :tcpip:func:`backlight_on/set <BrickletLCD20x4.backlight_on>`
                                                                                |                                      | :tcpip:func:`backlight_off/set <BrickletLCD20x4.backlight_off>`
                                                                                |                                      | :tcpip:func:`config <BrickletLCD20x4.get_config>`
                                                                                |                                      | :tcpip:func:`config/set <BrickletLCD20x4.set_config>`
                                                                                |                                      | :tcpip:func:`button_pressed <BrickletLCD20x4.is_button_pressed>`
                                                                                |                                      | :tcpip:func:`default_text_counter <BrickletLCD20x4.get_default_text_counter>`
                                                                                |                                      | :tcpip:func:`default_text_counter/set <BrickletLCD20x4.set_default_text_counter>`

 :ref:`LED Strip Bricklet <led_strip_bricklet>`                                 | bricklet/led_strip                   | :tcpip:func:`rgb_values <BrickletLEDStrip.get_rgb_values>`
                                                                                |                                      | :tcpip:func:`rgb_values/set <BrickletLEDStrip.set_rgb_values>`
                                                                                |                                      | :tcpip:func:`frame_duration <BrickletLEDStrip.get_frame_duration>`
                                                                                |                                      | :tcpip:func:`frame_duration/set <BrickletLEDStrip.set_frame_duration>`
                                                                                |                                      | :tcpip:func:`supply_voltage <BrickletLEDStrip.get_supply_voltage>`
                                                                                |                                      | :tcpip:func:`clock_frequency <BrickletLEDStrip.get_clock_frequency>`
                                                                                |                                      | :tcpip:func:`clock_frequency/set <BrickletLEDStrip.set_clock_frequency>`
                                                                                |                                      | :tcpip:func:`chip_type <BrickletLEDStrip.get_chip_type>`
                                                                                |                                      | :tcpip:func:`chip_type/set <BrickletLEDStrip.set_chip_type>`

 :ref:`Line Bricklet <line_bricklet>`                                           | bricklet/line                        | :tcpip:func:`reflectivity <BrickletLine.get_reflectivity>`

 :ref:`Linear Poti Bricklet <line_bricklet>`                                    | bricklet/linear_poti                 | :tcpip:func:`position <BrickletLinearPoti.get_position>`

 :ref:`Load Cell Bricklet <load_cell_bricklet>`                                 | bricklet/load_cell                   | :tcpip:func:`weight <BrickletLoadCell.get_weight>`
                                                                                |                                      | :tcpip:func:`led_on <BrickletLoadCell.is_led_on>`
                                                                                |                                      | :tcpip:func:`led_on/set <BrickletLoadCell.led_on>`
                                                                                |                                      | :tcpip:func:`led_off/set <BrickletLoadCell.led_off>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletLoadCell.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletLoadCell.set_moving_average>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletLoadCell.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletLoadCell.set_configuration>`
                                                                                |                                      | :tcpip:func:`tare/set <BrickletLoadCell.tare>`

 :ref:`Moisture Bricklet <moisture_bricklet>`                                   | bricklet/moisture                    | :tcpip:func:`moisture_value <BrickletMoisture.get_moisture_value>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletMoisture.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletMoisture.set_moving_average>`

 :ref:`Motion Detector Bricklet <motion_detector_bricklet>`                     | bricklet/motion_detector             | :tcpip:func:`motion_detected <BrickletMotionDetector.get_motion_detected>`

 :ref:`Multi Touch Bricklet <multi_touch_bricklet>`                             | bricklet/multi_touch                 | :tcpip:func:`touch_state <BrickletMultiTouch.get_touch_state>`
                                                                                |                                      | :tcpip:func:`electrode_config <BrickletMultiTouch.get_electrode_config>`
                                                                                |                                      | :tcpip:func:`electrode_config/set <BrickletMultiTouch.set_electrode_config>`
                                                                                |                                      | :tcpip:func:`electrode_sensitivity <BrickletMultiTouch.get_electrode_sensitivity>`
                                                                                |                                      | :tcpip:func:`electrode_sensitivity/set <BrickletMultiTouch.set_electrode_sensitivity>`
                                                                                |                                      | :tcpip:func:`recalibrate/set <BrickletMultiTouch.recalibrate>`

 :ref:`Piezo Speaker Bricklet <piezo_speaker_bricklet>`                         | bricklet/piezo_speaker               | :tcpip:func:`beep/set <BrickletPiezoSpeaker.beep>`
                                                                                |                                      | :tcpip:func:`morse_code/set <BrickletPiezoSpeaker.morse_code>`

 :ref:`PTC Bricklet <ptc_bricklet>`                                             | bricklet/ptc                         | :tcpip:func:`temperature <BrickletPTC.get_temperature>`
                                                                                |                                      | :tcpip:func:`resistance <BrickletPTC.get_resistance>`
                                                                                |                                      | :tcpip:func:`sensor_connected <BrickletPTC.is_sensor_connected>`
                                                                                |                                      | :tcpip:func:`wire_mode <BrickletPTC.get_wire_mode>`
                                                                                |                                      | :tcpip:func:`wire_mode/set <BrickletPTC.set_wire_mode>`
                                                                                |                                      | :tcpip:func:`noise_rejection_filter <BrickletPTC.get_noise_rejection_filter>`
                                                                                |                                      | :tcpip:func:`noise_rejection_filter/set <BrickletPTC.set_noise_rejection_filter>`

 :ref:`Real-Time Clock Bricklet <real_time_clock_bricklet>`                     | bricklet/real_time_clock             | :tcpip:func:`date_time <BrickletRealTimeClock.get_date_time>`
                                                                                |                                      | :tcpip:func:`date_time/set <BrickletRealTimeClock.set_date_time>`
                                                                                |                                      | :tcpip:func:`timestamp <BrickletRealTimeClock.get_timestamp>`
                                                                                |                                      | :tcpip:func:`offset <BrickletRealTimeClock.get_offset>`
                                                                                |                                      | :tcpip:func:`offset/set <BrickletRealTimeClock.set_offset>`

 :ref:`Remote Switch Bricklet <remote_switch_bricklet>`                         | bricklet/remote_switch               | :tcpip:func:`switching_state <BrickletRemoteSwitch.get_switching_state>`
                                                                                |                                      | :tcpip:func:`repeats <BrickletRemoteSwitch.get_repeats>`
                                                                                |                                      | :tcpip:func:`repeats/set <BrickletRemoteSwitch.set_repeats>`
                                                                                |                                      | :tcpip:func:`switch_socket_a/set <BrickletRemoteSwitch.switch_socket_a>`
                                                                                |                                      | :tcpip:func:`switch_socket_b/set <BrickletRemoteSwitch.switch_socket_b>`
                                                                                |                                      | :tcpip:func:`dim_socket_b/set <BrickletRemoteSwitch.dim_socket_b>`
                                                                                |                                      | :tcpip:func:`switch_socket_c/set <BrickletRemoteSwitch.switch_socket_c>`

 :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>`                             | bricklet/rotary_poti                 | :tcpip:func:`position <BrickletRotaryPoti.get_position>`

 :ref:`Rotary Encoder Bricklet <rotary_encoder_bricklet>`                       | bricklet/rotary_encoder              | :tcpip:func:`count <BrickletRotaryEncoder.get_count>` (ruft :tcpip:func:`get_count <BrickletRotaryEncoder.get_count>` mit *false* auf)
                                                                                |                                      | :tcpip:func:`pressed <BrickletRotaryEncoder.is_pressed>`
                                                                                |                                      | :tcpip:func:`_reset_count/set <BrickletRotaryEncoder.get_count>` (ruft :tcpip:func:`get_count <BrickletRotaryEncoder.get_count>` mit *true* auf)

 :ref:`Solid State Relay Bricklet <solid_state_relay_bricklet>`                 | bricklet/solid_state_relay           | :tcpip:func:`state <BrickletSolidStateRelay.get_state>`
                                                                                |                                      | :tcpip:func:`state/set <BrickletSolidStateRelay.set_state>`
                                                                                |                                      | :tcpip:func:`monoflop <BrickletSolidStateRelay.get_monoflop>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletSolidStateRelay.set_monoflop>`


 :ref:`Sound Intensity Bricklet <sound_intensity_bricklet>`                     | bricklet/sound_intensity             | :tcpip:func:`intensity <BrickletSoundIntensity.get_intensity>`

 :ref:`Temperature Bricklet <temperature_bricklet>`                             | bricklet/temperature                 | :tcpip:func:`temperature <BrickletTemperature.get_temperature>`
                                                                                |                                      | :tcpip:func:`i2c_mode <BrickletTemperature.get_i2c_mode>`
                                                                                |                                      | :tcpip:func:`i2c_mode/set <BrickletTemperature.set_i2c_mode>`

 :ref:`Temperature IR Bricklet <temperature_ir_bricklet>`                       | bricklet/temperature_ir              | :tcpip:func:`ambient_temperature <BrickletTemperatureIR.get_ambient_temperature>`
                                                                                |                                      | :tcpip:func:`object_temperature <BrickletTemperatureIR.get_object_temperature>`
                                                                                |                                      | :tcpip:func:`emissivity <BrickletTemperatureIR.get_emissivity>`
                                                                                |                                      | :tcpip:func:`emissivity/set <BrickletTemperatureIR.set_emissivity>`

 :ref:`Tilt Bricklet <tilt_bricklet>`                                           | bricklet/tilt                        | :tcpip:func:`tilt_state <BrickletTilt.get_tilt_state>`

 :ref:`UV Light Bricklet <uv_light_bricklet>`                                   | bricklet/uv_light                    | :tcpip:func:`uv_light <BrickletUVLight.get_uv_light>`

 :ref:`Voltage Bricklet <voltage_bricklet>`                                     | bricklet/voltage                     | :tcpip:func:`voltage <BrickletVoltage.get_voltage>`

 :ref:`Voltage/Current Bricklet <voltage_current_bricklet>`                     | bricklet/voltage_current             | :tcpip:func:`voltage <BrickletVoltageCurrent.get_voltage>`
                                                                                |                                      | :tcpip:func:`current <BrickletVoltageCurrent.get_current>`
                                                                                |                                      | :tcpip:func:`power <BrickletVoltageCurrent.get_power>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletVoltageCurrent.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletVoltageCurrent.set_configuration>`
                                                                                |                                      | :tcpip:func:`calibration <BrickletVoltageCurrent.get_calibration>`
                                                                                |                                      | :tcpip:func:`calibration/set <BrickletVoltageCurrent.set_calibration>`

Unterstützung für andere Bricks und Bricklets hinzufügen
--------------------------------------------------------

Der Brick MQTT Proxy wurde entwickelt um einfach für andere Bricks und Bricklets
erweiterbar zu sein. Im 
`Source des Python-Scripts <https://github.com/Tinkerforge/brick-mqtt-proxy/blob/master/brick-mqtt-proxy.py>`__
finden sich weitere Informationen dazu wie dies funktioniert. Um ein anderes 
Produkt hinzuzufügen muss nur eine eigene Proxy Klasse von ``DeviceProxy`` 
abgeleitet werden. Kommentare im Sourcecode beschreiben die notwendige Struktur.
