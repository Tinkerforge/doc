
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Silent Stepper Brick
:FIXME_shoplink: ../../../shop/bricks/silent-stepper-brick.html

.. include:: Silent_Stepper_Brick.substitutions


.. _silent_stepper_brick:

Silent Stepper Brick
====================

.. note::
 This Brick is currently work-in-progress!


Features
--------

* Drives one bipolar stepper motor over USB (max. **46V**, **1.6A** per phase)
* Noiseless operation of stepper motors
* Position, velocity and acceleration controllable
* Stepper resolution from full-step to 1/256-step
* Extendable via two Bricklets ports

.. _silent_stepper_brick_description:

Description
-----------

With the Silent Stepper :ref:`Brick <primer_bricks>` one bipolar
`stepper motor <https://en.wikipedia.org/wiki/Stepper_motor>`__
with a maximum current of **1.6A** and a maximum voltage of **46V** per phase
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
or wireless (:ref:`WIFI <wifi_v2_extension>`) connections.

The stepper motor can be powered by an external power supply connected
directly to the Brick (black connector) or by the stack internal power supply.
If an external power supply is connected the Brick automatically switches to 
this power supply.

It is possible to drive stepper motors completely noiseless.

TODO: Stealth, Coolstep, Spreadcycle, etc.?

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Maximum Motor Current per Phase   1.6A
Minimum/Maximum Input Voltage     8V/46V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Step Resolution                   1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128, 1/256
Maximum Velocity                  0 to 65535, configurable as limit, in steps/s
Maximum Acceleration              0 to 65535, configurable as limit, in steps/s²
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet Ports                    2
Dimensions (W x D x H)            40 x 40 x 17mm (1.57 x 1.57 x 0.67")
Weight                            TBDg
Current Consumption               TBDmA
================================  ============================================================


Resources
---------

* TCM2130 datasheet (`Download <https://github.com/Tinkerforge/silent-stepper-brick/raw/master/datasheets/TMC2130_datasheet.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/silent-stepper-brick/raw/master/hardware/silent-stepper-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/silent_stepper_brick_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/silent-stepper-brick/zipball/master>`__)

.. _silent_stepper_brick_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the
Stepper Brick.

TODO: Add silent stepper images

.. image:: /Images/Bricks/brick_stepper_caption_600.jpg
   :scale: 100 %
   :alt: Stepper Brick with caption
   :align: center
   :target: ../../_images/Bricks/brick_stepper_caption_800.jpg

.. _silent_stepper_brick_test:

Test your Silent Stepper Brick
------------------------------

|test_intro|

Connect a stepper motor to the Brick and a suitable power supply
(see :ref:`here <stepper_brick_connectivity>`). Your setup should look
like below.

TODO: Add Silent Stepper Brick image

.. image:: /Images/Bricks/brick_stepper_motor_setup_600.jpg
   :scale: 100 %
   :alt: Stepper Brick with motor
   :align: center
   :target: ../../_images/Bricks/brick_stepper_motor_setup_1200.jpg

|test_tab|

TODO: Add Silent Stepper Brick image

.. image:: /Images/Bricks/stepper_brickv.jpg
   :scale: 100 %
   :alt: Stepper Brick in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/stepper_brickv.jpg

In the left part of the GUI you can enable the driver and control
the velocity, acceleration and deceleration of the stepper. Below
there are three buttons that control the direction of
the stepper and stop it. For example if you press "Forward",
the stepper will increase its speed to "Max Velocity" with the given
acceleration. If you press "Stop" it will decrease its speed to "0" with
the given deceleration.

Below you can set the stepping modes (full- to 1/256-step)
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

At the very bottom all of the Basic, Stealth, Coolste, Spreadcycle and Misc
configurations can be set. The last tab shows the current status of the
driver.

|test_pi_ref|


Power Supply
------------

The connected stepper can be powered through the black on-board power-connector
or through a :ref:`Power Supply <primer_power_supplies>` in the
stack. The Brick switches automatically to the on-board power-connector when
a voltage is measured there.


Error LED
---------

The red LED is enabled if the input voltage is below the user
configurable minimum voltage.


Modes and Features
------------------

Stealth Mode
^^^^^^^^^^^^

TODO

Coolstep Mode
^^^^^^^^^^^^^

TODO

Classic Mode
^^^^^^^^^^^^

TODO

Spreadcycle
^^^^^^^^^^^

TODO

Stallguard
^^^^^^^^^^

TODO


Help! I don't understand half of the words
------------------------------------------

The TCM2130 is a powerful stepper motor driver. Unfortunately this comes with
lots of modes, features and configuration possibilites. In our experience,
you can leave all of the configurations but the Basic Configurations 
(first tab in Brick Viewer) as default. We did choose sane default values for
all of the configurations.

If you want to understand all of the features in detail and the description in
this documentation is not enough, you can take a look at the
`TCM2130 datasheet <https://github.com/Tinkerforge/silent-stepper-brick/raw/master/datasheets/TMC2130_datasheet.pdf>`__.

For convenience, we provide a table that shows which API function parameters
changes what TCM2130 register.

.. |nbsp| unicode:: 0xA0
   :trim:

============================== ==================================== ============================= ===============================================
Function                       Parameter                            Register Name @Address[bits]  Note
============================== ==================================== ============================= ===============================================
SetBasicConfiguration          Standstill Current                   ihold @0x10[4..0]             Value is converted to 0-31
|nbsp|                         Motor Run Current                    irun @0x10[12..8]             Value is converted to 0-31
|nbsp|                         Standstill Delay Time                iholddelay @0x10[19..16]      Value is converted to 2^18 clock cycles
|nbsp|                         Power Down Time                      tpowerdown @0x11              Value is converted to 2^18 clock cycles
|nbsp|                         Stealth Threshold                    tpwmthrs @0x13                Value is converted to time between two steps
|nbsp|                         Coolstep Threshold                   tcoolthrs @0x14               Value is converted to time between two steps
|nbsp|                         Classic Threshold                    thigh @0x15                   Value is converted to time between two steps
|nbsp|                         High Velocity Chopper Mode           vhighchm @0x6C[19]            |nbsp|
------------------------------ ------------------------------------ ----------------------------- -----------------------------------------------
------------------------------ ------------------------------------ ----------------------------- -----------------------------------------------
SetSpreadcycleConfiguration    Slow Decay Duration                  toff @0x6C[3..0]              |nbsp|
|nbsp|                         Enable Random Slow Decay             rndtf @0x6C[13]               |nbsp|
|nbsp|                         Fast Decay Duration                  fd3/hstrt @0x6C[11/6..4]      Used if chm=1, otherwise ignored
|nbsp|                         Hysteresis Start Value               hstrt @0x6C[6..4]             Used if chm=0, otherwise ignored
|nbsp|                         Hysteresis End Value                 hend @0x6C[10..7]             Used if chm=0, otherwise ignored
|nbsp|                         Sinewave Offset                      hend @0x6C[10..7]             Used if chm=1, otherwise ignored
|nbsp|                         Chopper Mode                         chm @0x6C[14]                 |nbsp|
|nbsp|                         Comperator Blank Time                tbl @0x6C[16..15]             |nbsp|
|nbsp|                         Fast Decay Without Comperator        disfdcc @0x6C[12]             |nbsp|
------------------------------ ------------------------------------ ----------------------------- -----------------------------------------------
------------------------------ ------------------------------------ ----------------------------- -----------------------------------------------
SetStealthConfiguration        Enable Stealth                       en_pwm_mode @0x00[2]          |nbsp|
|nbsp|                         Amplitude                            pwm_ampl @0x70[7..0]          |nbsp|
|nbsp|                         Gradient                             pwm_grad @0x70[15..8]         |nbsp|
|nbsp|                         Enable Autoscale                     pwm_autoscale @0x70[18]       |nbsp|
|nbsp|                         Force Symmetric                      pwm_symmetric @0x70[19]       |nbsp|
|nbsp|                         Freewheel Mode                       freewheel @0x70[21..20]       |nbsp|
------------------------------ ------------------------------------ ----------------------------- -----------------------------------------------
------------------------------ ------------------------------------ ----------------------------- -----------------------------------------------
SetCoolstepConfiguration       Minimum Stallguard Value             semin @0x6D[3..0]             |nbsp|
|nbsp|                         Maximum Stallguard Value             semax @0x6D[11..8]            |nbsp|
|nbsp|                         Current Up Step Width                seup @0x6D[7..4]              |nbsp|
|nbsp|                         Current Down Step Width              sedn @0x6D[14..13]            |nbsp|
|nbsp|                         Minimum Current                      seimin @0x6D[15]              |nbsp|
|nbsp|                         Stallguard Threshold Value           sgt @0x6D[22..16]             |nbsp|
|nbsp|                         Stallguard Mode                      sfilt 0x6D@[24]               |nbsp|
------------------------------ ------------------------------------ ----------------------------- -----------------------------------------------
------------------------------ ------------------------------------ ----------------------------- -----------------------------------------------
SetMiscConfiguration           Disable Short To Ground Protection   diss2g @0x6C[30]              |nbsp|
|nbsp|                         Synchronize Phase Frequency          sync @0x6C[23..20]            |nbsp|
============================== ==================================== ============================= ===============================================

.. _silent_stepper_brick_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Silent_Stepper_Brick_hlpi.table
