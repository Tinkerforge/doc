
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Dust Detector Bricklet
:FIXME_shoplink: ../../../shop/bricklets/dust-detector-bricklet.html

.. include:: Dust_Detector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dust_detector_bricklet:

Dust Detector Bricklet
======================

.. note::
  Diese Bricklet ist noch in Entwicklung!


Features
--------

* Misst Staubdichte zwischen 0 und 500µg/m³
* Erkennt Partikel ab einer Größe von ~0,5µm

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
Stromverbrauch                        TBDmA
------------------------------------  ------------------------------------------------------------
------------------------------------  ------------------------------------------------------------
Minimale detektierbare Partikelgröße  ~0,5µm
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


.. _dust_detector_bricklet_case:

Gehäuse
-------


.. _dust_detector_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Dust_Detector_hlpi.table
