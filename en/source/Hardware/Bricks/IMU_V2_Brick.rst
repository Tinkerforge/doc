
:shoplink: ../../../shop/bricks/imu-v2-brick.html

.. include:: IMU_V2_Brick.substitutions


.. _imu_v2_brick:

IMU Brick 2.0
=============

.. raw:: html

    {% tfgallery %}

	Bricks/brick_imu_v2_tilted1_[?|?].jpg          IMU Brick 2.0
	Bricks/brick_imu_v2_tilted2_[?|?].jpg          IMU Brick 2.0
	Bricks/brick_imu_v2_front_[?|?].jpg            IMU Brick 2.0
	Bricks/brick_imu_v2_caption_[?|?].jpg          IMU Brick 2.0 with caption
	Bricks/brick_imu_v2_top_[?|?].jpg              IMU Brick 2.0 top
	Bricks/brick_imu_v2_bottom_[?|?].jpg           IMU Brick 2.0 bottom
	Dimensions/imu_brick_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Full fledged IMU/AHRS with 9 degrees of freedom (3-axis each: accelerometer,
  compass, gyroscope)
* No accumulating errors, no gimbal lock!
* Factory calibrated, automatic continuous self-calibration during operation
* Calculates quaternions, linear acceleration, gravity vector as well as
  independent heading, roll and pitch angles
* Directly readable by USB, extendable by two Bricklet ports


.. _imu_v2_brick_description:

Description
-----------

The IMU Brick 2.0 is the successor of the :ref:`imu_brick` with
higher resolution sensors, easier recalibration, additional continuous
self-calibration and an **accuracy increase by two orders of magnitude**.

The IMU :ref:`Brick <primer_bricks>` 2.0 is equipped with a 3-axis
accelerometer, magnetometer (compass) and gyroscope and works as a **USB**
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
used, the IMU Brick 2.0 does not have a
`gimbal lock <https://en.wikipedia.org/wiki/Gimbal_lock>`__,
as known from Euler angles.

Two :ref:`Bricklet <primer_bricklets>` ports can be used to extend the
features of this Brick. For Example a :ref:`GPS Bricklet <gps_bricklet>` can be
attached to get position information.

The IMU Brick 2.0 can be use together with other Bricks in a
:ref:`stack <primer_stack>`. For example an additional
:ref:`Master Brick <master_brick>` with
:ref:`Master Extension <primer_master_extensions>` allows to replace the USB
connection by other cable based (:ref:`RS485 <rs485_extension>`,
:ref:`Ethernet <ethernet_extension>`) or wireless (:ref:`WIFI <wifi_extension>`)
connections.

The IMU Brick 2.0 currently still uses 10-pole Bricklet connectors.
:ref:`You need 10p-7p Bricklet cables to connect Bricklets to it <tutorial_bricklet_cables>`.

A comparison video between IMU Brick 1.0 and IMU Brick 2.0 is available on Youtube:

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/Aq3SqVen5AQ" frameborder="0" allowfullscreen></iframe>


Technical Specifications
------------------------

===================================================  ============================================================
Property                                             Value
===================================================  ============================================================
Acceleration, Magnetic, Angular Velocity Resolution  14bit, 16bit, 16bit
Heading, Roll, Pitch Resolution                      0.0625° steps
Quaternion Resolution                                16bit
Sampling Rate                                        100Hz
---------------------------------------------------  ------------------------------------------------------------
---------------------------------------------------  ------------------------------------------------------------
Bricklet Ports                                       2
Dimensions (W x D x H)                               40 x 40 x 19mm (1.57 x 1.57 x 0.75")
Weight                                               12g
Current Consumption                                  415mW (83mA at 5V)
===================================================  ============================================================


Resources
---------

* BNO055 datasheet (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/datasheets/BNO055.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/hardware/imu-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/imu_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/imu-v2-brick/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2Bf80YI>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/imu_v2/imu.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/imu_v2/imu.FCStd>`__)

Connectivity
------------

The following picture depicts the different connection possibilities of the
IMU Brick 2.0.

.. image:: /Images/Bricks/brick_imu_v2_caption_600.jpg
   :scale: 100 %
   :alt: IMU Brick 2.0 with caption
   :align: center
   :target: ../../_images/Bricks/brick_imu_v2_caption_800.jpg


Test your IMU Brick 2.0
-----------------------

|test_intro|

|test_tab|

.. image:: /Images/Bricks/imu_v2_brickv.jpg
   :scale: 100 %
   :alt: IMU Brick 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/imu_v2_brickv.jpg

You can see all of the available data form the IMU Brick 2.0. If you hold the
IMU Brick in the orientation as shown in the image and press
"Save Orientation", the movements that you make with the IMU Brick should be
mirrored in the Brick Viewer.

|test_pi_ref|


Calibration
-----------

The IMU Brick 2.0 does continuous self-calibration during usage. It is not
necessary to start a specific manual calibration process. The IMU can store the
calibration data to speed-up the self-calibration after each restart. This
data is initialized at the factory.

.. image:: /Images/Screenshots/imu_v2_brick_calibration.jpg
   :scale: 100 %
   :alt: IMU Brick 2.0 calibration in Brick Viewer
   :align: center
   :target: ../../_images/Screenshots/imu_v2_brick_calibration.jpg

Click the "Calibration" button in Brick Viewer to see the current continuous
self-calibration status. The dialog also allows to update the saved calibration
data.


.. _imu_v2_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: IMU_V2_Brick_hlpi.table
