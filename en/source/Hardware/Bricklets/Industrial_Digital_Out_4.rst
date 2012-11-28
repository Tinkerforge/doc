.. include:: Industrial_Digital_Out_4.substitutions


.. _industrial_digital_out_4_bricklet:

Industrial Digital Out 4 Bricklet
================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_digital_out_4_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_digital_out_4_tilted_600.jpg",
	               "Industrial Digital Out 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_out_4_vertical_100.jpg",
	             "Bricklets/bricklet_industrial_digital_out_4_vertical_600.jpg",
	             "Industrial Digital Out 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_out_4_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_digital_out_4_horizontal_600.jpg",
	             "Industrial Digital Out 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_out_4_master_100.jpg",
	             "Bricklets/bricklet_industrial_digital_out_4_master_600.jpg",
	             "Industrial Digital Out 4 Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_out_4_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_digital_out_4_brickv.jpg",
	             "Industrial Digital Out 4 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_digital_out_4_bricklet_dimensions_100.png",
	             "Dimensions/industrial_digital_out_4_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 4 channel digital output
* Output voltages up to 36V
* Galvanically isolated


Description
-----------

The Industrial Digital Out 4 :ref:`Bricklet <product_overview_bricklets>` can be used to
extend :ref:`Bricks <product_overview_bricks>` by four galvanically isolated digital outputs.
The outputs have to be supplied externally with a voltage up to
36 `Volt <http://en.wikipedia.org/wiki/Volt>`__. 
Output isolation permits the usage without a direct electric connection, 
such that ground loops can be prevented and an additional degree of safety is added.

Typical applications are the interfacing of industrial control, such as PLC's or frequency converters,
or the usage in environments were electrical ground levels can not be connected.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
External Voltage Supply           Up to 36V
Output Type                       Four operational amplifier outputs
Output Current                    max. 25mA
Isolation                         5000Vrms (optocoppler value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 14mm (1,57 x 1,57 x 0,55")
Weight                            10g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-digital-out-4-bricklet/raw/master/hardware/industrial-digital-out-4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial-digital-out-4_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-digital-out-4-bricklet/zipball/master>`__)


Connectivity
------------

The Industrial Digital Out 4 Bricklet has an 8pole terminal.
Please see the picture below for the pinout.


.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_vertical_350.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Pinout
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_vertical_1200.jpg


.. _industrial_digital_out_4_bricklet_test:

Test your Industrial Digital Out 4 Bricklet
-------------------------------------------

|test_intro|

|test_connect|.
Additionally connect a voltage source to power the Bricklet and a load
you want to switch. For testing purposes we have connected a battery
and a LED (see picture below).


.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_master_600.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_master_1200.jpg

|test_tab|

If everything went as expected you can switch the LED by changing the output
state with the Brick Viewer.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg

|test_pi_ref|


.. _industrial_digital_out_4_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Industrial_Digital_Out_4_hlpi.table
