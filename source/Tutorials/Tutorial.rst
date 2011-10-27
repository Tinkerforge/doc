.. _tutorial:

Tutorial
========

The following tutorial will demonstrate how to use 
:ref:`Bricks <product_overview_bricks>` and 
:ref:`Bricklets <product_overview_bricklets>` 
with the :ref:`High Level Programming Interface <pi_hlpi>`.

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
shown to other Bricks. Click :ref:`here <product_overview_bricks>` for 
an overview of all available Bricks.


Phase 1: Testing
^^^^^^^^^^^^^^^^

Before the DC Brick can be used, the :ref:`brickd` and the :ref:`brickv` 
have to be installed, installation instructions can be found 
:ref:`here <brickv_installation>` and :ref:`here <brickd_installation>`. 
The Brick Daemon is a bridge 
between the Bricks/Bricklets and the programming language API bindings. 
The Brick Viewer is a GUI for testing purposes.

After the installation you are ready to tinker! Take the DC Brick and 
connect a motor and a battery as shown the picture below (You can of
course also use a power supply instead of the battery or e.g. a Servo Brick
and a servo instead of the DC Brick and a motor):

.. image:: /Images/Bricks/brick_dc_motor_setup_600.jpg
   :scale: 100 %
   :alt: DC Brick with connected Motor 
   :align: center
   :target: ../_images/Bricks/brick_dc_motor_setup_1200.jpg

Start the Brick Viewer and connect the
DC Brick over a USB cable with your PC. After pressing the "connect"
button in the viewer you should get a tab called "DC Brick". Select it.
Your Brick Viewer now looks as depicted below:

.. image:: /Images/Bricks/dc_brickv.jpg
   :scale: 100 %
   :alt: DC Brick view in Brick Viewer
   :align: center
   :target: ../_images/Bricks/dc_brickv.jpg

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
languages, in this tutorial we use `Python <http://www.python.org>`__,
since it is easy to understand. 

The necessary steps to get everything working are essentially
the same in all programming language. This tutorial together with the 
examples in the "Programming Interfaces" section of every product should 
allow you to get any Brick working with any programming language.

In the following we assume that you now the basics of the programming
language you picked and that the necessary compilers/interpreters are
already installed.

Download the API bindings for your programming language from the Downloads 
:ref:`page <downloads>` and install them. Installation instructions can
be found :ref:`here <api_bindings>` and in the readme.txt supplied with
the API bindings.

Create a folder for your DC Brick test project.
Download one of the examples for the DC Brick as a starting point 
from :ref:`here <dc_brick_python_examples>` and place it in the folder.

In this tutorial we take a look at **example_configuration.py**:

.. literalinclude:: /Software/Bricks/DC_Brick_Python_example_configuration.py
 :language: python
 :linenos:
 :tab-width: 4

**Line 12** creates an IP Connection to the Brick Daemon running on the host 
defined in **Lines 4-5**. It is possible to run your program on 
another PC than the one which has the Brick Daemon running (e.g. you can
write a program on you phone that controls a Brick connected to your PC).

**Line 14** creates an object that allows to control the DC Brick. 
It is necessary to assign the Unique Identifier (UID) of the Brick
(in this example defined in **Line 6**). Change it corresponding to 
your device!

.. note::
   The easiest way to get the UID of your device is to use the Brick Viewer.
   If you connect a device to the PC, the Viewer will display the UID in 
   the "Setup" tab. 

In **Line 15** the DC Brick object is attached to the IP Connection.
This makes it possible to control multiple devices on different 
hosts from within one program.

The **Lines 19-24** configure the DC Brick and let the motor run full 
speed forward.

**Line 26** is used to prevent program termination until you
press enter.

Run this python script and use it or other examples as a starting point
for your own project.

.. note::

   A full description of the API and further examples can be found in the
   description page of the product. In case of the DC Brick 
   :ref:`here <dc_brick_programming_interfaces>`.

Add Bricklets to extend features
--------------------------------

You can add Bricklets to extend the features of Bricks.
Click :ref:`here <product_overview_bricklets>` for an overview of available 
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
   :alt: DC Brick with connected Motor and Rotary Poti Bricklet
   :align: center
   :target: ../_images/Tutorial_1_1200.jpg

If you now connect the DC Brick to the PC, not only a "DC Brick" tab but
also a "Rotary Poti Bricklet" tab will be shown in the Brick Viewer.
Select the "Rotary Poti Bricklet" tab and rotate the potentiometer.
You should see a corresponding movement in the viewer.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Rotary Poti Bricklet
   :align: center
   :target: _images/Bricklets/bricklet_rotary_poti_brickv.jpg


Phase 2: Write your own Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To incorporate the Rotary Poti Bricklet in our small project 
we change the program to allow controlling of the motor
velocity with the rotary poti. It now look as follows (`Download <https://raw.github.com/Tinkerforge/doc/master/source/Tutorials/tutorial_brick_bricklet_test.py>`__):

