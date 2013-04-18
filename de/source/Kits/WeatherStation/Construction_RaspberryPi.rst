
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starterkit: Wetterstation</a> / Konstruktion: Raspberry Pi Wetterstation

.. _starter_kit_weather_station_construction_rpi:

Konstruktion: Raspberry Pi Wetterstation
========================================

Die Wetterstation kann über ein Embedded Board wie z.B. das Raspberry Pi
gesteuert werden. Das Raspberry Pi kann direkt in das Gehäuse eingebaut werden
auch wenn es nicht einfach ist alles zu integrieren.

Wir installieren einen :ref:`Master Brick <master_brick>`,
eine :ref:`Step-Down Power Supply <step_down_power_supply>`, ein :ref:`DC Jack
Adapter <dc_jack_adapter>` und das Raspberry Pi im Gehäuse.
Das Raspberry Pi (und der Master Brick) werden über den DC Jack Adapter durch
die Step-Down Power Supply versorgt.

Wie der DC Jack Adapter befestigt werden kann ist oben beschrieben
(:ref:`starter_kit_weather_station_construction_wifi`).

Die Step-Down Power Supply (mit dem Master Brick obenauf) ist über
10mm Abstandsbolzen befestigt. Die SD Karte kann dabei unter die Step-Down
Power Supply geschoben werden. Der Micro USB Stecker führt dabei links
an dem Step-Down Power Supply Abstandsbolzen vorbei. Über die Ausschnitte
im Gehäuse kann das Raspberry Pi mittels Kabelbindern befestigt werden.

Der grüne 5V Ausgang auf der Step-Down Power Supply wird dazu genutzt
um das Raspberry Pi über einen Micro USB Stecker mit Strom zu versorgen.
Der schwarze Stecker ist hingegen mit dem DC Jack Adapter verbunden.
Der Master Brick wird einfach mit einem kurzen Mini USB Kabel an das Raspberry
Pi angeschlossen.

.. image:: /Images/Kits/weather_station_construction_rpi_front_350.jpg
   :scale: 100 %
   :alt: Raspberry Pi Wetterstation Aufbau Schritt 1
   :align: center
   :target: ../../_images/Kits/weather_station_construction_rpi_front_1200.jpg

Auf der Rückansicht sehen wir wie das Raspberry Pi eingebaut wurde.

.. image:: /Images/Kits/weather_station_construction_rpi_back_350.jpg
   :scale: 100 %
   :alt: Raspberry Pi Wetterstation Aufbau Schritt 2
   :align: center
   :target: ../../_images/Kits/weather_station_construction_rpi_back_1200.jpg

So wie das Raspberry Pi verbaut wurde kann auch ein Netzwerkkabel angeschlossen
werden. Natürlich ist es auch möglich das Raspberry Pi 180° gedreht einzubauen.
Hierdurch kann ein kürzeres Mini USB Kabel verwendet werden, aber die Ethernet
Buchse ist nicht mehr so gut zugänglich.

Die Befestigung des Raspberry Pis an der Außenseite der Rückseite stellt eine
weitere Möglichkeit dar.
