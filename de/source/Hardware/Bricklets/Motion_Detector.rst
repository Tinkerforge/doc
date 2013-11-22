
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

* Passiver Infrarot Bewegungssensor
* Erkennt Bewegungen in einer Distanz von bis zu 7m (konfigurierbar)
* Hoher Erfassungswinkel (100°)

Beschreibung
------------

Das Motion Detector :ref:`Bricklet <product_overview_bricklets>` ist mit einem
Passive-Infrared (PIR) Sensor ausgestattet. Es kann benutzt werden um Bewegungen
von Personen und Tieren zu erkennen. Es hat eine konfigurierbare Reichweite von
3m bis 7m mit einem Erfassungswinkel von 100°.

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
Blockierzeit                      2,5s
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

|test_connect|. Anschließend muss der Bewegungssensor auf das Bricklet gesteckt
werden.

|test_tab|
Wenn alles wie erwartet funktioniert wird nun eine erkannte Bewegung
angezeigt.

.. image:: /Images/Bricklets/bricklet_motion_detector_brickv.jpg
   :scale: 100 %
   :alt: Motion Detector Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_brickv.jpg

|test_pi_ref|



Empfindlichkeit, Verzögerungs- und Blockierzeit
------------------------------------------------

.. image:: /Images/Bricklets/bricklet_motion_detector_potentiometer_caption_350.jpg
   :scale: 100 %
   :alt: Motion Detector Foto mit beschrifteten Potentiometer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_potentiometer_caption_1200.jpg

Der Sensor ist mit zwei Potentiometern ausgestattet. Mit dem rechten 
Potentiometer kann die Empfindlichkeit des Sensors und damit die 
Erkennungsreichweite (3-7m) eingestellt werden. 
Drehen des Potentiometer im Uhrzeigersinn erhöht die Erkennungsreichweite.

Mit dem linken Potentiometer wird die Verzögerungszeit (Delay Time) eingestellt
(5s-200s). Für diese Zeit bleibt der Sensor im "Bewegung erkannt" Zustand,
nachdem die erste Bewegung detektiert wurde. Drehen des Potentiometer im
Uhrzeigersinn erhöht die Verzögerungszeit.

Während der Verzögerungszeit ignoriert der Sensor Bewegung und bleibt im
"Bewegung erkannt" Zustand. Nach der Verzögerungszeit wechselt der Sensor in
den "keine Bewegung erkannt" Zustand, auch wenn weiterhin Bewegung vorhanden
ist. Der Sensor bleibt dann im "keine Bewegung erkannt" Zustand für die Dauer
der Blockierzeit von 2,5s (nicht einstellbar). Nach der Verzögerungs- und
Blockierzeit ist der Sensor wieder bereit auf Bewegung zu reagieren.

Dies bedeutet, dass der Sensor höchstens alle Verzögerungszeit plus
Blockierzeit Sekunden auf Bewegung reagiert. Bei anhaltender Bewegung wechselt
der Sensor fortlaufend zwischen "Bewegung erkannt" und "keine Bewegung erkannt"
Zustand. Dabei bleibt er für die Verzögerungszeit im "Bewegung erkannt" Zustand
und für die Blockierzeit im "keine Bewegung erkannt" Zustand.


.. _motion_detector_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Motion Detector Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-motion-detector-bricklet.html>`__ ist verfügbar.

.. FIXME image:: /Images/Cases/bricklet_motion_detector_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Motion Detector Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_motion_detector_case_built_up_1000.jpg

.. include:: Motion_Detector.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/motion_detector_exploded_350.png
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