.. literalinclude:: tutorial_brick_bricklet_test.py
 :language: python
 :linenos:
 :tab-width: 4

**Lines 4-7** are the typical configurations, the UID has to be changed
according to the Bricks/Bricklets you use.

In **Lines 23-28** an IP Connection to the Brick Daemon is established.
The Brick and Bricklet devices are created and added to the IP Connection.

We configure the Rotary Poti Bricklet, such that it calls the method 
**cb_position** every time the position of the potentiometer changes.
**Line 31** configures this callback to be called with a period of
50ms if the position changes. If the position is unchanged there won't
be any callbacks. This is an efficient implementation, only the bare minimum
of USB bandwidth is used.
The callback method is registered in **Line 32**.
**cb_position** is defined in **Line 16-19**, 
it sets a new velocity based on the current position of the potentiometer.

In **Lines 35-36** we enable the motor and set a maximum acceleration. This
allows the motor to follow the potentiometer movements immediately.

In **Lines 36-38** we wait for user input to prevent program termination.
After this the motor is stopped and the IP Connection destroyed.


.. _tutorial_build_stacks:

Build Stacks
---------------

To reduce wiring and save space it is possible to stack Bricks.
You need a :ref:`Master Brick <master_brick>` at the bottom with a PC 
connection to route the data between the PC and the Bricks in the Stack.

The stacking is transparent, that means there is **no code change necessary**
between a version that uses Bricks separately connected over USB to a PC
or a version with an additional Master and stacked Bricks.

It is possible to use more than one Master Brick in a Stack.
But only the Master Brick at the bottom of the Stack acts as the master of
the Stack. The other Master Bricks can however be used to connect more 
Bricklets.

The master of a Stack powers each device of the Stack over its USB 
connection with a maximum of 500mA. Every driver Brick in the Stack needs 
to be powered by its own onboard power-connector. To again reduce wiring and
save space it is possible to use a 
:ref:`Power-Supply Board <product_overview_powersupplies>`, which
is attached at the bottom of the Stack (below the master).
These boards power the Stacks internal power signal.
That means, that each driver Brick which is not powered by its onboard
power-connector is powered through the Stack by the Power-Supply Board.

Additionally the Power-Supply Board creates a 5V signal to power the devices of 
the Stack. No power is drawn from the PC if a Power-Supply
Board is used. This is especially useful if a small embedded device is
utilized to control the Bricks and Bricklets, since it might not be able
to deliver the needed power.

The master of the Stack can measure the voltage and the current flow
of the power supply connected to the Power-Supply Board.

.. note::

   Each driver Brick switches automatically to the Stack internal
   power signal if no external supply is attached over the onboard 
   power-connector. Keep this in mind!

In the following we extend the previous part by attaching a Master Brick
below the DC Brick with the connected rotary poti.

.. note::

   The white corners show how to plug the Bricks together.

Phase 1: Testing
^^^^^^^^^^^^^^^^

Build a Stack consisting of a Power-Supply with connected batterie, 
a Master Brick with connected Rotary Poti Bricklet and a DC Brick with
connected motor (from bottom to top).

This setup is depicted in the image below.

.. image:: /Images/Tutorial/tutorial_2_600.jpg
   :scale: 100 %
   :alt: DC Brick in Stack with Master and Power Supply with connected Motor and Rotary Poti Bricklet
   :align: center
   :target: ../_images/Tutorial_2_1200.jpg

If you connect the Master Brick to the PC over USB, 
the Brick Viewer should show the Master Brick (measuring current and voltage
flowing through the Stack), the DC Brick and the Rotary Poti Bricklet.

Phase 2: Write your own Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the stacking is transparent you are able to run
the program of the previous part without any changes!


Cross-Link Stacks
-----------------

The stacks as shown so far in the tutorial are not super exciting,
they only reduce wiring and save space. But, as you might have already 
guessed, there is more to it. It is possible to attach **Extensions** to the
Stack, which extend the Stack with interfaces other than USB 
(e.g. ZigBee, RS485, Ethernet).

This means we will be able to control the velocity of the Motor with 
the Rotary Poti wirelessly without changing the code from part two of
the tutorial!

.. 2x Stacks (USB) -> Chibi

.. note::

   This part of the tutorial is currently missing. It will show how
   to connect two stacks with Chibi (ZigBee) to allow wireless control
   of the DC Brick with the Rotary Poti Bricklet without any code
   modifications!


.. image:: /Images/Tutorial/tutorial_4_600.jpg
   :scale: 100 %
   :alt: DC Brick with connected Motor in Stack with Master, Chibi Extension and Power Supply as well as Stack with Master, Chibi Extension and Rotary Poti Bricklet
   :align: center
   :target: ../_images/Tutorial_4_1200.jpg
