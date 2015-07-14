
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Humidity Bricklet
:shoplink: ../../../shop/bricklets/humidity-bricklet.html

.. include:: Humidity.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _humidity_bricklet:

Humidity Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_humidity_tilted_350.jpg",
	               "Bricklets/bricklet_humidity_tilted_600.jpg",
	               "Humidity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_humidity_vertical_100.jpg",
	             "Bricklets/bricklet_humidity_vertical_600.jpg",
	             "Humidity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_humidity_horizontal_100.jpg",
	             "Bricklets/bricklet_humidity_horizontal_600.jpg",
	             "Humidity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_humidity_master_100.jpg",
	             "Bricklets/bricklet_humidity_master_600.jpg",
	             "Humidity Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_ambient_light_case_built_up_100.jpg",
	             "Cases/bricklet_ambient_light_case_built_up_600.jpg",
	             "Humidity Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_humidity_brickv_100.jpg",
	             "Bricklets/bricklet_humidity_brickv.jpg",
	             "Humidity Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/humidity_bricklet_dimensions_100.png",
	             "Dimensions/humidity_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst relative Luftfeuchtigkeit
* Ausgabe in 0,1% RH Schritten (12Bit Auflösung)


.. _humidity_bricklet_description:

Beschreibung
------------

Mit dem Humidity :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` die `relative Luftfeuchtigkeit
<https://de.wikipedia.org/wiki/Relative_Luftfeuchtigkeit>`__ messen.
Die gemessene Luftfeuchtigkeit kann in Prozent direkt ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf veränderte Luftfeuchtigkeit zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Typische Anwendungen sind der Aufbau einer Wetterstation oder in
Umweltmessungen.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            HIH-5030
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Relative Luftfeuchtigkeit (RH)    0% RH - 100% RH in 0,1% RH Schritten, 12Bit Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* HIH-5030 Datenblatt (`Download <https://github.com/Tinkerforge/humidity-bricklet/raw/master/datasheets/hih-5030.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/humidity-bricklet/raw/master/hardware/humidity-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/humidity_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/humidity-bricklet/zipball/master>`__)


.. _humidity_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_humidity_master_600.jpg
   :scale: 100 %
   :alt: Humidity Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_humidity_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessen relative
Luftfeuchtigkeit des Sensors angezeigt.
Der Graph gibt den zeitlichen Verlauf der Luftfeuchtigkeit wieder.
Das folgende Bild entstand durch Ausatmen auf den Sensor. Die Luftfeuchtigkeit
steigt durch die feuchte Atemluft und fällt dann wieder ab.

.. image:: /Images/Bricklets/bricklet_humidity_brickv.jpg
   :scale: 100 %
   :alt: Humidity Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_humidity_brickv.jpg

|test_pi_ref|

.. _humidity_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Humidity Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Ambient Light Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Humidity.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Humidity Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


Troubleshooting
---------------

Wenn sich durch Kondensation genug flüssiges Wasser auf dem Sensor bildet,
entsteht ein leitender Pfad auf dem Sensor. Dies führt zu einer Messung von
0% Luftfeuchtigkeit. Sobald dieses Wasser wieder verdunstet ist nimmt der Sensor 
seinen normalen Betrieb wieder auf. Für den Einsatz in Umgebungen mit 
Kondensation empfiehlt sich eine Montage des Sensors kopfüber. Reicht dies noch
nicht aus, so kann der Sensor z.B. durch Schaumstoff geschützt werden.


.. _humidity_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Humidity_hlpi.table
