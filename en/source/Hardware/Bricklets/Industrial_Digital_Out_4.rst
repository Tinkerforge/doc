
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Digital Out 4 Bricklet
:shoplink: ../../../shop/bricklets/industrial-digital-out-4-bricklet.html

.. include:: Industrial_Digital_Out_4.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_digital_out_4_bricklet:

Industrial Digital Out 4 Bricklet
=================================

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
	    tfdocimg("Bricklets/bricklet_industrial_digital_out_4_setup_100.jpg",
	             "Bricklets/bricklet_industrial_digital_out_4_setup_600.jpg",
	             "Industrial Digital Out 4 Bricklet setup")
	}}
	{{
	    tfdocimg("Cases/bricklet_industrial_case_100.jpg",
	             "Cases/bricklet_industrial_case_600.jpg",
	             "Industrial Digital Out 4 in Case")
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
* Groupable


.. _industrial_digital_out_4_bricklet_description:

Description
-----------

The Industrial Digital Out 4 :ref:`Bricklet <primer_bricklets>` can be used to
extend :ref:`Bricks <primer_bricks>` by four galvanically isolated digital outputs.
The outputs have to be supplied externally with a voltage of up to
36 `Volt <http://en.wikipedia.org/wiki/Volt>`__. 
Output isolation permits the usage without a direct electric connection, 
such that ground loops can be prevented and an additional degree of safety is added.

Typical applications are the interfacing of industrial controllers, such as PLC's or frequency converters,
or the usage in environments were electrical ground levels can not be connected.

If you need more then four outputs, you can add another Industrial Digital Out 4
Bricklet and group these together. If you do this, you have eight outputs which can
set simultaneously in contrast to set both Bricklets successively.
Grouping is only possible for Bricklets connected to one Brick.
Thus you can group up to four Industrial Bricklets on a Master Brick or
two on other Bricks.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               2mA (per active output pin)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
External Voltage Supply           Up to 36V
Output Type                       Four operational amplifier outputs
Maximum Output Current            25mA (per output pin)
Isolation                         5000Vrms (optocoupler value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 14mm (1.57 x 1.57 x 0.55")
Weight                            10g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-digital-out-4-bricklet/raw/master/hardware/industrial-digital-out-4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_digital_out_4_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-digital-out-4-bricklet/zipball/master>`__)


Connectivity
------------

The Industrial Digital Out 4 Bricklet has an 8 pole terminal.
Please see the picture below for the pinout.

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet pinout
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_caption_1200.jpg


.. _industrial_digital_out_4_bricklet_test:

Test your Industrial Digital Out 4 Bricklet
-------------------------------------------

|test_intro|

|test_connect|.
Additionally connect a voltage source to power the Bricklet and a load
you want to switch. For testing purposes we have connected a battery
and a LED (see picture below).

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_setup_1200.jpg

|test_tab|

If everything went as expected you can switch the LED by changing the output
state with the Brick Viewer.

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_brickv.jpg

|test_pi_ref|

.. _industrial_digital_out_4_bricklet_case:

Case
----

A `laser-cut case for the Industrial Digital Out 4 Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Digital Out 4 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Digital_Out_4.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Digital Out 4 Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_digital_out_4_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Digital_Out_4_hlpi.table
