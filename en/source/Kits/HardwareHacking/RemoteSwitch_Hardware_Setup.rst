
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Control Remote Switches Hardware Setup

.. _starter_kit_hardware_hacking_remote_switch_hardware:

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

The big IC left of the red DIP switch is the HX2262. If you remove the casing 
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
6          A      red
7          B      blue
8          C      -
9          GND    black
10         D      -
11         -      -         
12         ON     yellow
13         OFF    purple
========== ====== ==========

After that it will look like this:

.. image:: /Images/Kits/hardware_hacking_remote_soldered_closeup_remote_350.jpg
   :scale: 100 %
   :alt: Remote Control Close Lookup with soldered wires
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_closeup_remote_1200.jpg

Next we will connect these wires to the connector of the Industrial Quad Relay.
Each Input will be connected to one relay each. The other connectors of these 
relays will be connected to GND which will be bypassed (black wires).
 
.. image:: /Images/Kits/hardware_hacking_remote_soldered_closeup_iqr_top_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Connector Close Lookup
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_closeup_iqr_top_1200.jpg

After that we are finished. The full hardware setup will look like this:
 
.. image:: /Images/Kits/hardware_hacking_remote_soldered_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay with connected Remote Control
   :align: center
   :target: ../../_images/Kits/hardware_hacking_remote_soldered_1200.jpg

