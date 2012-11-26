.. include:: Industrial_Digital_In_4.substitutions


.. _industrial_digital_in_4_bricklet:

Industrial Digital In 4 Bricklet
================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_analog_in_tilted_350.jpg",
	               "Bricklets/bricklet_analog_in_tilted_600.jpg",
	               "Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_in_vertical_100.jpg",
	             "Bricklets/bricklet_analog_in_vertical_600.jpg",
	             "Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_in_horizontal_100.jpg",
	             "Bricklets/bricklet_analog_in_horizontal_600.jpg",
	             "Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_in_master_100.jpg",
	             "Bricklets/bricklet_analog_in_master_600.jpg",
	             "Analog In Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_in_brickv_100.jpg",
	             "Bricklets/bricklet_analog_in_brickv.jpg",
	             "Analog In Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/analog_in_bricklet_dimensions_100.png",
	             "Dimensions/analog_in_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 4 channel digital input 
* Input voltages up to 36V
* Galvanically isolated


Description
-----------

The Industrial Digital In 4 :ref:`Bricklet <product_overview_bricklets>` can be used to
extend :ref:`Bricks <product_overview_bricks>` by four galvanically isolated digital inputs.
The input voltage can be up to 36 `volts <http://en.wikipedia.org/wiki/Volt>`__ high. 
Input isolation permits the usage without a direct electric connection, 
such that ground loops can be prevented and an additional degree of safety is added.

Typical applications are the interfacing of industrial control, such as PLC's or frequency converters,
or the usage in environments were electrical ground levels can not be connected.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Input Type                        Four optocoppler inputs
Input Current                     TBD
Max. Low Level Voltage            TBD V
Min. High Level Voltage           TBD V
Max. Input Voltage                36V
Isolation                         5000Vrms (optocoppler value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x TBDmm (TBD x TBD x TBD")
Weight                            TBDg
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-bricklet/raw/master/hardware/analog-in-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial-digital-in-4_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-bricklet/zipball/master>`__)


Connectivity
------------

The Industrial Digital In 4 Bricklet has an 8pole terminal. With it you can access
four inputs, whereas each input is connected to one LED inside the optocoppler.
To use one input connect it as depicted below:

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_vertical_350.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_vertical_1200.jpg


.. _industrial_digital_in_4_bricklet_test:

Test your Industrial Digital In 4 Bricklet
------------------------------------------

|test_intro|

|test_connect|.
Additionally connect a voltage source to the Bricklet.
For testing purposes we have connected a battery
(see picture below).

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_master_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_master_1200.jpg

|test_tab|
If everything went as expected you can now see the voltage in Volt
and a graph that shows the voltage over time.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg

|test_pi_ref|


.. _industrial_digital_in_4_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Industrial_Digital_In_4_hlpi.table
