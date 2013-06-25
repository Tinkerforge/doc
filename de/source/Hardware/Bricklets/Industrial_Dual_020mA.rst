
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#bricklets">Bricklets</a> / Industrial Dual 0-20mA Bricklet
:shoplink: ../../../shop/bricklets/industrial-dual-0-20-ma-bricklet.html

.. include:: Industrial_Dual_020mA.substitutions


.. _industrial_dual_0_20_ma_bricklet:

Industrial Dual 0-20mA Bricklet
===============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_dual_0_20_ma_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_dual_0_20_ma_tilted_600.jpg",
	               "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20_ma_vertical_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20_ma_vertical_600.jpg",
	             "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20_ma_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20_ma_horizontal_600.jpg",
	             "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20_ma_master_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20_ma_master_600.jpg",
	             "Industrial Dual 0-20mA Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20_ma_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20_ma_brickv.jpg",
	             "Industrial Dual 0-20mA Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_dual_0_20_ma_bricklet_dimensions_100.png",
	             "Dimensions/industrial_dual_0_20_ma_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}

Features
--------

* Präzisions-Stromsensor, misst Strom zwischen 0 und 22.5mA
* Kann IEC 60381-1 Sensoren vom Typ 2 und Typ 3 auslesen (`Einheitssignal <http://de.wikipedia.org/wiki/Einheitssignal>`__)
* Hohe Genauigkeit (0,15%), Auflösung (bis zu 0,172µA) und Abtastrate (bis zu 240 SPS)
* Es ist möglich zu detektieren ob ein Sensor angeschlossen/defekt ist


Beschreibung
------------

Mit dem Industrial Dual 0-20mA :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` Ströme von 0 bis 22.5mA gemessen werden. 

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
Auflösung                         bis zu 0,172µA (18 bit)
Abtastrate                        bis zu 240 Samples pro Sekunde
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (L x B x H)           40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Gewicht                           TBD
================================  ============================================================


Ressourcen
----------

* Datenblatt (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/datasheets/mcp3423.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/hardware/industrial-dual-0-20ma-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/industrial_dual_0_20ma_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Die folgenden Verbindungsdiagramme zeigen wie Sensoren
vom Typ 2/3 angeschlossen werden können:

.. http://commons.wikimedia.org/wiki/File:Einheitssignal-type-2.svg
.. http://commons.wikimedia.org/wiki/File:Einheitssignal-type-3.svg

.. _industrial_dual_0_20_ma_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| sowie eine Stromquelle (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_ptc_master_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert sollte der Tab wie im folgenden Bild
aussehen.

.. image:: /Images/Bricklets/bricklet_ptc_brickv.jpg
   :scale: 100 %
   :alt: PTC Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_brickv.jpg

Bei Interaktion mit dem Sensor sollte sich der Stromwert entsprechend
im Brick Viewer ändern.

|test_pi_ref|

.. _industrial_dual_0_20_ma_bricklet_programming_interfaces:

Programmierschnittstelle
------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte Beschreibung.

.. include:: Industrial_Dual_020mA_hlpi.table
