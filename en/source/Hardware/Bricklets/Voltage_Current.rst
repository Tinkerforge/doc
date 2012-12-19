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
	    tfdocimg("Bricklets/bricklet_voltage_current_master_100.jpg",
	             "Bricklets/bricklet_voltage_current_master_600.jpg",
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

* Measure power, voltage and current up to 720W/36V/20A
* Bidirectional current measurement (e.g. charge/discharge)
* Configurable averaging and ADC conversion time
* 1mW, 1mV, 1mA resolution

Description
-----------

The Voltage/Current :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend :ref:`Bricks <product_overview_bricks>` by the possibility to measure
power/voltage/current. To do this you only have to put the Bricklet between
your power supply (e.g. battery) and your load (e.g. motor).

In case of battery powered systems you can measure the state of the battery
by bidirectional current measurement (charge/discharge).


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            INA226 + 4m Ohm Shunt Resistor
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Current                           max +-20A
Maximum Input Voltage             36V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 18mm (1.18 x 1.18 x 0.67")
Weight                            10g
================================  ============================================================


Resources
---------

* INA226 Datasheet (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/raw/master/datasheets/INA226.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/raw/master/hardware/voltage-current-bricklet-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/voltage_current_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/zipball/master>`__)


Connectivity
------------

You have to connect the Voltage/Current Bricklet between your power supply and 
your load. Connect the power supply with the terminal marked with "IN" and the
load with the terminal "OUT". The polarity is marked with "+" and "-".

.. warning:
Keep in mind the polarity! This Bricklet is not short circuit protected!




.. _voltage_current_bricklet_test:

First Test
----------

|test_intro|

|test_connect|.

Connect a motor and a battery to the Bricklet as displayed in the following
picture.

.. image:: /Images/Bricklets/bricklet_voltage_current_master_600.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet with Battery and Motor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_master_1200.jpg

|test_tab|

If everything went as expected you can now see the current used by the motor 
and a graph that shows the current over time.

.. image:: /Images/Bricklets/bricklet_voltage_current_brickv.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_brickv.jpg

In the screenshot you can see a high curren peak. This is caused by the starting
of the motor when the battery is connected.

|test_pi_ref|


.. _voltage_current_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programmierschnittstelle <pi_hlpi>` for a detailed description.

.. include:: Voltage_Current_hlpi.table
