
:shoplink: ../../../shop/bricklets/motion-detector-bricklet.html

.. include:: Motion_Detector.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _motion_detector_bricklet:

Motion Detector Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_motion_detector_tilted_[?|?].jpg           Motion Detector Bricklet
	Bricklets/bricklet_motion_detector_horizontal_[?|?].jpg       Motion Detector Bricklet
	Cases/bricklet_motion_detector_case_tilted_[?|?].jpg          Motion Detector Bricklet in Case
	Bricklets/bricklet_motion_detector_brickv_[100|].jpg          Motion Detector Bricklet in Brick Viewer
	Dimensions/motion_detector_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Passive Infrared Motion Sensor
* Detects motion in distances of up to 7m (configurable)
* High sensing angle (100°)


.. _motion_detector_bricklet_description:

Description
-----------

The Motion Detector :ref:`Bricklet <primer_bricklets>` is equipped
with a passive infrared (PIR) sensor. It can be used to extend 
:ref:`Bricks <primer_bricks>` to sense movement of people and animals. 
It has a configurable detection range of 3m to 7m with a sensing angle of 100°.

By using configurable events it is possible to react on detected motion without
polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
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

|test_connect|. Attach the motion detector on top of the Bricklet.

|test_tab|
If everything went as expected you can now see when a motion is detected.

.. image:: /Images/Bricklets/bricklet_motion_detector_brickv.jpg
   :scale: 100 %
   :alt: Motion Detector Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_brickv.jpg

|test_pi_ref|



.. _motion_detector_bricklet_sensitivity_delay_block_time:

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
after no motion is detected anymore. Rotating the potentiometer clockwise
increase the delay time.

If motion is detected the sensor enters the "motion detected" state and stays
in this state as long as there is continuous motion. After no motion is detected
anymore the sensor stays in the "motion detected" state for the duration of the
delay time. If no motion is detected during the delay time then the sensor
enters the "no motion detected" state. But if motion is detected during the
delay time then it stays in the "motion detected" state. This means the sensor
will only leave the "motion detected" state if there is no motion for the
duration of the delay time.

If the sensor enters the "no motion detected" state it will ignore motion
for the duration of the block time (2.5s, not configurable). After the block
time the sensor is ready to detect motion again if there is any.


Status LED
----------

The blue LED on the Bricklet is on if the sensor is in the "motion detected"
state and is off if the sensor is in the "no motion detected" state.


..
  Modification Possibilities
  --------------------------
  The motion sensor can also be placed independently from the Bricklet. To do this a
  small jumper is delivered with the sensor and the Bricklet. Place the Jumper
  on the sensor as depicted below.

  TODO Image sensor with placed jumper

  After this you have to establish a connection between the sensor and the
  Bricklet. For example this can be done by soldering three wires on them as
  depicted below

  TODO Image sensor <-> cable <-> Bricklet


.. _motion_detector_bricklet_case:

Case
----

A `laser-cut case for the Motion Detector Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-motion-detector-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_motion_detector_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for Motion Detector Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_motion_detector_case_tilted_1000.jpg

.. include:: Motion_Detector.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/motion_detector_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Motion Detector Bricklet
   :align: center
   :target: ../../_images/Exploded/motion_detector_exploded.png

|bricklet_case_hint|


.. _motion_detector_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Motion_Detector_hlpi.table
