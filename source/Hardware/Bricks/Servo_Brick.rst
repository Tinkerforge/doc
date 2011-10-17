.. _servo_brick:

Servo
=====

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Bricks/brick_servo_tilted_front_350.jpg", 
	             "Bricks/brick_servo_tilted_front_100.jpg", 
	             "Bricks/brick_servo_tilted_front_800.jpg", 
	             "Servo Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_servo_tilted_back_350.jpg", 
	             "Bricks/brick_servo_tilted_back_100.jpg", 
	             "Bricks/brick_servo_tilted_back_800.jpg", 
	             "Servo Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_servo_setup_350.jpg", 
	             "Bricks/brick_servo_setup_100.jpg", 
	             "Bricks/brick_servo_setup_1200.jpg", 
	             "Servo Brick with Servo") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_servo_setup_big_350.jpg", 
	             "Bricks/brick_servo_setup_big_100.jpg", 
	             "Bricks/brick_servo_setup_big_1200.jpg", 
	             "Servo Brick with Servos") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_servo_caption_350.jpg", 
	             "Bricks/brick_servo_caption_100.jpg", 
	             "Bricks/brick_servo_caption_800.jpg", 
	             "Servo Brick with caption") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_servo_top_350.jpg", 
	             "Bricks/brick_servo_top_100.jpg", 
	             "Bricks/brick_servo_top_800.jpg", 
	             "Servo Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_servo_bottom_350.jpg", 
	             "Bricks/brick_servo_bottom_100.jpg", 
	             "Bricks/brick_servo_bottom_800.jpg", 
	             "Servo Brick") 
	}}
	{{ 
	    tfdocimg("Dimensions/dc_brick_dimensions_350.png", 
	             "Dimensions/dc_brick_dimensions_100.png", 
	             "Dimensions/dc_brick_dimensions.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}



Description
-----------

The Servo :ref:`Brick <product_overview_bricks>` is equipped with a 32-bit 
ARM microcontroller and is able to control up to **7**
`RC servos <http://en.wikipedia.org/wiki/Servo_Motor#RC_servos>`_
with a maximum current of **3A**.
The output voltage is adjustable up to **9V**, the drawn current of each
servo can be measured independently.
Additionally output PWM is configurable for each servo independently.

It is compatible to other Tinkerforge 
:ref:`Bricks <product_overview_bricks>`
and can be used within a stack. 
Two :ref:`Bricklet <product_overview_bricklets>` ports 
can be used to extend the features of this device. 

The servos can be powered by an external power supply connected
directly to the Brick or by the stack internal power supply.
If an external power supply is connected the Brick switches
automatically to this power supply.

Controlling the device is possible in several ways. You can control it via 
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless 
(**Zigbee**, **WLAN**) connections via an additional Master Brick with corresponding 
Master Extension (:ref:`High Level Concept <pi_hlpi>`). 

In the future it will be possible to control the device low level via a 
**I2C**, **SPI** or **UART (serial)** interface from other microcontroller 
boards (:ref:`Low Level Concept <pi_llpi>`). 
Since the firmware is open source it is possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`). 
Currently we are not offering an on device API.


Technical Specifications
------------------------

===================================== ============================================================
Property                              Value
===================================== ============================================================
Microcontroller                       ATSAM3S2B (128kB Flash, 32k RAM)
------------------------------------- ------------------------------------------------------------
Maximum Motor Current (Sum)           3A
Minimum/Maximum Input Voltage         5V/25V
Output Voltage                        Software adustable 2V - 9V
Device Current Consumption            60mA
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
Weight                                18g
===================================== ============================================================

\* Configurable per servo

Resources
---------

* MCP3008 Datasheet (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/datasheets/MCP3008.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/hardware/servo-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/servo_brick_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/servo-brick/zipball/master>`__)




.. _servo_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the 
Servo Brick.

.. image:: /Images/Bricks/brick_servo_caption_600.jpg
   :scale: 100 %
   :alt: Servo Brick with caption
   :align: center
   :target: ../../_images/Bricks/brick_servo_caption_800.jpg


.. _servo_brick_test:

Test your Servo Brick
---------------------

To test the Servo Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes. 

Connect a RC Servo to a port of the Brick and a suitable power supply. 
Your setup should look as shown below.

.. image:: /Images/Bricks/brick_servo_setup_600.jpg
   :scale: 100 %
   :alt: Servo Brick with connected Servo
   :align: center
   :target: ../../_images/Bricks/brick_servo_setup_1200.jpg

Now connect the Brick to the PC over USB, you should see a tab named
"Servo Brick" in the Brick Viewer after you pressed "connect". Select it.

.. image:: /Images/Bricks/servo_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Servo Brick
   :align: center
   :target: ../../_images/Bricks/servo_brickv.jpg

In the left part of the GUI you can select the servo
to control. You can enable it, configure the 
`PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`__ and configure
the corresponding position. Additionally you can see the current consumption of
the servo. Below there are four sliders to control
the position, velocity and acceleration of the servo. The fourth slider
can be used to change the period of the PWM 
(see :ref:`Configure Servo PWM <servo_brick_configure_servo_pwm>` for more 
information).

On the right side you can see the external and stack voltage.
Below are graphical representations for the state of each servo.
Beneath you can configure the minimum input voltage, which allows for
undervoltage signals if the voltage is too low.
Also you can configure the output voltage 
(Caution: A too high output voltage may damage your servo!).
At the bottom right there is a "Start Test" button, which starts
a test sequence that performs random movements for each servo.

To start testing enable servo 0 and play around with the controls
or let the Brick Viewer perform a test.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <servo_brick_programming_interfaces>` section for 
the API of the Servo Brick and examples in different programming languages.

.. _servo_brick_configure_servo_pwm:

Configure Servo PWM
-------------------

Typically you control a RC servo by a PWM signal with a 
period of 20ms and an on-time of 1ms - 2ms depending on the position you want
to achieve. However, some servos do not work properly with these standard
settings. Therefore we provide a fully configurable PWM.

The default value for the period is 19.5ms. This period worked on all servos 
we could get our fingers on (20ms did not work with some of the cheaper 
chinese servos). If the datasheet of your servo does specify a preferred
period, use it. But it is likely that you don't have to change this value.

More interesting is the minimum and maximum pulse width. The default pulse
width is 1ms - 2ms. Most servos can however rotate further when 
minimum/maximum pulse width is decreased/increased. If your servo comes
with a datasheet we recommend to use the values described in there. If you
don't have a datasheet you can try to incrementally extend the pulse width
until the servo starts to rattle. Use the biggest pulse width that does not
produce rattling.

.. warning::

   A wrong PWM configuration for an extended period of time can damage 
   your servo.

   
Servo Power Supply
------------------

The Servo Brick is equipped with an internal power-supply.
It offers the possibility to adjust the output voltages for the connected 
servos.
The internal power supply can be powered through the onboard power-connector
(black connector) or through a 
:ref:`Power Supply Board <product_overview_powersupplies>` in a stack.
The Servo Brick switches autonomously to the onboard power-connector when 
there is a voltage measured. Since we use a step-down switcher for the 
internal power supply please consider that the input voltage of the Brick has
to be 1V higher than the configured output voltage to assure stable operation.

.. warning::

   A too high output voltage can damage your servo.

Error LED Sources
-----------------

The red LED is enabled so long as the input voltage is below the user 
configurable minimum voltage.


.. _servo_brick_programming_interfaces:


Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <servo_brick_c_api>`", ":ref:`Examples <servo_brick_c_examples>`", "Installation"
   "C#", ":ref:`API <servo_brick_csharp_api>`", ":ref:`Examples <servo_brick_csharp_examples>`", "Installation"
   "Java", ":ref:`API <servo_brick_java_api>`", ":ref:`Examples <servo_brick_java_examples>`", "Installation"
   "Python", ":ref:`API <servo_brick_python_api>`", ":ref:`Examples <servo_brick_python_examples>`", "Installation"


Low Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. note::  Coming soon! 

  A special firmware is planned to control the Servo Brick over 
  SPI, I2C and UART.
  
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

FAQ
---

My servos are shaking, help!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The reason for this is typically a voltage drop, caused by repeated high
current peaks produced by the connected servos. First you should check
the input voltage, it should be at least 1V higher then the configured
output voltage.

Typically this problem occurs when the power supply can't handle the
high current peaks. To test if your power supply is the problem, you can
try batteries. Batteries normally don't have problems with current peaks.

If you are using batteries and the problem is still occurring, check
the voltage of the batteries when the servos are in use. If your batteries
are too weak, the voltage is dropping (in this case use full batteries).

If your servos only start shaking when you reach the maximum/minimum angle,
you have configured a too high/low pulse width. In this case you have to 
reduce the pulse width, otherwise your servos might get damaged over time.
