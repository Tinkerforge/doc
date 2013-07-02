
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Hardware Hacking for Beginners 

.. _starter_kit_hardware_hacking_for_beginners:

Hardware Hacking for Beginners
==============================

Hardware hacking with Starter Kit: Hardware Hacking is easy, etc etc!

There are two different modules in this kit for two different purposes:

Industrial Quad Relay Bricklet
------------------------------

General Description
^^^^^^^^^^^^^^^^^^^

The :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`
consists of four
`Solid State Relays <http://en.wikipedia.org/wiki/Solid_state_relay>`__.
Relays are electromechanical driven switches, which means that you can short 
cut a signal controlled by another electrical signal. In case of solid state 
relays the switches are not electromechanical, there are no mechanical parts 
in there.

If you want to switch something with it, you have to consider the maximum 
allowed voltage of 30V. So do not try to switch mains voltage directly!
In many cases the maximum voltage inside the circuit of 
a product is given by the voltage of the supply. For example if you have a 
battery powered device it is very likely that the maximum voltage in all 
circuits of this device will not exceed the voltage of the battery. If you 
have a wall adapter powered device, the maximum voltage will most likely
not exceed the output voltage of the wall adapter. Of course there are exception.
If you are not sure, measure it.

In one sentence: Typical applications for this module can be found in
switching other circuits on or off. To explain these applications
let us start with a simple example. The following schematic
depicts a LED with the typically necessary series resistor which can
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

Of course we can add a second switch in parallel to the first one, such that
the LED will light if one of the two is switched on. If both are switched on
the LED will light, too.

TODO: second switch can force on, but not off stat if first switch is on

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_two_switches_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch and LED, with two switches
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_two_switches_1500.jpg

That's the basic idea to make a circuit controllable with an Industrial Quad 
Relay Bricklet. We simply install the Quad Relay in parallel to an existing
switch to bypass it.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_switch_qr_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch and LED and Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_switch_qr_1500.jpg

Of couse you can create your own circuits and integrate the Industrial Quad 
Relay Bricklet as a switch, too.

So how to use the the Industrial Quad Relay Bricklet?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's say you have a device which have buttons to trigger different actions
and you want to make them externally triggerable. At next you have to take a 
closer look at these buttons and their connections on the circuit board. 
In most cases you can directly see two traces of the circuit board connected
with a button. If you have identified the connection you only have to solder
two wires, each to one trace, on it and connect one relay of the Industrial
Quad Relay Bricklet with it.

.. image:: /Images/Kits/hardware_hacking_garage_remote_top_closeup.jpg
   :scale: 100 %
   :alt: Button on circuit board closeup
   :align: center
   :target: ../../_images/Kits/hardware_hacking_garage_remote_top_closeup.jpg

TODO: add arrows to the pads in the image

The picture above depicts a button on a circuit board. You can see two traces,
one on the upper right corner and one on the bottom right corner
connected with the button. To make this button externally triggerable you have
to solder one wire each to the upper right and bottom right pad of the button.

TODO: before/after image of connected quad relay


Industrial Digital In 4 Bricklet
--------------------------------

General Description
^^^^^^^^^^^^^^^^^^^

The :ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>` is
equipped with four `Optocouplers <http://en.wikipedia.org/wiki/Optocoupler>`__.
Technically speaking a optocoupler consists of a LED which triggers a phototransistor
with light. This way there is no direct electrical connection between the
triggering LED and the switching phototransistor, it is galvanically isolated.

So less technical speaking the Industrial Digital In 4 Bricklet is equipped
with four LEDs. If one of these LEDs is on, the respective input will be
read out as logical high. If it is not on the input will be read out as
logical low.

If you want to use Industrial Digital In 4 Bricklet to read out a state of
a device you have to connect it to one of the inputs. This has to be done such
that the LED will be on if the state to read out is electrically high and will
be off if the state is electrically low. Take a look at the electrical
description of the Bricklet:
Voltages below 2V are interpreted as "low" (LED is off). Voltage above
3V are interpreted as "high" (LED is on). If the voltage is between 2V and 3V
it is undefined how the LED will react. Therefore, this voltage range should be
avoided.

Using the Industrial Digital In 4 Bricklet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example we want to read out the state of a very simple schematic:
A LED is switched by some kind of circuitry, in this case a
simple switch.

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
connected the wires to the Digital In does not matter. If the Digital In does
not show any reaction if the LED is triggered simply swap the wires on
the input. The wiring will look as following:

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_switch_digital_in_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch and LED and Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_switch_digital_in_1500.jpg

Identify the Series Resistor of a LED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are many different kinds of resistor packages. The most common 
are wired packages.

TODO FOTO WIRED RESISTOR  Metallfilm, Kohleschicht etc.

Nowadays many products use so called `Surface-Mount Devices (SMD)
<http://en.wikipedia.org/wiki/Surface-mount_device>`__.
These devices can differ in their size extremely. There are very tiny devices
possible (e.g. casing 0201: 0.6mm x 0.3mm) or large devices (e.g. casing 2920: 
7.4mm x 5.1mm). There are resistors, capacitors, inductances and other devices 
which can be found directly mounted on the circuit board. 

TODO FOTO SMD Bauteile

But how to know what kind of device it is?
There are different possibilities. Experts can tell you which device it may be
by identifing its optical features. If the device has a marking it is possible
to even identifing the value (e.g. 1k Ohm resistor or 22 Ohm resistor). If 
there is no marking and it can't be recognized it has to be identified by
measuring or by identifing its purpose in the circuit.

That's the starting point for this kit. If you like to readout the status of a 
LED follow the traces until you reach a wired or SMD device. It will most likely
be the series resistor.

TODO FOTOS Beispiele für LED + Vorwiderstand auf Leiterplatte


Soldering a wire to a solder pad
--------------------------------

To solder a wire to a pad, you need a 
`soldering iron <http://en.wikipedia.org/wiki/Soldering_iron>`__ 
and `solder <http://en.wikipedia.org/wiki/Solder>`__.

Don't be afraid if you have never soldered something! You only
need to solder a wires to a solder pad if you want to hack
hardware with the Starter Kit: Hardware Hacking.

You can solder a wire to a pad in five steps:

* Heat the solder pad with the soldering iron
* Add solder to the pad while it is hot
* Attach the wire to the pad
* Remove the soldering iron (still hold the wire to the pad)
* Wait until solder pad is cooled down

To make it easier, you can also apply some solder to the
stripped part of the wire first.

We also made a small video to show the process:

TODO: Video
