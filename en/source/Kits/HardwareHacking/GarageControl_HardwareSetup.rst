
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Control Garage Door Openers Hardware Setup

.. _starter_kit_hardware_hacking_garage_control_hardware_setup:

Control Garage Door Openers Hardware Setup
==========================================

The hardware of garage door openers can be really complex. Besides the radio 
transmitter there are complex electronics for ciphering, for example. So we don't
want to take a closer look at it. But we don't have to, since the only thing we
are interested in is to trigger the button we normally use to operate the door.

We will not trigger the button directly, but we will be able to bypass
it as described :ref:`here <starter_kit_hardware_hacking_for_beginners_quad_relay>`.

Dismantle the Casing
--------------------

At first we have to dismantle the casing of the remote switch. 
With a small screwdriver this is an easy task.

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_350.jpg
   :scale: 100 %
   :alt: Remote Control with dismantled Casing
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_1200.jpg

After removing the casing we can take a look at the five control buttons.
We are only interested in the most left button since this one controls
the garage door on this model. 

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup.jpg
   :scale: 100 %
   :alt: Closeup of Remote Control Button
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup.jpg

Connect Wires
-------------

If we take a closer look at the button we will find that only two of the four
pads are connected with traces. So we have identified the points were we have
to solder our wires.

.. image:: /Images/Kits/hardware_hacking_garage_remote_soldered_350.jpg
   :scale: 100 %
   :alt: Remote Control with soldered wires
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_soldered_1200.jpg

Connect the other wire ends to one relay of the Industrial Quad Relay Bricklets 
8 pole connector. After that we can test our work by using the Brick
Viewer software. Open the Industrial Quad Relay Bricklet tab and switch the
related relay. You should be able to trigger the remote control.

After this test we can close the casing of the remote control and have finished
our task.

.. image:: /Images/Kits/hardware_hacking_garage_remote_finished_new_350.jpg
   :scale: 100 %
   :alt: Garage Door Remote Control with attached Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_finished_new_1200.jpg
