Tutorial
========

The following tutorial will demonstrate how to use our products with the 
:ref:`High Level Programming Interface<pi_hlpi>`. See :ref:`<pi>` for
other possibilities. We will demonstrate our system with specific products
representative for all others.

Use a single Brick
------------------

We choose our :ref:`DC Brick <dc_brick>` for this tutorial part as representation
for all other :ref:`Bricks <product_overview_bricks>`.

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
Different sliders allow you to modify the velocity and the acceleration
of the motor. To play around you have to click "Enable", after this
you are in control. Have fun!


After this test lets write our own application. Since we support many
programming languages we choose `Python <http://www.python.org>`__
in this tutorial. The necessary steps to get everything working are essentially
the same. This tutorial together with the examples in the 
"Programming Interfaces" section of every product should allow you to get
everything working in other languages than Python (see a installation 
description for bindings :ref:`here <tools_installation_bindings>`).

We suggest that you have installed python already, when not
download it `here <http://python.org/download/>`__ and install it.

Create a folder for your DC Brick test project.
Download the Python bindings for the DC Brick `here <TBD TODO>`__
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

Add Bricklets to extend features
--------------------------------

You can add Bricklets to extend the features of your Brick.
See :ref:`here <product_overview_bricklets>` for an overview over all Bricklets.

To use a Bricklet simply connect it to your Brick over the supplied cable.
Press the "Reset" button on the Brick to let it initialize the Bricklet
and make it useable. See the "Test your ... Bricklet" section in the 
documentation of your Bricklet for further instructions and tests.

If you like to replace a Bricklet by another, do the following:

1. Remove old Bricklet
2. Press "reset" at Brick:

   *After this the Brick's Bricklet port is configured default as input.*
3. Connect new Bricklet
4. Press "reset" at Brick again:

   *After this the Bricklet code is loaded and Brick's Bricklet port is 
   configured according to new connected Bricklet.*

.. warning::

   A wrong handling of Bricklets can destroy your hardware!

   If you replace a Bricklet without removing power of the Brick or bringing 
   the Brick's Bricklet port in an input state 
   (e.g. by removing the old Bricklet and afterwards resetting the Brick)
   you can connect two hardware modules both active driving a signal.
   This can lead to a shortcut and destroyed hardware.

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

