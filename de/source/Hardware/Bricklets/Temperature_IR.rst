
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#bricklets">Bricklets</a> / Temperature IR Bricklet
:shoplink: ../../../shop/bricklets/temperature-ir-bricklet.html

.. include:: Temperature_IR.substitutions


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

* MLX90614 Datenblatt (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/raw/master/datasheets/MLX90614.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/raw/master/hardware/temperature-ir-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/temperature_ir_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/zipball/master>`__)


.. _temperature_ir_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_temperature_ir_master_600.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_temperature_ir_brickv.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_brickv.jpg

Wenn der Sensor in verschiedene Richtungen gerichtet wird dann sollte sich die
Objekttemperatur abhängig vom angepeilten Objekt ändern. Die Umgebungstemperatur
sollte stabil bleiben, außer der Sensor wird z.B. durch Berührung erwärmt.

Für akkurate Messungen der Objekttemperatur ist es möglich die Emissivität
des zu messenden Materials einzustellen: 0xFFFF = 65535 entspricht einer
Emissivität von 1,0. Die Standard Emissivität ist 0,98 (0,98 * 0xFFFF = 64224).

|test_pi_ref|


.. _temperature_ir_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Temperature_IR_hlpi.table
