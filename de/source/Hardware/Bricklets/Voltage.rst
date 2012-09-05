.. include:: Voltage.substitutions


.. _voltage_bricklet:

Voltage Bricklet
================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_voltage_tilted_350.jpg",
	               "Bricklets/bricklet_voltage_tilted_600.jpg",
	               "Voltage Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_vertical_100.jpg",
	             "Bricklets/bricklet_voltage_vertical_600.jpg",
	             "Voltage Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_horizontal_100.jpg",
	             "Bricklets/bricklet_voltage_horizontal_600.jpg",
	             "Voltage Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_master_100.jpg",
	             "Bricklets/bricklet_voltage_master_600.jpg",
	             "Voltage Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_brickv_100.jpg",
	             "Bricklets/bricklet_voltage_brickv.jpg",
	             "Voltage Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/voltage_bricklet_dimensions_100.png",
	             "Dimensions/voltage_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Spannungen bis zu 50V
* Ausgabe in 1mV Schritten (12Bit Auflösung)


Beschreibung
------------

Mit dem Voltage :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` Spannungen messen.
Über eine Schraubklemme wird das Bricklet mit der zu messenden Spannung
verbunden. Der Messbereicht beträgt 0-50V. Die gemessene Spannung kann direkt
in `Volt <http://de.wikipedia.org/wiki/Volt>`__ ausgelesen werden.
Zusätzlich können Events definiert werden die ausgelöst werden wenn eine
bestimmte Spannung über- oder unterschritten wird.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            Spannungsteiler mit Faktor 0,0625
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Spannung                          0V - 50V in 1mV Schritten, 12Bit Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 25 x 14mm (0,98 x 0,98 x 0,55")
Gewicht                           4g
================================  ============================================================


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/voltage-bricklet/raw/master/hardware/voltage-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/voltage_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/voltage-bricklet/zipball/master>`__)


.. _voltage_bricklet_test:

Teste dein Voltage Bricklet
---------------------------

|test_intro|

|test_connect|.
Als nächstes muss noch eine Spannungsquelle mit dem Bricklet Verbunden werden.
Zum Beispiel eine Batterie wie im folgenden Bild.

.. image:: /Images/Bricklets/bricklet_voltage_master_600.jpg
   :scale: 100 %
   :alt: Voltage Bricklet mit Batterie verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird die gemessene Spannung angezeigt.
Der Graph gibt den zeitlichen Verlauf der Spannung wieder.

.. image:: /Images/Bricklets/bricklet_voltage_brickv.jpg
   :scale: 100 %
   :alt: Voltage Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_brickv.jpg

|test_pi_ref|


.. _voltage_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Voltage_hlpi.table
