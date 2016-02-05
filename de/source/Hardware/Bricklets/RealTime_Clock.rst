
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Real-Time Clock Bricklet
:FIXME_shoplink: ../../../shop/bricklets/real-time-clock-bricklet.html

.. include:: RealTime_Clock.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _real_time_clock_bricklet:

Real-Time Clock Bricklet
========================

.. note::
  Diese Bricklet ist noch in Entwicklung!


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
:ref:`RED Bricks <red_brick>` oder :ref:`Raspberry Pis <embedded_raspberry_pi>`
zu halten.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Echtzeituhr                       PCF85263A
Stromverbrauch                    | < 5mW (< 1mA bei 5V)
                                  | 105µW (320nA bei 3,3V) im Batteriemodus*
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Datumsformat                      2000-01-01 bis 2099-12-31 mit Wochentag und Schaltjahre
Uhrzeitformat                     24h mit Hundertstelsekunden
Genauigkeit                       | ±20ppm (±52,6 Sekunden pro Monat) unkalibriert
                                  | bis runter zu ±1ppm (±2,6 Sekunden pro Monat) kalibriert*
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           TBD
Gewicht                           TBD
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

.. _real_time_clock_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: RealTime_Clock_hlpi.table
