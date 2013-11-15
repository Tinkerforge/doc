
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Rotary Poti Bricklet
:shoplink: ../../../shop/bricklets/rotary-poti-bricklet.html

.. include:: Rotary_Poti.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rotary_poti_bricklet:

Rotary Poti Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_rotary_poti_tilted_350.jpg",
	               "Bricklets/bricklet_rotary_poti_tilted_600.jpg",
	               "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_front_100.jpg",
	             "Bricklets/bricklet_rotary_poti_front_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_vertical_100.jpg",
	             "Bricklets/bricklet_rotary_poti_vertical_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_horizontal_100.jpg",
	             "Bricklets/bricklet_rotary_poti_horizontal_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_knob_100.jpg",
	             "Bricklets/bricklet_rotary_poti_knob_600.jpg",
	             "Rotary Poti Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_master_100.jpg",
	             "Bricklets/bricklet_rotary_poti_master_600.jpg",
	             "Rotary Poti Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_poti_brickv_100.jpg",
	             "Bricklets/bricklet_rotary_poti_brickv.jpg",
	             "Rotary Poti Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/rotary_poti_bricklet_dimensions_100.png",
	             "Dimensions/rotary_poti_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 300° rotary potentiometer
* Outputs position from -150° to 150° in 1° steps


Description
-----------

The Rotary Poti :ref:`Bricklet <product_overview_bricklets>` is equipped with
a 1-turn rotary `potentiometer <http://en.wikipedia.org/wiki/Potentiometer>`__.
It can be connected to a
:ref:`Brick <product_overview_bricks>`, with which the position of the
slider can be read out. With configurable events it is possible to react on
changing positions without polling.

You can use this Bricklet for speed, volume control or similar purposes.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Rotary Potentiometer              1-turn, 300°
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          -150° to 150° (left to right) in 1° steps
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 25 x 23mm (1.18 x 0.98 x 0.9")*
Weight                            5g*
================================  ============================================================

\* without knob


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/raw/master/hardware/rotary-poti-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rotary_poti_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/zipball/master>`__)


.. _rotary_poti_bricklet_test:

Test your Rotary Poti Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_rotary_poti_master_600.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg

Turn the potentiometer.
You should be able to create a similar graph by turning the potentiometer
from left left to right and back to left.

|test_pi_ref|

.. _rotary_poti_bricklet_case:

Case
----

A `laser-cut case for the Rotary Poti Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-rotary-poti-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_rotary_poti_case_350.jpg
   :scale: 100 %
   :alt: Case for Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_rotary_poti_case_1000.jpg

.. include:: Rotary_Poti.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/rotary_poti_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Exploded/rotary_poti_exploded.png

|bricklet_case_hint|

.. _rotary_poti_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Rotary_Poti_hlpi.table
