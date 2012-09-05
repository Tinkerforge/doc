.. include:: Analog_Out.substitutions


.. _analog_out_bricklet:

Analog Out Bricklet
===================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_analog_out_tilted_350.jpg",
	               "Bricklets/bricklet_analog_out_tilted_600.jpg",
	               "Analog Out Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_out_vertical_100.jpg",
	             "Bricklets/bricklet_analog_out_vertical_600.jpg",
	             "Analog Out Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_out_horizontal_100.jpg",
	             "Bricklets/bricklet_analog_out_horizontal_600.jpg",
	             "Analog Out Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_out_master_100.jpg",
	             "Bricklets/bricklet_analog_out_master_600.jpg",
	             "Analog Out Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_out_brickv_100.jpg",
	             "Bricklets/bricklet_analog_out_brickv.jpg",
	             "Analog Out Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/analog_out_bricklet_dimensions_100.png",
	             "Dimensions/analog_out_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Generates configurable voltages up to 5V*
* Specification in 1mV steps (12bit resolution)
* Configurable with load resistor to ground


Description
-----------

The Analog Out :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by the
capability to generate voltages between 0V and 5V*.
The voltage can be configured directly in `Volt
<http://en.wikipedia.org/wiki/Volt>`__ without any conversion.
The device is equipped with a 12-bit `Digital-to-Analog Converter (DAC)
<http://en.wikipedia.org/wiki/Digital-to-analog_converter>`__.
Instead of generating a voltage it is also possible to choose between a 1k,
100k or 500k Ohm load resistor to ground (pull-down).


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
DAC                               MCP4725
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Voltage                           0V - 5V* in 1mV steps, 12bit resolution
Maximum Current                   24mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 25 x 14mm (1.18 x 0.98 x 0.55")
Weight                            6g
================================  ============================================================

\* The maximum output voltage depends on the supply voltage. If the connected
Brick is powered over USB, 5V may not be reached. The reason for this is a
voltage drop about 0.5V caused by protection diodes on our products.
If you need to reach 5V, you have to use a stack supply,
e.g. the :ref:`Step-Down Power Supply <step-down>`.


Resources
---------

* MCP4725 datasheet (`Download <https://github.com/Tinkerforge/analog-out-bricklet/raw/master/datasheets/MCP4725.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/analog-out-bricklet/raw/master/hardware/analog-out-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog-out_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/analog-out-bricklet/zipball/master>`__)


Connectivity
------------

The Analog Out Bricklet has four terminals. All terminals are outputs.
Between VOUT and GND the output voltage is applied. 3.3V and 5V are
additional outputs with fixed voltages you can use to power things.

.. image:: /Images/Bricklets/bricklet_analog_out_vertical_350.jpg
    :scale: 100 %
    :alt: Analog Out Bricklet Terminals
    :align: center
    :target: ../../_images/Bricklets/bricklet_analog_out_vertical_1200.jpg


.. _analog_out_bricklet_test:

Test your Analog Out Bricklet
-----------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_analog_out_master_600.jpg
   :scale: 100 %
   :alt: Analog Out Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_out_master_1200.jpg

|test_tab|
In this tab you can configure the voltage on the output pin.
For test purposes, you can measure this voltage with a voltmeter.
If everything went as expected the voltage on the voltmeter and the voltage
you have configured should be identical.

.. image:: /Images/Bricklets/bricklet_analog_out_brickv.jpg
   :scale: 100 %
   :alt: Analog Out Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_out_brickv.jpg

|test_pi_ref|


.. _analog_out_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Analog_Out_hlpi.table
