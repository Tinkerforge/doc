
:shoplink: ../../../shop/bricks/stepper-brick.html

.. include:: Stepper_Brick.substitutions


.. _stepper_brick:

Stepper Brick
=============

.. raw:: html

	{% tfgallery %}

	Bricks/brick_stepper_tilted_front_[?|?].jpg        Stepper Brick
	Bricks/brick_stepper_tilted_back_[?|?].jpg         Stepper Brick
	Bricks/brick_stepper_motor_setup_[?|?].jpg         Stepper Brick with motor
	Bricks/brick_stepper_caption_[?|?].jpg             Stepper Brick with caption
	Bricks/brick_stepper_top_[?|?].jpg                 Stepper Brick top
	Bricks/brick_stepper_bottom_[?|?].jpg              Stepper Brick bottom
	Dimensions/stepper_brick_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Drives one bipolar stepper motor over USB (max. **38V**, **2.5A** per phase)
* API for many programming languages available
* Position, velocity and acceleration controllable
* Full, half, quarter and eighth step modes
* Configurable decay mode
* Extendable via two Bricklets ports


.. _stepper_brick_description:

Description
-----------

With the Stepper :ref:`Brick <primer_bricks>` one bipolar
`stepper motor <https://en.wikipedia.org/wiki/Stepper_motor>`__
with a maximum current of **2.5A** and a maximum voltage of **38V** per phase
can be controlled over **USB**.  With the provided API for many 
:ref:`programming languages <stepper_brick_programming_interface>` you can 
control the direction, velocity and acceleration of the connected motor.

The maximum driving current and the 
:ref:`decay mode <stepper_brick_decay_mode>` can also be controlled.
The current consumption and power supply voltage can be measured by the API.

Two :ref:`Bricklet <primer_bricklets>` ports can be used to extend the 
features of this Brick. It can also be used together with other Bricks in a
:ref:`stack <primer_stack>`. For example an additional 
:ref:`Master Brick <master_brick>` with
:ref:`Master Extension <primer_master_extensions>` allows
to replace the USB connection by other cable based 
(:ref:`RS485 <rs485_extension>`, :ref:`Ethernet <ethernet_extension>`) 
or wireless (:ref:`WIFI <wifi_extension>`) connections.

The stepper motor can be powered by an external power supply connected
directly to the Brick (black connector) or by the stack internal power supply.
If an external power supply is connected the Brick automatically switches to 
this power supply.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Maximum Motor Current per Phase   2.5A
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
Current Consumption               60mA
================================  ============================================================


Resources
---------

* DRV8811 datasheet (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/datasheets/drv8811.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/stepper-brick/raw/master/hardware/stepper-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/stepper_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/stepper-brick/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2BCk72r>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/stepper/stepper.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/stepper/stepper.FCStd>`__)


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

|test_intro|

Connect a stepper motor to the Brick and a suitable power supply
(see :ref:`here <stepper_brick_connectivity>`). Your setup should look
like below.

.. image:: /Images/Bricks/brick_stepper_motor_setup_600.jpg
   :scale: 100 %
   :alt: Stepper Brick with motor
   :align: center
   :target: ../../_images/Bricks/brick_stepper_motor_setup_1200.jpg

|test_tab|

.. image:: /Images/Bricks/stepper_brickv.jpg
   :scale: 100 %
   :alt: Stepper Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/stepper_brickv.jpg

..
  FIXME: update image, to remove decay slider also put the warning about
         sync rect from the api docs here

In the left part of the GUI you can enable the driver and control
the velocity, acceleration and deceleration of the stepper. Below
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

|test_pi_ref|


Power Supply
------------

The connected stepper can be powered through the black on-board power-connector
or through a :ref:`Power Supply <primer_power_supplies>` in a
stack. The Brick switches automatically to the on-board power-connector when
a voltage is measured there.


.. _stepper_brick_decay_mode:

Decay Modes
-----------

For a good explanation of the different decay modes see
`this <https://ebldc.com/?p=86/>`__ blog post by Avayan.

A good decay mode is unfortunately different for every motor. The best
way to work out a good decay mode for your stepper motor, if you can't
measure the current with an oscilloscope, is to listen at the sound of
the motor. If the value is too low, you often hear a high pitched
sound and if it is too high you can often hear a humming sound.

Generally, fast decay mode (small value) will be noisier but also
allow higher motor speeds.


Error LED
---------

The red LED is enabled if the input voltage is below the user
configurable minimum voltage.


.. _stepper_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Stepper_Brick_hlpi.table


FAQ
---

Stepper makes funny noises
^^^^^^^^^^^^^^^^^^^^^^^^^^

Stepper motors can produce high pitch or humming noises, even if
they are standing still, if the decay mode is not configured correctly
for the connected motor.

Try to play around with the decay mode as described
:ref:`here <stepper_brick_decay_mode>`.
