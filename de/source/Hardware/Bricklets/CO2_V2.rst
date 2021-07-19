
:shoplink: ../../../shop/bricklets/co2-v2-bricklet.html

.. include:: CO2_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _co2_v2_bricklet:

CO2 Bricklet 2.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_co2_v2_tilted_[?|?].jpg           CO2 Bricklet 2.0
	Bricklets/bricklet_co2_v2_tilted2_[?|?].jpg          CO2 Bricklet 2.0
	Bricklets/bricklet_co2_v2_top_[?|?].jpg              CO2 Bricklet 2.0
	Bricklets/bricklet_co2_v2_side_[?|?].jpg             CO2 Bricklet 2.0
	Bricklets/bricklet_co2_v2_brickv_[100|].jpg          CO2 Bricklet 2.0 im Brick Viewer
	Dimensions/co2_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Misst CO2 Konzentration von 400 bis 10000ppm (Teile pro Million)
* Hohe Genauigkeit von ±30ppm (gesamter Messbereich) und ±3% (Messwert)
* Misst Temperatur und Luftfeuchtigkeit zur Kompensation
* Umgebungsluftdruck kann für zusätzliche Kompensation gesetzt werden


.. _co2_v2_bricklet_description:

Beschreibung
------------

Mit dem CO2 :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` die `CO2 Konzentration
<https://de.wikipedia.org/wiki/Kohlenstoffdioxid>`__ der Luft messen.
Die gemessene CO2 Konzentration kann in `ppm
<https://de.wikipedia.org/wiki/Parts_per_million>`__
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf
CO2 Konzentrationsänderungen zu reagieren ohne die Werte laufend abzufragen
(kein Polling notwendig).

Das Bricklet misst Temperatur und Luftfeuchte. Diese Werte werden
intern zur Kompensation genutzt und können zusätzlich ausgesen werden.

Eine weitere Kompensation kann über den Luftdruck geschehen. Dieser
kann extern gemessen und über die API gesetzt werden um weitere
Kompensationen durchzuführen und die CO2-Messung noch zu verbessern.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            Sensirion SCD30
Stromverbrauch (Durchschnitt)     60mW (12mA bei 5V)
Stromverbrauch (Peak)             400mW (80mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
CO2-Konzentration Auflösung       1ppm mit Bereich 400ppm bis 10000ppm
Temperatur Auflösung              0,01°C mit Bereich -40°C bis 70°c
Luftfeuchte Auflösung             0,01%RH mit Bereich 0%RH bis 100%RH
--------------------------------  ------------------------------------------------------------
CO2-Konzentration Genauigkeit     ±30ppm (voller Messbereich), ±3% (von Messung)
Temperatur Genauigkeit            ± (0.4°C + 0.023 × (T [°C] – 25°C))*
Luftfeuchte Genauigkeit           ± 3 %RH
--------------------------------  ------------------------------------------------------------
Messfrequenz                      0,5 Messungen pro Sekunde
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           35 x 40 x 18mm (1,38 x 1,57 x 0,71")
Gewicht                           9g
================================  ============================================================

\* Die Temperatur wird direkt am Sensor gemessen. Wenn sich das Bricklet 
in einem Gehäuse befindet, kann es vorkommen, dass sich die Temperatur im Gehäuse
anders verhält als die Umgebungsluft außerhalb des Gehäuses. Das Bricklet
besitzt eine API um diesen Unterschied auszugleichen.


Ressourcen
----------

* SCD30 Datenblatt (`Download <https://github.com/Tinkerforge/co2-v2-bricklet/raw/master/datasheets/SCD30.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/co2-v2-bricklet/raw/master/hardware/co2-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/co2_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/co2-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2VEHtyN>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/co2_v2/co2-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/co2_v2/co2-v2.FCStd>`__)


Luftdruck-Kompensation und Temperatur-Offset
--------------------------------------------

Das CO2 Bricklet 2.0 besitzt eine API um den Umgebungsluftdruck für eine
zusätzliche interne Kompensation zu setzen, um dadurch die Genauigkeit
der CO2-Konzentration zu erhöhen.

Dafür kann das :ref:`Barometer Bricklet 2.0 <barometer_v2_bricklet>` oder
:ref:`Air Quality Bricklet <air_quality_bricklet>` genutzt werden um
den Luftdruck zu messen und periodisch zu setzen.

Falls das Bricklet in einem Gehäuse verwendet wird kann es passieren, dass die
Luft im Gehäuse sich mehr erhitzt als die Umgebungsluft. Dieser
Temperatur-Offset kann mit der API kalibriert werden.
Wir empfehlen das Bricklet im Gehäuse für mindestens 24 Stunden laufen zu
lassen bis die Temperatur ein Gleichgewicht erreicht hat.


.. _co2_v2_bricklet_calibration:

CO2 Kalibrierung
----------------

Gassensoren müssen in regelmäßigen Abständen kalibriert werden. Normalerweise
wird dies über ein Prüfgas mit einer spezifizierten Menge CO2 durchgeführt.
Da dies für Sensoren zu Hause unpraktisch ist kalibriert sich der
Sensor dieses Bricklets (Sensirion SCD30) permanent automatisch selbst
(ASC).

Dies schreibt Sensirion darüber:

.. note::
 To work properly SCD30 has to see fresh air on a regular basis. Optimal 
 working conditions are given when the sensor sees fresh air for one hour 
 every day so that ASC can constantly re-calibrate. ASC only works in 
 continuous measurement mode.

Das bedeutet, dass wenn der Sensor keine Frischluft in der Zeit sieht,
er sich mit falschen Werten neu kalibriert. Die Genauigkeit des Sensors
nimmt dadurch ab.


.. _co2_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_co2_v2_brickv.jpg
   :scale: 100 %
   :alt: CO2 Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_co2_v2_brickv.jpg

|test_pi_ref|



.. _co2_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: CO2_V2_hlpi.table
