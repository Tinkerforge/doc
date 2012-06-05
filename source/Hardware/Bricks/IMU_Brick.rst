.. _imu_brick:

IMU Brick
=========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricks/brick_imu_tilted_front_350.jpg", 
	             "Bricks/brick_imu_tilted_front_600.jpg", 
	             "IMU Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_imu_tilted_back_100.jpg", 
	             "Bricks/brick_imu_tilted_back_600.jpg", 
	             "IMU Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_imu_caption_100.jpg", 
	             "Bricks/brick_imu_caption_600.jpg", 
	             "IMU Brick with caption") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_imu_top_100.jpg", 
	             "Bricks/brick_imu_top_600.jpg", 
	             "IMU Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_imu_bottom_100.jpg", 
	             "Bricks/brick_imu_bottom_600.jpg", 
	             "IMU Brick") 
	}}
	{{ 
	    tfdocimg("Dimensions/imu_brick_dimensions_100.png", 
	             "Dimensions/imu_brick_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * 9 DOF: Full fledged attitude heading reference system
 * No accumulating errors, no gimbal lock!
 * Factory calibrated, easy to recalibrate
 * Calculates quaternions as well as roll, pitch and yaw.
 * One USB port and two Bricklet ports

Description
-----------

The IMU :ref:`Brick <product_overview_bricks>` is equipped with a 32-bit ARM
microcontroller and an `inertial measurement unit
<http://en.wikipedia.org/wiki/Inertial_measurement_unit>`__.
It has 9 degrees of freedom and consists of a 3-axis accelerometer, 
magnetometer and gyroscope. The board computes 
`quaternions <http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__ 
as well as `roll, pitch and yaw
<http://en.wikipedia.org/wiki/File:Rollpitchyawplain.png>`__ information, 
it is a complete `Attitude and heading reference system
<http://en.wikipedia.org/wiki/AHRS>`__. 
The API allows access to the calculated data and
also the acceleration, magnetic field and angular velocity for the 
three axes. If the quaternion representation is used, the IMU Brick does
not have a `gimbal lock <http://en.wikipedia.org/wiki/Gimbal_lock>`__,
as known from euler angles.

It is compatible to other Tinkerforge 
:ref:`Bricks <product_overview_bricks>`
and can be used within a stack. 
Two :ref:`Bricklet <product_overview_bricklets>` ports 
can be used to extend the features of this device. 

Controlling the device is possible in several ways. You can control it via 
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless 
(**Zigbee**, **WLAN**) connections via an additional Master Brick with 
corresponding Master-Extension (:ref:`High Level Concept <pi_hlpi>`). 

In the future it will be possible to control the device low level via a 
**I2C**, **SPI** or **UART (serial)** interface from other microcontroller 
boards (:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is opensource it is possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`).
Currently we are not offering an on device API.

Technical Specifications
------------------------

===================================================  ============================================================
Property                                             Value
===================================================  ============================================================
Microcontroller                                      ATSAM3S2B (128kB Flash, 32k RAM)
Current Consumption                                  53mA
---------------------------------------------------  ------------------------------------------------------------
Acceleration, Magnetic, Angular Velocity Resolution  16-bit
Roll, Pitch, Yaw Resolution                          16-bit, output in 0.01 degree steps
Quaternion Resolution                                32-bit
---------------------------------------------------  ------------------------------------------------------------
---------------------------------------------------  ------------------------------------------------------------
Bricklet Ports                                       2
Dimensions (W x D x H)                               40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                                               12g
===================================================  ============================================================


Resources
---------

* 3-axis Accelerometer/Magnetometer LSM303 Datasheet (`Download <http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00260288.pdf>`__)
* 3-axis Gyroscope ITG-3200 Datasheet (`Download <http://invensense.com/mems/gyro/documents/PS-ITG-3200A.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/imu-brick/raw/master/hardware/imu-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/imu_brick_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/imu-brick/zipball/master>`__)


.. _imu_brick_test:

Test your IMU Brick
-------------------

To test the IMU Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>` 
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes. 

Connector your IMU Brick to the PC over USB, you should see a tab named
"IMU Brick" in the Brick Viewer after you pressed "connect". Select it.

.. image:: /Images/Bricks/imu_brickv.jpg
   :scale: 60 %
   :alt: Brickv view of the IMU Brick
   :align: center
   :target: ../../_images/Bricks/imu_brickv.jpg

You can see all of the available data form the IMU Brick. If you hold the
IMU Brick in the orientation as shown in the image and press
"Save Orientation", the movements that you make with the IMU Brick should be
mirrored in the Brick Viewer. Before you press "Save Orientation" you should
hold the IMU Brick still for about 15 seconds, so it can converge to the
correct position.


Connectivity
------------

The following picture depicts the different connection possibilities of the 
IMU Brick.

.. image:: /Images/Bricks/brick_imu_caption_600.jpg
   :scale: 100 %
   :alt: IMU Brick with caption
   :align: center
   :target: ../../_images/Bricks/brick_imu_caption_800.jpg

IMU Calibration
---------------

The IMU Brick comes factory calibrated and should work out of the box. It is 
however easy to recalibrate, if necessary.

The factory calibration has taken place in a room without any significant
magnetic fields. If you want to operate the IMU Brick near something that
has a magnetic field (e.g. near a motor), you will have to recalibrate
the magnetometer in the exact position where it will be used later on!

To calibrate the magnetometer press on "Calibrate" in the Brick Viewer and
choose "Magnetometer" in the tab of the new window. Press "Start Calibration"
and now change the orientation of the IMU Brick until the bias and gain values
shown in the GUI do not change anymore. Press "Ready" when this is the case 
and you are done.

Accelerometer and gyroscope can be calibrated similarly, follow the
instructions as given by the calibration tool. We recommend that you
export the calibration before you start recalibrating the accelerometer
and the gyroscope, so you are able to go back to the old calibration.

We recommend that you don't try to recalibrate the gyroscope gain, it is not
possible without suitable external machinery. 

The factory calibration for your IMU Brick can be found at:
http://download.tinkerforge.com/imu_calibration/YOUR_IMU_UID.txt
(replace YOUR_IMU_UID by the UID of your IMU Brick).
If you accidentially miscalibrated a sensor or you
flashed a new firmware version, you can reimport the factory calibration.

Quaternions vs Euler Angles
---------------------------

We highly recommend that you use  
`quaternions <http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__
in your project rather than euler angles (`roll, pitch and yaw
<http://en.wikipedia.org/wiki/File:Rollpitchyawplain.png>`__), since the latter
exhibits a `gimbal lock <http://en.wikipedia.org/wiki/Gimbal_lock>`__.

A formula to transform quaternions to rotation matrices can be found in the
API documentation.

Note that Euler Angles always have an order in which they are applied. For
example: You can't just use the yaw value of the Euler Angles and use it 
as a compass. The same is true for the other angles.

If you want this kind of data (i.e. an angle that is detached from the other
angles) you can use quaternions to calculate it.

For example, to get a compass without gimbal lock that is independent of the
other angles you can do the following: Multiply the quaternions with a vector 
facing in the y axis, take the x and y component from the result and calculate 
the angle for the vector.

To multiply a quaternion (q) with a 3d vector (v) you have to represent the
vector as a quaternion with w=0 (v') and calculate: 

.. math::
 q\cdot v'\cdot q^{-1},

where q^-1 is the conjugate of the quaternion. After that you can calculate the 
angle with atan2.

Pseudo code for this for all angles::

	q = getQuaternion()
	v1 = Vector3d(0, 0, 1)
	v2 = q*v1
	x_angle = atan2(v2.y, v2.z)

	q = getQuaternion()
	v1 = Vector3d(0, 0, 1)
	v2 = q*v1
	y_angle = atan2(v2.x, v2.z)

	q = getQuaternion()
	v1 = Vector3d(0, 1, 0)
	v2 = q*v1
	z_angle = atan2(v2.x, v2.y)

All angles calculated and completely simplified::

	x_angle = atan2(2*y*z - 2*x*w, w*w + z*z - x*x - y*y)*180/PI
	y_angle = atan2(2*w*y + 2*x*z, w*w + z*z  -x*x - y*y)*180/PI
	z_angle = atan2(-w*y + x*y + y*x - w*w, w*w + y*y - z*y - x*x)*180/PI


What is this sourcery, how does it work?
----------------------------------------
With the sensor data gathered by the IMU Brick (angular velocity, acceleration, 
magnetic field), it is possible to apply sensor fusion to accquire an absolute
orientation. 

For this process often a
`Kalman Filter <http://en.wikipedia.org/wiki/Kalman_filter>`__ is used.
The filter that is used in the IMU Brick is based on
`this paper <http://imumargalgorithm30042010sohm.googlecode.com/files/An%20efficient%20orientation%20filter%20for%20inertial%20and%20inertialmagnetic%20sensor%20arrays.pdf>`__ 
by S. O. Madgwick. In our tests this new state of the art filter 
could achieve significantly better results than a Kalman Filter.

Madgwick's filter calculates the orientation by numerically integrating the 
estimated orientation rate. It is computed as the rate of change of 
orientation measured by the gyroscopes. The magnitude of the gyroscope 
measurement error is removed in the direction of the estimated error,
which is computed from accelerometer and magnetometer measurements. 

.. image:: /Images/Bricks/imu_math_magic.png
   :scale: 100 %
   :alt: Block diagram of orientation filter from S. O. Madgwick: "An efficient orientation filter for inertial and inertial/magnetic sensor arrays", University of Bristol, April 2010.
   :align: center
   :target: ../../_images/Bricks/imu_math_magic.png

Image and explanation from S. O. Madgwick: "An efficient orientation filter 
for inertial and inertial/magnetic sensor arrays", University of Bristol, 
April 2010.

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: IMU_Brick_hlpi.table

Low Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note::  Coming soon! 

  A special firmware to control the IMU Brick over 
  SPI, I2C and UART is planned.
  
..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "SPI", "API", "Examples", "Installation"
     "I2C", "API", "Examples", "Installation"
     "UART(serial)", "API", "Examples", "Installation"


On Device Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note:: Coming soon!

  An API and documentation for direct on device programming (comparable
  to arduino) is planned.
  You can however already use our firmware as a starting point for your 
  own modifications (C knowledge required).

..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "Programming", "API", "Examples", "Installation"

