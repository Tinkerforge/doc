
.. include:: Industrial_PTC.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_ptc_bricklet:

Industrial PTC Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_ptc_tilted_[?|?].jpg           Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_w_connector_[?|?].jpg      Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_tilted2_[?|?].jpg          Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_horizontal_[?|?].jpg       Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_w_ptc1_[?|?].jpg           Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_w_ptc2_[?|?].jpg           Industrial PTC Bricklet
	Bricklets/bricklet_industrial_ptc_brickv_[100|].jpg          Industrial PTC Bricklet im Brick Viewer
	Dimensions/industrial_ptc_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}

Features
--------

* Unterstützt Pt100 und Pt1000 Sensoren
* Unterstützt 2-Leiter, 3-Leiter und 4-Leiter Typ
* Misst Temperaturen mit 0,05% Genauigkeit auf der vollen Skala von -246 bis 849°C
* Auflösung von 0,03125°C (15Bit), Ausgabe in 0,01°C Schritten


.. _industrial_ptc_bricklet_description:

Beschreibung
------------

Mit dem Industrial PTC :ref:`Bricklet <primer_bricklets>` können
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

Das Industrial PTC Bricklet hat einen 7 Pol Bricklet Stecker und wird
mit einem ``7p-10p`` Bricklet Kabel mit einem Brick verbunden.

Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
RTD-zu-Digital-Wandler            MAX31865
Stromverbrauch                    50mW (10mA bei 5V)
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
Abmessung (W x D x H)             40 x 40 x 12mm (1,57 x 1,57 x 0,47")

Gewicht                           11g
================================  ============================================================


Ressourcen
----------

* MAX31865 Datenblatt (`Download <https://github.com/Tinkerforge/industrial-ptc-bricklet/raw/master/datasheets/MAX31865.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-ptc-bricklet/raw/master/hardware/industrial-ptc-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_ptc_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-ptc-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://a360.co/3e42mLH>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_ptc/industrial-ptc.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_ptc/industrial-ptc.FCStd>`__)


.. _industrial_ptc_bricklet_jumper_configuration:

Jumper-Konfiguration
--------------------

Konfiguriere die Jumper für Pt100/Pt1000 Sensor und für 2/3/4-Leiter Typ
wie unten dargestellt. Die rot markierten Stifte der Stiftleisten müssen für
den korrespondierenden Sensortyp mit einem Jumper überbrückt werden.

.. image:: /Images/Bricklets/bricklet_industrial_ptc_pt_wire_600.jpg
   :scale: 100 %
   :alt: Industrial PTC Bricklet Jumper-Konfiguration
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_ptc_pt_wire_1000.jpg

.. _industrial_ptc_bricklet_connectivity:

Anschlussmöglichkeiten
----------------------

Die folgenden Verbindungsdiagramme zeigen wie
Widerstandsthermometer vom Typ 2/3/4-Leiter angeschlossen werden können:

.. image:: /Images/Bricklets/bricklet_industrial_ptc_caption_600.jpg
   :scale: 100 %
   :alt: Industrial PTC Bricklet Verbindungsdiagramme
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_ptc_caption_1000.jpg

Zusätzlich muss die Leiteranzahl mit Hilfe der API gesetzt werden.

.. _industrial_ptc_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| sowie ein Pt100/1000 Sensor angeschlossen werden (siehe folgendes Bild).
In diesem Beispiel wird ein 2-Leiter Pt100 Sensor verwendet.

.. image:: /Images/Bricklets/bricklet_industrial_ptc_sensor_600.jpg
   :scale: 100 %
   :alt: Industrial PTC Bricklet mit 2-Leiter Pt100 Sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_ptc_sensor_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_industrial_ptc_brickv.jpg
   :scale: 100 %
   :alt: Industrial PTC Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_ptc_brickv.jpg

Wenn der Sensor in die Hand genommen wird sollte die angezeigte Temperatur 
steigen (oder fallen wenn es im Raum sehr warm ist).

|test_pi_ref|


.. _industrial_ptc_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial PTC Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial PTC Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_PTC.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial PTC Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_ptc_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_PTC_hlpi.table
