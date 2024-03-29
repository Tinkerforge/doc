
:shoplink: ../../../shop/bricklets/servo-v2-bricklet.html

.. include:: Servo_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _servo_v2_bricklet:

Servo Bricklet 2.0
==================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_servo_v2_tilted_[100|600].jpg       Servo Bricklet 2.0
	Bricklets/bricklet_servo_v2_tilted2_[100|600].jpg      Servo Bricklet 2.0
	Bricklets/bricklet_servo_v2_top_[100|600].jpg          Servo Bricklet 2.0
	Bricklets/bricklet_servo_v2_w_servo_[100|600].jpg      Servo Bricklet 2.0 with two servos
	Bricklets/bricklet_servo_v2_caption_[100|600].jpg      Servo Bricklet 2.0 connectivity
	Bricklets/bricklet_servo_v2_brickv_[100|].jpg          Servo Bricklet 2.0 in Brick Viewer
	Dimensions/servo_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Controls up to **10** RC Servos
* Brushless motors with external ESC also controllable
* Adjustable Period and pulse width
* Uses motion planning to reach position with smooth motion
* Velocity and acceleration/deceleration can be configured
* Current measurement for each individual channel


.. _servo_v2_bricklet_description:

Description
-----------

The Servo :ref:`Bricklet <primer_bricklets>` is able to control up to **10**
`RC servos <https://en.wikipedia.org/wiki/Servo_(radio_control)>`__. With the 
provided API for many :ref:`programming languages <servo_brick_programming_interface>` 
you can control the position, velocity and acceleration/deceleration of the connected 
servos. Motion planning is used to reach a position with smooth motion.
The current-draw of each servo can be measured independently. 
Additionally output PWM (pulse width and period) is configurable for each servo.

The servos are powered by an external power supply (black connector). The voltage
from this connector is directly connected to the servos.

Technical Specifications
------------------------

===================================== ============================================================
Property                              Value
===================================== ============================================================
Current Consumption                   75mW (15mA at 5V)
Input Voltage                         5V-24V (is directly supplied to servo/fan)
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Output Period*                        1µs - 65535µs
Pulse Width*                          1µs - 65535µs
Velocity*                             0 - 500000 °/100s
Acceleration*                         0 - 500000 °/100s²
Deceleration*                         0 - 500000 °/100s²
------------------------------------- ------------------------------------------------------------
------------------------------------- ------------------------------------------------------------
Dimensions (W x D x H)                40 x 40 x 10mm (1.57 x 1.57 x 0.39")
Weight                                9g
===================================== ============================================================

\* configurable per servo channel

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/servo-v2-bricklet/raw/master/hardware/servo-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/servo_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/servo-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://a360.co/3yLdt4j>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/servo_v2/servo-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/servo_v2/servo-v2.FCStd>`__)


.. _servo_v2_bricklet_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the
Servo Bricklet 2.0.

.. image:: /Images/Bricklets/bricklet_servo_v2_caption_600.jpg
   :scale: 100 %
   :alt: Servo Bricklet 2.0 with caption
   :align: center
   :target: ../../_images/Bricklets/bricklet_servo_v2_caption_800.jpg


.. _servo_v2_bricklet_test:

Test your Servo Bricklet 2.0
----------------------------

|test_intro|

Connect a RC servo to a port of the Brick and a suitable power supply.

|test_tab|


.. image:: /Images/Bricklets/bricklet_servo_v2_brickv.jpg
   :scale: 100 %
   :alt: Servo Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_servo_v2_brickv.jpg

In the left part of the tab you can select the servo
to control. You can enable and disable it, configure the
`PWM <https://en.wikipedia.org/wiki/Pulse-width_modulation>`__ pulse width and
define the degree range. Additionally you can see the current consumption of
the servo. Below there are four sliders to control
the position, velocity and acceleration of the servo. The fourth slider
can be used to change the period of the PWM
(see :ref:`Configure Servo PWM <servo_v2_bricklet_configure_servo_pwm>` for more
information).

On the right side you can see the input voltage.
Below are graphical representations for the state of each servo.

|test_pi_ref|


.. _servo_v2_bricklet_configure_servo_pwm:

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


Usage of ESCs to drive brushless motors
---------------------------------------

With this Brick you can control up to 10 brushless motors by using external
Electronic Speed Controllers (ESC). Simply connect the brushless
motor to the ESC and the ESC to the Servo Brick. With this construction
the maximum brushless motor current only depends on your selected ESC.

.. warning::
 Many ESCs have a build-in Battery Eliminator Circuits (BEC) which can be used
 to power RC receivers.
 If you use a ESC with BEC you have to disable it! Otherwise your ESC or
 the Brick can be destroyed. To disable BEC you have to remove the red
 wire from the connector you plug in the Servo Brick
 (`external video tutorial <https://www.youtube.com/watch?v=clNvfjhMQ5w>`__).

.. warning::
 If you use the same power supply for your ESC and the Servo Brick, additionally
 you have to remove the black (GND) wire too. If you don't remove it, the motor
 current can flow through the Servo Brick and can destroy the current measurement
 circuit.


Connect other Hardware
----------------------

Also other hardware like fan cooler with PWM input can be controlled.

You can use 12V fans or 24V fans and connect the 12V/24V to to the black
input voltage connector. The control PWM input of the fan must however
accept 0V low level und 5V high level. The majority of 12V/24V PWM
controllable fans work this way, but check the datasheet of of the fan
before you connect it.

Coming Soon: Image/Video + example configuration


.. _servo_v2_bricklet_case:

Case
----

TBD

..
	A `laser-cut case for the Servo Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-servo-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_servo_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Servo Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_servo_v2_case_1000.jpg

	.. include:: Servo_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/servo_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Servo Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/servo_v2_exploded.png

	|bricklet_case_hint|


.. _servo_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Servo_V2_hlpi.table



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
