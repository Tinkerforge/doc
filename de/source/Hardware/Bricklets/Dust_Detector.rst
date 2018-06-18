
:shoplink: ../../../shop/bricklets/dust-detector-bricklet.html

.. include:: Dust_Detector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dust_detector_bricklet:

Dust Detector Bricklet
======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dust_detector_tilted1_[?|?].jpg          Dust Detector Bricklet
	Bricklets/bricklet_dust_detector_tilted2_[?|?].jpg          Dust Detector Bricklet
	Bricklets/bricklet_dust_detector_horizontal_[?|?].jpg       Dust Detector Bricklet
	Bricklets/bricklet_dust_detector_brickv_[100|].jpg          Dust Detector Bricklet im Brick Viewer
	Dimensions/dust_detector_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Dust Detector Bricklet ist abgekündigt.
 Als Ersatz wird das :ref:`Particulate Matter Bricklet <particulate_matter_bricklet>`
 empfohlen.


Features
--------

* Misst Staubdichte zwischen 0 und 500µg/m³


.. _dust_detector_bricklet_description:

Beschreibung
------------

Mit dem Dust Detector :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Staubdichte messen. Die gemessene Staubdichte
kann in µg/m³ ausgelesen werden.
Mit konfigurierbaren Events ist es möglich auf Staubdichteänderungen zu
reagieren ohne die Werte laufend abzufragen (kein Polling notwendig).

Typische Anwendungsmöglichkeiten sind die Messung von Zigarettenqualm, Smog,
Hausstaub, Pollen usw.


Technische Spezifikation
------------------------

====================================  ============================================================
Eigenschaft                           Wert
====================================  ============================================================
Sensor                                GP2Y1010AU
Stromverbrauch                        120mW (24mA bei 5V)
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Auslösung                             1µg/m³
Messbereich                           0-500µg/m³
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)               60 x 50 x 20mm (2,36 x 1,97 x 0,79")
Gewicht                               26g
====================================  ============================================================


Ressourcen
----------

* GP2Y1010AU Datenblatt (`Download <https://github.com/Tinkerforge/dust-detector-bricklet/raw/master/datasheets/GP2Y1010AU.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/dust-detector-bricklet/raw/master/hardware/dust-detector-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dust_detector_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dust-detector-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2iVZbZ7>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/dust_detector/dust-detector.step>`__,  `FreeCAD <http://download.tinkerforge.com/3d/bricklets/dust_detector/dust-detector.FCStd>`__)


.. _dust_detector_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird die Staubdichte in µg/m³
angezeigt. Der Graph gibt den zeitlichen Verlauf der Staubdichte wieder.

.. image:: /Images/Bricklets/bricklet_dust_detector_brickv.jpg
   :scale: 100 %
   :alt: Dust Detector Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dust_detector_brickv.jpg

|test_pi_ref|


.. _dust_detector_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Dust_Detector_hlpi.table
