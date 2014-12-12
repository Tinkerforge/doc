
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#tutorials-and-faq">Tutorials and FAQ</a> / First Steps - Tutorial

.. _tutorial_first_steps:

First Steps - Tutorial
======================

The following tutorial will demonstrate how to use
:ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>`
with the :ref:`Programming Interface <programming_interface>`.

In the first part we use the :ref:`DC Brick <dc_brick>`
to drive a motor. After this we make the velocity of this motor
controllable by a rotary
`potentiometer <http://en.wikipedia.org/wiki/Potentiometer>`__ by attaching
a :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>`. At the end
we show how to stack Bricks together to reduce wiring and
communicate over wireless or cable based interfaces.


Use a single Brick
------------------

We choose the DC Brick as a representative throughout
this tutorial. It is however easily possible to transfer the concepts
shown to other Bricks. Click :ref:`here <primer_bricks>` for
an overview of all available Bricks.


Phase 1: Testing
^^^^^^^^^^^^^^^^

To test the DC Brick you need to have the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
(for installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`). The Brick Viewer has to be connected
to the Brick Daemon, click the "Connect" button in Brick Viewer to ensure this.

The Brick Daemon is a bridge between the Bricks/Bricklets and the programming
language specific API bindings. The Brick Viewer provides a graphical interface
for testing purposes.

After the installation you are ready to tinker! Take the DC Brick and
connect a motor and a battery as shown the picture below (you can of
course also use a power supply instead of the battery or e.g. a Servo Brick
and a servo instead of the DC Brick and a motor):

.. image:: /Images/Bricks/brick_dc_motor_setup_600.jpg
   :scale: 100 %
   :alt: DC Brick with connected motor
   :align: center
   :target: ../../_images/Bricks/brick_dc_motor_setup_1200.jpg

Now connect the Brick to the PC over USB, you should see a new tab named
"DC Brick" in the Brick Viewer after a moment. Select this tab.
Your Brick Viewer now looks as depicted below:

.. image:: /Images/Bricks/dc_brickv.jpg
   :scale: 100 %
   :alt: DC Brick tab in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/dc_brickv.jpg

You can see the voltage of the connected battery as "External Voltage"
and the current used by the motor as "Current Consumption" as well as
a representation of the current velocity on the right side.
Different sliders allow you to modify velocity and acceleration
of the motor as well as the
`PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`__ frequency
of the driver. After clicking "Enable" you are in control of the motor.


Phase 2: Write your own Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The DC Brick and motor are verified to work properly, there is now
nothing in the way to write a first program that controls the DC Brick.

You can choose one of the :ref:`available <api_bindings>` programming
languages, in this tutorial we use `Python <http://www.python.org>`__.

The necessary steps to get everything working are essentially
the same in all programming language. This tutorial together with the
examples in the API documentation of every product should
allow you to get any Brick working with any programming language.

In the following we assume that you now the basics of the programming
language you picked and that the necessary compilers/interpreters are
already installed.

Download the API bindings for your programming language from the Downloads
:ref:`page <downloads>` and install them. Installation instructions can
be found :ref:`here <api_bindings>` and in the ``readme.txt`` supplied with
the API bindings.

Create a folder for your DC Brick test project.
Download one of the examples for the DC Brick as a starting point
from :ref:`here <dc_brick_python_examples>` and place it in the folder.

In this tutorial we take a look at ``example_configuration.py``:

.. literalinclude:: /Software/Bricks/DC_Brick_Python_example_configuration.py
 :language: python
 :linenos:
 :tab-width: 4

**Line 12** creates an IP Connection object.

**Line 13** creates an object that allows to control the DC Brick.
It is necessary to pass the Unique Identifier (UID) of the Brick
(in this example defined in **Line 6**) and the IPConnection object.
Change the UID corresponding to your device! 

.. note::
 The easiest way to get the UID of your device is to use the Brick Viewer.
 If you connect a device to the PC, the Viewer will display the UID in
 the "Setup" tab.

In **Line 15** the IP Connection is connected. It is possible to run 
your program on another PC than the one which has the Brick Daemon 
running (e.g. you can write a program for your smart phone that
controls a Brick connected to your PC).

The **Lines 18-23** configure the DC Brick and let the motor run full
speed forward.

**Line 25** is used to prevent program termination until you
press enter.

Run this Python script and use it or other examples as a starting point
for your own project.

.. note::
 A full description of the API and further examples can be found in the
 description page of each product. In case of the
 DC Brick :ref:`here <dc_brick_programming_interface>`.


Add Bricklets to extend features
--------------------------------

You can add Bricklets to extend the features of Bricks.
Click :ref:`here <primer_bricklets>` for an overview of available
Bricklets.

To use a Bricklet, connect it to your Brick over the supplied cable
when the Brick is not powered.

