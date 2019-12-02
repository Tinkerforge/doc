
:shoplink: ../../../shop/bricklets/ptc-v2-bricklet.html

.. include:: PTC_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ptc_v2_bricklet:

PTC Bricklet 2.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ptc_v2_tilted_[?|?].jpg           PTC Bricklet 2.0
	Bricklets/bricklet_ptc_v2_tilted2_[?|?].jpg          PTC Bricklet 2.0
	Bricklets/bricklet_ptc_v2_top_[?|?].jpg              PTC Bricklet 2.0
	Bricklets/bricklet_ptc_v2_sensor_[?|?].jpg           PTC Bricklet 2.0 mit 2-wire Pt100 RTD
	Bricklets/bricklet_ptc_v2_jumper_[?|?].jpg           PTC Bricklet 2.0 mit Jumper
	Cases/bricklet_ptc_v2_case_[?|?].jpg                 PTC Bricklet 2.0 im Gehäuse
	Bricklets/bricklet_ptc_v2_brickv_[100|].jpg          PTC Bricklet 2.0 im Brick Viewer
	Dimensions/ptc_v2_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Unterstützt Pt100 und Pt1000 Sensoren
* Unterstützt 2-Leiter, 3-Leiter und 4-Leiter Typ
* Misst Temperaturen mit 0,05% Genauigkeit auf der vollen Skala von -246 bis 849°C
* Auflösung von 0,03125°C (15Bit)


.. _ptc_v2_bricklet_description:

Beschreibung
------------

Mit dem PTC :ref:`Bricklet <primer_bricklets>` 2.0 können
:ref:`Bricks <primer_bricks>` Temperaturen über Pt100 und Pt1000
Sensoren messen. 

Es können Pt100 und Pt1000 Sensoren vom Typ 2-Leiter, 3-Leiter und 4-Leiter
verwendet werden.

Die gemessene Temperatur kann in `°C
<https://de.wikipedia.org/wiki/Grad_Celsius>`__ ausgelesen werden. Zusätzlich
können Events konfiguriert werden die ausgelöst werden wenn eine bestimmte
Temperatur über- oder unterschritten wird.

Das Bricklet verfügt über keine galvanische Trennung zum Tinkerforge System. 
Das heißt es gibt eine direkte elektrische Verbindung zwischen den 
Anschlussklemmen des Bricklets und dem restlichen System. Sollte dies in der 
jeweiligen Anwendung zu ungewollten Verbindungen, Masseschleifen oder 
Kurzschlüssen führen, so ist der Einsatz zusammen mit einem :ref:`Isolator Bricklet <isolator_bricklet>` ratsam.

Das PTC Bricklet 2.0 hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
RTD-zu-Digital-Wandler            MAX31865
Stromverbrauch                    40mW (8mA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Unterstütze Pt-Sensor Typen       Pt100 und Pt1000 mit 2-Leiter, 3-Leiter oder 4-Leiter
Genauigkeit                       Mindestens 0,05% auf voller Skala
Eingangsschutz                    +-50V
Temperaturauflösung               0,03125°C (15Bit)
Konvertierungszeit                21ms
Fehlerdetektion                   Open RTD element, RTD value out-of-range, short across RTD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (W x D x H)             35 x 30 x 15mm (1,38 x 1,18 x 0,59")
Gewicht                           9g
================================  ============================================================


Ressourcen
----------

* MAX31865 Datenblatt (`Download <https://github.com/Tinkerforge/ptc-v2-bricklet/raw/master/datasheets/MAX31865.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ptc-v2-bricklet/raw/master/hardware/ptc-v2-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ptc_v2_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ptc-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2rjjW4L>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/ptc_v2/ptc-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/ptc_v2/ptc-v2.FCStd>`__)


.. _ptc_v2_bricklet_jumper_configuration:

Jumper-Konfiguration
--------------------

Konfiguriere die Jumper für Pt100/Pt1000 Sensor und für 2/3/4-Leiter Typ
wie unten dargestellt. Die rot markierten Stifte der Stiftleisten müssen für
den korrespondierenden Sensortyp mit einem Jumper überbrückt werden.

.. image:: /Images/Bricklets/bricklet_ptc_v2_pt_wire_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet 2.0 Jumper-Konfiguration
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_v2_pt_wire_1000.jpg

.. _ptc_v2_bricklet_connectivity:

Anschlussmöglichkeiten
----------------------

Die folgenden Verbindungsdiagramme zeigen wie
Widerstandsthermometer vom Typ 2/3/4-Leiter angeschlossen werden können:

.. image:: /Images/Bricklets/bricklet_ptc_v2_connectivity_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet 2.0 Verbindungsdiagramme
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_v2_connectivity_1000.jpg

Zusätzlich muss die Leiteranzahl mit Hilfe der API gesetzt werden.


.. _ptc_v2_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| sowie ein Pt100/1000 Sensor angeschlossen werden (siehe folgendes Bild).
In diesem Beispiel wird ein 3-Leiter Pt100 Sensor verwendet.

.. image:: /Images/Bricklets/bricklet_ptc_v2_sensor_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet mit 2-Leiter Pt100 Sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_v2_sensor_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_ptc_v2_brickv.jpg
   :scale: 100 %
   :alt: PTC Bricklet 2.0 im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_v2_brickv.jpg

Wenn der Sensor in die Hand genommen wird sollte die angezeigte Temperatur 
steigen (oder fallen wenn es im Raum sehr warm ist).

|test_pi_ref|


.. _ptc_v2_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das PTC Bricklet 2.0
<https://www.tinkerforge.com/de/shop/cases/case-ptc-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ptc_v2_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für PTC Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_ptc_v2_case_1000.jpg

.. include:: PTC_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ptc_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für PTC Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/ptc_exploded.png

|bricklet_case_hint|


.. _ptc_v2_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: PTC_V2_hlpi.table
