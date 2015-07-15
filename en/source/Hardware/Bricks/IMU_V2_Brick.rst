
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / IMU Brick 2.0
:FIXME_shoplink: ../../../shop/bricks/imu-v2-brick.html

.. include:: IMU_V2_Brick.substitutions


.. _imu_v2_brick:

IMU Brick 2.0
=============

.. note::
 This Brick is currently work-in-progress!


Features
--------

* Full fledged IMU/AHRS with 9 degrees of freedom (3-axis each: accelerometer,
  compass, gyroscope)
* No accumulating errors, no gimbal lock!
* Factory calibrated, automatic continuous self-calibration during operation
* Calculates quaternions, linear acceleration, gravity vector as well as
  heading, roll and pitch
* Directly readable by USB, extendable by two Bricklet ports


.. _imu_v2_brick_description:

Description
-----------

The IMU Brick 2.0 is the successor of the :ref:`imu_brick` with
higher resolution sensors, easier recalibration, additional continuous
self-calibration and an **accuracy increase by two orders of magnitude**.

The IMU :ref:`Brick <primer_bricks>` 2.0 is equipped with a 3-axis
accelerometer, magnetometer (compass) and gyroscope and works as a **USB**
`inertial measurement unit <http://en.wikipedia.org/wiki/Inertial_measurement_unit>`__.
It can measure 9 degrees of freedom and computes
`quaternions <http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__,
linear acceleration, gravity vector as well as `heading, roll and pitch
<http://en.wikipedia.org/wiki/File:Rollpitchyawplain.png>`__ information.
It is a complete `attitude and heading reference system
<http://en.wikipedia.org/wiki/AHRS>`__.

The API, provided for many :ref:`programming languages <imu_brick_programming_interface>`,
allows access to the calculated data and also the acceleration, magnetic field
and angular velocity of the three axes. If the quaternion representation is
used, the IMU Brick 2.0 does not have a
`gimbal lock <http://en.wikipedia.org/wiki/Gimbal_lock>`__,
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

Technical Specifications
------------------------

===================================================  ============================================================
Property                                             Value
===================================================  ============================================================
Acceleration, Magnetic, Angular Velocity Resolution  14bit, 16bit, 16bit
Heading, Roll, Pitch Resolution                      0.01° steps
Quaternion Resolution                                16bit
Sampling Rate                                        100Hz
---------------------------------------------------  ------------------------------------------------------------
---------------------------------------------------  ------------------------------------------------------------
Bricklet Ports                                       2
Dimensions (W x D x H)                               40 x 40 x 19mm (1.57 x 1.57 x 0.75")
Weight                                               12g
Current Consumption                                  TBDmA
===================================================  ============================================================

Resources
---------

* BNO055 datasheet (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/datasheets/BNO055.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/hardware/imu-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/imu_v2_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/imu-v2-brick/zipball/master>`__)


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

Click the "Calibration" button in Brick Viewer to see the current continuous
self-calibration status. The dialog also allows to update the saved calibration
data.


.. _imu_v2_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: IMU_V2_Brick_hlpi.table
