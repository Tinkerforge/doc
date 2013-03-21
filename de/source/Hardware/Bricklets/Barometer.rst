
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#bricklets">Bricklets</a> / Barometer Bricklet

.. include:: Barometer.substitutions


.. _barometer_bricklet:

Barometer Bricklet
==================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_barometer_tilted_350.jpg",
	               "Bricklets/bricklet_barometer_tilted_600.jpg",
	               "Barometer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_barometer_vertical_100.jpg",
	             "Bricklets/bricklet_barometer_vertical_600.jpg",
	             "Barometer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_barometer_horizontal_100.jpg",
	             "Bricklets/bricklet_barometer_horizontal_600.jpg",
	             "Barometer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_barometer_brickv_100.jpg",
	             "Bricklets/bricklet_barometer_brickv.jpg",
	             "Barometer Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/barometer_bricklet_dimensions_100.png",
	             "Dimensions/barometer_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}

Features
--------

* Misst Luftdruck und Höhenänderungen
* Auflösung 0,012mbar / 0,1m
* Bereich 10 bis 1200mbar


Beschreibung
------------

Mit dem Barometer Bricklet können Bricks den Luftdruck im Bereich von 10 bis
1200mbar mit einer Auflösung von 0,012mbar messen. Die Messung ist intern
temperaturkompensiert.
Das Bricklet ist mit einem MS5611-01BA01 Sensor ausgestattet der auch als
Altimeter (Höhenmesser) genutzt werden kann. Da der Luftdruck sich schon über
kurze Zeiträume signifikant ändern kann ist die erreichbare Genauigkeit begrenzt.
Eine mögliche Lösung um die Genauigkeit und Stabilität der Höhenmessung zu
steigern ist Sensorfusion mit den Sensordaten eines :ref:`IMU Bricks <imu_brick>`
durchzuführen.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            MS5611-01BA01
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Luftdruck Bereich                 10 - 1200mbar
Auflösung                         0,012mbar / 0,1m
Genauigkeit (25°C, 750mbar)       +- 1,5mbar
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* MS5611 Datenblatt (`Download <https://github.com/Tinkerforge/barometer-bricklet/raw/master/datasheets/ms5611-01ba01.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/barometer-bricklet/raw/master/hardware/barometer-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/barometer_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/barometer-bricklet/zipball/master>`__)


.. _barometer_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird der Luftdruck in mbar angezeigt.
Der Graph gibt den zeitlichen Verlauf des Luftdrucks wieder.

.. image:: /Images/Bricklets/bricklet_barometer_brickv.jpg
   :scale: 70 %
   :alt: Barometer Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_barometer_brickv.jpg

|test_pi_ref|


.. _barometer_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Barometer_hlpi.table
