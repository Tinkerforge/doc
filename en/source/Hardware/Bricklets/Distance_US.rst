
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Distance US Bricklet
:shoplink: ../../../shop/bricklets/distance-us-bricklet.html

.. include:: Distance_US.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _distance_us_bricklet:

Distance US Bricklet
====================

.. raw:: html

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
	    tfdocimg("Bricklets/bricklet_distance_us_tilted_back_100.jpg",
	             "Bricklets/bricklet_distance_us_tilted_back_600.jpg",
	             "Distance US Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_distance_us_w_sensor_100.jpg",
	             "Bricklets/bricklet_distance_us_w_sensor_600.jpg",
	             "Distance US Bricklet with sensor")
	}}
	{{
	    tfdocimg("Cases/bricklet_distance_us_case_front_100.jpg",
	             "Cases/bricklet_distance_us_case_front_600.jpg",
	             "Distance US Bricklet in Case")
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
* 12bit resolution

Description
-----------

The Distance US :ref:`Bricklet <product_overview_bricklets>` is equipped with
an `ultrasonic distance sensor <http://en.wikipedia.org/wiki/Ultrasonic_sensor>`__.
It can measure distances from 2cm to 400cm.
The measured distance is reported as unitless value, not in mm. This is because
the relation between the distance value and the actual distance depends on the
exact value of the 5V supply voltage. Deviations in the supply voltage result
in deviations in the measured distance values.
With configurable events it is possible to react on changing distances without
polling. Typical applications can be found in robotics, usage as light barrier
alternative and so on.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            HC-SR04
Current Consumption               8mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Distance                          2cm - 400cm, 12bit resolution
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

|test_connect|.

|test_tab|
If everything went as expected you can now see the measured distance.

.. image:: /Images/Bricklets/bricklet_distance_us_brickv.jpg
   :scale: 100 %
   :alt: Distance US Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_us_brickv.jpg

|test_pi_ref|

.. _distance_us_bricklet_case:

Case
----

A `laser-cut case for the Distance US Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-distance-us-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_distance_us_case_front_350.jpg
   :scale: 100 %
   :alt: Case for Distance US Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_distance_us_case_front_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet (each long spacer consists of 2x 9mm and 1x 12mm pieces),
* build up side plates and put them around Bricklet and sensor (the front plate is asymmetric, the wider margin goes to the right side, when viewed from the outside),
* screw bottom plate to bottom spacers,
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the Distance US Bricklet case:

.. image:: /Images/Exploded/distance_us_exploded_350.png
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
