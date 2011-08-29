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

The Stepper :ref:`Brick <product_overview_bricks>` is equipped with a 32-bit ARM
microcontroller and is able to control one 
`Stepper motor <http://en.wikipedia.org/wiki/Stepper_motor>`_
with a maximum current of **2.5A** and a maximum voltage of **38V** per winding.
The maximum driving current and :ref:`decay mode <stepper_brick_decay_mode>` 
can be controlled by API.
Steps, velocity and acceleration of the connected stepper motor can be controlled,
the current consumption and power supply voltages can be measured. 

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
Maximum Current Per Winding       2.5A
Minimum/Maximum Input Voltage     8V/38V
Device Current Consumption        TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Step Modes                        full, half, quarter, eighth steps
Decay Mode                        slow decay, fast decay or configureable mixed decay
Maximum Velocity                  0 to 65535, configurable as limit, in steps/s
Maximum Acceleration              0 to 65535, configurable as limit, in steps/s²
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    4
Dimensions (W x D x H)            40 x 40 x 17mm  (1.57 x 1.57 x 0.67")
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
or through a :ref:`Power-Supply Board <product_overview_powersupply>` in a stack.
The Brick switches autonomously to the onboard power-connector when
a voltage is there measured.




.. _stepper_brick_decay_mode:

Decay Modes
-----------

A good explanation of decay modes can be found 
`here <http://robot.avayanex.com/?p=86/>`_.

A good decay mode is unfortunately different in for every motor. The best
way to work out a good decay mode for your stepper motor, if you can't
measure the current with an oscilloscope, is to listen at the sound of
the motor. If the value is too low, you often hear a high pitched 
sound and if it is too high you can often hear a humming sound.

Generally, fast decay mode (small value) will be noisier but also
allow higher motor speeds.


Interfaces and Coding
---------------------

High Level Interfaces
^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Interfaces <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "Python", ":ref:`API <stepper_brick_python_api>`", ":ref:`Examples <stepper_brick_python_examples>`", "Installation"
   "Java", ":ref:`API <stepper_brick_java_api>`", ":ref:`Examples <stepper_brick_java_examples>`", "Installation"
   "C", ":ref:`API <stepper_brick_c_api>`", ":ref:`Examples <stepper_brick_c_examples>`", "Installation"
   "C++", ":ref:`API <stepper_brick_cpp_api>`", ":ref:`Examples <stepper_brick_cpp_examples>`", "Installation"


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


Stepper Motor makes wired noises
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Reason:** 
 * The decay mode might be adjusted.

**Solutions:**
 * Adjust the decay mode as desribed :ref:`here <stepper_brick_decay_mode>`.

