
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#bricklets">Bricklets</a> / Industrial Dual 0-20mA Bricklet
:shoplink: ../../../shop/bricklets/industrial-dual-0-20ma-bricklet.html

.. include:: Industrial_Dual_020mA.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_0_20ma_bricklet:

Industrial Dual 0-20mA Bricklet
===============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_dual_0_20ma_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_dual_0_20ma_tilted_600.jpg",
	               "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20ma_vertical_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20ma_vertical_600.jpg",
	             "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20ma_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20ma_horizontal_600.jpg",
	             "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20ma_sensor_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20ma_sensor_600.jpg",
	             "Industrial Dual 0-20mA Bricklet mit Umgebungslichtsensor")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20ma_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20ma_brickv.jpg",
	             "Industrial Dual 0-20mA Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_dual_0_20ma_dimensions_100.png",
	             "Dimensions/industrial_dual_0_20ma_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}

Features
--------

* Präzisions-Stromsensor, misst Strom zwischen 0 und 22,5mA
* Kann IEC 60381-1 Sensoren vom Typ 2 und Typ 3 auslesen (`Einheitssignal <http://de.wikipedia.org/wiki/Einheitssignal>`__)
* Hohe Genauigkeit (0,15%), Auflösung (bis zu 0,172µA) und Abtastrate (bis zu 240 SPS)
* Es ist möglich zu detektieren ob ein Sensor angeschlossen/defekt ist


Beschreibung
------------

Mit dem Industrial Dual 0-20mA :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` Ströme von 0 bis 22,5mA gemessen werden.

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
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Messbereich                       0mA - 22,5mA
Unterstützte Sensoren             IEC 60381-1 Typ 2 und Typ 3
Genauigkeit                       0,15% mit 40ppm/°C
Auflösung                         bis zu 0,172µA (18Bit)
Abtastrate                        bis zu 240 Samples pro Sekunde
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (L x B x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           8g
================================  ============================================================


Ressourcen
----------

* MCP3423 Datenblatt (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/datasheets/mcp3423.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/hardware/industrial-dual-0-20ma-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_0_20ma_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Die folgenden Verbindungsdiagramme zeigen wie Sensoren
vom Typ 2/3 angeschlossen werden können:

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_connectivity_600.jpg
   :scale: 100 %
   :alt: Verbindungsdiagramm für Typ 2/3 Sensoren
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_connectivity_1200.jpg

.. _industrial_dual_0_20ma_bricklet_test:

Beide Sensorports ("Sensor 0" und "Sensor 1") können unabhängig
voneinander genutzt werden.

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

Ein `laser-geschnittenes Gehäuse für das Industrial Dual 0-20mA Bricklet <https://www.tinkerforge.com/de/shop/cases/case-industrial-bricklet.html>`__ ist verfügbar.

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

.. _industrial_dual_0_20ma_bricklet_programming_interfaces:

Programmierschnittstelle
------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte Beschreibung.

.. include:: Industrial_Dual_020mA_hlpi.table
