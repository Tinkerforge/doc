.. include:: Linear_Poti.substitutions


.. _linear_poti_bricklet:

Linear Poti Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_linear_poti_tilted_350.jpg",
	               "Bricklets/bricklet_linear_poti_tilted_600.jpg",
	               "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_front_100.jpg",
	             "Bricklets/bricklet_linear_poti_front_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_vertical_100.jpg",
	             "Bricklets/bricklet_linear_poti_vertical_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_horizontal_100.jpg",
	             "Bricklets/bricklet_linear_poti_horizontal_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_knob_100.jpg",
	             "Bricklets/bricklet_linear_poti_knob_600.jpg",
	             "Linear Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_master_100.jpg",
	             "Bricklets/bricklet_linear_poti_master_600.jpg",
	             "Linear Poti Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_linear_poti_brickv_100.jpg",
	             "Bricklets/bricklet_linear_poti_brickv.jpg",
	             "Linear Poti Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/linear_poti_bricklet_dimensions_100.png",
	             "Dimensions/linear_poti_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 59mm linear potentiometer
* Outputs position from 0% to 100% in 1% steps


Description
-----------

The Linear Poti :ref:`Bricklet <product_overview_bricklets>` is equipped with
a linear `potentiometer <http://en.wikipedia.org/wiki/Potentiometer>`__
("fader", "slider"). It can be connected to a
:ref:`Brick <product_overview_bricks>`, with which the position of the
slider can be read out.
With configurable events it is possible to react on changing positions
without polling.

You can use this Bricklet for speed, volume control or similar purposes.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Linear Potentiometer              59mm (2.32") adjustable length
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          0% - 100% (slider down - slider up) in 1% steps
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 85 x 20mm (0.98 x 3.35 x 0.78")*
Weight                            14g*
================================  ============================================================

\* without knob


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/raw/master/hardware/linear-poti-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/linear_poti_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/zipball/master>`__)


.. _linear_poti_bricklet_test:

Test your Linear Poti Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_linear_poti_master_600.jpg
   :scale: 100 %
   :alt: Linear Poti Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_linear_poti_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_linear_poti_brickv.jpg
   :scale: 100 %
   :alt: Linear Poti Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_current12_brickv.jpg

Move the potentiometer.
You should be able to create a similar graph
by moving the potentiometer from bottom to top and back to bottom.

|test_pi_ref|


.. _linear_poti_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Linear_Poti_hlpi.table
