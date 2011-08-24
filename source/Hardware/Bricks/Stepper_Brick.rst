.. _stepper_brick:

Stepper Brick
=============

.. raw:: html

	<img alt="Servo Brick 1" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
	<img alt="Servo Brick 2" src="../../_images/Bricks/Servo_Brick/servo_brick2.jpg" style="width: 303.0px; height: 233.0px;" /></a>
.. raw:: latex

	\includegraphics{Images/Bricks/Servo_Brick/servo_brick2.jpg}


Description
-----------

The Stepper :ref:`Brick <concepts_bricks>` is a microcontroller board 
that is able to control one 
`Stepper motor <http://en.wikipedia.org/wiki/Stepper_motor>`_. 
It is compatible to other Tinkerforge 
:ref:`Bricks <concepts_bricks>`
and can be used within a :ref:`Stack <concepts_stack>`. 
Two :ref:`Bricklet <concepts_bricklets>` ports 
can be used to extend the features of this device by 
interfacing up to two Bricklets. The Brick can drive the stepper motor with 
a maximum current up to **2.5A** per winding. 
The current consumption can be measured. 


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

================================  ============================================================
Property                          Value
================================  ============================================================
Maximum Winding Current           2.5A
Minimum/Maximum Input Voltage     8V/TBD
Device Current Consumption        TBD
--------------------------------  ------------------------------------------------------------

--------------------------------  ------------------------------------------------------------
PWM Frequency                     TBD
Velocity Resolution               TBD
Acceleration Resolution           TBD
.. Acceleration Resolution           :math:`\frac{1}{2^{16}}\;\frac{\text{Velocity}}{\text{s}^2}`
--------------------------------  ------------------------------------------------------------

--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            TBD
================================  ============================================================


Resources
---------

 * Schematic (Download)
 * DRV8811 Datasheet (`Download <http://www.ti.com/lit/gpn/drv8811>`_)
 * Kicad Project (Download)

   `Kicad Project Page <http://kicad.sourceforge.net/>`_

Connectivity
------------

The following picture depicts the different connection possibilities of the 
Stepper Brick.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Outline and Drilling Plan
-------------------------

.. image:: /Images/Dimensions/stepper_dimensions.png
   :width: 300pt
   :alt: alternate text
   :align: center


Powersupply
^^^^^^^^^^^

.. Todo: Bildchen

The connected stepper can be powered through the onboard power-connector
or through a :ref:`Power-Supply Board <concepts_powersupply>` in a Stack.
The Brick switches autonomously to the onboard power-connector when
a voltage is there measured.



Motor not running correctly
^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Reasons:** 
 * The reason for this is typically a voltage drop-in caused by the
   connected motor. 
 * Another reason might be a to low input voltage of the Stepper Brick.
 * Not correctly connected
 * Defective motor.

**Solution:**
 * Check input voltage.
 * More powerful powersupply. Typically batteries are better suited than wall power adapters.
 * In case of you are using batteries to power the device, check the voltage of
   the batteries and keep in mind that this voltage can break-in while delivering
   high currents. 
 * Reduce load of motor.
 * Fix motor connection
 * Change motor when defect.

Interfaces and Coding
---------------------

:ref:`High Level Interfaces <concepts_hlpi>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <stepper_brick_python_api>`", ":ref:`Examples <stepper_brick_python_examples>`", "Installation"
   "Java", ":ref:`API <stepper_brick_java_api>`", ":ref:`Examples <stepper_brick_java_examples>`", "Installation"
   "C", ":ref:`API <stepper_brick_c_api>`", ":ref:`Examples <stepper_brick_c_examples>`", "Installation"
   "C++", ":ref:`API <stepper_brick_cpp_api>`", ":ref:`Examples <stepper_brick_cpp_examples>`", "Installation"


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

Motor is not running correctly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Reason:** 
 * The reason for this is typically a voltage drop-in, caused by the connected
   motor. 
 * Another reason might be a low input voltage of the Stepper Brick.
 * Not correctly connected.
 * Defective Stepper.

**Solutions:**
 * Check input voltage. If too low, change supply.
 * More powerful powersupply. Typically batteries are better suited than wall power adapters.
 * In case of you are using batteries to power the device, check the voltage of
   the batteries and keep in mind that this voltage can break-in while delivering
   high currents. 
 * Reduce the load of the motor.
 * Check connection of Brick and stepper.
 * Defective Motor?
