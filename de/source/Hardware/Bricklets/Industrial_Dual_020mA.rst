
:shoplink: ../../../shop/bricklets/industrial-dual-0-20ma-bricklet.html

.. include:: Industrial_Dual_020mA.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _industrial_dual_0_20ma_bricklet:

Industrial Dual 0-20mA Bricklet
===============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_0_20ma_tilted_[?|?].jpg      Industrial Dual 0-20mA Bricklet
	Bricklets/bricklet_industrial_dual_0_20ma_vertical_[?|?].jpg    Industrial Dual 0-20mA Bricklet
	Bricklets/bricklet_industrial_dual_0_20ma_horizontal_[?|?].jpg  Industrial Dual 0-20mA Bricklet
	Bricklets/bricklet_industrial_dual_0_20ma_sensor_[100|600].jpg  Industrial Dual 0-20mA Bricklet mit Umgebungslichtsensor
	Cases/bricklet_industrial_case_[100|600].jpg                    Industrial Dual 0-20mA Bricklet im Gehäuse
	Bricklets/bricklet_industrial_dual_0_20ma_brickv_[100|].jpg     Industrial Dual 0-20mA Bricklet im Brick Viewer
	Dimensions/industrial_dual_0_20ma_dimensions_[100|600].png      Umriss und Bohrplan

	{% tfgalleryend %}


Features
--------

* Präzisions-Stromsensor, misst Strom zwischen 0 und 22,5mA
* Kann IEC 60381-1 Sensoren vom Typ 2 und Typ 3 auslesen
  (`Einheitssignal <https://de.wikipedia.org/wiki/Einheitssignal>`__)
* Hohe Genauigkeit (0,15%), Auflösung (bis zu 0,172µA) und Abtastrate (bis zu 240 SPS)
* Es ist möglich zu detektieren ob ein Sensor angeschlossen/defekt ist


.. _industrial_dual_0_20ma_bricklet_description:

Beschreibung
------------

Mit dem Industrial Dual 0-20mA :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Ströme von 0 bis 22,5mA gemessen werden.

Das Bricklet kann genutzt werden um bis zu zwei IEC 60381-1 Typ 2 und Typ 3 Sensoren
auszulesen 

Der gemessene Strom kann in nA ausgelesen werden. Zusätzlich
können Events konfiguriert werden die ausgelöst werden wenn ein bestimmter
Stromwert über- oder unterschritten wird.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            MCP3423
Stromverbrauch                    1mA
Maximale Versorgungsspannung      25V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Messbereich                       0mA - 22,5mA
Unterstützte Sensoren             IEC 60381-1 Typ 2 und Typ 3
Genauigkeit                       0,15% mit 40ppm/°C
Auflösung                         bis zu 0,172µA (18Bit)
Abtastrate                        bis zu 240 Samples pro Sekunde
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* MCP3423 Datenblatt (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/datasheets/mcp3423.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/hardware/industrial-dual-0-20ma-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_0_20ma_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://autode.sk/2BflPX6>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_dual_0_20ma/industrial-dual-0-20ma.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_dual_0_20ma/industrial-dual-0-20ma.FCStd>`__)


Anschlussmöglichkeit
--------------------

Die folgenden Verbindungsdiagramme zeigen wie Sensoren
vom Typ 2/3 angeschlossen werden können:

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_connectivity_600.jpg
   :scale: 100 %
   :alt: Verbindungsdiagramm für Typ 2/3 Sensoren
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_connectivity_1200.jpg


Beide Sensorports ("Sensor 0" und "Sensor 1") können unabhängig
voneinander genutzt werden. Über den "Supply" Eingang können die Sensoren 
versorgt werden (bis zu 48V).

.. _industrial_dual_0_20ma_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| sowie eine Stromquelle (siehe folgendes Bild).
In diesem Beispiel nutzen wir einen 4-20mA Umgebungslichtsensor.

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_sensor_600.jpg
   :scale: 100 %
   :alt: Industrial Dual 0-20mA Bricklet mit Umgebungslichtsensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_sensor_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual 0-20mA Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_brickv.jpg

Bei Interaktion mit dem Sensor sollte sich der Stromwert entsprechend
im Brick Viewer ändern.

|test_pi_ref|


.. _industrial_dual_0_20ma_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Industrial Dual 0-20mA Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Industrial Dual 0-20mA Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Dual_020mA.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Industrial Dual 0-20mA Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_dual_0_20ma_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Industrial_Dual_020mA_hlpi.table
