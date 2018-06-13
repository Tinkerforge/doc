
.. include:: GPS.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _gps_bricklet:

GPS Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_gps_tilted_[?|?].jpg           GPS Bricklet
	Bricklets/bricklet_gps_horizontal_[?|?].jpg       GPS Bricklet
	Bricklets/bricklet_gps_battery_[100|600].jpg      GPS Bricklet
	Cases/bricklet_gps_case_[100|600].jpg             GPS Bricklet im Gehäuse
	Bricklets/bricklet_gps_brickv_[100|].jpg          GPS Bricklet im Brick Viewer
	Dimensions/gps_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

.. note::

 Das GPS Bricklet ist abgekündigt und wird nicht mehr verkauft.
 Als Ersatz wird das :ref:`GPS Bricklet 2.0 <gps_v2_bricklet>`
 empfohlen.

Features
--------

* Empfängt Bewegungs-, Positions-, Höhen- und Zeitdaten
* Interne Antenne, externe Antenne optional
* 66 Kanäle, 10Hz Update-Rate
* Hohe Empfindlichkeit und Genauigkeit, Störunterdrückung


.. _gps_bricklet_description:

Beschreibung
------------
Mit dem GPS :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` über 
`GPS <https://de.wikipedia.org/wiki/GPS>`__ ihre Position bestimmen.
Es ist auch möglich Bewegungsdaten (Richtung und Geschwindigkeit),
Höheninformationen (Höhe und 
`Geodial Separation <https://de.wikipedia.org/wiki/World_Geodetic_System_1984>`__),
sowie hochgenaue Zeit- und Datumsinformationen zu bekommen.

Das verwendete GPS Modul ist optimiert auf eine sehr kurze Zeit bis
zum ersten Fix, verfügt über eine hohe Empfindlichkeit (-165dBm) und 
liefert mit 10Hz Updatefrequenz auch schnell genug Daten für Drohnen o.ä. 
Eine interne Störunterdrückung verbessert den Empfang wenn Bluetooth- 
oder WLAN-Geräte in der Nähe sind.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
GPS Modul Chipsatz                MTK MT3339 (PA6H Modul)
Stromverbrauch                    35mA (Acquisition), 30mA (Tracking)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Empfindlichkeit                   -148dBm (Acquisition), -165dBm (Tracking)*
Positionsgenauigkeit              3,0m (50% CEP)*
Zeit bis erster Fix               < 35s (ohne Batterie), < 1s (mit Batterie)*
Update-Rate                       10Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 35 x 12mm (1,57 x 1,38 x 0,47")
Gewicht                           12g (ohne Batterie)
================================  ============================================================

\* Datenblattangaben


Ressourcen
----------

* PA6H Datenblatt (`Download <https://github.com/Tinkerforge/gps-bricklet/raw/master/datasheets/FGPMMOPA6H.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/gps-bricklet/raw/master/hardware/gps-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/gps_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/gps-bricklet/zipball/master>`__)

Externe Antenne
---------------

Über einen `U.FL <https://en.wikipedia.org/wiki/Hirose_U.FL>`__ Stecker können
externe Antennen angeschlossen werden. Dies ist sinnvoll wenn die Antenne
an einer anderen Position verbaut werden oder wenn der Empfang verbessert
werden soll. Das Modul erkennt automatisch die externe Antenne und schaltet um.

Der Anschluss ist kurzschlussfest und versorgt die Antenne mit 3,3V/28mA.
Die externe Antennen sollte folgende Anforderungen erfüllen:

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Polarisation                      Rechtsdrehend polarisiert
Frequenzbereich                   1,57542GHz ± 1,023MHz
Stromversorgung                   3,0V bis 3,6V mit 4mA bis 20mA
Verstärkung                       > +15dBi
Impedanz                          50Ω
Rauschfaktor                      < 1,5dB
================================  ============================================================


.. _gps_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_gps_brickv.jpg
 :scale: 100 %
 :alt: GPS Bricklet im Brick Viewer
 :align: center
 :target: ../../_images/Bricklets/bricklet_gps_brickv.jpg

|test_pi_ref|


.. _gps_bricklet_fix_led:

Fix LED
-------

Die blaue "Fix" LED zeigt den Status der Positionsdaten an. Wenn kein Fix
vorhanden ist (Positionsdaten sind ungültig), dann blinkt die LED in einem
1 Sekunden Muster. Sobald ein Fix erreicht wurde geht die blaue LED aus und
die Positionsdaten sind gültig.


.. _gps_bricklet_case:

Gehäuse
-------

Ein laser-geschnittenes Gehäuse für das GPS Bricklet war verfügbar, wird
aber nicht mehr verkauft.

.. image:: /Images/Cases/bricklet_gps_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für GPS Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_gps_case_1000.jpg

.. include:: GPS.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/gps_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für GPS Bricklet
   :align: center
   :target: ../../_images/Exploded/gps_exploded.png

|bricklet_case_hint|


.. _gps_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: GPS_hlpi.table
