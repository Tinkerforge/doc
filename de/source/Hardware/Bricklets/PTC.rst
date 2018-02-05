
:shoplink: ../../../shop/bricklets/ptc-bricklet.html

.. include:: PTC.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ptc_bricklet:

PTC Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ptc_tilted_[?|?].jpg      PTC Bricklet
	Bricklets/bricklet_ptc_vertical_[?|?].jpg    PTC Bricklet
	Bricklets/bricklet_ptc_horizontal_[?|?].jpg  PTC Bricklet
	Bricklets/bricklet_ptc_sensor_[100|600].jpg  PTC Bricklet with 3-wire Pt100 RTD
	Bricklets/bricklet_ptc_jumper_[100|600].jpg  PTC Bricklet
	Cases/bricklet_ptc_case_[100|600].jpg        PTC Bricklet im Gehäuse
	Bricklets/bricklet_ptc_brickv_[100|].jpg     PTC Bricklet im Brick Viewer
	Dimensions/ptc_dimensions_[100|600].png      Umriss und Bohrplan

	{% tfgalleryend %}

Features
--------

* Unterstützt Pt100 und Pt1000 Sensoren
* Unterstützt 2-Leiter, 3-Leiter und 4-Leiter Typ
* Misst Temperaturen mit 0,5% Genauigkeit auf der vollen Skala von -246 bis 849°C
* Auflösung von 0,03125°C (15Bit), Ausgabe in 0,01°C Schritten


.. _ptc_bricklet_description:

Beschreibung
------------

Mit dem PTC :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Temperaturen über Pt100 und Pt1000
Sensoren messen. 

Es können Pt100 und Pt1000 Sensoren vom Typ 2-Leiter, 3-Leiter und 4-Leiter
verwendet werden.

Die gemessene Temperatur kann in `°C
<https://de.wikipedia.org/wiki/Grad_Celsius>`__ ausgelesen werden. Zusätzlich
können Events konfiguriert werden die ausgelöst werden wenn eine bestimmte
Temperatur über- oder unterschritten wird.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
RTD-zu-Digital-Wandler            MAX31865
Stromverbrauch                    2mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Unterstütze Pt-Sensor Typen       Pt100 und Pt1000 mit 2-Leiter, 3-Leiter oder 4-Leiter
Genauigkeit                       Mindestens 0,5% auf voller Skala
Eingangsschutz                    +-50V
Temperaturauflösung               0,03125°C (15Bit)
Konvertierungszeit                21ms
Fehlerdetektion                   Open RTD element, RTD value out-of-range, short across RTD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             35 x 30 x 15mm (1,38 x 1,18 x 0,59")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* MAX31865 Datenblatt (`Download <https://github.com/Tinkerforge/ptc-bricklet/raw/master/datasheets/MAX31865.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ptc-bricklet/raw/master/hardware/ptc-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ptc_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ptc-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2knGTQP>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/ptc/ptc.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/ptc/ptc.FCStd>`__)


.. _ptc_bricklet_jumper_configuration:

Jumper-Konfiguration
--------------------

Konfiguriere die Jumper für Pt100/Pt1000 Sensor und für 2/3/4-Leiter Typ
wie unten dargestellt. Die rot markierten Stifte der Stiftleisten müssen für
den korrespondierenden Sensortyp mit einem Jumper überbrückt werden.

.. image:: /Images/Bricklets/bricklet_ptc_pt_wire_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet Jumper-Konfiguration
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_pt_wire_1000.jpg

.. _ptc_bricklet_connectivity:

Anschlussmöglichkeiten
----------------------

Die folgenden Verbindungsdiagramme zeigen wie
Widerstandsthermometer vom Typ 2/3/4-Leiter angeschlossen werden können:

.. image:: /Images/Bricklets/bricklet_ptc_connectivity_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet Verbindungsdiagramme
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_connectivity_1000.jpg

Zusätzlich muss die Leiteranzahl mit Hilfe der API gesetzt werden.

.. _ptc_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| sowie ein Pt100/1000 Sensor angeschlossen werden (siehe folgendes Bild).
In diesem Beispiel wird ein 3-Leiter Pt100 Sensor verwendet.

.. image:: /Images/Bricklets/bricklet_ptc_sensor_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet mit 3-Leiter Pt100 Sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_sensor_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_ptc_brickv.jpg
   :scale: 100 %
   :alt: PTC Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_brickv.jpg

Wenn der Sensor in die Hand genommen wird sollte die angezeigte Temperatur 
steigen (oder fallen wenn es im Raum sehr warm ist).

|test_pi_ref|

.. _ptc_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das PTC Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-ptc-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ptc_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für PTC Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ptc_case_1000.jpg

.. include:: PTC.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ptc_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für PTC Bricklet
   :align: center
   :target: ../../_images/Exploded/ptc_exploded.png

|bricklet_case_hint|


.. _ptc_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: PTC_hlpi.table
