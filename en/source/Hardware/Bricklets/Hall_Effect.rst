
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Hall Effect Bricklet
:FIXME_shoplink: ../../../shop/bricklets/hall-effect-bricklet.html

.. include:: Hall_Effect.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _hall_effect_bricklet:

Hall Effect Bricklet
====================

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

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
	    tfdocimg("Bricklets/bricklet_hall_effect_master_100.jpg",
	             "Bricklets/bricklet_hall_effect_master_600.jpg",
	             "Hall Effect Bricklet with Master Brick")
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
* Counts appearances of magnetic field
* Can be used to read out water/electricity meter

Description
-----------

The Hall Effect Bricklet can detect the presence of magnetic fields.
It counts the appearances of magnetic fields and can thus be used to
measure the speed of a wheel with attached magnet.

Example applications are:

* Detection if a door is closed
* Reading out water/electricity meters

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Operation                         Omnipolar (North and South pole is detected)
Operation Point                   -35/35 Gauss
Release Point                     -25/25 Gauss
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/raw/master/hardware/hall-effect-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/hall_effect_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/hall-effect-bricklet/zipball/master>`__)


.. _hall_effect_bricklet_test:

Test your Hall Effect Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_hall_effect_master_600.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_master_1200.jpg

|test_tab|
If everything went as expected you can now see the detection of a
magnetic field.

.. image:: /Images/Bricklets/bricklet_hall_effect_brickv.jpg
   :scale: 100 %
   :alt: Hall Effect Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_hall_effect_brickv.jpg

|test_pi_ref|


.. _hall_effect_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Hall_Effect_hlpi.table
