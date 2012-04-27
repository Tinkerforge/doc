.. _dc_brick:

DC Brick
========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricks/brick_dc_tilted_front_350.jpg", 
	             "Bricks/brick_dc_tilted_front_600.jpg", 
	             "DC Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_dc_tilted_back_100.jpg", 
	             "Bricks/brick_dc_tilted_back_600.jpg", 
	             "DC Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_dc_motor_setup_100.jpg", 
	             "Bricks/brick_dc_motor_setup_600.jpg", 
	             "DC Brick with Motor") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_dc_caption_100.jpg", 
	             "Bricks/brick_dc_caption_600.jpg", 
	             "DC Brick with caption") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_dc_top_100.jpg", 
	             "Bricks/brick_dc_top_600.jpg", 
	             "DC Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_dc_bottom_100.jpg", 
	             "Bricks/brick_dc_bottom_600.jpg", 
	             "DC Brick") 
	}}
	{{ 
	    tfdocimg("Dimensions/dc_brick_dimensions_100.png", 
	             "Dimensions/dc_brick_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}

Features
--------

 * Drives one brushed DC motor with max 28V and 5A
 * Direction, velocity and acceleration controllable
 * Over-temperature and over-current events
 * Drive/Brake and Drive/Coast mode configurable
 * One USB port and two Bricklet ports


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

The DC motor can be powered by an external power supply connected
directly to the Brick or by the stack internal powe rsupply.
If an external power supply is connected the Brick switches
automatically to this power supply.

Controlling the device is possible in several ways. You can control it via 
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless 
(**Zigbee**, **WLAN**) connections via an additional Master Brick with 
corresponding Master-Extension (:ref:`High Level Concept <pi_hlpi>`). 

In the future it will be possible to control the device low level via a 
**I2C**, **SPI** or **UART (serial)** interface from other microcontroller 
boards (:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is opensource it is possible to program the device
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
* Schematic (`Download <https://github.com/Tinkerforge/dc-brick/raw/master/hardware/dc-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dc_brick_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/dc-brick/zipball/master>`__)

.. _dc_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the 
DC Brick.

.. image:: /Images/Bricks/brick_dc_caption_600.jpg
   :scale: 100 %
   :alt: DC Brick with caption
   :align: center
   :target: ../../_images/Bricks/brick_dc_caption_800.jpg

.. _dc_brick_test:

Test your DC Brick
------------------

To test the DC Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>` 
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes. 

Connect a DC brushed Motor to the Brick and a suitable power supply. 
Your setup should look as shown below.

.. image:: /Images/Bricks/brick_dc_motor_setup_600.jpg
   :scale: 100 %
   :alt: DC Brick with connected Motor 
   :align: center
   :target: ../../_images/Bricks/brick_dc_motor_setup_1200.jpg

Now connect the Brick to the PC over USB, you should see a tab named
"DC Brick" in the Brick Viewer after you pressed "connect". Select it.

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
Below you find a graphical representation of the velocity of the motor.
At the bottom you can configure the minimum motor voltage, which allows for
undervoltage signals if the voltage is too low.

Below the sliders you can test the "Full Brake" and change the driving modes
(see :ref:`here <dc_brick_drive_mode>` for more information).
To start testing enable the driver and play around with the controls.

After this test you can go on with writing your own application.
See the :ref:`Programming Interface <dc_brick_programming_interfaces>` section for 
the API of the DC Brick and examples in different programming languages.

Motor Power Supply
------------------

The connected motor can be powered through the onboard power-connector 
(black connector) 
or through a :ref:`Power Supply Board <product_overview_powersupplies>` in a 
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
   Disadvantageous is a higher current consumption and a resulting faster
   heat-up of the driver.

 * Drive/Coast

   In this mode the motor is either driving or freewheeling.
   Advantageous is a lower current consumption and a resulting slower heat-up.
   The control of the velocity and acceleration is less precise, it can
   "lag behind".

Error LED Sources
-----------------

The red LED is enabled if the voltage is below the minimum voltage
(configurable) or the driver is in emergency shutdown state
caused by over temperature or over current. To get the Brick operational 
again you have to increase the voltage or in the latter case you have to 
let the driver cool down and enable it again.

.. _dc_brick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <dc_brick_c_api>`", ":ref:`Examples <dc_brick_c_examples>`", ":ref:`Installation <api_bindings_c>`"
   "C#", ":ref:`API <dc_brick_csharp_api>`", ":ref:`Examples <dc_brick_csharp_examples>`", ":ref:`Installation <api_bindings_csharp>`"
   "Java", ":ref:`API <dc_brick_java_api>`", ":ref:`Examples <dc_brick_java_examples>`", ":ref:`Installation <api_bindings_java>`"
   "Python", ":ref:`API <dc_brick_python_api>`", ":ref:`Examples <dc_brick_python_examples>`", ":ref:`Installation <api_bindings_python>`"


Low Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note::  Coming soon! 

  A special firmware to control the DC Brick over 
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

..
	FAQ
	---

	Motor is not running correctly
	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	**Reasons:** 
	 * Voltage drop, caused by the connected motor. 
	 * Low input voltage for the DC Brick.
	 * Not correctly connected.
	 * Defective motor.

	**Solutions:**
	 * Check input voltage. If too low, increase voltage.
	 * More powerful power supply. Typically batteries are better suited than wall power adapters.
	 * In case of you are using batteries to power the device, check the voltage of
	   the batteries and keep in mind that this voltage can break-in while delivering
	   high currents. 
	 * Reduce the load of the motor.
	 * Check connection between Brick and motor.
	 * Change Motor when defect.
