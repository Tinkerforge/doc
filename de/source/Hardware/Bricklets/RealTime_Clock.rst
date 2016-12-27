
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Real-Time Clock Bricklet
:shoplink: ../../../shop/bricklets/real-time-clock-bricklet.html

.. include:: RealTime_Clock.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _real_time_clock_bricklet:

Real-Time Clock Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_real_time_clock_tilted_[?|?].jpg           Real-Time Clock Bricklet
	Bricklets/bricklet_real_time_clock_horizontal_[?|?].jpg       Real-Time Clock Bricklet
	Bricklets/bricklet_real_time_clock_red_master_[100|600].jpg   Real-Time Clock Bricklet mit RED Brick und Master Brick
	Bricklets/bricklet_real_time_clock_brickv_[100|].jpg          Real-Time Clock Bricklet im Brick Viewer
	Dimensions/real_time_clock_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Batteriegepufferte Echtzeituhr
* Hundertstelsekunden Uhrzeitauflösung
* Geringer Stromverbrauch im Batteriemodus


.. _real_time_clock_bricklet_description:

Beschreibung
------------

Mit dem batteriegepufferte Real-Time Clock :ref:`Bricklet <primer_bricklets>`
können :ref:`Bricks <primer_bricks>` Datum und Uhrzeit über lange Zeiträume
genau halten, auch wenn der Brick nicht durchgehend mit Strom versorgt wird.

Dieses Bricklet kann auch verwendet werden um die Systemzeit eines
:ref:`RED Bricks <red_brick_examples>` (mit diesem `Beispielprogram
<https://github.com/Tinkerforge/red-brick/tree/master/programs/rtc_time>`__) oder
:ref:`Raspberry Pis <embedded_raspberry_pi>` zu halten.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Echtzeituhr                       PCF85263A
Stromverbrauch                    | < 5mW (< 1mA bei 5V)
                                  | 1,05µW (680nA bei 1,55V) im Batteriemodus*
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Datumsformat                      2000-01-01 bis 2099-12-31 mit Wochentag und Schaltjahre
Uhrzeitformat                     24h mit Hundertstelsekunden
Genauigkeit                       | ±20ppm (±52,6 Sekunden pro Monat) unkalibriert
                                  | bis runter zu ±1ppm (±2,6 Sekunden pro Monat) kalibriert*
Batterietyp                       SR621SW / 364 / SR60 / S621 / SG1 oder LR60 / L621 / AG1
Batterieabmessung                 6,8 x 2,2mm (0,27 x 0,09")
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             25 x 25 x 5mm (0,98 x 0,98 x 0,19")
Gewicht                           3g
================================  ============================================================

\* Datenblattangabe

Ressourcen
----------

* PCF85263A Datenblatt (`Download <https://github.com/Tinkerforge/real-time-clock-bricklet/raw/master/datasheets/PCF85263A.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/real-time-clock-bricklet/raw/master/hardware/rtc-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/real_time_clock_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/real-time-clock-bricklet/zipball/master>`__)


.. _real_time_clock_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird Datum und Zeit des Bricklets sowie
das lokale Datum und die lokale Zeit angezeigt

Datum und Zeit des Bricklets können mit dem "Save Local" Knopf auf die
das lokale Datum und die lokale Zeit gesetzt werden.

.. image:: /Images/Bricklets/bricklet_real_time_clock_brickv.jpg
   :scale: 100 %
   :alt: Real-Time Clock Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_real_time_clock_brickv.jpg

|test_pi_ref|


.. _real_time_clock_bricklet_case:

Gehäuse
-------

Coming soon...

.. _real_time_clock_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RealTime_Clock_hlpi.table
