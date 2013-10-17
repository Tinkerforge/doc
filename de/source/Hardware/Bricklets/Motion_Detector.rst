
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Motion Detector Bricklet
:FIXME_shoplink: ../../../shop/bricklets/motion-detector-bricklet.html

.. include:: Motion_Detector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _motion_detector_bricklet:

Motion Detector Bricklet
========================

.. note::
 Dieses Bricklet ist im Moment in der Prototyp-Phase und die Software/Hardware
 sowie die Dokumentation sind in einem unfertigen Zustand.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_motion_detector_tilted_350.jpg",
	               "Bricklets/bricklet_motion_detector_tilted_600.jpg",
	               "Motion Detector Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_motion_detector_vertical_100.jpg",
	             "Bricklets/bricklet_motion_detector_vertical_600.jpg",
	             "Motion Detector Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_motion_detector_horizontal_100.jpg",
	             "Bricklets/bricklet_motion_detector_horizontal_600.jpg",
	             "Motion Detector Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_motion_detector_master_100.jpg",
	             "Bricklets/bricklet_motion_detector_master_600.jpg",
	             "Motion Detector Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_motion_detector_brickv_100.jpg",
	             "Bricklets/bricklet_motion_detector_brickv.jpg",
	             "Motion Detector Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/motion_detector_bricklet_dimensions_100.png",
	             "Dimensions/motion_detector_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Erkennt Bewegungen in einer Distanz von bis zu 7m (konfigurierbar)
* Hoher Erfassungswinkel (100°)

Beschreibung
------------

Das Motion Detector Bricklet ist mit einem Passive-Infrared (PIR) Sensor
ausgestattet. Es kann benutzt werden um Bewegungen von Personen zu erkennen.
Es hat eine konfigurierbare Reichweite von 3m bis 7m mit einem
Erfassungswinkel von 100°.

Es ist auch möglich Events zu nutzen. Dadurch ist möglich auf eine
Bewegungserkennung zu reagieren ohne zu pollen.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Erkennungsreichweite              3-7m (konfigurierbar)
Erfassungswinkel                  100°
Verzögerungszeit                  3-200s (konfigurierbar)
Blockierungszeit                  2,5s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 45 x 30mm (0,98 x 1,78 x 1,18")
Gewicht                           12g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/motion-detector-bricklet/raw/master/hardware/motion-detector-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/motion_detector_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/motion-detector-bricklet/zipball/master>`__)


.. _motion_detector_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. FIXME image:: /Images/Bricklets/bricklet_motion_detector_master_600.jpg
   :scale: 100 %
   :alt: Motion Detector Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird nun eine erkannte Bewegung
angezeigt.

.. FIXME image:: /Images/Bricklets/bricklet_motion_detector_brickv.jpg
   :scale: 100 %
   :alt: Motion Detector Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_brickv.jpg

|test_pi_ref|

.. _motion_detector_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Motion Detector Bricklet <https://www.tinkerforge.com/de/shop/cases/case-motion-detector-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_motion_detector_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Motion Detector Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_motion_detector_case_built_up_1000.jpg

.. include:: Motion_Detector.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/motion_detector_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Motion Detector Bricklet
   :align: center
   :target: ../../_images/Exploded/motion_detector_exploded.png

|bricklet_case_hint|


.. _motion_detector_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Motion_Detector_hlpi.table
