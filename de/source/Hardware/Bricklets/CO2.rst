
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / CO2 Bricklet
:shoplink: ../../../shop/bricklets/co2-bricklet.html

.. include:: CO2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _co2_bricklet:

CO2 Bricklet
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_co2_tilted1_350.jpg",
	               "Bricklets/bricklet_co2_tilted1_600.jpg",
	               "CO2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_co2_tilted2_100.jpg",
	             "Bricklets/bricklet_co2_tilted2_600.jpg",
	             "CO2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_co2_horizontal_100.jpg",
	             "Bricklets/bricklet_co2_horizontal_600.jpg",
	             "CO2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_co2_brickv_100.jpg",
	             "Bricklets/bricklet_co2_brickv.jpg",
	             "CO2 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/co2_bricklet_dimensions_100.png",
	             "Dimensions/co2_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Misst CO2 Konzentration von 0 bis 10000ppm (Teile pro Million)
* Hohe Genauigkeit von ±30ppm (gesamter Messbereich) und ±3% (Messwert)


.. _co2_bricklet_description:

Beschreibung
------------

Mit dem CO2 :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` die `CO2 Konzentration
<https://de.wikipedia.org/wiki/Kohlenstoffdioxid>`__ der Luft messen.
Die gemessene CO2 Konzentration kann in `ppm
<https://de.wikipedia.org/wiki/Parts_per_million>`__
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf
CO2 Konzentrationsänderungen zu reagieren ohne die Werte laufend abzufragen
(kein Polling notwendig).

Dieses Bricklet kann z.B. für automatische Lüftungssteuerung und
Umweltdatenmessung genutzt werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            SenseAir K30
Stromverbrauch                    | 200mW (40mA bei 5V, Idle)
                                  | 1750mW (350mA bei 5V, Messend)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Messbereich                       0ppm bis 10000ppm
Genauigkeit                       ±30ppm (gesamter Messbereich), ±3% (Messwert)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             60 x 65 x 15mm (2,36 x 2,56 x 0,59")
Gewicht                           29g
================================  ============================================================


Ressourcen
----------

* SenseAir K30 Datenblatt (`Download <https://github.com/Tinkerforge/co2-bricklet/raw/master/datasheets/K30_Datasheet.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/co2-bricklet/raw/master/hardware/co2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/co2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/co2-bricklet/zipball/master>`__)


.. _co2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_co2_brickv.jpg
   :scale: 100 %
   :alt: CO2 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_co2_brickv.jpg

|test_pi_ref|


.. _co2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: CO2_hlpi.table
