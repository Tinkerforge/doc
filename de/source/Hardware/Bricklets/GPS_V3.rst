
:shoplink: ../../../shop/bricklets/gps-v3-bricklet.html

.. include:: GPS_V3.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _gps_v3_bricklet:

GPS Bricklet 3.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_gps_v3_tilted1_[?|?].jpg          GPS Bricklet 3.0
	Bricklets/bricklet_gps_v3_tilted2_[?|?].jpg          GPS Bricklet 3.0
	Bricklets/bricklet_gps_v3_top_[?|?].jpg              GPS Bricklet 3.0 Oberseite
	Bricklets/bricklet_gps_v3_brickv_[100|].jpg          GPS Bricklet 3.0 im Brick Viewer
	Dimensions/gps_v3_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Unterstützt GPS, GLONASS und Galileo gleichzeitig
* Empfängt Bewegungs-, Positions-, Höhen- und Zeitdaten sowie PPS-Signal
* Elevation, Azimuth und SNR für jeden GPS/GLONASS/Galileo Satelliten abfragbar.
* 99 Kanäle, 10Hz Update-Rate
* Hohe Empfindlichkeit und Genauigkeit, Störunterdrückung


.. _gps_v3_bricklet_description:

Beschreibung
------------

Mit dem GPS :ref:`Bricklet <primer_bricklets>` 3.0 können
:ref:`Bricks <primer_bricks>` über 
`GPS <https://de.wikipedia.org/wiki/GPS>`__ ihre Position bestimmen.
Es ist auch möglich Bewegungsdaten (Richtung und Geschwindigkeit),
Höheninformationen (Höhe und 
`Geodial Separation <https://de.wikipedia.org/wiki/World_Geodetic_System_1984>`__),
sowie hochgenaue Zeit- und Datumsinformationen mit PPS-Signal zu erhalten.

Aktuelle Werte für Elevation, Azimuth und SNR können für jeden GPS, GLONASS
und Galileo Satelliten ausgelesen werden.

Das verwendete GPS Modul ist optimiert auf eine sehr kurze Zeit bis
zum ersten Fix, verfügt über eine hohe Empfindlichkeit (-165dBm) und 
liefert mit 10Hz Updatefrequenz auch schnell genug Daten für Drohnen o.ä. 
Eine interne Störunterdrückung verbessert den Empfang wenn Bluetooth- 
oder WLAN-Geräte in der Nähe sind.

Das Bricklet hat eine interne Antenna. Über einen U.FL Stecker kann zusätzlich eine externe
Antenne verbunden werden.

Eine CR1025 Knopfzellenbatterie wird mit dem Bricklet ausgeliefert. Die Batterie
wird genutzt um Positionsinformationen zu speichern wenn die Stromversorgung
wegfällt. Mit den gespeicherten Informationen kann ein Fix schneller wieder
hergestellt werden, wenn die Stromversorgung wieder zur Verfügung steht.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
GPS Modul Chipsatz                CDTop PA1616D
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Empfindlichkeit                   -148dBm (Acquisition), -165dBm (Tracking)*
Positionsgenauigkeit              3,0m (50% CEP)*
Zeit bis erster Fix               < 35s (ohne Batterie), < 1s (mit Batterie)*
Update-Rate                       10Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 12mm (1,57 x 1,57 x 0,47")
Gewicht                           20g (mit Batterie)
Stromverbrauch                    ca. 73mA
================================  ============================================================

\* Datenblattangaben


Ressourcen
----------

* PA1616D Datenblatt (`Download <https://github.com/Tinkerforge/gps-v3-bricklet/raw/master/datasheets/PA1616D.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/gps-v3-bricklet/raw/master/hardware/gps-v3-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/gps_v3_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/gps-v3-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2BgLPRK>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/gps_v3/gps-v3.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/gps_v3/gps-v3.FCStd>`__)

Externe Antenne
---------------

Das GPS Bricklet 3.0 hat keine interne Antenne. Eine externe Antenne muss 
über einen `U.FL <https://en.wikipedia.org/wiki/Hirose_U.FL>`__ Stecker 
angeschlossen werden.

Der Stecker ist Kurzschlussfest und versorgt die Antenne mit 3.3V/20mA

Das Bricklet hat eine interne GPS-Antenne. Es ist zusätzlich möglich eine externe
Antenne  den U.FL Stecker anzuschließen. Wenn eine externe Antenna angeschlossen wird,
nutzt das Bricklet diese automatisch und die interne Antenne wird deaktiviert. Eine kompatible
Antenne mit langem Kabel gibt es `bei uns im Shop <https://www.tinkerforge.com/de/shop/gps-antenna-sma-300cm.html>`__.

Für guten Empfang muss das Bricklet so befestigt werden, dass die Antenne
nach oben zeigt.

.. _gps_v3_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_gps_v3_brickv.jpg
 :scale: 100 %
 :alt: GPS Bricklet 3.0 im Brick Viewer
 :align: center
 :target: ../../_images/Bricklets/bricklet_gps_v3_brickv.jpg

|test_pi_ref|


.. _gps_v3_bricklet_fix_led:

Fix LED
-------

Die grüne "Fix" LED zeigt den Status der Positionsdaten an. Die LED blinkt
solange kein Fix vorhanden ist und geht an sobald ein Fix erreicht ist.

Wenn das GPS-Modul per Batterie betrieben wird, geht die LED aus um Strom zu
sparen.


.. _gps_v3_bricklet_case:

Gehäuse
-------

TBD


.. _gps_v3_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: GPS_V3_hlpi.table