We use a :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>` and the
:ref:`DC Brick <dc_brick>` from the previous part of this tutorial,
but it is easy to transfer the shown concepts to any Bricklet
connected to any Brick.


Phase 1: Testing
^^^^^^^^^^^^^^^^

Connect the Rotary Poti Bricklet to your DC Brick as depicted in the image
below.

.. image:: /Images/Tutorial/tutorial_1_600.jpg
   :scale: 100 %
   :alt: DC Brick with connected motor and Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Tutorial/tutorial_1_1200.jpg

If you now connect the DC Brick to the PC, not only a "DC Brick" tab but
also a "Rotary Poti Bricklet" tab will be shown in the Brick Viewer.
Select the "Rotary Poti Bricklet" tab and rotate the potentiometer.
You should see a corresponding movement in the viewer.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet tab in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg


Phase 2: Write your own Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To incorporate the Rotary Poti Bricklet in our small project
we change the program to allow controlling of the motor
velocity with the rotary poti. It now look as follows
(`Download <https://raw.githubusercontent.com/Tinkerforge/doc/master/en/source/Tutorials/Tutorial_Extending/tutorial_brick_bricklet_test.py>`__):

.. literalinclude:: tutorial_brick_bricklet_test.py
 :language: python
 :linenos:
 :tab-width: 4

**Lines 4-7** are the typical configurations, the UID has to be changed
according to the Bricks and Bricklets you use.

In **Lines 22-27** an IP Connection to the Brick Daemon is established and
the Brick and Bricklet device objects are created.

We configure the Rotary Poti Bricklet, such that it calls the function
``cb_position`` every time the position of the potentiometer changes.
**Line 29** configures this callback to be triggered with a period of
50ms if the position changes. If the position is unchanged there won't
be any callbacks. This is an efficient implementation, only the bare minimum
of USB bandwidth is used. The callback function is registered in **Line 30**.
``cb_position`` is defined in **Lines 16-19**, it sets a new velocity based on
the current position of the potentiometer.

In **Lines 32-33** we enable the motor and set a maximum acceleration. This
allows the motor to follow the potentiometer movements immediately.

In **Lines 35-37** we wait for user input to prevent program termination.
After this the motor is stopped before the program ends.


.. _tutorial_first_steps_build_stacks:

Build Stacks
------------

To reduce wiring and save space it is possible to stack Bricks.
You need a :ref:`Master Brick <master_brick>` at the bottom with a PC
connection to route the data between the PC and the Bricks in the stack.

The stacking is transparent, that means there is **no code change necessary**
between a version that uses Bricks separately connected over USB to a PC
or a version with an additional Master and stacked Bricks.

It is possible to use more than one Master Brick in a stack.
But only the Master Brick at the bottom of the stack acts as the master of
the stack. The other Master Bricks can however be used to connect more
Bricklets.

The master of a stack powers each device of the stack over its USB
connection with a maximum of 500mA. Every driver Brick in the stack can
to be powered by its own on-board power-connector. To again reduce wiring and
save space it is possible to use a
:ref:`Power Supply <primer_power_supplies>`, which
is attached at the bottom of the stack (below the Master Brick).
These boards power the stacks internal power signal.
That means, that each driver Brick which is not powered by its on-board
power-connector is powered through the stack by the Power Supply.

Additionally the Power Supply creates a 5V signal to power the devices of
the stack. No power is drawn from the PC if a Power Supply
is used. This is especially useful if a small embedded device is
utilized to control the Bricks and Bricklets, since it might not be able
to deliver the needed power.

The master of the stack can measure the voltage and the current flow
of the connected power supply.

.. note::
 Each driver Brick switches automatically to the stack internal
 power signal if no external supply is attached over the on-board
 power-connector. Keep this in mind!

In the following we extend the previous part by attaching a Master Brick
below the DC Brick with the connected Rotary Poti Bricklet.

.. note::
 The white corners show how to plug the Bricks together.


Phase 1: Testing
^^^^^^^^^^^^^^^^

Build a stack consisting of a Step-Down Power Supply with connected battery,
a Master Brick with connected Rotary Poti Bricklet and a DC Brick with
connected motor (from bottom to top).

This setup is depicted in the image below.

.. image:: /Images/Tutorial/tutorial_2_600.jpg
   :scale: 100 %
   :alt: DC Brick in stack with Master Brick and Step-Down Power Supply with connected motor and Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Tutorial/tutorial_2_1200.jpg

If you connect the Master Brick to the PC over USB,
the Brick Viewer should show the Master Brick (measuring current and voltage
flowing through the stack), the DC Brick and the Rotary Poti Bricklet.


Phase 2: Write your own Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the stacking is transparent you are able to run
the program of the previous part without any changes!


Crosslink Stacks
----------------

The stacks as shown so far in the tutorial are not super exciting,
they only reduce wiring and save space. But, as you might have already
guessed, there is more to it. It is possible to attach **Master Extensions** to
the stack, which extend the stack with interfaces other than USB,
e.g. :ref:`RS485 <rs485_extension>` or :ref:`WIFI <wifi_extension>`, and 
:ref:`Ethernet <ethernet_extension>`.

To create a RS485 bus between two stacks, you need two need one Master Brick and
two RS485 Master Extensions additionally to the
previous part. Attach one RS485 Extension on top of your stack and build a new
stack from the other RS485 Extension and the Master Brick. Wire up the two
Extension. Finally, connect the Rotary Poti Bricklet to this new stack.

Now connect each stack separately to your PC and configure it with
the Brick Viewer as described in the
:ref:`RS485 documentation <rs485_configuration>`.
It is necessary that you power up the slave stacks prior to the master stack.

You should see two Master Bricks, the Rotary
Poti Bricklet and the DC Brick in the Brick Viewer. If this is the case
you can run your previously written code without any change.
