
:DISABLED_shoplink: ../../../shop/bricklets/distance-us-v2-bricklet.html

.. include:: Distance_US_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _distance_us_v2_bricklet:

Distance US Bricklet 2.0
========================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_distance_us_v2_tilted_[?|?].jpg           Distance US Bricklet 2.0
	Bricklets/bricklet_distance_us_v2_top_[?|?].jpg              Distance US Bricklet 2.0
	Bricklets/bricklet_distance_us_v2_bottom_[?|?].jpg           Distance US Bricklet 2.0
	Bricklets/bricklet_distance_us_v2_side_[?|?].jpg             Distance US Bricklet 2.0
	Bricklets/bricklet_distance_us_v2_brickv_[100|].jpg          Distance US Bricklet 2.0 im Brick Viewer
	Dimensions/distance_us_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Entfernungen von 30cm bis 500cm mit Ultraschall
* Auflösung beträgt 1mm


.. _distance_us_v2_bricklet_description:

Beschreibung
------------

Das Distance US :ref:`Bricklet <primer_bricklets>` ist mit einem
`Ultraschall-Entfernungsmesser
<https://de.wikipedia.org/wiki/Entfernungsmessung#Laufzeitmessung>`__
ausgestattet. :ref:`Bricks <primer_bricks>` können hiermit Entfernungen zwischen 
30cm und 500cm messen. 

Mit konfigurierbaren Events ist es möglich, auf veränderte Distanzmessung
zu reagieren, ohne die Werte laufend abzufragen (kein Polling notwendig).

Das Distance US Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            MaxSonar HRLV MB1013
Stromverbrauch                    50mW (10mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Entfernungen                      30cm - 500cm
Auflösung                         1mm
Aktualisierungsrate               2Hz / 10Hz (konfigurierbar)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           35 x 35 x 20mm (1.38 x 1.38 x 0.78")
Gewicht                           9g
================================  ============================================================


Ressourcen
----------

* Datenblatt MaxSonar HRLV MB1013 (`Download <https://github.com/Tinkerforge/distance-us-v2-bricklet/raw/master/datasheets/HRLV-MaxSonar-EZ_Datasheet.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/distance-us-v2-bricklet/raw/master/hardware/distance-us-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/distance_us_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/distance-us-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2TyiysF>`__ | Download: `STEP <https://download.tinkerforge.com/3d/distance_us_v2/distance_us_v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/distance_us_v2/distance_us_v2.FCStd>`__)


.. _distance_us_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die Entfernungsmessung angezeigt.

.. image:: /Images/Bricklets/bricklet_distance_us_v2_brickv.jpg
   :scale: 100 %
   :alt: Distance US Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_us_v2_brickv.jpg

|test_pi_ref|



.. _distance_us_v2_bricklet_beam_pattern:

Beam Pattern
------------

Das Distance US Bricklet 2.0 nutzt den MB1013-Sensor von MaxBotix.

Der Sensor hat folgendes *Beam Pattern* (2d-Darstellung von
Entfernungsmessungen mit unterschiedlichem Winkel):

.. image:: /Images/Bricklets/bricklet_distance_us_v2_beam_pattern.png
   :scale: 100 %
   :alt: Distance US Bricklet 2.0 beam pattern
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_us_v2_beam_pattern.png

.. _distance_us_v2_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das Distance US Bricklet 2.0
	<https://www.tinkerforge.com/de/shop/cases/case-distance-us-v2-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_distance_us_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Distance US Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_distance_us_v2_case_1000.jpg

	.. include:: Distance_US_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/distance_us_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Distance US Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/distance_us_v2_exploded.png

	|bricklet_case_hint|


.. _distance_us_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Distance_US_V2_hlpi.table
