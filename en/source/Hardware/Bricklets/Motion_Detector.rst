
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Motion Detector Bricklet
:FIXME_shoplink: ../../../shop/bricklets/motion-detector-bricklet.html

.. include:: Motion_Detector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _motion_detector_bricklet:

Motion Detector Bricklet
========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_motion_detector_tilted_350.jpg",
	               "Bricklets/bricklet_motion_detector_tilted_600.jpg",
	               "Motion Detector Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_motion_detector_horizontal_100.jpg",
	             "Bricklets/bricklet_motion_detector_horizontal_600.jpg",
	             "Motion Detector Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_motion_detector_brickv_100.jpg",
	             "Bricklets/bricklet_motion_detector_brickv.jpg",
	             "Motion Detector Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/motion_detector_bricklet_dimensions_100.png",
	             "Dimensions/motion_detector_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Passive Infrared Motion Sensor
* Detects motion in distances of up to 7m (configurable)
* High sensing angle (100°)

Description
-----------

The Motion Detector :ref:`Bricklet <product_overview_bricklets>` is equipped
with a passive infrared (PIR) sensor. It can be used to sense movement of
people and animals. It has a configurable detection range of 3m to 7m with a
sensing angle of 100°.

By using configurable events it is possible to react on detected motion without
polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Detection Range                   3-7m (configurable)
Sensing Angle                     100°
Delay Time                        3-200s (configurable)
Block Time                        2.5s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 45 x 30mm (0.98 x 1.78 x 1.18")
Weight                            12g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/motion-detector-bricklet/raw/master/hardware/motion-detector-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/motion_detector_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/motion-detector-bricklet/zipball/master>`__)


.. _motion_detector_bricklet_test:

Test your Motion Detector Bricklet
----------------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_motion_detector_master_600.jpg
   :scale: 100 %
   :alt: Motion Detector Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_master_1200.jpg

|test_tab|
If everything went as expected you can now see when a motion is detected.

.. image:: /Images/Bricklets/bricklet_motion_detector_brickv.jpg
   :scale: 100 %
   :alt: Motion Detector Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_brickv.jpg

|test_pi_ref|


Sensitivity, Delay Time and Block Time
--------------------------------------

.. image:: /Images/Bricklets/bricklet_motion_detector_potentiometer_caption_350.jpg
   :scale: 100 %
   :alt: Motion Detector Image with potentiometer labled
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_potentiometer_caption_1200.jpg

The sensor is equipped with two potentiometers. The potentiometer on the right
side adjusts the sensitivity of the sensor which controls the detection range
(3-7m). Turning the potentiometer clockwise increase the range.

The potentiometer on the left side adjusts the delay time of the sensor
(5s-200s). This is the time the sensor stays in the "motion detected" state
after motion was first detected. Rotating the potentiometer clockwise increase
the delay time.

During the delay time the sensor ignores motion and stays in the "motion
detected" state. It goes back to the "no motion detected" state after the delay
time, even if there is continuous motion. The sensor stays in the "no
motion detected" state for the block time of 2.5s (not configurable). After the
delay and block time the sensor is ready to detect motion again if there is any.

This means that the sensor will react to motion at most every delay time plus
block time seconds. For continuous motion the sensor will continuously alternate
between "motion detected" state and "no motion detected" state and stay in
"motion detected" state for the delay time and stay in "no motion detected"
state for the block time.


.. _motion_detector_bricklet_case:

Case
----

A `laser-cut case for the Motion Detector Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-motion-detector-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_motion_detector_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Motion Detector Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_motion_detector_case_built_up_1000.jpg

.. include:: Motion_Detector.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/motion_detector_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Motion Detector Bricklet
   :align: center
   :target: ../../_images/Exploded/motion_detector_exploded.png

|bricklet_case_hint|


.. _motion_detector_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Motion_Detector_hlpi.table
