.. include:: Voltage_Current.substitutions


.. _voltage_current_bricklet:

Voltage/Current Bricklet
========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_voltage_current_tilted_350.jpg",
	               "Bricklets/bricklet_voltage_current_tilted_600.jpg",
	               "Voltage/Current Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_horizontal_100.jpg",
	             "Bricklets/bricklet_voltage_current_horizontal_600.jpg",
	             "Voltage/Current Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_vertical_100.jpg",
	             "Bricklets/bricklet_voltage_current_vertical_600.jpg",
	             "Voltage/Current Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_setup_100.jpg",
	             "Bricklets/bricklet_voltage_current_setup_600.jpg",
	             "Voltage/Current Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_brickv_100.jpg",
	             "Bricklets/bricklet_voltage_current_brickv.jpg",
	             "Voltage/Current Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/voltage_current_bricklet_dimensions_100.png",
	             "Dimensions/voltage_current_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Auflösung 1mW, 1mV, 1mA über kompletten Messbereich
* Misst Leistung, Spannung und Strom bis zu 720W/36V/20A
* Bidirektionale Strommessung (z.B. Laden/Entladen)
* Konfigurierbare Mittelwertbildung, ADC-Wandlungszeit

Beschreibung
------------

Mit dem Voltage/Current :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` um die Fähigkeit Leistung/Spannung/Strom
zu messen erweitert werden. Das Bricklet wird einfach
zwischen Spannungsversorgung (z.B. Batterie) und Last (z.B. Motor) eingebaut.

In akkubetriebenen Systemen können über die bidirektionale Strommessung
Aussagen über den Ladezustand des Akkus getroffen werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            INA226 + 4m Ohm Shunt Widerstand
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximaler Strom                   +-20A
Maximale Spannung                 36V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (L x B x H)             30 x 30 x 18mm (1.18 x 1.18 x 0.67")
Gewicht                           10g
================================  ============================================================


Resourcen
---------

* INA226 Datenblatt (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/raw/master/datasheets/INA226.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/raw/master/hardware/voltage-current-bricklet-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/voltage_current_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Voltage/Current Bricklet wird einfach zwischen Stromversorgung und der 
Last eingebaut. Schließe an die Klemme beschriftet mit "IN" die 
Stromversorgung an. An die Klemme "OUT" die Last. Die Polung ist mit "+" 
und "-" vor der Klemme gekennzeichnet.

.. warning:
Wichtig beachte die Polung beim anschließen! Das Bricklet ist nicht 
verpolungssicher!




.. _voltage_current_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

Als nächstes muss noch eine Last und eine Stromquelle mit dem Bricklet 
verbunden werden.  
Zum Beispiel einen Motor und eine Batterie wie im folgenden Bild.

.. image:: /Images/Bricklets/bricklet_voltage_current_setup_600.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet with Battery and Motor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_setup_1200.jpg

|test_tab|

Wenn alles wie erwartet funktioniert wird die Stromaufnahme des Motors 
angezeigt.
Der Graph gibt den zeitlichen Verlauf der Stromaufnahme wieder.

.. image:: /Images/Bricklets/bricklet_voltage_current_brickv.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_brickv.jpg

Der Screenshot zeigt eine hohe Spitze. Diese wird durch das Anfahren des Motors
beim Anschließen der Batterie verursacht.

|test_pi_ref|


.. _voltage_current_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine
detaillierte Beschreibung.

.. include:: Voltage_Current_hlpi.table
