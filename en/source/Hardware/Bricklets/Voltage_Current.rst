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
	             "Voltage/Current Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_brickv_100.png",
	             "Bricklets/bricklet_voltage_current_brickv.png",
	             "Voltage/Current Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/voltage_current_bricklet_dimensions_100.png",
	             "Dimensions/voltage_current_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measure power, voltage and current up to 720W/36V/20A
* 1mW, 1mV, 1mA resolution over the whole range
* Bidirectional current measurement (e.g. charge/discharge)
* Configurable averaging and ADC conversion time

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
Sensor                            INA226 with 4m Ohm Shunt Resistor
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximum Current                   +-20A
Maximum Input Voltage             36V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 18mm (1.18 x 1.18 x 0.67")
Weight                            10g
================================  ============================================================


Resources
---------

* INA226 Datasheet (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/raw/master/datasheets/ina226.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/raw/master/hardware/voltage-current-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/voltage_current_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/zipball/master>`__)


Connectivity
------------

You have to connect the Voltage/Current Bricklet between your power supply and 
your load. Connect the power supply with the terminal marked with "IN" and the
load with the terminal marked "OUT". The polarity is marked with "+" and "-".

.. warning:
 
 Keep the polarity in mind! This Bricklet is not protected against polarity reversal!


Calibration
-----------

The current measurement of the Voltage/Current Bricklet is factory calibrated
at room temperature. The readings can shift by a few mA if the environment
is very cold or very hot. In this case you can recalibrate the Bricklet
with a precise multimeter:

Start the Brick Viewer and set "Gain Multiplier" and "Gain Divisor" to 1, press
"Save Calibration". Now read the real current measurement from your multimeter
and put it in the "Gain Multiplier" field. Put the current current measurement
from the Voltage/Current Bricklet in the "Gain Divisor" field and press
"Save Calibration" again.

Now the Voltage/Current Bricklet is calibrated for the new environment.


.. _voltage_current_bricklet_test:

First Test
----------

|test_intro|

|test_connect|.

Connect a motor and a battery to the Bricklet as displayed in the following
picture.

.. image:: /Images/Bricklets/bricklet_voltage_current_setup_600.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet with Battery and Motor
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_setup_1200.jpg

|test_tab|

If everything went as expected you can now see the current used by the motor 
and a graph that shows the current over time. You can see that the voltage
drops a bit because of the high load. In this example the motor
utilizes about 40W power.

.. image:: /Images/Bricklets/bricklet_voltage_current_brickv.png
   :scale: 70 %
   :alt: Voltage/Current Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_brickv.png

|test_pi_ref|


.. _voltage_current_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed 
description.

.. include:: Voltage_Current_hlpi.table
