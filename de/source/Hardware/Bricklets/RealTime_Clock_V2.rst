
:DISABLED_shoplink: ../../../shop/bricklets/real-time-clock-v2-bricklet.html

.. include:: RealTime_Clock_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _real_time_clock_v2_bricklet:

Real-Time Clock Bricklet 2.0
============================

.. note::
  Dieses Bricklet befindet sich aktuell noch in der Entwicklung!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_real_time_clock_v2_tilted_[?|?].jpg           Real-Time Clock Bricklet 2.0
	Bricklets/bricklet_real_time_clock_v2_horizontal_[?|?].jpg       Real-Time Clock Bricklet 2.0
	Bricklets/bricklet_real_time_clock_v2_master_[100|600].jpg       Real-Time Clock Bricklet 2.0 mit Master Brick
	Cases/bricklet_real_time_clock_v2_case_[100|600].jpg             Real-Time Clock Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_real_time_clock_v2_brickv_[100|].jpg          Real-Time Clock Bricklet 2.0 im Brick Viewer
	Dimensions/real_time_clock_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Batteriegepufferte Echtzeituhr
* Hundertstelsekunden Uhrzeitauflösung
* Geringer Stromverbrauch im Batteriemodus


.. _real_time_clock_v2_bricklet_description:

Beschreibung
------------

Mit dem batteriegepufferte Real-Time Clock :ref:`Bricklet <primer_bricklets>` 2.0
können :ref:`Bricks <primer_bricks>` Datum und Uhrzeit über lange Zeiträume
genau halten, auch wenn der Brick nicht durchgehend mit Strom versorgt wird.

Dieses Bricklet kann auch verwendet werden um die Systemzeit eines
:ref:`RED Bricks <red_brick_examples>` (mit diesem `Beispielprogram
<https://github.com/Tinkerforge/red-brick/tree/master/programs/rtc_time>`__) oder
:ref:`Raspberry Pis <embedded_raspberry_pi>` zu halten.

Das Real-Time Clock Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Echtzeituhr                       PCF85263A
Stromverbrauch                    | 40mW (8mA bei 5V)
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


Ressourcen
----------

* PCF85263A Datenblatt (`Download <https://github.com/Tinkerforge/real-time-clock-bricklet/raw/master/datasheets/PCF85263A.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/real-time-clock-v2-bricklet/raw/master/hardware/real-time-clock-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/real_time_clock_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/real-time-clock-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _real_time_clock_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert wird Datum und Zeit des Bricklets sowie
das lokale Datum und die lokale Zeit angezeigt

Datum und Zeit des Bricklets können mit dem "Save Local" Knopf auf die
das lokale Datum und die lokale Zeit gesetzt werden.

.. image:: /Images/Bricklets/bricklet_real_time_clock_v2_brickv.jpg
   :scale: 100 %
   :alt: Real-Time Clock Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_real_time_clock_v2_brickv.jpg

|test_pi_ref|


.. _real_time_clock_v2_bricklet_case:

Gehäuse
-------

..
	Ein `laser-geschnittenes Gehäuse für das Real-Time Clock Bricklet 2.0
	<https://www.tinkerforge.com/de/shop/cases/case-real-time-clock-v2-bricklet.html>`__ ist verfügbar.

	.. image:: /Images/Cases/bricklet_real_time_clock_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Gehäuse für Real-Time Clock Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_real_time_clock_v2_case_1000.jpg

	.. include:: RealTime_Clock_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/real_time_clock_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Explosionszeichnung für Real-Time Clock Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/real_time_clock_v2_exploded.png

	|bricklet_case_hint|


.. _real_time_clock_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RealTime_Clock_V2_hlpi.table
