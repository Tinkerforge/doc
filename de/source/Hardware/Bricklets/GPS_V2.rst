
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / GPS Bricklet 2.0
:shoplink: ../../../shop/bricklets/gps-v2-bricklet.html

.. include:: GPS_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _gps_v2_bricklet:

GPS Bricklet 2.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_gps_v2_tilted_[?|?].jpg           GPS Bricklet 2.0
	Bricklets/bricklet_gps_v2_tilted_back_[?|?].jpg      GPS Bricklet 2.0
	Bricklets/bricklet_gps_v2_top_[?|?].jpg              GPS Bricklet 2.0 Oberseite
	Bricklets/bricklet_gps_v2_bottom_[?|?].jpg           GPS Bricklet 2.0 Unterseite
	Cases/bricklet_gps_v2_case_built_up1_[?|?].jpg       GPS Bricklet 2.0 im Gehäuse
	Cases/bricklet_gps_v2_case_built_up2_[?|?].jpg       GPS Bricklet 2.0 im Gehäuse
	Cases/bricklet_gps_v2_case_built_up3_[?|?].jpg       GPS Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_gps_v2_brickv_[100|].jpg          GPS Bricklet 2.0 im Brick Viewer
	Dimensions/gps_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

Features
--------

* Unterstützt GPS und GLONASS gleichzeitig (später auch Galileo durch Softwareupdate)
* Empfängt Bewegungs-, Positions-, Höhen- und Zeitdaten sowie PPS-Signal
* Elevation, Azimuth und SNR für jeden GPS/GLONASS Satelliten abfragbar.
* 99 Kanäle, 10Hz Update-Rate
* Hohe Empfindlichkeit und Genauigkeit, Störunterdrückung


.. _gps_v2_bricklet_description:

Beschreibung
------------
Mit dem GPS :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` über 
`GPS <https://de.wikipedia.org/wiki/GPS>`__ ihre Position bestimmen.
Es ist auch möglich Bewegungsdaten (Richtung und Geschwindigkeit),
Höheninformationen (Höhe und 
`Geodial Separation <https://de.wikipedia.org/wiki/World_Geodetic_System_1984>`__),
sowie hochgenaue Zeit- und Datumsinformationen mit PPS-Signal zu erhalten.

Aktuelle Werte für Elevation, Azimuth und SNR können für jeden GPS und GLONASS
Satelliten ausgelesen werden.

Das verwendete GPS Modul ist optimiert auf eine sehr kurze Zeit bis
zum ersten Fix, verfügt über eine hohe Empfindlichkeit (-165dBm) und 
liefert mit 10Hz Updatefrequenz auch schnell genug Daten für Drohnen o.ä. 
Eine interne Störunterdrückung verbessert den Empfang wenn Bluetooth- 
oder WLAN-Geräte in der Nähe sind.

Eine 25 x 25mm große aktive Patch-Antenne mit großer Verstärkung ist permanent auf
der Unterseite befestigt und über einen U.FL Stecker mit dem GPS Modul
verbunden. Die Steckverbindung kann gelöst werden um eine andere externe Antenne
anzuschließen.

Eine CR1025 Knopfzellenbatterie wird mit dem Bricklet ausgeliefert. Die Batterie
wird genutzt um Positionsinformationen zu speichern wenn die Stromversorgung
wegfällt. Mit den gespeicherten Informationen kann ein Fix schneller wieder
hergestellt werden, wenn die Stromversorgung wieder zur Verfügung steht.

Das GPS Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
GPS Modul Chipsatz                GlobalTop Firefly X1
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Empfindlichkeit                   -148dBm (Acquisition), -165dBm (Tracking)*
Positionsgenauigkeit              3,0m (50% CEP)*
Zeit bis erster Fix               < 35s (ohne Batterie), < 1s (mit Batterie)*
Update-Rate                       10Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 35 x 12mm (1,57 x 1,38 x 0,47")
Gewicht                           20g (mit Batterie und Antenne)
Stromverbrauch                    ca. 73mA
================================  ============================================================

\* Datenblattangaben


Ressourcen
----------

* FireFly X1 Datenblatt (`Download <https://github.com/Tinkerforge/gps-v2-bricklet/raw/master/datasheets/FireFly_X1.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/gps-v2-bricklet/raw/master/hardware/gps-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/gps_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/gps-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2BgLPRK>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/gps_v2/gps.step>`__,  `FreeCAD <http://download.tinkerforge.com/3d/bricklets/gps_v2/gps.FCStd>`__)

Externe Antenne
---------------

Das GPS Bricklet 2.0 hat keine interne Antenne. Eine externe Antenne muss 
über einen `U.FL <https://en.wikipedia.org/wiki/Hirose_U.FL>`__ Stecker 
angeschlossen werden.

Der Stecker ist Kurzschlussfest und versorgt die Antenne mit 3.3V/20mA

Eine 25mmx25mm Patch-Antenne gehört zum Lieferumfang des Bricklets, sie ist
an der Unterseite des Bricklets befestigt. Es ist möglich den U.FL Stecker
der Antenne zu entfernen und eine andere Antenne zu nutzen. Eine kompatible
Antenne mit langem Kabel gibt es `bei uns im Shop <https://www.tinkerforge.com/de/shop/gps-antenna-sma-300cm.html>`__.

Für guten Empfang muss das Bricklet so befestigt werden, dass die Antenne
nach oben zeigt.

.. _gps_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_gps_v2_brickv.jpg
 :scale: 100 %
 :alt: GPS Bricklet 2.0 im Brick Viewer
 :align: center
 :target: ../../_images/Bricklets/bricklet_gps_v2_brickv.jpg

|test_pi_ref|


.. _gps_v2_bricklet_fix_led:

Fix LED
-------

Die grüne "Fix" LED zeigt den Status der Positionsdaten an. Die LED blinkt
solange kein Fix vorhanden ist und geht an sobald ein Fix erreicht ist.

Wenn das GPS-Modul per Batterie betrieben wird, geht die LED aus um Strom zu
sparen.


.. _gps_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das GPS Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-gps-v2-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_gps_v2_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für GPS Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_gps_v2_case_built_up1_1000.jpg

.. include:: GPS_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/gps_v2_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für GPS Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/gps_v2_exploded.png

|bricklet_case_hint|

Das Gehäuse hat ein Loch für einen `U.FL nach SMA Adapter Kabel <https://www.tinkerforge.com/de/shop/gps-pigtail-cable.html>`__
welches genutzt werden kann um eine `externe SMA Antenne <https://www.tinkerforge.com/de/shop/gps-antenna-sma-300cm.html>`__
anzuschließen.

.. image:: /Images/Bricklets/bricklet_gps_v2_case_with_sma_antenna_600.jpg
   :scale: 100 %
   :alt: GPS Bricklet 2.0 mit SMA-Stecker und Antenne
   :align: center
   :target: ../../_images/Bricklets/bricklet_gps_v2_case_with_sma_antenna_1200.jpg


.. _gps_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: GPS_V2_hlpi.table
