
:shoplink: ../../../shop/bricklets/motion-detector-bricklet.html

.. include:: Motion_Detector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _motion_detector_bricklet:

Motion Detector Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_motion_detector_tilted_[?|?].jpg           Motion Detector Bricklet
	Bricklets/bricklet_motion_detector_horizontal_[?|?].jpg       Motion Detector Bricklet
	Cases/bricklet_motion_detector_case_tilted_[?|?].jpg          Motion Detector Bricklet in Case
	Bricklets/bricklet_motion_detector_brickv_[100|].jpg          Motion Detector Bricklet im Brick Viewer
	Dimensions/motion_detector_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das Motion Detector Bricklet ist abgekündigt.
 Als Ersatz wird das :ref:`Motion Detector Bricklet 2.0 <motion_detector_v2_bricklet>`
 empfohlen.

Features
--------

* Passiver Infrarot Bewegungssensor
* Erkennt Bewegungen in einer Distanz von bis zu 7m (konfigurierbar)
* Hoher Erfassungswinkel (100°)


.. _motion_detector_bricklet_description:

Beschreibung
------------

Das Motion Detector :ref:`Bricklet <primer_bricklets>` erweitert 
:ref:`Bricks <primer>` um einen Passiv-Infrarot (PIR) Sensor. Es kann benutzt
werden um Bewegungen von Personen und Tieren zu erkennen. Es hat eine 
konfigurierbare Reichweite von 3m bis 7m mit einem Erfassungswinkel von 100°.

Es ist auch möglich Events zu nutzen. Dadurch ist möglich auf eine
Bewegungserkennung zu reagieren ohne zu pollen.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
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


.. _motion_detector_bricklet_sensitivity_delay_block_time:

Empfindlichkeit, Verzögerungs- und Blockierzeit
------------------------------------------------

.. image:: /Images/Bricklets/bricklet_motion_detector_potentiometer_caption_350.jpg
   :scale: 100 %
   :alt: Motion Detector Foto mit beschrifteten Potentiometer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_potentiometer_caption_1200.jpg

Der Sensor ist mit zwei Potentiometern ausgestattet. Mit dem rechten 
Potentiometer kann die Empfindlichkeit (Sensitivity) des Sensors und damit die
Erkennungsreichweite (3-7m) eingestellt werden. 
Drehen des Potentiometer im Uhrzeigersinn erhöht die Erkennungsreichweite.

Mit dem linken Potentiometer wird die Verzögerungszeit (Delay) eingestellt
(5s-200s). Für diese Zeit bleibt der Sensor im "Bewegung erkannt" Zustand,
nachdem keine Bewegung mehr erkannt wurde. Drehen des Potentiometer im
Uhrzeigersinn erhöht die Verzögerungszeit.

Wenn der Sensor Bewegung erkennt wechselt er in den "Bewegung erkannt" Zustand
und bleibt in diesem Zustand solange weiterhin Bewegung vorhanden ist. Nachdem
die Bewegung endet bleibt der Sensor noch für die Dauer der Verzögerungszeit im
"Bewegung erkannt" Zustand. Falls währenddessen keine Bewegung mehr erkannt wird
wechselt der Sensor in den "keine Bewegung erkannt" Zustand. Falls aber Bewegung
erkannt wird bleibt der Sensor weiterhin im "Bewegung erkannt" Zustand. Dies
bedeutet, dass der Sensor den "Bewegung erkannt" Zustand nur dann verlässt,
wenn für die Dauer der Verzögerungszeit keine Bewegung mehr erkannt wird.

Wenn der Sensor in den "keine Bewegung erkannt" Zustand gewechselt ist, dann
ignoriert er für die Dauer der Blockierzeit (2,5s, nicht einstellbar) jegliche
Bewegung. Nach dem Ablauf der Blockierzeit ist der Sensor wieder bereit auf
Bewegung zu reagieren.


Status LED
----------

Die blaue LED auf dem Bricklet ist an, wenn der Sensor im "Bewegung erkannt"
Zustand ist. Sie ist aus, wenn der Sensor im "keine Bewegung erkannt" Zustand
ist.


..
  Modifikationsmöglichkeiten
  --------------------------

  Der Bewegungssensor kann auch unabhängig vom Bricklet angebracht werden.
  Dazu muss zuerst der mitgelieferte Jumper auf die Stiftleiste wie nachfolgend
  abgebildet gesteckt werden.

  TODO Image sensor with placed jumper

  Anschließend muss eine Verbindung zwischen dem Sensor und dem Bricklet
  hergestellt werden. Dazu kann zum Beispiel, wie nachfolgend abgebildet,
  ein Kabel genutzt werden, dass an beide angelötet wird.

  TODO Image sensor <-> cable <-> Bricklet


.. _motion_detector_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Motion Detector Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-motion-detector-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_motion_detector_case_tilted_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Motion Detector Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_motion_detector_case_tilted_1000.jpg

.. include:: Motion_Detector.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/motion_detector_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Motion Detector Bricklet
   :align: center
   :target: ../../_images/Exploded/motion_detector_exploded.png

|bricklet_case_hint|


.. _motion_detector_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Motion_Detector_hlpi.table
