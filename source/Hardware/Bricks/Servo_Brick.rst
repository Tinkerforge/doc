.. _servo_brick:

Servo Brick
===========

.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

The Servo :ref:`Brick <product_overview_bricks>` is equipped with a 32-bit 
ARM microcontroller and is able to control up to **7**
`RC servos <http://en.wikipedia.org/wiki/Servo_Motor#RC_servos>`_
with a maximum current up to **3A**.
The output voltage is adjustable up to **9V**, the drawn current of each
servo can be measured independently.
Additionally output PWM is configurable for each servo independently.

It is compatible to other Tinkerforge 
:ref:`Bricks <product_overview_bricks>`
and can be used within a stack. 
Two :ref:`Bricklet <product_overview_bricklets>` ports 
can be used to extend the features of this device. 

The servos can be powered by an external powersupply connected
directly to the Brick or by the stack internal powersupply.
If an external powersupply is connected the Brick switches
automatically to this powersupply.

Controlling the device is possible in several ways. You can control it via 
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless 
(**Zigbee**, **WLAN**) connections via an additional Master Brick with according 
Master Extension (:ref:`High Level Concept <pi_hlpi>`). 

In the future it will be possible to control the device low level via a 
**I2C**, **SPI** or **UART (serial)** interface from other microcontroller 
boards (:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is opensource it is of course possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`). 
Currently we are not offering an on device API.


Technical Specifications
------------------------

===================================== ============================================================
Property                              Value
===================================== ============================================================
Maximum Motor Current (Sum)           3A
Minimum/Maximum Input Voltage         5V/25V
Output Voltage                        Software adustable 2.0 - 9.0V
Device Current Consumption            TBD
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Output Period\*                       2000µs - 65535µs
Pulsewidth\*                          1µs - 65535µs
Velocity\*                            0 - 65535 °/100s
Acceleration\*                        1 - 65535 °/100s²
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Bricklet Ports                        2
Dimensions (W x D x H)                40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                                TBD
===================================== ============================================================

\* configurable per servo

Resources
---------

 * Schematic (Download)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

Connectivity
------------

The following picture depicts the different connection possibilities of the 
Servo Brick.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/servo_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center

Servo Powersupply
-----------------

.. Todo: Bildchen

This device is equipped with an internal power-supply.
It offers the possibilty to adjust the output voltages for the connected servos.
The internal powersupply can be powered through the onboard power-connector
or through a :ref:`Power-Supply Board <product_overview_powersupplies>` in a stack.
The Brick switches autonomously to the onboard power-connector when there
is a voltage measured. Since we use a step-down switcher for the internal power-supply
please consider that the input voltage of the Brick has to be 1V higher 
than the configured output voltage to assure stable operation.


Test your Servo Brick
---------------------

A simple test consists of a RC servo and a accumulator connected to the Servo
Brick (check for correct polarities). 
The test configuration is depicted in the following picture.
Connect the brick with the USB cable to your PC.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

After installing our software (Brickd, Brickv) you can see the connected Servo
Brick in the Brickv.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Click on the Servo Brick tab and control the connected servo.
You can now go on with writing your own application.
See :ref:`Interface and Coding <servo_interface_coding>` section for the API of
the Servo Brick and examples in your programming language.


.. _servo_interface_coding:


Interfaces and Coding
---------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^
See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <servo_brick_python_api>`", ":ref:`Examples <servo_brick_python_examples>`", "Installation"
   "Java", ":ref:`API <servo_brick_java_api>`", ":ref:`Examples <servo_brick_java_examples>`", "Installation"
   "C", ":ref:`API <servo_brick_c_api>`", ":ref:`Examples <servo_brick_c_examples>`", "Installation"
   "C++", ":ref:`API <servo_brick_cpp_api>`", ":ref:`Examples <servo_brick_cpp_examples>`", "Installation"

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

Servos dither, not work correctly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Reasons:** 
 * The reason for this is typically a voltage drop-in, caused by repeated high
   current peaks produced by the connected servos. 
 * Another reason might be a low input voltage of the Servo Brick.
 * Not correctly connected
 * Defective Servos.

**Solutions:**
 * Check input voltage. If too low, change supply.
 * More powerful powersupply. Typically batteries are better suited than wall power adapters.
 * In case of you are using batteries to power the device, check the voltage of
   the batteries and keep in mind that this voltage can break-in while delivering
   high currents.
 * Connect less servos.
 * Reduction of load.
 * Check connection of Brick and servos.
 * Look for defective servos. Test them indepentenly until defect servo is
   found.
