
:shoplink: ../../../shop/bricklets/distance-us-v2-bricklet.html

.. include:: Distance_US_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _distance_us_v2_bricklet:

Distance US Bricklet 2.0
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_distance_us_v2_tilted_[?|?].jpg           Distance US Bricklet 2.0
	Bricklets/bricklet_distance_us_v2_top_[?|?].jpg              Distance US Bricklet 2.0
	Bricklets/bricklet_distance_us_v2_bottom_[?|?].jpg           Distance US Bricklet 2.0
	Bricklets/bricklet_distance_us_v2_side_[?|?].jpg             Distance US Bricklet 2.0
	Bricklets/bricklet_distance_us_v2_brickv_[100|].jpg          Distance US Bricklet 2.0 in Brick Viewer
	Dimensions/distance_us_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures distances from 30cm to 500cm with ultrasound
* Resolution of 1mm


.. _distance_us_v2_bricklet_description:

Description
-----------

The Distance US :ref:`Bricklet <primer_bricklets>` 2.0 is equipped with
an `ultrasonic distance sensor <https://en.wikipedia.org/wiki/Ultrasonic_sensor>`__
and extends :ref:`Bricks <primer_bricks>` by the possibility to measure 
distances from 30cm to 500cm.

With configurable events it is possible to react on changing distances without
polling. Typical applications can be found in robotics, usage as light barrier
alternative and so on.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MaxSonar HRLV MB1013
Current Consumption               50mW (10mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Distance                          30cm - 500cm
Resolution                        1mm
Update Rate                       2Hz / 10Hz (configurable)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 35 x 20mm (1.38 x 1.38 x 0.78")
Weight                            9g
================================  ============================================================


Resources
---------

* Datasheet MaxSonar HRLV MB1013 (`Download <https://github.com/Tinkerforge/distance-us-v2-bricklet/raw/master/datasheets/HRLV-MaxSonar-EZ_Datasheet.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/distance-us-v2-bricklet/raw/master/hardware/distance-us-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/distance_us_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/distance-us-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2TyiysF>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/distance_us_v2/distance-us-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/distance_us_v2/distance-us-v2.FCStd>`__)


.. _distance_us_v2_bricklet_test:

Test your Distance US Bricklet 2.0
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the measured distance.

.. image:: /Images/Bricklets/bricklet_distance_us_v2_brickv.jpg
   :scale: 100 %
   :alt: Distance US Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_us_v2_brickv.jpg

|test_pi_ref|


.. _distance_us_v2_bricklet_beam_pattern:

Beam Pattern
------------

The Distance US Bricklet 2.0 uses the MB1013 sensor from MaxBotix.

You can find the beam pattern (2d-representation of measured distances
with different angles) below:

.. image:: /Images/Bricklets/bricklet_distance_us_v2_beam_pattern.png
   :scale: 100 %
   :alt: Distance US Bricklet 2.0 beam pattern
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_us_v2_beam_pattern.png


.. _distance_us_v2_bricklet_case:

Case
----

A `laser-cut case for the Distance US Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-distance-us-v2-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_distance_us_v2_case_350.jpg
   :scale: 100 %
   :alt: Case for Distance US Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_distance_us_v2_case_1000.jpg

.. include:: Distance_US_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/distance_us_v2_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Distance US Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/distance_us_v2_exploded.png

|bricklet_case_hint|


.. _distance_us_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Distance_US_V2_hlpi.table
