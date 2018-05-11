
:shoplink: ../../../shop/bricklets/motion-detector-v2-bricklet.html

.. include:: Motion_Detector_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _motion_detector_v2_bricklet:

Motion Detector Bricklet 2.0
============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_motion_detector_v2_tilted_[?|?].jpg             Motion Detector Bricklet 2.0
	Bricklets/bricklet_motion_detector_v2_side_[?|?].jpg               Motion Detector Bricklet 2.0
	Bricklets/bricklet_motion_detector_v2_bottom_[?|?].jpg             Motion Detector Bricklet 2.0
	Bricklets/bricklet_motion_detector_v2_top_[?|?].jpg                Motion Detector Bricklet 2.0
	Bricklets/bricklet_motion_detector_v2_tilted_black_lense_[?|?].jpg Motion Detector Bricklet 2.0 (black lense)
	Cases/bricklet_motion_detector_v2_case_built_up_[?|?].jpg          Motion Detector Bricklet 2.0 in case
	Cases/bricklet_motion_detector_v2_case_be_built_up_[100|].jpg      Motion Detector Bricklet 2.0 in case (black)
	Bricklets/bricklet_motion_detector_v2_brickv_[100|].jpg            Motion Detector Bricklet 2.0 in Brick Viewer
	Dimensions/motion_detector_v2_bricklet_dimensions_[100|600].png    Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Passive Infrared Motion Sensor
* Detects motion in distances of up to 12m (sensitivity configurable)
* High sensing angle (120°)
* Fresnel lens has controllable backlight

.. _motion_detector_v2_bricklet_description:

Description
-----------

The Motion Detector :ref:`Bricklet <primer_bricklets>` is equipped
with a passive infrared (PIR) sensor. It can be used to extend 
:ref:`Bricks <primer_bricks>` to sense movement of people and animals. 
It has a configurable detection range of up to 12m with a sensing angle of 120°.

By using configurable events it is possible to react on detected motion without
polling.

The fresnel lens has a blue backlight with controllable intensity. The backlight
can be used as an indicator for detected motion or as a general purpose indication
light.

The Motion Detector Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Backlight in action:

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_motion_detector_v2_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_motion_detector_v2_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_motion_detector_v2_video.webm" type="video/webm">
	</video>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption (LEDs off)    37mW
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensing Range                     up to 12m
Sensing Angle                     120°
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 45 x 30mm (0.98 x 1.78 x 1.18")
Weight                            6g
================================  ============================================================


Resources
---------

* PIR Sensor AS612 (`Download <https://github.com/Tinkerforge/motion-detector-v2-bricklet/raw/master/datasheets/AS612.pdf>`__)
* Fresnel Lens S8002-2W (`Download <https://github.com/Tinkerforge/motion-detector-v2-bricklet/raw/master/datasheets/S8002-2w.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/motion-detector-v2-bricklet/raw/master/hardware/motion-detector-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/motion_detector_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/motion-detector-v2-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2sBeApm>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/motion_detector_v2/motion-detector-v2.step>`__,  `FreeCAD <http://download.tinkerforge.com/3d/bricklets/motion_detector_v2/motion-detector-v2.FCStd>`__)


.. _motion_detector_v2_bricklet_test:

Test your Motion Detector Bricklet 2.0
--------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see when a motion is detected.

.. image:: /Images/Bricklets/bricklet_motion_detector_v2_brickv.jpg
   :scale: 100 %
   :alt: Motion Detector Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_motion_detector_v2_brickv.jpg

|test_pi_ref|



.. _motion_detector_v2_bricklet_case:

Case
----

A `laser-cut case for the Motion Detector Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-motion-detector-v2-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_motion_detector_v2_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Motion Detector Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_motion_detector_v2_case_built_up_1000.jpg

.. include:: Motion_Detector_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/motion_detector_v2_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Motion Detector Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/motion_detector_v2_exploded.png

|bricklet_case_hint|


.. _motion_detector_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Motion_Detector_V2_hlpi.table
