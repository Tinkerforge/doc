.. _imu_brick:

IMU
===

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


Description
-----------

 .. note::  Coming soon! The IMU Brick is not yet ready to buy.

The IMU :ref:`Brick <product_overview_bricks>` is a equipped with a 32-bit ARM
microcontroller and an `inertial measurement unit
<http://en.wikipedia.org/wiki/Inertial_measurement_unit>`_.
It consists of a 3-axis accelerometer, magnetometer and gyroscope.
The board computes `roll, pitch and yaw
<http://en.wikipedia.org/wiki/File:Rollpitchyawplain.png>`_ information, 
it is a complete `Attitude and heading reference system
<http://en.wikipedia.org/wiki/AHRS>`_. 
The API allows access to the roll, pitch and yaw data,
but also acceleration, magnetic field and angular velocity for the 
three axes. Besides the `euler angles 
<http://en.wikipedia.org/wiki/Euler_angles>`_ (roll, pitch, yaw) it is 
also possible to get an 
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
(**Zigbee**, **WLAN**) connections via a Master Brick with corresponding
Master-Extension (:ref:`High Level Concept <pi_hlpi>`). 

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
Roll, Pitch, Yaw Resolution                          16-bit
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
* Schematic (Download)
* Outline and drilling plan (Download)
* Project source code and design files (Download)


.. _imu_brick_test:

Test your IMU Brick
-------------------

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

TBD

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note::  Coming soon! 

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", "API", "Examples", "Installation"
   "C#", "API", "Examples", "Installation"
   "Java", "API", "Examples", "Installation"
   "Python", "API", "Examples", "Installation"


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

