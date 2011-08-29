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

The IMU :ref:`Brick <product_overview_bricks>` is a microcontroller board 
which is equipped with a `inertial measurement unit
<http://en.wikipedia.org/wiki/Inertial_measurement_unit>`_
consists of a 3-axis accelerometer, magnetometer and gyroscope.
The board can compute `heading , attitude and yaw
<http://en.wikipedia.org/wiki/File:Rollpitchyawplain.png>`_. 
Therefore it is a complete `Attitude and heading reference system
<http://en.wikipedia.org/wiki/AHRS>`_. The board is named "IMU" since AHRS is
not a common term.

It is compatible to other Tinkerforge 
:ref:`Bricks <product_overview_bricks>`
and can be used within a Stack. 
Two :ref:`Bricklet <product_overview_bricklets>` ports 
can be used to extend the features of this device by 
interfacing up to two Bricklets. 

Controlling the device is possible in several ways. You can control it via 
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless 
(**Zigbee**, **WLAN**) connections via a Master Brick with according 
Master Extension (:ref:`High Level Concept <_pi_hlpi>`). 
Also it is possible to control the device low level via a **I2C**, **SPI** or
**UART (serial)** interface from other microcontroller boards
(:ref:`Low Level Concept <pi_llpi>`). A direct interface for
Arduinos is provided by our :doc:`Tinkershield </Hardware/Tinkershield>`.
Since the firmware is opensource it is of course possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`).

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
TBD                               TBD
--------------------------------  ------------------------------------------------------------

--------------------------------  ------------------------------------------------------------
Pitch Resolution                  TBD
Acceleration Resolution           :math:`\frac{1}{2^{16}}\;\frac{\text{Velocity}}{\text{s}^2}`
--------------------------------  ------------------------------------------------------------

--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            TBD
================================  ============================================================


Resources
---------

 * Schematic (Download)
 * 3-axis Accelerometer/Magnetometer LSM303 Datasheet (`Download <http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00260288.pdf>`_)
 * 3-axis Gyroscope ITG-3200 Datasheet (`Download <http://invensense.com/mems/gyro/documents/PS-ITG-3200-00-01.4.pdf>`_)
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

.. image:: /Images/Dimensions/imu_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center



Interfaces and Coding
---------------------

:ref:`High Level Interfaces <pi_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", "API", "Examples", "Installation"
   "Java", "API", "Examples", "Installation"
   "C", "API", "Examples", "Installation"
   "C++", "API", "Examples", "Installation"


Low Level Interfaces
^^^^^^^^^^^^^^^^^^^^
.. csv-table::
   :header: "Interface", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "SPI", "API", "Examples", "Installation"
   "I2c", "API", "Examples", "Installation"
   "UART(serial)", "API", "Examples", "Installation"


Direct on Device Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
   :header: "Interface", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Programming", "API", "Examples", "Installation"


IMU Calibration
---------------

TBD

Troubleshoot
------------


IMU is not working correctly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Reasons:** 
 * Erroneous Calibration

**Solutions:**
 * Calibrate your device
