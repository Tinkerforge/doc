.. _stepper_brick:

Stepper Brick
=============

.. raw:: html

        {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
        {{ tfdocstart() }}
        {{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
        {{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #1") }}
        {{ tfdocend() }}


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

The stepper motor can be powered by an external powersupply connected
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
Microcontroller                   ATSAM3S2B (128kB Flash, 32k RAM)
--------------------------------  ------------------------------------------------------------
Maximum Current Per Winding       2.5A
Minimum/Maximum Input Voltage     8V/38V
Device Current Consumption        60mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Step Modes                        full, half, quarter, eighth steps
Decay Mode                        slow decay, fast decay or configureable mixed decay
Maximum Velocity                  0 to 65535, configurable as limit, in steps/s
Maximum Acceleration              0 to 65535, configurable as limit, in steps/s²
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    2
Dimensions (W x D x H)            40 x 40 x 17mm  (1.57 x 1.57 x 0.67")
Weight                            20g
================================  ============================================================


Resources
---------

* DRV8811 Datasheet (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/datasheets/drv8811.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/hardware/stepper-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/stepper_brick_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/stepper-brick/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



.. _stepper_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the 
Stepper Brick.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: Connectivity of the Stepper Brick
   :align: center
   :target: ../../_images/Bricks/servo_brick_anschluesse.jpg




.. _stepper_brick_test:

Test your Stepper Brick
-----------------------

To test your Stepper Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For an installation guide click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes. 

Connect a Stepper Motor to the Brick and a appropiate power supply
(see :ref:`here <stepper_brick_connectivity>`). Your assembly should look
like below.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Stepper Brick with connected Stepper and Battery
   :align: center
   :target: ../../_images/Bricklets/io16_brickv.jpg

Now connect the Brick to the PC over USB, you should see a tab named
"Stepper Brick" in the Brick Viewer after you pressed "connect", select it.

.. image:: /Images/Bricks/stepper_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Stepper Brick
   :align: center
   :target: ../../_images/Bricks/stepper_brickv.jpg

In the left part of the GUI you can enable the driver and control
the velocity, acceleration, deceleration and the decay mode
(see :ref:`stepper_brick_decay_mode`) of the stepper. Below
you have three buttons which let control you the direction of
the stepper and stop. For example if you press "Forward",
the stepper will increase its speed to "Max Velocity" with the given 
acceleration. If you press "Stop" it will decrease its speed to "0" with
the given deceleration.

Below you can set the stepping mode (full, half, quater, eigth) stepping mode
and trigger a "Full Brake" which lets the motor immediately stop.

If you like you can also drive to a specific position (measured in steps)
by entering it at "DrivingTo" an press "Go". Also you can drive a
specific number of steps. By using these controls the motor will accelerate
until reaching the maximum velocity and decelerating to reach the specified
position.

On the right side the current position and remaining steps are shown
as well as the stack and external voltages.
Below is a graphical representation of the velocity of the stepper.
Beneath you can configure the minimum input voltage, which lets you get
undervoltage signals if the voltage is below. The motor current can also be
adapted to the connected motor (be aware that a too high current can damage your 
motor).

To start testing enable the driver and play around with the controls.

After this test you can go on with writing your own application.
See :ref:`Interface and Coding <stepper_brick_programming_interfaces>` section for 
the API of the Stepper Brick and examples in your programming language.




Powersupply
^^^^^^^^^^^

The connected stepper can be powered through the onboard power-connector
or through a :ref:`Power-Supply Board <product_overview_powersupplies>` in a stack.
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


Error LED Sources
-----------------

The red LED is enabled so long as the input voltage is below the user 
configureable minimum voltage.


.. _stepper_brick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <stepper_brick_c_api>`", ":ref:`Examples <stepper_brick_c_examples>`", "Installation"
   "C#", ":ref:`API <stepper_brick_csharp_api>`", ":ref:`Examples <stepper_brick_csharp_examples>`", "Installation"
   "Java", ":ref:`API <stepper_brick_java_api>`", ":ref:`Examples <stepper_brick_java_examples>`", "Installation"
   "Python", ":ref:`API <stepper_brick_python_api>`", ":ref:`Examples <stepper_brick_python_examples>`", "Installation"



Low Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


On Device Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

