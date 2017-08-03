
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Barometer Bricklet
:shoplink: ../../../shop/bricklets/barometer-bricklet.html

.. include:: Barometer.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _barometer_bricklet:

Barometer Bricklet
==================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_barometer_tilted_[?|?].jpg           Barometer Bricklet
	Bricklets/bricklet_barometer_vertical_[?|?].jpg         Barometer Bricklet
	Bricklets/bricklet_barometer_horizontal_[?|?].jpg       Barometer Bricklet
	Cases/bricklet_ambient_light_case_built_up_[?|?].jpg    Barometer Bricklet im Gehäuse
	Bricklets/bricklet_barometer_brickv_[100|].jpg          Barometer Bricklet im Brick Viewer
	Dimensions/barometer_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

Features
--------

* Misst Luftdruck und Höhenänderungen
* Auflösung 0,012mbar / 0,1m
* Bereich 10 bis 1200mbar


.. _barometer_bricklet_description:

Beschreibung
------------

Mit dem Barometer :ref:`Bricklet <primer_bricklets>` können 
:ref:`Bricks <primer_bricks>` den Luftdruck im Bereich von 10 bis
1200mbar mit einer Auflösung von 0,012mbar messen. Die Messung ist intern
temperaturkompensiert.
Das Bricklet ist mit einem MS5611-01BA01 Sensor ausgestattet der auch als
Altimeter (Höhenmesser) genutzt werden kann. Da der Luftdruck sich schon über
kurze Zeiträume signifikant ändern kann ist die erreichbare Genauigkeit begrenzt.
Eine mögliche Lösung um die Genauigkeit und Stabilität der Höhenmessung zu
steigern ist Sensorfusion mit den Sensordaten eines :ref:`IMU Bricks <imu_brick>`
durchzuführen (siehe 
`Youtube Video <https://www.youtube.com/watch?v=TaqtzG7lyp0>`__).


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            MS5611-01BA01
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Luftdruck Bereich                 10 - 1200mbar
Auflösung                         0,012mbar / 0,1m
Genauigkeit (25°C, 750mbar)       ±1,5mbar
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
* 3D Modell (`Online ansehen <http://a360.co/2wo7RMu>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/barometer/barometer.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/barometer/barometer.FCStd>`__)


.. _barometer_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird der Luftdruck in mbar angezeigt.
Der Graph gibt den zeitlichen Verlauf des Luftdrucks wieder.

.. image:: /Images/Bricklets/bricklet_barometer_brickv.jpg
   :scale: 100 %
   :alt: Barometer Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_barometer_brickv.jpg

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
  0,0065 °C/Meter)
* ``Tfe`` ist die Temperatur am Messort in °C
* ``H`` ist die Höhe des Messortes in Metern

`Hier <https://rechneronline.de/barometer/>`__ gibt es einen Online-Rechner der
diese Formel berechnet. Die Höhe des Messortes kann leicht mit `Google Maps
<http://www.mapcoordinates.net/de>`__ bestimmt werden.

Höhenangabe
^^^^^^^^^^^

Die Höhenangabe des Barometer Bricklets bezieht sich standardmäßig auf einen
Referenzluftdruck von 1013,25 mbar und wird mittels einer Approximation
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


.. _barometer_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Barometer Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Barometer Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Barometer.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Barometer Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _barometer_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Barometer_hlpi.table
