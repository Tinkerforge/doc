.. _stepper_brick:

Stepper Brick
=============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricks/brick_stepper_tilted_front_350.jpg",
	             "Bricks/brick_stepper_tilted_front_600.jpg",
	             "Stepper Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_tilted_back_100.jpg",
	             "Bricks/brick_stepper_tilted_back_600.jpg",
	             "Stepper Brick")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_motor_setup_100.jpg",
	             "Bricks/brick_stepper_motor_setup_600.jpg",
	             "Stepper Brick with motor")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_caption_100.jpg",
	             "Bricks/brick_stepper_caption_600.jpg",
	             "Stepper Brick with caption")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_top_100.jpg",
	             "Bricks/brick_stepper_top_600.jpg",
	             "Stepper Brick top")
	}}
	{{
	    tfdocimg("Bricks/brick_stepper_bottom_100.jpg",
	             "Bricks/brick_stepper_bottom_600.jpg",
	             "Stepper Brick bottom")
	}}
	{{
	    tfdocimg("Dimensions/stepper_brick_dimensions_100.png",
	             "Dimensions/stepper_brick_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Drives one bipolar stepper motor with max. **38V** and **2.5A** per phase
* Position, velocity and acceleration controllable
* Full, half, quarter and eighth step modes
* Configurable decay mode
* One USB port and two Bricklet ports


Description
-----------

The Stepper :ref:`Brick <product_overview_bricks>` is equipped with a 32-bit ARM
microcontroller and is able to control one bipolar
`stepper motor <http://en.wikipedia.org/wiki/Stepper_motor>`__
with a maximum current of **2.5A** and a maximum voltage of **38V** per phase.
The maximum driving current and the
:ref:`decay mode <stepper_brick_decay_mode>` as well as
steps, velocity and acceleration of the connected stepper motor can be
controlled. The current consumption and power supply voltage can be measured.

It is compatible to other Tinkerforge
:ref:`Bricks <product_overview_bricks>`
and can be used within a stack.
Two :ref:`Bricklet <product_overview_bricklets>` ports
can be used to extend the features of this device.

The stepper motor can be powered by an external power supply connected
directly to the Brick or by the stack internal power supply.
If an external power supply is connected the Brick switches
automatically to this power supply.

Controlling the device is possible in several ways. You can control it via
a PC connection. This connection can be established directly with a **USB**
cable or by other cable based (**RS485**, **Ethernet**) or wireless
(**WLAN**) connections via an additional Master Brick with
corresponding Master Extension (:ref:`High Level Concept <pi_hlpi>`).

Since the firmware is open source it is possible to program the device
directly (:ref:`On Device Programming <pi_odpi>`).
Currently we are not offering an On Device API.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Microcontroller                   ATSAM3S2B (128kB Flash, 32kB RAM)
Current Consumption               60mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximum Motor Current Per Phase   2.5A
Minimum/Maximum Input Voltage     8V/38V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Step Modes                        full, half, quarter, eighth steps
Decay Modes                       slow decay, fast decay or configurable mixed decay
Maximum Velocity                  0 to 65535, configurable as limit, in steps/s
Maximum Acceleration              0 to 65535, configurable as limit, in steps/s²
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    2
Dimensions (W x D x H)            40 x 40 x 17mm (1.57 x 1.57 x 0.67")
Weight                            20g
================================  ============================================================


Resources
---------

* DRV8811 Datasheet (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/datasheets/drv8811.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/hardware/stepper-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/stepper_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/stepper-brick/zipball/master>`__)


.. _stepper_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the
Stepper Brick.


.. image:: /Images/Bricks/brick_stepper_caption_600.jpg
   :scale: 100 %
   :alt: Stepper Brick with caption
   :align: center
   :target: ../../_images/Bricks/brick_stepper_caption_800.jpg


.. _stepper_brick_test:

Test your Stepper Brick
-----------------------

To test the Stepper Brick you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect a stepper motor to the Brick and a suitable power supply
(see :ref:`here <stepper_brick_connectivity>`). Your setup should look
like below.

.. image:: /Images/Bricks/brick_stepper_motor_setup_600.jpg
   :scale: 100 %
   :alt: Stepper Brick with motor
   :align: center
   :target: ../../_images/Bricks/brick_stepper_motor_setup_1200.jpg

Now connect the Brick to the PC over USB, you should see a tab named
"Stepper Brick" in the Brick Viewer after you pressed "Connect". Select it.

.. image:: /Images/Bricks/stepper_brickv.jpg
   :scale: 100 %
   :alt: Stepper Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/stepper_brickv.jpg

In the left part of the GUI you can enable the driver and control
the velocity, acceleration, deceleration and the decay mode
(see :ref:`stepper_brick_decay_mode`) of the stepper. Below
there are three buttons that control the direction of
the stepper and stop it. For example if you press "Forward",
the stepper will increase its speed to "Max Velocity" with the given
acceleration. If you press "Stop" it will decrease its speed to "0" with
the given deceleration.

Below you can set the stepping mode (full, half, quarter, eighth) stepping mode
and trigger a "Full Brake", which stops the motor immediately.

You can drive to a specific position (measured in steps)
by entering it at "Drive To" an press "Go". Also you can drive a
specific number of steps. By using these controls the motor will accelerate
until reaching the maximum velocity and decelerate before reaching the
specified position.

On the right side the current position and remaining steps are shown
as well as the stack and external voltages.
Below is a graphical representation of the velocity of the stepper.
Beneath you can configure the minimum input voltage, which allows for
undervoltage signals if the voltage is too low. In the bottom right the
motor current can be configured according to the connected motor.

To start testing set a motor current suitable for your stepper motor, enable
the driver and play around with the controls.

After this test you can go on with writing your own application.
See the :ref:`Programming Interface <stepper_brick_programming_interfaces>` section
for the API of the Stepper Brick and examples in different programming languages.


Power Supply
^^^^^^^^^^^^

The connected stepper can be powered through the on-board power-connector
or through a :ref:`Power Supply <product_overview_powersupplies>` in a
stack. The Brick switches autonomously to the on-board power-connector when
a voltage is measured there.


.. _stepper_brick_decay_mode:

Decay Modes
-----------

A good explanation of decay modes can be found
`here <http://robot.avayanex.com/?p=86/>`_.

A good decay mode is unfortunately different for every motor. The best
way to work out a good decay mode for your stepper motor, if you can't
measure the current with an oscilloscope, is to listen at the sound of
the motor. If the value is too low, you often hear a high pitched
sound and if it is too high you can often hear a humming sound.

Generally, fast decay mode (small value) will be noisier but also
allow higher motor speeds.


Error LED Sources
-----------------

The red LED is enabled if the input voltage is below the user
configurable minimum voltage.


.. _stepper_brick_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Stepper_Brick_hlpi.table


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

Stepper makes funny noises
^^^^^^^^^^^^^^^^^^^^^^^^^^

Stepper motors can produce high pitch or humming noises, even if
they are standing still, if the decay mode is not configured correctly
for the connected motor.

Try to play around with the decay mode as described
:ref:`here <stepper_brick_decay_mode>`.
