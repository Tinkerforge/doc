
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

* Full fledged IMU/AHRS with 9 degrees of freedom (3-axis each: accelerometer, compass, gyroscope)
* No accumulating errors, no gimbal lock!
* Factory calibrated, continuous calibration during operation
* Calculates quaternions, linear acceleration, gravity vector as well as heading, roll and pitch
* Directly readable by USB, extendable by two Bricklet ports
* API for many programming languages available

.. _imu_v2_brick_description:

Description
-----------

The IMU Brick 2.0 is the successor of the :ref:`IMU Brick <imu_brick>`. It has
higher resolution sensors, easier recalibration, additional
continuous calibration and an **accuracy increase by two orders of magnitude**.

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
Dimensions (W x D x H)                               40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                                               TBDg
Current Consumption                                  TBDmA
===================================================  ============================================================

Resources
---------

* BNO055 (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/datasheets/BNO055.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/imu-v2-brick/raw/master/hardware/imu-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/imu_v2_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/imu-v2-brick/zipball/master>`__)


Test your IMU Brick 2.0
-----------------------


.. _imu_v2_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: IMU_V2_Brick_hlpi.table
