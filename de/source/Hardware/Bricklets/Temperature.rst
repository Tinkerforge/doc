
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Temperature Bricklet
:shoplink: ../../../shop/bricklets/temperature-bricklet.html

.. include:: Temperature.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

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
	    tfdocimg("Cases/bricklet_ambient_light_case_built_up_100.jpg",
	             "Cases/bricklet_ambient_light_case_built_up_600.jpg",
	             "Temperature Bricklet im Gehäuse")
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
Stromverbrauch                    1mA
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

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_temperature_master_600.jpg
   :scale: 100 %
   :alt: Temperature Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_temperature_brickv.jpg
   :scale: 100 %
   :alt: Temperature Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_brickv.jpg

Als einfacher Test kann eine Wärmequelle wie z.B. ein Finger auf den Sensor
gelegt werden, die angezeigte Temperatur sollte steigen (oder fallen wenn es
im Raum sehr warm ist).

|test_pi_ref|


.. _temperature_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Temperature Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Temperature Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Temperature.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Temperature Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _temperature_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Temperature_hlpi.table
