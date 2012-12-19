.. include:: GPS.substitutions


.. _gps_bricklet:

GPS Bricklet
============


Features
--------

* Empfängt Bewegungs-, Positions-, Höhen- und Zeitdaten
* Interne Antenne, externe Antenne optional
* 66 Kanäle, 10Hz Updaterate
* Hohe Empfindlichkeit und Genauigkeit, Störunterdrückung


Beschreibung
------------
Mit dem GPS :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` über 
`GPS <http://de.wikipedia.org/wiki/GPS>`__ ihre Position bestimmen.
Es ist auch möglich Bewegungsdaten (Richtung und Geschwindigkeit),
Höheninformationen (Höhe und 
`Geodial Separation <http://de.wikipedia.org/wiki/World_Geodetic_System_1984>`__),
sowie hochgenaue Zeit- bzw. Datumsinformationen zu bekommen.

Das verwendete GPS Modul ist optimiert auf eine sehr kurze Zeit bis
zum ersten Fix, verfügt über eine hohe Empfindlichkeit (-165dBm) und 
liefert mit 10Hz Updatefrequenz auch schnell genug Daten für Drohnen o.ä. 

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
GPS Modul Chipsatz                MTK MT3339 (PA6H Modul)
Empfindlichkeit                   -148dBm (Acquisition), -165dBm (Tracking)*
Positionsgenauigkeit              3.0m (50% CEP)*
Zeit bis erster Fix               <35s (ohne Batterie), <1s (mit Batterie)*
Update-Rate                       10Hz
================================  ============================================================
\* Datenblattangaben


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/gps-bricklet/raw/master/hardware/gps-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/gps_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/gps-bricklet/zipball/master>`__)
* PA6H Datasheet (`Download <https://github.com/Tinkerforge/gps-bricklet/raw/master/datasheets/FGPMMOPA6H.pdf>`__)

Externe Antenne
---------------

Über einen `U.FL <http://en.wikipedia.org/wiki/Hirose_U.FL>`__ Verbinder können 
externe Antennen angeschlossen werden. Dies ist sinnvoll wenn die Antenne
an einer anderen Position verbaut werden oder wenn der Empfang verbessert
werden soll. Das Modul erkennt automatisch die externe Antenne und schaltet um.

Der Anschluss ist kurzschlussfest und versorgt die Antenne mit 3.3V/28mA.
Die externe Antennen sollte folgende Anforderungen erfüllen:

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Polarisation                      Rechtsdrehend polarisiert
Frequenzbereich                   1.57542GHz +/- 1.023MHz
Stromversorgung                   3.0V - 3.6V, 4mA - 20mA
Verstärkung                       >+15dBi
Impedanz                          50 Ohm
Rauschfaktor                      < 1.5dB
================================  ============================================================


.. _gps_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

..
  .. image:: /Images/Bricklets/bricklet_gps_master_600.jpg
     :scale: 100 %
     :alt: GPS Bricklet verbunden mit Master Brick
     :align: center
     :target: ../../_images/Bricklets/bricklet_gps_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

..
  .. image:: /Images/Bricklets/bricklet_gps_brickv.jpg
     :scale: 100 %
     :alt: GPS Bricklet im Brick Viewer
     :align: center
     :target: ../../_images/Bricklets/bricklet_gps_brickv.jpg

|test_pi_ref|


.. _gps_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: GPS_hlpi.table
