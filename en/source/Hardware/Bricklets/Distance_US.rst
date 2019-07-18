
.. include:: Distance_US.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _distance_us_bricklet:

Distance US Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_distance_us_tilted_[?|?].jpg           Distance US Bricklet
	Bricklets/bricklet_distance_us_vertical_[?|?].jpg         Distance US Bricklet
	Bricklets/bricklet_distance_us_horizontal_[?|?].jpg       Distance US Bricklet
	Bricklets/bricklet_distance_us_tilted_back_[?|?].jpg      Distance US Bricklet
	Bricklets/bricklet_distance_us_w_sensor_[100|600].jpg     Distance US Bricklet with sensor
	Cases/bricklet_distance_us_case_front_[?|?].jpg           Distance US Bricklet in Case
	Bricklets/bricklet_distance_us_brickv_[100|].jpg          Distance US Bricklet in Brick Viewer
	Dimensions/distance_us_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Distance US Bricklet is discontinued and is no longer sold. The
 Distance US Bricklet 2.0 is still in development. For now, the
 :ref:`Distance IR Bricklet 2.0 <distance_ir_v2_bricklet>` and the
 :ref:`Laser Range Finder Bricklet 2.0 <laser_range_finder_v2_bricklet>` are
 possible replacements.

Features
--------

* Measures distances from 2cm to 400cm with ultrasound
* 12bit resolution


.. _distance_us_bricklet_description:

Description
-----------

The Distance US :ref:`Bricklet <primer_bricklets>` is equipped with
an `ultrasonic distance sensor <https://en.wikipedia.org/wiki/Ultrasonic_sensor>`__
and extends :ref:`Bricks <primer_bricks>` by the possibility to measure 
distances from 2cm to 400cm.
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
* 3D model (`View online <https://autode.sk/2Ie3TvY>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/distance_us/distance_us.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/distance_us/distance_us.FCStd>`__)


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


.. _distance_us_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Distance_US_hlpi.table
