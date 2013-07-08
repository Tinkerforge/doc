
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Hardware Hacking for Beginners 

.. _starter_kit_hardware_hacking_for_beginners:

Hardware Hacking for Beginners
==============================

This Hardware Hacking Kit should encourage you to hack devices and gain some
basic knowledge about electronics. In the following there are some basic 
descriptions how to use the supplied hardware.

Basically there are two different purposes for the kit. Each is handled
by one specific Bricklet.

Industrial Quad Relay Bricklet
------------------------------

General Description
^^^^^^^^^^^^^^^^^^^

The :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
consists of four
`Solid State Relays <http://en.wikipedia.org/wiki/Solid_state_relay>`__.
Relays are electromechanical driven switches, which means that you can
short-circuit a signal controlled by another electrical signal with it. 
In case of solid state relays the switches are not electromechanical, there are 
no mechanical parts in there.

If you want to switch something with it, you have to consider the maximum 
allowed voltage of 30V. So do not try to switch mains voltage directly!
In many cases the maximum voltage inside the circuit of 
a product is given by the voltage of the supply. For example if you have a 
battery powered device it is very likely that the maximum voltage in all 
circuits of this device will not exceed the voltage of the battery. If you 
have a wall adapter powered device, the maximum voltage will most likely
not exceed the output voltage of the wall adapter. Of course there are 
exceptions. If you are not sure, measure it.

Summary: Typical applications for this Bricklet can be found in
switching other circuits on or off. To explain these applications
let us start with a simple example. The following schematic
depicts a LED (with the typical series resistor) which can
be turned on or off depending on the switch.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_off_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch and LED, switched off
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_off_1500.jpg

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_on_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch and LED, switched on
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_on_1500.jpg

If we can add a second switch in parallel to the first one, 
the LED will be on if one of the two switches is closed. If both switches
are closed the LED will be on, too. If one switch is closed, the other one can
not affect the state of the LED. The LED will be on.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_two_switches_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, two Switches and LED
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_two_switches_1500.jpg

That's the basic idea to make a circuit controllable with an Industrial Quad 
Relay Bricklet. We simply install a relay of the Bricklet in parallel to an
existing switch such that we can bypass it.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_switch_qr_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch, LED and Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_switch_qr_1500.jpg

Instead of hacking other devices, you can of course create your own circuits  
with the Industrial Quad Relay Bricklet.

How to use the the Industrial Quad Relay Bricklet?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's say you have a device which have buttons to trigger different actions
and you want to make them externally triggerable (e.g. remote control).
At first you have to take a 
closer look at these buttons and their connections on the circuit board. 
In most cases you can directly see two traces of the circuit board connected
with a button. If you have identified these connections, which should be
externally shortable, you only have to solder
two wires, each to one trace, on it and connect one relay of the Industrial
Quad Relay Bricklet with it.

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup2.jpg
   :scale: 100 %
   :alt: Button on circuit board closeup
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup2.jpg

The picture above depicts a button on a circuit board. You can see two traces,
one on the upper right corner and one on the bottom right corner
connected with the button. Now we have identified the two traces which are
shorted by the switch (compare to example circuit above).
To make the function of this button externally 
triggerable you have to solder one wire each to the upper right and bottom 
right pad of the button. At the end it will look at the following:

.. image:: /Images/Kits/hardware_hacking_garage_remote_soldered_350.jpg
   :scale: 100 %
   :alt: Button on circuit board closeup with soldered wires
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_soldered_1500.jpg

Both wires have to connected to one port of the Quad Relay Bricklet. Afterwards
you are able to trigger the action with the Quad Relay Bricklet which
was originally only triggered by the button.

Industrial Digital In 4 Bricklet
--------------------------------

General Description
^^^^^^^^^^^^^^^^^^^

The :ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>` is
equipped with four `Optocouplers <http://en.wikipedia.org/wiki/Optocoupler>`__.
Technically speaking an optocoupler consists of a LED which triggers a 
phototransistor with light. This way there is no direct electrical connection 
between the triggering LED and the switching phototransistor, it is 
galvanically isolated.

So less technical speaking the Industrial Digital In 4 Bricklet is equipped
with four internal LEDs. If one of these LEDs is on, the respective output will 
be read out as logical high. If it is not on the output will be read out as
logical low. These four outputs are connected to the microcontroller of the
connected Brick such that they can be read out by it.

