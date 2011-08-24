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

The Servo :ref:`Brick <concepts_bricks>` is a microcontroller board 
that is able to control 
`RC servo <http://en.wikipedia.org/wiki/Servo_Motor#RC_servos>`_
motors. It is compatible to other Tinkerforge 
:ref:`Bricks <concepts_bricks>`
and can be used within a :ref:`Stack <concepts_stack>`. 
Two :ref:`Bricklet <concepts_bricklets>` ports 
can be used to extend the features of this device by 
interfacing up to two Bricklets. The Brick can drive up to **7 Servos** with 
a maximum current up to **3A**. The current consumption of each Servo 
can be measured independently. The output voltage is software definable up to
**9V**, therefore high voltage servos are also supported.
PWMs maximum and minimum is user defineable.


Controlling the device is possible in several ways. You can control it via 
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless 
(**Zigbee**, **WLAN**) connections via a Master Brick with according 
Master-Extension (:ref:`High Level Concept <_concepts_hlpi>`). 
Also it is possible to control the device low level via a **I2C**, **SPI** or
**UART (serial)** interface from other microcontroller boards
(:ref:`Low Level Concept <concepts_llpi>`). A direct interface for
Arduinos is provided by our :doc:`Tinkershield </Hardware/Tinkershield>`.
Since the firmware is opensource it is of course possible to program the device
directly (:ref:`On Device Programming <concepts_odpi>`).

Technical Specifications
------------------------

===================================== ============================================================
Property                              Value
===================================== ============================================================
Maximum Motor Current (Sum)           3A
Minimum/Maximum Input Voltage         5V/28V
Output Voltage                        2.0 - 9.0V (software adjustable)
Device Current Consumption            TBD
Configurable Output Period per Servo  2000µs - 65535µs
------------------------------------- ------------------------------------------------------------

------------------------------------- ------------------------------------------------------------
PWM Frequency                         TBD
Velocity Resolution                   TBD
Acceleration Resolution               TBD
.. Acceleration Resolution            :math:`\frac{1}{2^{16}}\;\frac{\text{Velocity}}{\text{s}^2}`
------------------------------------- ------------------------------------------------------------

------------------------------------- ------------------------------------------------------------
Dimensions (W x D x H)                40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                                TBD
===================================== ============================================================


Resources
---------

 * Schematic (Download)
 * Datasheet (Download)
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


Powersupply
^^^^^^^^^^^

.. Todo: Bildchen

The connected motor can be powered through the onboard power-connector
or through a :ref:`Power-Supply Board <concepts_powersupply>` in a Stack.
The Brick switches autonomously to the onboard power-connector when
a voltage is there measured.

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

:ref:`High Level Interfaces <concepts_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <servo_brick_python_api>`", ":ref:`Examples <servo_brick_python_examples>`", "Installation"
   "Java", ":ref:`API <servo_brick_java_api>`", ":ref:`Examples <servo_brick_java_examples>`", "Installation"
   "C", ":ref:`API <servo_brick_c_api>`", ":ref:`Examples <servo_brick_c_examples>`", "Installation"
   "C++", ":ref:`API <servo_brick_cpp_api>`", ":ref:`Examples <servo_brick_cpp_examples>`", "Installation"

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
