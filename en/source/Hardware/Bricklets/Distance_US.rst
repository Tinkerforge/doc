
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Distance US Bricklet
:FIXME_shoplink: ../../../shop/bricklets/distance-us-bricklet.html

.. include:: Distance_US.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _distance_us_bricklet:

Distance US Bricklet
====================

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_distance_us_tilted_350.jpg",
	               "Bricklets/bricklet_distance_us_tilted_600.jpg",
	               "Distance US Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_us_vertical_100.jpg",
	             "Bricklets/bricklet_distance_us_vertical_600.jpg",
	             "Distance US Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_us_horizontal_100.jpg",
	             "Bricklets/bricklet_distance_us_horizontal_600.jpg",
	             "Distance US Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_us_master_100.jpg",
	             "Bricklets/bricklet_distance_us_master_600.jpg",
	             "Distance US Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_us_brickv_100.jpg",
	             "Bricklets/bricklet_distance_us_brickv.jpg",
	             "Distance US Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/distance_us_bricklet_dimensions_100.png",
	             "Dimensions/distance_us_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures distances from 2cm to 400cm with ultrasound
* Output in 1mm steps (12bit resolution)

Description
-----------

The Distance US Bricklet is equipped with an ultrasonic distance sensor.
It can measure distances from 2cm to 400cm. With configurable events it is possible to react on changing distances without polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Max Range                         400cm
Min Range                         2cm
Measuring Angle                   15°
Update Rate                       40Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            45 x 20 x 30mm (1.78 x 0.78 x 1.18")
Weight                            13g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/distance-us-bricklet/raw/master/hardware/distance-us-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/distance_us_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/distance-us-bricklet/zipball/master>`__)


.. _distance_us_bricklet_test:

Test your Distance US Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_distance_us_master_600.jpg
   :scale: 100 %
   :alt: Distance US Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_us_master_1200.jpg

|test_tab|
If everything went as expected you can now see the measured distance.

.. FIXME image:: /Images/Bricklets/bricklet_distance_us_brickv.jpg
   :scale: 100 %
   :alt: Distance US Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_us_brickv.jpg

|test_pi_ref|

.. _distance_us_bricklet_case:

Case
----

A `laser-cut case for the Distance US Bricklet <https://www.tinkerforge.com/en/shop/cases/case-distance-us-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_distance_us_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Distance US Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_distance_us_case_built_up_1000.jpg

.. include:: Distance_US.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/distance_us_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Distance US Bricklet
   :align: center
   :target: ../../_images/Exploded/distance_us_exploded.png

|bricklet_case_hint|


.. _distance_us_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Distance_US_hlpi.table