If you want to use the Industrial Digital In 4 Bricklet to read out a state of
another device you have to connect it to one of the four inputs. 
This has to be done such that the internal LED will be on if the state to read 
out is electrically high and will
be off if the state is electrically low. Take a look at the electrical
description of the Bricklet:
Voltages below 2V are interpreted as "low" (LED is off). Voltage above
3V are interpreted as "high" (LED is on). If the voltage is between 2V and 3V
it is undefined how the LED will react. Therefore, this voltage range should be
avoided.

How to use the Industrial Digital In 4 Bricklet?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example we want to read out the state of a very simple circuit
represented by a LED:
The LED is switched by some kind of circuitry, in this case a
simple manual switch. But it could also be an IC or similar.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_off_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch and LED, switched off
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_off_1500.jpg

To read out the state of the hardware, we can use the state of the LED. To read 
it out we connect one input of the Industrial Digital In 4 Bricklet to it. Since
the minimum high level input voltage is 3V it is not sufficient to connect it
to the LED. Typically the (forward-) voltage of an red LED is 1.7V so it is not 
high enough to trigger a high level on the input port of the Digital In.
To solve this we connect the Industrial Digital In 4 Bricklet to the LED and the
series resistor. The polarity or, to put it in another way, the way you have 
connected the wires to the Digital In does not matter. If the Digital In 4 
Bricklet does not show any reaction if the LED is triggered, simply swap the 
wires on the input. The wiring will look as following:

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_switch_digital_in_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch, LED and Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_switch_digital_in_1500.jpg

Identify the Series Resistor of a LED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are many different kinds of resistor packages. The most common 
are wired packages:

.. image:: /Images/Kits/hardware_hacking_for_beginner_tht_resistor_350.jpg
   :scale: 100 %
   :alt: Image of THT Resistors
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_tht_resistor_1500.jpg

Nowadays many products use so called `Surface-Mount Devices (SMD)
<http://en.wikipedia.org/wiki/Surface-mount_device>`__.
These devices can differ in their size extremely. There are very tiny devices
possible (e.g. casing 0201: 0.6mm x 0.3mm) or large devices (e.g. casing 2920: 
7.4mm x 5.1mm). There are resistors, capacitors, inductances and other devices 
which can be found directly mounted on the circuit board. 

.. image:: /Images/Kits/hardware_hacking_for_beginner_smd_resistor_350.jpg
   :scale: 100 %
   :alt: Image of SMD Resistors
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_smd_resistor_1500.jpg

But how to figure out what kind of device it is?
There are different options. Experts can tell you which device it may be
by looking at its optical features. If the device has a marking it is possible
to even identifying the value (e.g. 1k Ohm resistor or 22 Ohm resistor). If
there is no marking and it can't be recognized it has to be identified by
measuring or by determining its purpose in the circuit.

That's the starting point for this kit. If you like to readout the state of a 
LED follow the traces until you reach a wired or SMD device. It will most likely
be the series resistor. 

The next image depicts one example (based on the
:ref:`starter_kit_hardware_hacking_garage_control` example).

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup3_350.jpg
   :scale: 100 %
   :alt: LED with Series Resistor Closeup
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup3.jpg

You can see a SMD LED marked with a red arrow. There are two traces
connected to this LED. In one trace you can find a small SMD resistor (marked
with blue arrow). 

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup4_350.jpg
   :scale: 100 %
   :alt: LED with Series Resistor Closeup
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup4.jpg

So if you want to read our the state of this LED you have
to solder one wire directly to the LED (red circle) and one after the 
series resistor (one of the blue circles). That's it!

Soldering a wire to a solder pad
--------------------------------

To solder a wire to a pad, you need a 
`soldering iron <http://en.wikipedia.org/wiki/Soldering_iron>`__ 
and `solder <http://en.wikipedia.org/wiki/Solder>`__.

Don't be afraid if you have never soldered something! 
For the Starter Kit: Hardware Hacking it is only about
soldering a wire to a pad.

Soldering a wire to a pad can be done basically in five steps:

* Heat the solder pad with the soldering iron
* Add solder to the pad while it is hot, the solder of the pad should get liquid.
* Attach the wire to the pad
* Remove the soldering iron (still hold the wire to the pad)
* Wait until solder pad is cooled down

To make it easier, you can also apply some solder to the
stripped part of the wire first.

If you not sure about how to do this you can search for howto videos.
For example on `Youtube <www.youtube.com>`__ there are plenty of them.

