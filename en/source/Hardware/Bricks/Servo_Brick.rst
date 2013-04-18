
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#bricks">Bricks</a> / Servo Brick
:shoplink: ../../../shop/bricks/servo-brick.html

.. include:: Servo_Brick.substitutions


.. _servo_brick:

Servo Brick
===========

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_servo_tilted_front_350.jpg",
	               "Bricks/brick_servo_tilted_front_600.jpg",
	               "Servo Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_tilted_back_100.jpg",
	             "Bricks/brick_servo_tilted_back_600.jpg",
	             "Servo Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_setup_100.jpg",
	             "Bricks/brick_servo_setup_600.jpg",
	             "Servo Brick with servo")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_setup_big_100.jpg",
	             "Bricks/brick_servo_setup_big_600.jpg",
	             "Servo Brick with servos")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_caption_100.jpg",
	             "Bricks/brick_servo_caption_600.jpg",
	             "Servo Brick with caption")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_top_100.jpg",
	             "Bricks/brick_servo_top_600.jpg",
	             "Servo Brick top")
	}}
	{{
	    tfdocimg("Bricks/brick_servo_bottom_100.jpg",
	             "Bricks/brick_servo_bottom_600.jpg",
	             "Servo Brick bottom")
	}}
	{{
	    tfdocimg("Dimensions/servo_brick_dimensions_100.png",
	             "Dimensions/servo_brick_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Drives up to **7** RC Servos with max. **3A**
* Drives brushless motors (requires external ESC)
* Supports `TurboPWM <http://wiki.openpilot.org/display/Doc/TurboPWM>`__
* Software adjustable servo voltage, period and pulse width
* Position, velocity and acceleration controllable
* One USB port and two Bricklet ports


Description
-----------

The Servo :ref:`Brick <product_overview_bricks>` is equipped with a 32-bit
ARM microcontroller and is able to control up to **7**
`RC servos <http://en.wikipedia.org/wiki/Servo_Motor#RC_servos>`__
with a maximum current of **3A**.
The output voltage is adjustable up to **9V**, the drawn current of each
servo can be measured independently.
Additionally output PWM is configurable for each servo independently.

Brushless motors can be driven by usage of external Electronic Speed
Controllers (ESC). The maximum motor current depends only on the ESC such
that motors with 150A and more are possible to control.

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
(**WIFI**) connections via an additional Master Brick with
corresponding Master Extension (:ref:`High Level Concept <pi_hlpi>`).

Since the firmware is open source it is possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`).
Currently we are not offering an On Device API.


Technical Specifications
------------------------

===================================== ============================================================
Property                              Value
===================================== ============================================================
Microcontroller                       ATSAM3S2B (128kB Flash, 32kB RAM)
Current Consumption                   60mA
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Maximum Motor Current (Sum)           3A
Minimum/Maximum Input Voltage         5V/25V
Output Voltage                        Software adjustable 2V - 9V
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Output Period*                        1µs - 65535µs
Pulse Width*                          1µs - 65535µs
Velocity*                             0 - 65535 °/100s
Acceleration*                         1 - 65535 °/100s²
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Bricklet Ports                        2
Dimensions (W x D x H)                40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                                18g
===================================== ============================================================

\* configurable per servo


Resources
---------

* MCP3008 datasheet (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/datasheets/MCP3008.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/servo-brick/raw/master/hardware/servo-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/servo_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/servo-brick/zipball/master>`__)


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

|test_intro|

Connect a RC servo to a port of the Brick and a suitable power supply.
Your setup should look as shown below.

.. image:: /Images/Bricks/brick_servo_setup_600.jpg
   :scale: 100 %
   :alt: Servo Brick with servo
   :align: center
   :target: ../../_images/Bricks/brick_servo_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricks/servo_brickv.jpg
   :scale: 100 %
   :alt: Servo Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/servo_brickv.jpg

In the left part of the tab you can select the servo
to control. You can enable and disable it, configure the
`PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`__ pulse width and
define the degree range. Additionally you can see the current consumption of
the servo. Below there are four sliders to control
the position, velocity and acceleration of the servo. The fourth slider
can be used to change the period of the PWM
(see :ref:`Configure Servo PWM <servo_brick_configure_servo_pwm>` for more
information).

On the right side you can see the external and stack voltage.
Below are graphical representations for the state of each servo.
Beneath you can configure the minimum input voltage, which allows for
undervoltage signals if the voltage is too low.
Also you can configure the output voltage.

..warning::
 A too high output voltage might damage your servo!

At the bottom right there is a "Start Test" button, which starts
a test sequence that performs random movements for each servo.

|test_pi_ref|


.. _servo_brick_configure_servo_pwm:

Configure Servo PWM
-------------------

Typically you control a RC servo by a PWM signal with a
period of 20ms and an on-time of 1ms to 2ms depending on the position you want
to achieve. However, some servos do not work properly with these standard
settings. Therefore we provide a fully configurable PWM.

The default value for the period is 19.5ms. This period worked on all servos
we could get our fingers on (20ms did not work with some of the cheaper
Chinese servos). If the datasheet of your servo does specify a preferred
period, use it. But it is likely that you don't have to change this value.

More interesting is the minimum and maximum pulse width. The default pulse
width is 1ms to 2ms. Most servos can however rotate further when
minimum/maximum pulse width is decreased/increased. If your servo comes
with a datasheet we recommend to use the values described in there. If you
don't have a datasheet you can try to incrementally extend the pulse width
until the servo starts to rattle. Use the biggest pulse width that does not
produce rattling.

.. warning::
 A wrong PWM configuration for an extended period of time can damage
 your servo.


Power Supply
------------

The Servo Brick is equipped with an internal power supply.
It offers the possibility to adjust the output voltages for the connected
servos.
The internal power supply can be powered through the black on-board power-connector
or through a :ref:`Power Supply <product_overview_power_supplies>` in a stack.
The Servo Brick switches automatically to the on-board power-connector when
there is a voltage measured. Since we use a step-down controller for the
internal power supply please consider that the input voltage of the Brick has
to be 1V higher than the configured output voltage to assure stable operation.

.. warning::
 A too high output voltage can damage your servo.


Usage of ESCs to drive brushless motors
---------------------------------------

With this Brick you can control up to 7 brushless motors by using external
Electronic Speed Controllers (ESC). Simply connect the brushless
motor to the ESC and the ESC to the Servo Brick. With this construction
the maximum brushless motor current only depends on your selected ESC.

.. warning::
 Many ESCs have a build-in Battery Eliminator Circuits (BEC) which can be used
 to power RC receivers.
 If you use a ESC with BEC you have to disable it! Otherwise your ESC or
 the Brick can be destroyed. To disable BEC you have to remove the red
 wire from the connector you plug in the Servo Brick
 (`external video tutorial <http://www.youtube.com/watch?v=clNvfjhMQ5w>`__).

.. warning::
 If you use the same power supply for your ESC and the Servo Brick, additionally
 you have to remove the black (GND) wire too. If you don't remove it, the motor
 current can flow through the Servo Brick and can destroy the current measurement
 circuit.


Error LED
---------

The red LED is enabled so long as the input voltage is below the user
configurable minimum voltage.


.. _servo_brick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Servo_Brick_hlpi.table


On Device Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
 Coming soon!

 An API and documentation for direct on device programming (comparable
 to Arduino) is planned.
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
