.. _temperature_ir_bricklet:

Temperature IR Bricklet
=======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_temperature_ir_tilted_350.jpg",
	               "Bricklets/bricklet_temperature_ir_tilted_600.jpg",
	               "Temperature IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_ir_vertical_100.jpg",
	             "Bricklets/bricklet_temperature_ir_vertical_600.jpg",
	             "Temperature IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_ir_horizontal_100.jpg",
	             "Bricklets/bricklet_temperature_ir_horizontal_600.jpg",
	             "Temperature IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_ir_master_100.jpg",
	             "Bricklets/bricklet_temperature_ir_master_600.jpg",
	             "Temperature IR Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_ir_brickv_100.jpg",
	             "Bricklets/bricklet_temperature_ir_brickv.jpg",
	             "Temperature IR Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/temperature_ir_bricklet_dimensions_100.png",
	             "Dimensions/temperature_ir_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Kontaktlose Objekttemperaturmessung von -70°C bis 380°C
* Konfigurierbare Emissivität
* Misst Umgebungstemperatur von -40°C bis 85°C
* Ausgabe in 0,1°C Schritten (16Bit Auflösung)


Beschreibung
------------

Das Temperature IR :ref:`Bricklet <product_overview_bricklets>` ist mit einem
`Infrarot Thermometer <http://en.wikipedia.org/wiki/Infrared_thermometer>`__
ausgestattet. Es kann die Funktionen von Bricks mit der Möglichkeit kontaktlos
Temperatur zu messen erweitern.

Es ist möglich Objekt- und Umgebungstemperatur in `°C
<http://en.wikipedia.org/wiki/Degree_Celsius>`__ zu messen. Dabei kann die
`Emissivität <http://de.wikipedia.org/wiki/Emissionsgrad>`__ des zu messenden
Objekts eingestellt werden (die meisten Infrarot Thermometer können dies
nicht). Zusätzlich ist es möglich Events zu konfigurieren die ausgelöst werden
wenn eine bestimmte Temperatur über- oder unterschritten wird.


Technische Spezifikation
------------------------

===================================  =====================================================================
Eigenschaft                          Wert
===================================  =====================================================================
Sensor                               MLX90614ESF-BAA
-----------------------------------  ---------------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------------
Objekttemperatur                     -70°C bis 380°C in 0,1°C Schritten (16Bit Auflösung)
Umgebungstemperatur                  -40°C bis 85°C in 0,1°C Schritten (16Bit Auflösung)
Genauigkeit                          0,5°C über einen weiten Temperaturbereich
-----------------------------------  ---------------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------------
Abmessungen (B x T x H)              25 x 20 x 7mm (0,98 x 0,79 x 0,27")
Gewicht                              3g
===================================  =====================================================================


Ressourcen
----------

* MLX90614 Datenblatt (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/blob/master/datasheets/MLX90614.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/raw/master/hardware/temperature-ir-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/temperature_ir_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/zipball/master>`__)


.. _temperature_ir_bricklet_test:

Teste dein Temperature IR Bricklet
----------------------------------

Um das Temperature IR Bricklet testen zu können müssen der
:ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
sein (für Installationsanleitungen :ref:`hier <brickd_installation>`
und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
dem Brick Daemon verbunden sein.

Connect the Temperature IR Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable (see picture below).

.. image:: /Images/Bricklets/bricklet_temperature_ir_master_600.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_master_1200.jpg

Wenn du den Brick per USB an den PC anschließt sollte einen Moment später
im Brick Viewer ein neuer Tab namens "Temperature IR Bricklet" auftauchen.
Wähle diesen Tab aus.

If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_temperature_ir_brickv.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_brickv.jpg

Point the Bricklet in different
directions. The Brick Viewer will show the ambient temperature (the
temperature of the room) and the object temperature you point at.

It is possible to configure the emissivity of the material you
point at. Enter 0xFFFF = 65535 for an emissivity of 1.0.
The default is an emissivity of 0.98 (0.98 * 0xFFFF = 64224).

Nun kannst du dein eigenes Programm schreiben. Siehe den Abschnitt
:ref:`Programmierschnittstellen <temperature_ir_programming_interfaces>` über das
API des Temperature IR Bricklets und Beispiele in verschiedenen
Programmiersprachen.


.. _temperature_ir_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Temperature_IR_hlpi.table
