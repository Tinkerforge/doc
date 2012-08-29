.. _temperature_bricklet:

Temperature Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_temperature_tilted_350.jpg",
	               "Bricklets/bricklet_temperature_tilted_600.jpg",
	               "Temperature Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_vertical_100.jpg",
	             "Bricklets/bricklet_temperature_vertical_600.jpg",
	             "Temperature Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_horizontal_100.jpg",
	             "Bricklets/bricklet_temperature_horizontal_600.jpg",
	             "Temperature Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_master_100.jpg",
	             "Bricklets/bricklet_temperature_master_600.jpg",
	             "Temperature Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_brickv_100.jpg",
	             "Bricklets/bricklet_temperature_brickv.jpg",
	             "Temperature Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/temperature_bricklet_dimensions_100.png",
	             "Dimensions/temperature_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Umgebungstemperatur mit **0,5°C** Genauigkeit
* Temperaturbereich von -40°C bis 125°C
* Ausgabe in 0,1°C Schritten (12Bit Auflösung)


Beschreibung
------------

Mit dem Temperature :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` Temperaturen messen. Die gemessene
Temperatur kann in `°C
<http://de.wikipedia.org/wiki/Grad_Celsius>`__ ausgelesen werden. Zusätzlich
können Events konfiguriert werden die ausgelöst werden wenn eine bestimmte
Temperatur über- oder unterschritten wird.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            TMP102
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Umgebungstemperatur               -40°C bis 125°C in 0,1°C Schritten (12Bit Auflösung)
Genauigkeit                       0,5°C
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5 mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* TMP102 Datenblatt (`Download <https://github.com/Tinkerforge/temperature-bricklet/raw/master/datasheets/tmp102.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/temperature-bricklet/raw/master/hardware/temperature-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/temperature_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/temperature-bricklet/zipball/master>`__)


.. _temperature_bricklet_test:

Teste dein Temperature Bricklet
-------------------------------

Um das Temperature Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Connect the Temperature Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable
(see picture below).

.. image:: /Images/Bricklets/bricklet_temperature_master_600.jpg
   :scale: 100 %
   :alt: Temperature Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "Temperature Bricklet" auftauchen.
Wähle diesen Tab aus.

If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_temperature_brickv.jpg
   :scale: 100 %
   :alt: Temperature Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_brickv.jpg

Put your finger on the sensor to see the
temperature rising (or falling if it is extremely warm in your room).

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <temperature_programming_interfaces>` über das
API des Temperature Bricklets und Beispiele in verschiedenen
Programmiersprachen.


.. _temperature_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Temperature_hlpi.table
