
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Control Remote Switches Hardware Setup

.. _starter_kit_hardware_hacking_remote_switch_hardware_setup:

Remote Switch Hardware Setup
============================

Most remote controls for remote switches are equipped with an IC called HX2262.
Basically it has six different inputs: two to define if it is an ON or OFF
switch command and four inputs to define whereis it is A, B, C or D to switch.
An input is activated if it is switched to GND. All inputs are interconnected
in a matrix style order.

In this example we will use the Industrial Quad Relay Bricklet with its four
solid state relays to short the inputs ON, OFF, A and B to GND. This way
we will be able to switch two remote switches. If also C and D should be
switched an additional Industrial Quad Relay is necessary.

Take a look at the Remote Control
---------------------------------

If you open your remote control you will most likely see a circuit board like this:

.. image:: /Images/Kits/hardware_hacking_remote_open_350.jpg
   :scale: 100 %
   :alt: Remote Control Opened
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_open_1200.jpg

The big IC right of the red DIP switch is the HX2262. If you remove the casing
completely and take a look at the bottom side it should look like this:

.. image:: /Images/Kits/hardware_hacking_remote_bottom_350.jpg
   :scale: 100 %
   :alt: Remote Control Close Lookup Bottomside
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_bottom_1200.jpg

Next we have to solder the wires to connect to the inputs of the remote
control. We will solder five wires to the HX2262 IC:

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

After that it will look like this:

.. image:: /Images/Kits/hardware_hacking_remote_soldered_closeup_remote_350.jpg
   :scale: 100 %
   :alt: Remote Control Close Lookup with soldered wires
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_closeup_remote_1200.jpg

Next we will connect these wires to the Industrial Quad Relay Bricklet.
Each input will be connected to its own relay and each relay is also connected
to GND (black wires):

====== ========== =====
Signal Wire Color Relay
====== ========== =====
A      blue       0
B      red        1
ON     yellow     3
OFF    purple     4
====== ========== =====

Now each relay can connect one of the four signals to GND:

.. image:: /Images/Kits/hardware_hacking_remote_soldered_closeup_iqr_top_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet connector closeup
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_closeup_iqr_top_1200.jpg

After that we are finished. The full hardware setup will look like this:

.. image:: /Images/Kits/hardware_hacking_remote_soldered_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet with connected Remote Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_1200.jpg

