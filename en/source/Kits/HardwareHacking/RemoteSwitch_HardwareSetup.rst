
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Remote Switches Hardware Setup

.. _starter_kit_hardware_hacking_remote_switch_hardware_setup:

Remote Switch Hardware Setup
============================

This kit includes two remote control mains switches. So this example
describes how to hack the included remote control. There are many other 
remote control mains switches with similar or identical remote controls
on the market, so you can most likely use this description for these, too.

Most remote controls for remote control mains switches are equipped with an IC 
called HX2262. Basically it has six different inputs: Two to define if it is an 
ON or OFF switch command and four inputs to define what it switches (A, B, 
C or D). An input is activated if it is switched to GND. All inputs are 
interconnected in a matrix style order.

In this example we will use the :ref:`Industrial Quad Relay Bricklet 
<industrial_quad_relay_bricklet>` with its four
solid state relays to short the inputs ON, OFF, A and B to GND. This way
we will be able to switch two remote switches. If you want to also switch 
C and D, you can use an additional Industrial Quad Relay Bricklet.

The innards of the Remote Control
---------------------------------

If you open your remote control you will most likely see a circuit board like this:

.. image:: /Images/Kits/hardware_hacking_remote_open_350.jpg
   :scale: 100 %
   :alt: Remote control opened
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_open_1200.jpg

The big IC right of the red DIP switch is the HX2262. If you remove the casing
completely and take a look at the bottom side it should look like this:

.. image:: /Images/Kits/hardware_hacking_remote_bottom_350.jpg
   :scale: 100 %
   :alt: Remote control close lookup bottom side
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_bottom_1200.jpg


Solder wires to the IC
----------------------

Next we have to solder the wires to the HC2262 to connect to the inputs 
of the remote control. We will solder five wires to the HX2262 IC:
(:ref:`Small soldering tutorial <starter_kit_hardware_hacking_for_beginners_soldering>`)

========== ====== ==========
Pin Number Signal Wire Color
========== ====== ==========
6          A      blue
7          B      red
8          C      /
9          GND    black
10         D      /
11         /      /
12         ON     yellow
13         OFF    purple
========== ====== ==========

The following image depicts the position of the HX2262 and the pin
numbering:

.. image:: /Images/Kits/hardware_hacking_remote_bottom_labeled_350.jpg
   :scale: 100 %
   :alt: Remote control close lookup bottom side labeled
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_bottom_labeled_1200.jpg

After soldering it will look like this:

.. image:: /Images/Kits/hardware_hacking_remote_soldered_closeup_remote_350.jpg
   :scale: 100 %
   :alt: Remote control close lookup with soldered wires
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_closeup_remote_1200.jpg


.. _starter_kit_hardware_hacking_remote_switch_hardware_setup_relay_matrix:

Connect wires to the Industrial Quad Relay Bricklet
---------------------------------------------------

Next we will connect these wires (except black) to the Industrial Quad Relay 
Bricklet.
Each input of the HX2262 is connected to its own relay. Simply put it into one
of the two connectors of a relay.

====== ========== =====
Signal Wire Color Relay
====== ========== =====
A      blue       0
B      red        1
ON     yellow     2
OFF    purple     3
====== ========== =====

Now every Relay is connected to one wire, but each relay is missing the second 
wire. Since we want to switch to GND, the second connection has to be to GND. 
So we have to connect the black 
GND wire to all of them. We do this by connecting the black wire to one relay 
and the other relays will be connected to it by small wires we create of the 
second black wire. The next picture depicts the finished work.

.. image:: /Images/Kits/hardware_hacking_remote_soldered_closeup_iqr_top_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet connector closeup
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_closeup_iqr_top_1200.jpg

After that we are finished. The full hardware setup will look like this:

.. image:: /Images/Kits/hardware_hacking_remote_soldered_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet with connected remote control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_1200.jpg

