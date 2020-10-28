
:shoplink: ../../../shop/bricklets/imu-v3-bricklet.html

.. include:: IMU_V3.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _imu_v3_bricklet:

IMU Bricklet 3.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_imu_v3_tilted_[?|?].jpg           IMU Bricklet 3.0
	Bricklets/bricklet_imu_v3_tilted2_[?|?].jpg          IMU Bricklet 3.0
	Bricklets/bricklet_imu_v3_horizontal_[?|?].jpg       IMU Bricklet 3.0
	Bricklets/bricklet_imu_v3_brickv_[100|].jpg          IMU Bricklet 3.0 in Brick Viewer
	Dimensions/imu_v3_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Full fledged IMU/AHRS with 9 degrees of freedom (3-axis each: accelerometer,
  compass, gyroscope)
* No accumulating errors, no gimbal lock!
* Factory calibrated, automatic continuous self-calibration during operation
* Calculates quaternions, linear acceleration, gravity vector as well as
  independent heading, roll and pitch angles


.. _imu_v3_bricklet_description:

Description
-----------

The IMU Bricklet 3.0 offers the same functionality and performance as
the :ref:`IMU Brick 2.0 <imu_v2_brick>`, but in the form-factor of a Bricklet.

The IMU :ref:`Bricklet <primer_bricklets>` 3.0 is equipped with a 3-axis
accelerometer, magnetometer (compass) and gyroscope and works as 
`inertial measurement unit <https://en.wikipedia.org/wiki/Inertial_measurement_unit>`__.
It can measure 9 degrees of freedom and computes
`quaternions <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__,
linear acceleration, gravity vector as well as independent `heading, roll and
pitch <https://en.wikipedia.org/wiki/File:Rollpitchyawplain.png>`__ angles.
It is a complete `attitude and heading reference system
<https://en.wikipedia.org/wiki/AHRS>`__.

The API, provided for many :ref:`programming languages <imu_brick_programming_interface>`,
allows access to the calculated data and also the acceleration, magnetic field
and angular velocity of the three axes. If the quaternion representation is
used, the IMU Bricklet 3.0 does not have a
`gimbal lock <https://en.wikipedia.org/wiki/Gimbal_lock>`__,
as known from Euler angles.

The IMU Bricklet 3.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

.. raw:: html

	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_imu_v3_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_imu_v3_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_imu_v3_video.webm" type="video/webm">
	</video>


Technical Specifications
------------------------

===================================================  ============================================================
Property                                             Value
===================================================  ============================================================
Sensor                                               BNO055
Current Consumption                                  95mW (19mA at 5V)
---------------------------------------------------  ------------------------------------------------------------
---------------------------------------------------  ------------------------------------------------------------
Acceleration, Magnetic, Angular Velocity Resolution  14bit, 16bit, 16bit
Heading, Roll, Pitch Resolution                      0.0625° steps
Quaternion Resolution                                16bit
Sampling Rate                                        100Hz
---------------------------------------------------  ------------------------------------------------------------
---------------------------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)                               25 x 25 x 5mm (0.98 x 0.98 x 0.19")
Weight                                               3g 
===================================================  ============================================================


Resources
---------

* BNO055 datasheet (`Download <https://github.com/Tinkerforge/imu-v3-bricklet/raw/master/datasheets/bno055.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/imu-v3-bricklet/raw/master/hardware/imu-v3-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/imu_v3_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/imu-v3-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/imu_v3/imu-v3.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/imu_v3/imu-v3.FCStd>`__)


.. _imu_v3_bricklet_test:

Test your IMU Bricklet 3.0
--------------------------

|test_intro|

|test_connect|.

|test_tab|

.. image:: /Images/Bricklets/bricklet_imu_v3_brickv.jpg
   :scale: 100 %
   :alt: IMU Bricklet 3.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_imu_v3_brickv.jpg

You can see all of the available data form the IMU Bricklet 3.0. If you hold the
IMU Bricklet 3.0 in the orientation as shown in the image and press
"Save Orientation", the movements that you make with the IMU Bricklet 3.0 should be
mirrored in the Brick Viewer.

|test_pi_ref|


Calibration
-----------

The IMU Bricklet 3.0 does continuous self-calibration during usage. It is not
necessary to start a specific manual calibration process. The IMU can store the
calibration data to speed-up the self-calibration after each restart. This
data is initialized at the factory.

.. image:: /Images/Screenshots/imu_v3_bricklet_calibration.jpg
   :scale: 100 %
   :alt: IMU Bricklet 3.0 calibration in Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/imu_v3_bricklet_calibration.jpg

Click the "Calibration" button in Brick Viewer to see the current continuous
self-calibration status. The dialog also allows to update the saved calibration
data.


.. _imu_v3_bricklet_case:

Case
----

A `laser-cut case for the IMU Bricklet 3.0
<https://www.tinkerforge.com/en/shop/cases/case-real-time-clock-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_real_time_clock_v2_case_350.jpg
   :scale: 100 %
   :alt: Case for IMU Bricklet 3.0
   :align: center
   :target: ../../_images/Cases/bricklet_real_time_clock_v2_case_1000.jpg

.. include:: IMU_V3.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/real_time_clock_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for IMU Bricklet 3.0
   :align: center
   :target: ../../_images/Exploded/real_time_clock_exploded.png

|bricklet_case_hint|


.. _imu_v3_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: IMU_V3_hlpi.table
