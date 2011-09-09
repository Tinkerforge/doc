.. _tutorial:

Tutorial
========

The following tutorial will demonstrate how to use our products with the 
:ref:`High Level Programming Interface<pi_hlpi>`. See :ref:`<pi>` for
other possibilities. We will demonstrate our system with specific products
representative for all others.

Use a single Brick
------------------

We choose our :ref:`DC Brick <dc_brick>` for this tutorial part as representative
for all other :ref:`Bricks <product_overview_bricks>`.

Phase 1: Testing
^^^^^^^^^^^^^^^^

Firstly install the :ref:`brickd` and :ref:`brickv` on your PC as described 
:ref:`here <tools_installation_brickdv>`. The former is a bridge between the 
Bricks/Bricklets. The latter is a GUI only for testing purposes.

Now you are ready to play around. Take the DC Brick and 
connect a Motor and a battery as depicted in the picture below.

.. image:: /Images/Bricks/dc_brick_with_motor_battery.jpg
   :scale: 100 %
   :alt: DC Brick with connected motor and battery
   :align: center
   :target: ../../_images/Bricks/dc_brick_with_motor_battery.jpg


Start the Brick Viewer and connect your
DC Brick over the supplied USB cable with your PC. After pressing the "connect"
button in the viewer you should get a tab called "DC Brick". Select it.
Your Brick Viewer should now look like below.

.. image:: /Images/Bricks/dc_brickv.jpg
   :scale: 100 %
   :alt: DC Brick view in Brick Viewer
   :align: center
   :target: ../../_images/Bricks/dc_brickv.jpg

You can see the voltage of your connected battery and the current flow.
Different sliders allow you to modify velocity and acceleration
of the motor as well as the 
`PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`__ frequency 
of the driver. To play around you have to click "Enable", after this
you are in control. Have fun!

Phase 2: Write your own Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After this test let us write our own application. Since we support many
programming languages we choose `Python <http://www.python.org>`__
in this tutorial. The necessary steps to get everything working are essentially
the same. This tutorial together with the examples in the 
"Programming Interfaces" section of every product should allow you to get
everything working in other languages than Python (see a installation 
description for bindings :ref:`here <tools_installation_bindings>`).

We suggest that you have installed python already, when not
download it `here <http://python.org/download/>`__ and install it.

Create a folder for your DC Brick test project.
Download the Python bindings for the DC Brick from our
:ref:`Downloads page <downloads>`
and place them in the folder.

Download an example for the DC Brick as starting point 
`here <https://github.com/Tinkerforge/dc-brick/raw/master/software/bindings/python/example_configuration.py>`__.
Place it in your folder.

Have a look at *example_configuration.py*:

.. literalinclude:: /Software/Bricks/DC_Brick_Python_example_configuration.py
 :language: python
 :linenos:
 :tab-width: 4

**Line 12** creates an IP Connection to the Brick Deamon running on the host 
and port defined in **Lines 4-5**. This way enables you to run your program on 
another PC than the one which has the Brick Deamon running and the connected 
hardware (Bricks/Bricklets).

**Line 14** creates an object which lets you control your DC Brick. 
Therefore it is necessary to assign the Unique Identifier (UID) of your Brick
(In this example defined in **Line 6**). 

You have multiple options to get the UID of your device:

* Brickv: Brickv shows you all devices with corresponding UIDs
* Information of your Operating System: TODO
* The supplied UID packaged with the device when you bought ir (TODO correct?)

Change it corresponding to your device!

In **Line 15** the DC Brick object is attached to the IP Connection to your 
Brick Deamon. This way a program can control multiple devices on different 
hosts.

The **Lines 19-24** configures the DC Brick and let the motor running full 
speed forward.

**Line 26** is only used to prevent program termination until you
press any key.

Run this python script and use it or other examples as startingpoint
for your own project.

.. note::

   A full description of the API and further examples can you find in the
   product description pages. For example in case of the DC Brick 
   :ref:`here <dc_brick>`

Add Bricklets to extend features
--------------------------------

You can add Bricklets to extend the features of your Brick.
See :ref:`here <product_overview_bricklets>` for an overview over all Bricklets.

To use a Bricklet connect it to your Brick over the supplied cable
when the Brick is not powered.

.. warning::

   A wrong handling of Bricklets can destroy your hardware!

   If you replace a Bricklet without removing power of the Brick
   you can connect two hardware modules both active driving a signal.
   This can lead to a shortcut and destroyed hardware.


In this tutorial we use a
:ref:`Rotary Poti Bricklet <rotary_poti_bricklet>` and the
:ref:`DC Brick <dc_brick>` from the previous part of this tutorial as 
representative for all other Bricklets and Bricks.

Phase 1: Testing
^^^^^^^^^^^^^^^^

Connect the Rotary Poti Bricklet to your DC Brick as depicted in the image 
below.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: DC Brick with connected Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/current12_brickv.jpg

As in the former part of this tutorial connect the DC Brick to you PC
and notice the "DC Brick" and "Rotary Poti Bricklet" tabs in the Brick Viewer.
Lets select the "Rotary Poti Bricklet" tab and rotate the potentiometer.
You should see a corresponding movement in the viewer.

.. image:: /Images/Bricklets/rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Bricklets/rotary_poti_brickv.jpg


Phase 2: Write your own Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After these Tests lets take the previous created DC Brick test folder
and download the Python bindings for the Rotary Poti Bricklet 
`here <TBD TODO>`__ and place them in the folder.

Have a look at *tutorial_brick_bricklet_test.py*:

.. literalinclude:: tutorial_brick_bricklet_test.py
 :language: python
 :linenos:
 :tab-width: 4

Essentially the script is a mixture from different DC Brick and
Rotary Poti Bricklet examples.

**Lines 4-7** are the typical configuration and has to be adapted by
your used hardware.  

In **Lines 23-28** an IP Connection to the Brick Deamon is established
the Brick/Bricklet devices are created and added to the IP Connection.

We configure the Rotary Poti Bricklet, such that it calls a method 
**cb_position** everytime the position of the potentiometer changes.
**Line 31** configures this callback to be called with a period of
50ms if the position changes permanently. If the position is unchanged we will
get no callbacks. Therefore it is a very efficient implementation.
The callback method is registered in **Line 32**.
**cb_position** is defined in **Line 16-19**. 
It sets a new velocity based on the current position of the potentiometer.

In **Lines 35-36** we enable the motor and set a maximum acceleration such
that the motor will follow our potentiometer movements immediately.

In **Lines 36-38** we wait for user input to prevent programm termination.
After this we stop the motor and destroy the IP Connection.

Building Stacks
---------------

To reduce the wiring or saving USB hubs you can stack Bricks.
You need a :ref:`Master Brick <master_brick>` at the bottom with a PC 
connection to route the data between the PC and the Bricks of the Stack.

The stacking is transparent, that means there is no code change necessary
between a version which uses Bricks seperately connected over USB to a PC
or a version with an additional Master and stacked Bricks.


* 2x Bricks -> Master + 2x Bricks (Stack)

Cross-Link Stacks
-----------------

* 2x Stacks (USB) -> Chibi

