
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Hall Effect Bricklet
:shoplink: ../../../shop/bricklets/hall-effect-bricklet.html

.. include:: Hall_Effect.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _hall_effect_bricklet:

Hall Effect Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_hall_effect_tilted_350.jpg",
	               "Bricklets/bricklet_hall_effect_tilted_600.jpg",
	               "Hall Effect Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_hall_effect_vertical_100.jpg",
	             "Bricklets/bricklet_hall_effect_vertical_600.jpg",
	             "Hall Effect Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_hall_effect_horizontal_100.jpg",
	             "Bricklets/bricklet_hall_effect_horizontal_600.jpg",
	             "Hall Effect Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_hall_effect_tilted_back_100.jpg",
	             "Bricklets/bricklet_hall_effect_tilted_back_600.jpg",
	             "Hall Effect Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_hall_effect_brickv_100.jpg",
	             "Bricklets/bricklet_hall_effect_brickv.jpg",
	             "Hall Effect Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/hall_effect_bricklet_dimensions_100.png",
	             "Dimensions/hall_effect_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Detects presence of magnetic field
* Counts (dis-)appearances of magnetic fields
* Can be used to read out water/electricity meter


.. _hall_effect_bricklet_description:

Description
-----------

The Hall Effect :ref:`Bricklet <primer_bricklets>` extends 
:ref:`Bricks <primer_bricks>` and can detect the
presence of magnetic fields. It counts the (dis-)appearances of magnetic fields
and can for example be used to measure the speed of a wheel with attached magnet
with up to 13Hz.

Example applications are:

* Detect if a door is open or closed
* Reading out water/electricity meters

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            AH180N
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Operation                         Omnipolar (North and South pole is detected)
Trigger Point                     -35/35 Gauss
Release Point                     -25/25 Gauss
Sampling Rate                     8Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* AH180N datasheet (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/raw/master/datasheets/AH180N.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/raw/master/hardware/hall-effect-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/hall_effect_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/zipball/master>`__)


.. _hall_effect_bricklet_test:

Test your Hall Effect Bricklet
------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the detection of a
magnetic field. A magnet can be used to test the Bricklet by moving it near
the Bricklet.


.. image:: /Images/Bricklets/bricklet_hall_effect_brickv.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_brickv.jpg

|test_pi_ref|


.. _hall_effect_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Hall_Effect_hlpi.table
