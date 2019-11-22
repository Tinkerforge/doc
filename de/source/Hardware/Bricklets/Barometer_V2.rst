
:shoplink: ../../../shop/bricklets/barometer-v2-bricklet.html

.. include:: Barometer_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _barometer_v2_bricklet:

Barometer Bricklet 2.0
======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_barometer_v2_tilted_[?|?].jpg           Barometer Bricklet 2.0
	Bricklets/bricklet_barometer_v2_top_[?|?].jpg              Barometer Bricklet 2.0
	Bricklets/bricklet_barometer_v2_brickv_[100|].jpg          Barometer Bricklet 2.0 im Brick Viewer
	Dimensions/barometer_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst Luftdruck, Temperatur und Höhenänderungen
* Auflösung 0,0075hPa / 6,25cm
* Bereich 260 bis 1260hPa


.. _barometer_v2_bricklet_description:

Beschreibung
------------

Mit dem Barometer :ref:`Bricklet <primer_bricklets>` 2.0 können 
:ref:`Bricks <primer_bricks>` den Luftdruck im Bereich von 260 bis
1260hPa mit einer Auflösung von 0,0075hPa messen. Die Messung ist intern
temperaturkompensiert.

Das Bricklet ist mit einem LPS22HB Sensor ausgestattet der auch als
Altimeter (Höhenmesser) genutzt werden kann. Da der Luftdruck sich schon über
kurze Zeiträume signifikant ändern kann ist die erreichbare Genauigkeit begrenzt.
Eine mögliche Lösung um die Genauigkeit und Stabilität der Höhenmessung zu
steigern ist Sensorfusion mit den Sensordaten eines :ref:`IMU Brick 2.0 <imu_v2_brick>`
durchzuführen (siehe `Youtube Video <https://www.youtube.com/watch?v=TaqtzG7lyp0>`__).

Das Barometer Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            LPS22HB
Stromverbrauch                    30mW (6mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Luftdruckbereich                  260 bis 1260hPa
Auflösung                         0,0075hPa / 6,25cm
Genauigkeit (0-65°C)              ±1,1hPa unkalibriert, ±0,2hPa kalibriert
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Temperaturbereich                 -40 bis +85°C
Auflösung                         0,01°C
Genauigkeit                       ±1,5°C
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           1,6g
================================  ============================================================

\* OPC = One-Point Calibration, siehe TODO

Ressourcen
----------

* LPS22HB Datenblatt (`Download <https://github.com/Tinkerforge/barometer-v2-bricklet/raw/master/datasheets/LPS22HB.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/barometer-v2-bricklet/raw/master/hardware/barometer-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/barometer_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/barometer-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2NYG7XC>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/barometer_v2/barometer-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/barometer_v2/barometer-v2.FCStd>`__)


.. _barometer_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird der Luftdruck in hPa angezeigt.
Der Graph gibt den zeitlichen Verlauf des Luftdrucks wieder.

.. image:: /Images/Bricklets/bricklet_barometer_v2_brickv.jpg
   :scale: 100 %
   :alt: Barometer Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_barometer_v2_brickv.jpg

|test_pi_ref|


Luftdruck verstehen
-------------------

Luftdruck ist ein kompliziertes Thema. Zwei häufig gestellte Fragen sind:
Warum weicht die Luftdruckmessung des Barometer Bricklets vom Wetterbericht ab
und warum weicht die Höhenangabe von der wirklichen Höhe des Messortes ab?

Luftdruckangabe
^^^^^^^^^^^^^^^

Das Barometer Bricklet gibt den Luftdruck in Referenz auf die Höhe des
Messortes an, in der Luftfahrt als `QFE
<https://de.wikipedia.org/wiki/Barometrische_H%C3%B6henmessung_in_der_Luftfahrt#QFE>`__
Wert bekannt. Im Wetterbericht wird der Luftdruck aber in Referenz auf Meereshöhe
und speziell temperaturkorrigiert angegeben, in der Luftfahrt als `QFF
<https://de.wikipedia.org/wiki/Barometrische_H%C3%B6henmessung_in_der_Luftfahrt#QFF>`__
Wert bekannt.

Mit der `barometrischen Höhenformel
<https://de.wikipedia.org/wiki/Barometrische_H%C3%B6henformel>`__ kann der QFF
Wert aus QFE Wert approximiert werden::

 QFF = QFE / [1 - Tg * H / (273,15 + Tfe + Tg * H)] ^ (0,034163 / Tg)

* ``Tg`` ist der Temperaturgradient, dieser gibt an, wie schnell die Temperatur
  mit steigender Höhe fällt (eine gute Schätzung bei normalem Wetter ist
  0,0065°C/m)
* ``Tfe`` ist die Temperatur am Messort in °C
* ``H`` ist die Höhe des Messortes in Metern

`Hier <https://rechneronline.de/barometer/>`__ gibt es einen Online-Rechner der
diese Formel berechnet. Die Höhe des Messortes kann leicht mit `Google Maps
<https://www.mapcoordinates.net/de>`__ bestimmt werden.

Höhenangabe
^^^^^^^^^^^

Die Höhenangabe des Barometer Bricklets bezieht sich standardmäßig auf einen
Referenzluftdruck von 1013,25hPa und wird mittels einer Approximation
des `International Standard Atmosphere <https://de.wikipedia.org/wiki/Normatmosph%C3%A4re>`__
Modells berechnet. Eine so bestimmte Höhe ist in der Luftfahrt als `QNE
<https://de.wikipedia.org/wiki/Barometrische_H%C3%B6henmessung_in_der_Luftfahrt#QNE>`__
Wert bekannt.

Für eine genauere Höhenangabe in Referenz auf Meereshöhe muss der
Referenzluftdruck für den Messort angegeben werden. In der Luftfahrt wird
hierfür der `QNH
<https://de.wikipedia.org/wiki/Barometrische_H%C3%B6henmessung_in_der_Luftfahrt#QNH>`__
Wert verwendet. Daher ist dieser Wert häufig bei Flugplätze zu erfahren.
Es kann aber auch der QFF Wert verwendet werden, bei diesem Wert fließt die
Temperatur anders in die Berechnung ein als beim QNH Wert, der QFF Wert ist
aber typischerweise dem QNH Wert ähnlich.

.. _barometer_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Barometer Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Barometer Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Barometer_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Barometer Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _barometer_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Barometer_V2_hlpi.table
