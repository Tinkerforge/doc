.. _dc_brick:

DC Brick
========

.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

The DC :ref:`Brick <product_overview_bricks>` is equipped with a 32-bit ARM
microcontroller and is able to control one 
`DC brushed motor <http://en.wikipedia.org/wiki/Brushed_DC_electric_motor>`_
bi-directional with max **5A** and **28V**. The current consumption and
power supply voltages can be measured. 
Velocity and acceleration of the motor can be controlled.
In case of overtemperature and overcurrent signals are triggered.
For battery driven applications an undervoltage signal is user configureable.
Additionally, the drive mode can be switched between Drive/Brake and 
Drive/Coast (see :ref:`Drive Modes <dc_brick_drive_mode>`).

It is compatible to other Tinkerforge 
:ref:`Bricks <product_overview_bricks>`
and can be used within a stack. 
Two :ref:`Bricklet <product_overview_bricklets>` ports 
can be used to extend the features of this device. 

The dc motor can be powered by an external powersupply connected
directly to the Brick or by the stack internal powersupply.
If an external powersupply is connected the Brick switches
automatically to this powersupply.

Controlling the device is possible in several ways. You can control it via 
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless 
(**Zigbee**, **WLAN**) connections via an additional Master Brick with according 
Master-Extension (:ref:`High Level Concept <pi_hlpi>`). 

In the future it will be possible to control the device low level via a 
**I2C**, **SPI** or **UART (serial)** interface from other microcontroller 
boards (:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is opensource it is of course possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`). 
Currently we are not offering an on device API.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Maximum Motor Current (Peak)      5A
Minimum/Maximum Input Voltage     6V/28V
Device Current Consumption        TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
PWM Frequency                     Configurable, 1-20khz, default 15khz
Velocity                          -32767 to 32767, full reverse to full forward, 0=stop
Acceleration                      0 to 65535, velocity/s, increment for velocity per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    2
Dimensions (W x D x H)            40mm x 40mm x 17mm  (1.57" x 1.57" x 0.67")
Weight                            TBD
================================  ============================================================

Resources
---------

 * Schematic (Download)
 * MC33926 Datasheet (`Download <http://cache.freescale.com/files/analog/doc/data_sheet/MC33926.pdf>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

  
Connectivity
------------

The following picture depicts the different connection possibilities of the 
DC Brick.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/dc_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


Motor Powersupply
-----------------

.. Todo: Bildchen

The connected motor can be powered through the onboard power-connector
or through a :ref:`Power-Supply Board <product_overview_powersupplies>` in a stack.
The Brick switches autonomously to the onboard power-connector when there
is a voltage measured. 

.. _dc_brick_drive_mode:

Drive Modes
-----------

There are two possible modes of motor controls:
 * Drive/Brake

   In this mode the motor is always either driving or braking, there is no 
   freewheeling possible. A more linear correlation between PWM and velocity 
   is an advantage of this mode. 
   Therefore it is possible to accelerate more precise. 
   Typically motors can be driven with slower velocities in this mode.
   Disadvantageous is a higher current consumption and a resulting higher
   heat-up of the driver.

 * Drive/Coast

   In this mode the motor is either driving or freewheeling.
   Advantageous is a lower current consumption and a resulting lesser heat-up.
   Therefore it might be possible that it the control of the velocity and 
   acceleration is less precise.
 

Interfaces and Coding
---------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^
See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <dc_brick_python_api>`", ":ref:`Examples <dc_brick_python_examples>`", "Installation"
   "Java", ":ref:`API <dc_brick_java_api>`", ":ref:`Examples <dc_brick_java_examples>`", "Installation"
   "C", ":ref:`API <dc_brick_c_api>`", ":ref:`Examples <dc_brick_c_examples>`", "Installation"
   "C++", ":ref:`API <dc_brick_cpp_api>`", ":ref:`Examples <dc_brick_cpp_examples>`", "Installation"


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

Motor is not running correctly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Reasons:** 
 * The reason for this is typically a voltage drop-in, caused by the connected
   motor. 
 * Another reason might be a low input voltage of the DC Brick.
 * Not correctly connected
 * Defective motor.

**Solutions:**
 * Check input voltage. If too low, change supply.
 * More powerful powersupply. Typically batteries are better suited than wall power adapters.
 * In case of you are using batteries to power the device, check the voltage of
   the batteries and keep in mind that this voltage can break-in while delivering
   high currents. 
 * Reduce the load of the motor.
 * Check connection of Brick and motor.
 * Change Motor when defect.
