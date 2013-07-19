
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Industrial Digital In 4 Bricklet
:shoplink: ../../../shop/bricklets/industrial-digital-in-4-bricklet.html

.. include:: Industrial_Digital_In_4.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_digital_in_4_bricklet:

Industrial Digital In 4 Bricklet
================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_digital_in_4_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_digital_in_4_tilted_600.jpg",
	               "Industrial Digital In 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_vertical_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_vertical_600.jpg",
	             "Industrial Digital In 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_horizontal_600.jpg",
	             "Industrial Digital In 4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_setup_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_setup_600.jpg",
	             "Industrial Digital In 4 Bricklet setup")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_digital_in_4_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_digital_in_4_brickv.jpg",
	             "Industrial Digital In 4 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_digital_in_4_bricklet_dimensions_100.png",
	             "Dimensions/industrial_digital_in_4_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 4 channel digital input 
* Input voltages up to 36V
* Galvanically isolated
* Groupable


Description
-----------

The Industrial Digital In 4 :ref:`Bricklet <product_overview_bricklets>` can 
be used to extend :ref:`Bricks <product_overview_bricks>` by four galvanically 
isolated digital inputs. The input voltage can be up to 36 
`volts <http://en.wikipedia.org/wiki/Volt>`__. 

Input isolation permits the usage without a direct electrical connection, 
such that ground loops can be prevented and an additional degree of safety is 
added.

Typical applications are the interfacing of industrial controllers, such as 
PLC's or frequency converters, or the usage in environments were electrical 
ground levels can not be connected.

If you need more then four inputs, you can add another Industrial Digital In 4
Bricklet and group these together. If you do this, you have eight inputs which can
read simultaneously in contrast to read both Bricklets successively.
Grouping is only possible for Bricklets connected to one Brick.
Thus you can group up to four Industrial Bricklets on a Master Brick or
two on other Bricks.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Input Type                        Four optocoupled inputs (including 4.7k Ohm series resistor)
Input Current                     Depending on input voltage, ca. 1mA/5V, ca. 5mA/24V
Maximum Input Voltage             36V
Low Level Voltage                 0-2V
High Level Voltage                3-36V
Isolation                         5000Vrms (optocoupler value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            8g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-bricklet/raw/master/hardware/industrial-digital-in-4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_digital_in_4_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-bricklet/zipball/master>`__)


Connectivity
------------

The Industrial Digital In 4 Bricklet has an 8 pole terminal. With it you can 
access the four inputs. Each input is connected to one LED inside the 
optocoupler.

To use one input connect it as depicted below:

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_caption_1200.jpg


.. _industrial_digital_in_4_bricklet_test:

Test your Industrial Digital In 4 Bricklet
------------------------------------------

|test_intro|

|test_connect|.
Additionally connect a voltage source to one of the Bricklet inputs.
For testing purposes we have connected a battery
(see picture below).

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_setup_1200.jpg

|test_tab|

If everything went as expected you can change the state of the input channel
by connecting and disconnecting the battery.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_brickv.jpg

|test_pi_ref|

.. _industrial_digital_in_4_bricklet_case:

Case
----

A `laser-cut case for the Industrial Digital In 4 Bricklet <https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Digital_In_4.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|

.. _industrial_digital_in_4_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Industrial_Digital_In_4_hlpi.table
