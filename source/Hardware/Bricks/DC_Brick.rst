.. _dc_brick:

DC Brick
========

.. raw:: html

        {% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
        {{ tfdocstart() }}
        {{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
        {{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #1") }}
        {{ tfdocend() }}


Description
-----------

The DC :ref:`Brick <product_overview_bricks>` is equipped with a 32-bit ARM
microcontroller and is able to control one 
`DC brushed motor <http://en.wikipedia.org/wiki/Brushed_DC_electric_motor>`_
bi-directional with max **5A** and **28V**. The current consumption and
power supply voltages can be measured,
velocity and acceleration of the motor can be controlled.
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
Microcontroller                   ATSAM3S2B (128kB Flash, 32k RAM)
--------------------------------  ------------------------------------------------------------
Maximum Motor Current (Peak)      5A
Minimum/Maximum Input Voltage     6V/28V
Device Current Consumption        53mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
PWM Frequency                     Configurable, 1-20khz, default 15khz
Velocity                          -32767 to 32767, full reverse to full forward, 0=stop
Acceleration                      0 to 65535, velocity/s, increment for velocity per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    2
Dimensions (W x D x H)            40mm x 40mm x 17mm  (1.57" x 1.57" x 0.67")
Weight                            18g
================================  ============================================================

Resources
---------

* MC33926 Datasheet (`Download <https://github.com/Tinkerforge/dc-brick/raw/master/datasheets/MC33926.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/dc-brick/raw/master/hardware/dc-brick-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dc_brick_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/dc-brick/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__


.. _dc_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the 
DC Brick.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: Connectivity of DC Brick
   :align: center
   :target: ../../_images/Bricks/servo_brick_anschluesse.jpg



.. _dc_brick_test:

Test your DC Brick
------------------

To test your DC Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For an installation guide click :ref:`here <brickd_installation>` 
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes. 

Connect an DC brushed Motor to the Brick and a appropiate power supply
(see :ref:`here <dc_brick_connectivity>`). Your assembly should look
like below.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: DC Brick with connected Motor and Battery
   :align: center
   :target: ../../_images/Bricklets/io16_brickv.jpg

Now connect the Brick to the PC over USB, you should see a tab named
"DC Brick" in the Brick Viewer after you pressed "connect", select it.

.. image:: /Images/Bricks/dc_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the DC Brick
   :align: center
   :target: ../../_images/Bricks/dc_brickv.jpg

In this tab you can test your driver if you enable it.
You have three sliders to control
the velocity (forward and backward), the acceleration and the 
`PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`__ frequency which
is used by the driver to control the connected motor. On the right you see
the voltages of the two power sources and the current consumption.
Below you find a graphical representation of the velocity of your motor.
At the bottom you can configure the minimum motor voltage, which lets you get
undervoltage signals if the voltage is below.

Below the sliders you can test the "Full Brake" and change the driving modes
(see :ref:`here <dc_brick_drive_mode>` for more information).
To start testing enable the driver and play around with the controls.

After this test you can go on with writing your own application.
See :ref:`Interface and Coding <dc_brick_programming_interfaces>` section for 
the API of the DC Brick and examples in your programming language.

Motor Powersupply
-----------------

The connected motor can be powered through the onboard power-connector 
(black connector) 
or through a :ref:`Power-Supply Board <product_overview_powersupplies>` in a 
stack.
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

Error LED Sources
-----------------

The red LED is enabled if you are below the minimum voltage
(configurable) or the driver is in emergency shutdown state
caused by over temperature or over current. To get the Brick operational you have
to increase the voltage or in the latter case you have to let the driver 
cool down and reenabling or disabling the driver.

.. _dc_brick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <dc_brick_c_api>`", ":ref:`Examples <dc_brick_c_examples>`", "Installation"
   "C#", ":ref:`API <dc_brick_csharp_api>`", ":ref:`Examples <dc_brick_csharp_examples>`", "Installation"
   "Java", ":ref:`API <dc_brick_java_api>`", ":ref:`Examples <dc_brick_java_examples>`", "Installation"
   "Python", ":ref:`API <dc_brick_python_api>`", ":ref:`Examples <dc_brick_python_examples>`", "Installation"


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
