.. _imu_brick:

IMU Brick
=========

.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

The IMU :ref:`Brick <product_overview_bricks>` is a equipped with a 32-bit ARM
microcontroller and an `inertial measurement unit
<http://en.wikipedia.org/wiki/Inertial_measurement_unit>`_.
It consists of a 3-axis accelerometer, magnetometer and gyroscope.
The board computes `roll , pitch and yaw
<http://en.wikipedia.org/wiki/File:Rollpitchyawplain.png>`_ information, 
therefore it is a complete `Attitude and heading reference system
<http://en.wikipedia.org/wiki/AHRS>`_. 
The API lets you access the roll, pitch and yaw data,
but also acceleration, magnetic field and angular velocity for the 
three axes. Besides the `euler angles 
<http://en.wikipedia.org/wiki/Euler_angles>`_ (roll, pitch, yaw) it is 
possible to get an 
`quaternion <http://en.wikipedia.org/wiki/Quaternion>`_
representation which removes the `gimbal lock 
<http://en.wikipedia.org/wiki/Gimbal_lock>`_ problem of euler angels.

It is compatible to other Tinkerforge 
:ref:`Bricks <product_overview_bricks>`
and can be used within a stack. 
Two :ref:`Bricklet <product_overview_bricklets>` ports 
can be used to extend the features of this device by 
interfacing up to two Bricklets. 

Controlling the device is possible in several ways. You can control it via 
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless 
(**Zigbee**, **WLAN**) connections via a Master Brick with according 
Master-Extension (:ref:`High Level Concept <pi_hlpi>`). 

In the future it will be possible to control the device low level via a 
**I2C**, **SPI** or **UART (serial)** interface from other microcontroller 
boards (:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is opensource it is of course possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`).
Currently we are not offering an on device API.

Technical Specifications
------------------------

===================================================  ============================================================
Property                                             Value
===================================================  ============================================================
Acceleration, Magnetic, Angular Velocity Resolution  16-bit
Roll, Pitch, Yaw Resolution                          16-bit
Quaternion Resolution                                32-bit
---------------------------------------------------  ------------------------------------------------------------
---------------------------------------------------  ------------------------------------------------------------
Bricklet Ports                                       2
Dimensions (W x D x H)                               40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                                               TBD
===================================================  ============================================================


Resources
---------

 * Schematic (Download)
 * 3-axis Accelerometer/Magnetometer LSM303 Datasheet (`Download <http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00260288.pdf>`__)
 * 3-axis Gyroscope ITG-3200 Datasheet (`Download <http://invensense.com/mems/gyro/documents/PS-ITG-3200-00-01.4.pdf>`__)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

Connectivity
------------

The following picture depicts the different connection possibilities of the 
IMU Brick.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/imu_brick_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


IMU Calibration
---------------

TBD

Programming Interfaces
----------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^
See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", "API", "Examples", "Installation"
   "Java", "API", "Examples", "Installation"
   "C", "API", "Examples", "Installation"
   "C++", "API", "Examples", "Installation"


Low Level Interfaces
^^^^^^^^^^^^^^^^^^^^
 .. note::  Comming soon! 

  Currently you have to modify the firmware to use this feature.
  SPI, I2C and UART interface are present and can be easily accessed with our
  :ref:`Breakout Board <breakout_brick>`. A special firmware is planned
  to control this brick over the different interfaces by transmitted commands.
  
..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "SPI", "API", "Examples", "Installation"
     "I2C", "API", "Examples", "Installation"
     "UART(serial)", "API", "Examples", "Installation"


Direct on Device Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note:: Coming soon!

  Currently no API or special documentation exists for direct programming.
  You can use our firmware as startingpoint for your own modifications.

..
  .. csv-table::
     :header: "Interface", "API", "Examples", "Installation"
     :widths: 25, 8, 15, 12

     "Programming", "API", "Examples", "Installation"

Troubleshoot
------------


IMU is not working correctly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Reasons:** 
 * Erroneous Calibration

**Solutions:**
 * Calibrate your device
