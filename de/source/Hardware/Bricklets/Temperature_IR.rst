
:shoplink: ../../../shop/bricklets/temperature-ir-bricklet.html

.. include:: Temperature_IR.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _temperature_ir_bricklet:

Temperature IR Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_temperature_ir_tilted_[?|?].jpg           Temperature IR Bricklet
	Bricklets/bricklet_temperature_ir_vertical_[?|?].jpg         Temperature IR Bricklet
	Bricklets/bricklet_temperature_ir_horizontal_[?|?].jpg       Temperature IR Bricklet
	Bricklets/bricklet_temperature_ir_master_[100|600].jpg       Temperature IR Bricklet mit Master Brick
	Cases/bricklet_temperature_ir_case_[100|600].jpg             Temperature IR Bricklet im Gehäuse
	Bricklets/bricklet_temperature_ir_brickv_[100|].jpg          Temperature IR Bricklet im Brick Viewer
	Dimensions/temperature_ir_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Kontaktlose Objekttemperaturmessung von -70°C bis 380°C
* Konfigurierbare Emissivität
* Misst Umgebungstemperatur von -40°C bis 85°C
* Ausgabe in 0,1°C Schritten (16Bit Auflösung)


.. _temperature_ir_bricklet_description:

Beschreibung
------------

Das Temperature IR :ref:`Bricklet <primer_bricklets>` ist mit einem
`Infrarot Thermometer <https://en.wikipedia.org/wiki/Infrared_thermometer>`__
ausgestattet. Es kann die Funktionen von :ref:`Bricks <primer_bricks>`, mit der 
Möglichkeit kontaktlos Temperatur zu messen, erweitern.

Es ist möglich Objekt- und Umgebungstemperatur in `°C
<https://en.wikipedia.org/wiki/Degree_Celsius>`__ zu messen. Dabei kann die
`Emissivität <https://de.wikipedia.org/wiki/Emissionsgrad>`__ des zu messenden
Objekts eingestellt werden (die meisten Infrarot Thermometer können dies
nicht). Zusätzlich ist es möglich Events zu konfigurieren die ausgelöst werden
wenn eine bestimmte Temperatur über- oder unterschritten wird.


Technische Spezifikation
------------------------

===================================  =====================================================================
Eigenschaft                          Wert
===================================  =====================================================================
Sensor                               MLX90614ESF-BAA
Stromverbrauch                       2mA
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
* 3D Modell (`Online ansehen <http://autode.sk/2BcGJWF>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/temperature_ir/temperature-ir.step>`__,  `FreeCAD <http://download.tinkerforge.com/3d/bricklets/temperature_ir/temperature-ir.FCStd>`__)


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
Emissivität von 1,0.

|test_pi_ref|

.. _temperature_ir_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Temperature IR Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-temperature-ir-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_temperature_ir_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Temperature IR Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_temperature_ir_case_1000.jpg

Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Bricklet an Oberteil mit Abstandshalter von unten und den langen Schrauben von oben,
* baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Oberteil und
* schraube Unterteil auf unteren Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des Temperature IR Bricklet-Gehäuse:

.. image:: /Images/Exploded/temperature_ir_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Temperature IR Bricklet
   :align: center
   :target: ../../_images/Exploded/temperature_ir_exploded.png

|bricklet_case_hint|


.. _temperature_ir_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Temperature_IR_hlpi.table
