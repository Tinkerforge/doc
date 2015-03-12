
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#starterkits">Starterkits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html#konstruktion">Starterkit: Wetterstation</a> / Konstruktion: Raspberry Pi Wetterstation

.. _starter_kit_weather_station_construction_raspberry_pi:

Konstruktion: Raspberry Pi Wetterstation
========================================

Die Wetterstation kann über ein Embedded Board wie z.B.
dem :ref:`Raspberry Pi <embedded_raspberry_pi>`
gesteuert werden. Das Raspberry Pi kann direkt in das Gehäuse eingebaut werden
auch wenn es nicht einfach ist alles zu integrieren.

Wir installieren einen :ref:`Master Brick <master_brick>`,
eine :ref:`Step-Down Power Supply <step_down_power_supply>`, einen :ref:`DC Jack
Adapter <dc_jack_adapter>` und das Raspberry Pi im Gehäuse.
Das Raspberry Pi (und der Master Brick) werden über den DC Jack Adapter durch
die Step-Down Power Supply versorgt. Zur Stromversorgung des Raspberry Pi haben
wir den Stecker eines Micro USB Kabel abgeschnitten und die 
Stromversorgungsadern (5V, GND) mit dem 2 Pol Stecker verbunden, der bei der 
Step-Down Power Supply dabei ist (siehe Foto). 
Ist unklar welches die 5V und GND Ader ist, so kann die Belegung im Internet 
gefunden werden.

.. image:: /Images/Kits/weather_station_construction_rpi_micro_usb_cable_350.jpg
   :scale: 100 %
   :alt: Micro USB Kabel zur Stromversorgung des Raspberry Pi
   :align: center
   :target: ../../_images/Kits/weather_station_construction_rpi_micro_usb_cable_1200.jpg

Die Raspberry Pi Wetterstation ist eine Erweiterung der :ref:`Basisversion
<starter_kit_weather_station_construction_basic>`. Daher sollte zuerst die
Basisversion aufgebaut und dann, wie im Folgenden beschrieben, abgewandelt
werden.

Stapel und Raspberry Pi an Rückseite
------------------------------------

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

Wie der DC Jack Adapter befestigt werden kann ist in
der :ref:`WLAN Wetterstations <starter_kit_weather_station_construction_wifi>`
Aufbauanleitung beschrieben.

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
