
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#bricklets">Bricklets</a> / Voltage Bricklet

.. include:: Voltage.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

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
	             "Voltage Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_brickv_100.jpg",
	             "Bricklets/bricklet_voltage_brickv.jpg",
	             "Voltage Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/voltage_bricklet_dimensions_100.png",
	             "Dimensions/voltage_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures voltages up to 50V
* Output in 1mV steps (12bit resolution)


Description
-----------

The Voltage :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by the
capability to measure voltages. The measurement range is 0-50V.
The voltage can be read out directly in `Volt
<http://en.wikipedia.org/wiki/Volt>`__ without conversion.
With configurable events it is possible to react on changing
voltages without polling.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            Fixed voltage divider with factor 0.0625
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Voltage                           0V - 50V in 1mV steps, 12bit resolution
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 25 x 14mm (0.98 x 0.98 x 0.55")
Weight                            4g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/voltage-bricklet/raw/master/hardware/voltage-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/voltage_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/voltage-bricklet/zipball/master>`__)


.. _voltage_bricklet_test:

Test your Voltage Bricklet
--------------------------

|test_intro|

|test_connect|.
Additionally connect a voltage source to the Bricklet.
For testing purposes we have connected a battery
(see picture below).

.. image:: /Images/Bricklets/bricklet_voltage_master_600.jpg
   :scale: 100 %
   :alt: Voltage Bricklet with Battery connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_master_1200.jpg

|test_tab|
If everything went as expected you can now see the voltage in volt
and a graph that shows the voltage over time.

.. image:: /Images/Bricklets/bricklet_voltage_brickv.jpg
   :scale: 100 %
   :alt: Voltage Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_brickv.jpg

|test_pi_ref|


.. _voltage_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Voltage_hlpi.table
