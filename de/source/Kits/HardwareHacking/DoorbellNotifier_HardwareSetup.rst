
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starterkit: Hardware Hacking</a> / Hardware-Aufbau: Türklingel

.. _starter_kit_hardware_hacking_doorbell_notifier_hardware_setup:

Hardware-Aufbau: Türklingel
===========================

Der Hardwareaufbau ist sehr einfach. Typische Türklingeln werden mit 12V AC
(Wechselstrom) betrieben. Dieser wird über zwei Drähte an die Klingel angelegt.
An eine Klingel dieser Art kann das :ref:`Industrial Digital In 4 Bricklet
<industrial_digital_in_4_bricklet>` direkt parallel zur Klingel angeschlossen 
werden. Auf diese Art wird der Eingang des Bricklets getriggert wenn jemand an
der Tür klingelt. Eine genauere Beschreibung des Hardwareaufbaus findet man im
:ref:`Hardware-Aufbau <starter_kit_hardware_hacking_doorbell_notifier_hardware_setup_setup>`
Abschnitt.

Technische Beschreibung
-----------------------

Dieser Teil ist für die Leser gedacht, die in einer technischeren Beschreibung
interessiert sind.

Wenn wir einen genaueren Blick auf Graphen von Wechselspannungen werfen 
werden wir positive und negative Halbwellen sehen.

.. image:: /Images/Kits/hardware_hacking_doorbell_ac_current_plot_350.jpg
   :scale: 100 %
   :alt: Wechselstromgraph
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_ac_current_plot.jpg

Ein, an eine Wechselspannungsquelle angeschlossenes, Industrial Digital In 4
Bricklet besitzt im Eingang eine Leuchtdiode (LED im Optokoppler).
Diese wird bei jeder positive Halbwelle aufleuchten und bei jeder 
negativen Halbwelle
aus sein. Wenn also die Türklingel betätigt wird, fließt ein Strom durch die
Türklingel und durch die LED des Optokopplers. Der Eingang wird also 
getriggert.

.. _starter_kit_hardware_hacking_doorbell_notifier_hardware_setup_setup:

Hardware-Aufbau
---------------

Das Industrial Digital In 4 Bricklet ist parallel zu der Türklingel verbunden.
Der Aufbau ist im nächsten Bild abgebildet. Der dicke blaue und schwarze Draht
sind die original installierten Drähte die die Türklingel auslösen. Wir haben
einen dünneren roten und schwarzen Draht parallel dazu installiert und diese
mit dem ersten Eingang des Industrial Digital In 4 Bricklets verbunden.

.. image:: /Images/Kits/hardware_hacking_doorbell_open_350.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet mit Türklingel verbunden
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_open.jpg

Nachdem das Industrial Digital In 4 Bricklet mit der Türklingel verbunden wurde
können wir den Aufbau mit dem Brick Viewer testen. Dazu klingeln wir einfach
an der Tür und beobachten den Eingang des Bricklets. Dieser sollte zwischen
High und Low wechseln.

.. image:: /Images/Kits/hardware_hacking_doorbell_brickv_350.jpg
   :scale: 100 %
   :alt: Türklingel Signal im Brick Viewer
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_brickv.jpg

Nachdem wir das Gehäuse der Türklingel wieder geschlossen haben sieht der
Aufbau wie nachfolgend abgebildet aus. Um unsere Arbeit weniger auffällig zu
gestalten könnten wir natürlich auch längere Drähte zwischen der Türklingel
und dem Bricklet verwenden.

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_350.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet mit Türklingel verbunden (geschlossen)
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_closed.jpg

Eine andere Option ist der Einsatz einer WIFI Master Extension oder Ethernet 
Master Extension, so dass kein direkter USB Anschluss notwendig ist.

.. image:: /Images/Kits/hardware_hacking_doorbell_closed_wifi_350.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet mit Türklingel verbunden und WIFI Extension
   :align: center
   :target: ../../_images/Kits/hardware_hacking_doorbell_closed_wifi.jpg

