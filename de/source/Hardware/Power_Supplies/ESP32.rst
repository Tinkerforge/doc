
:shoplink: ../../../shop/power-supplies/esp32-power-supply.html

.. _esp32_power_supply:

ESP32 Power Supply
==================

.. raw:: html

	{% tfgallery %}

	Power_Supplies/psu_esp32_tilted_[?|?].jpg                  ESP32 Power Supply
	Power_Supplies/psu_esp32_tilted_bottom_[?|?].jpg           ESP32 Power Supply
	Power_Supplies/psu_esp32_w_esp_[?|?].jpg                   ESP32 Power Supply mit ESP32 Brick
	Power_Supplies/psu_esp32_w_esp_ethernet_[?|?].jpg          ESP32 Power Supply mit ESP32 Ethernet Brick

	{% tfgalleryend %}

Features
--------

* Versorgt ein ESP32 Brick oder ESP32 Ethernet Brick mit 5V
* Eingangsspannung 7V bis 27V DC

Beschreibung
------------

Die ESP32 Power Supply kann genutzt werden um einen :ref:`ESP32 Brick <esp32_brick>`
oder einen :ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>` und die damit verbundenen
:ref:`Bricklets <primer_bricklets>` mit Strom zu versorgen. Die Power Supply erzeugt 5VDC 
von einer Eingangsspannung zwischen 7V und 27V DC.

Das Modul ist 40 x 40mm groß und kann direkt über den Brickletanschlüssen
des Bricks mit 10mm Abstandsbolzen montiert werden. Die elektrische Verbindung zum Brick
erfolgt über den GPIO header des ESP32 (Ethernet) Bricks.

Technische Spezifikation
------------------------

===========================================  ============================================================
Eigenschaft                                  Wert
===========================================  ============================================================
Stromverbrauch                               20-30mA, abhängig von der Eingangsspannung
-------------------------------------------  ------------------------------------------------------------
-------------------------------------------  ------------------------------------------------------------
Minimale/Maximale Eingangsspannung           7V/27V DC
Maximaler Ausgangsstrom                      5V Versorgung: 1A
-------------------------------------------  ------------------------------------------------------------
-------------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)                      40 x 40 x 11mm  (1,57 x 1,57 x 0,43")
Gewicht                                      9g
===========================================  ============================================================

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/esp32-power-supply/raw/master/hardware/esp32-power-supply-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/esp32_power_supply_dimensions.png>`__)
* Platinenlayout (`Download <https://github.com/Tinkerforge/esp32-power-supply/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/x>`__ | Download: `STEP <https://download.tinkerforge.com/3d/power_supplies/esp32/esp32-power-supply.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/power_supplies/esp32/esp32-power-supply.FCStd>`__)

Elektrischer Anschluss und Befestigung
--------------------------------------

Um die ESP32 Power Supply auf einen ESP32 Brick oder ESP32 Ethernet Brick
aufzustecken mussen zuerst die Stiftleiste auf der Oberseite des ESP32 (Ethernet) Bricks 
eingelötet werden.

Anschließend kann die Power Supply auf den Brick mit vier
10mm Abstandsbolzen befestigt werden.

..
 Das nachfolgende Foto zeigt den elektrischen Anschluss der ESP32 Power
 Supply.

 .. image:: /Images/Power_Supplies/esp32_caption_600.jpg
    :scale: 100 %
    :alt: ESP32 Power Supply mit Beschriftung
    :align: center
    :target: ../../_images/Power_Supplies/esp32_caption_800.jpg
