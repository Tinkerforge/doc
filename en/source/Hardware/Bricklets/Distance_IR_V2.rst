
:DISABLED_shoplink: ../../../shop/bricklet/distance-ir-v2-bricklet.html

.. include:: Distance_IR_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _distance_ir_v2_bricklet:

Distance IR Bricklet 2.0
========================

.. note::
  This Bricklet is currently work-in-progress!

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_distance_ir_v2_tilted_[?|?].jpg           Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_tilted2_[?|?].jpg          Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_top_[?|?].jpg              Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_side_[?|?].jpg             Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_bottom_[?|?].jpg           Distance IR Bricklet 2.0
	Bricklets/bricklet_distance_ir_v2_brickv_[100|].jpg          Distance IR Bricklet 2.0 in Brick Viewer
	Dimensions/distance_ir_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures distances with IR light
* Sensor can be changed
* Supported ranges: 4-30cm, 10-80cm and 20-150cm


.. _distance_ir_v2_bricklet_description:

Description
-----------

The Distance IR :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure distances. `Sharp <http://www.sharpsma.com>`__ analog
infrared proximity sensors can be attached to the Bricklet.
After configuring the attached sensor you can read out the measured distance
in millimeters. With configurable events it is possible to react on changing
distances without polling.

Infrared sensors with different distance ranges are supported and available in the shop:

* `Infrared Sensor 4-30cm GP2Y0A41SK0F
  <https://www.tinkerforge.com/en/shop/bricklets/distance-ir-v2-4-30cm-bricklet.html>`__
* `Infrared Sensor 10-80cm GP2Y0A21YK0F
  <https://www.tinkerforge.com/en/shop/bricklets/distance-ir-v2-10-80cm-bricklet.html>`__
* `Infrared Sensor 20-150cm GP2Y0A02YK0F
  <https://www.tinkerforge.com/en/shop/bricklets/distance-ir-v2-20-150cm-bricklet.html>`__

Typically these types of sensors are used in robotics to measure distances
for mapping or localization purposes. But you can also use this sensors in
other applications, such as a finding out if a door is opened or closed.

The Distance IR Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

.. raw:: html

	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_distance_ir_v2_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_distance_ir_v2_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_distance_ir_v2_video.webm" type="video/webm">
	</video>

Technical Specifications
------------------------

================================  ==================================================================
Property                          Value
================================  ==================================================================
Sensor                            GP2Y0A41SK0F or GP2Y0A21YK0F or GP2Y0A02YK0F
Current Consumption               110mW (22mA at 5V)
--------------------------------  ------------------------------------------------------------------
--------------------------------  ------------------------------------------------------------------
Distance                          Depends on attached IR Sensor:

                                  * GP2Y0A41SK0F:   4cm -  30cm (1.57" - 11.81")
                                  * GP2Y0A21YK0F:  10cm -  80cm (3.94" - 31.50")
                                  * GP2Y0A02YK0F:  20cm - 150cm (7.87" - 59.06")
--------------------------------  ------------------------------------------------------------------
--------------------------------  ------------------------------------------------------------------
Dimensions (W x D x H)            45 x 13 x 5mm (1.76 x 0.51 x 0.19")*, fits on backside of sensor
Weight                            8g
================================  ==================================================================

\* without cable and sensor


Resources
---------

* GP2Y0A41SK0F datasheet (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/raw/master/datasheets/GP2Y0A41SK0F.pdf>`__)
* GP2Y0A21YK0F datasheet (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/raw/master/datasheets/GP2Y0A21YK0F.pdf>`__)
* GP2Y0A02YK0F datasheet (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/raw/master/datasheets/GP2Y0A02YK0F.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/raw/master/hardware/distance-ir-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/distance_ir_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/distance-ir-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2LPlBes>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/distance_ir_v2/distance-ir-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/distance_ir_v2/distance-ir-v2.FCStd>`__)


.. _distance_ir_v2_bricklet_test:

Test your Distance IR Bricklet 2.0
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the measured distance
of the sensor and a graph that shows the distance over time.

.. image:: /Images/Bricklets/bricklet_distance_ir_v2_brickv.jpg
   :scale: 100 %
   :alt: Distance IR Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_distance_ir_v2_brickv.jpg

|test_pi_ref|


.. _distance_ir_v2_bricklet_case:

Case
----

A `laser-cut case for the Distance IR Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-distance-ir-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_distance_ir_case_350.jpg
   :scale: 100 %
   :alt: Case for Distance IR Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_distance_ir_case_1000.jpg

.. include:: Distance_IR_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/distance_ir_v2_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Distance IR Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/distance_ir_v2_exploded.png

|bricklet_case_hint|


.. _distance_ir_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Distance_IR_V2_hlpi.table
