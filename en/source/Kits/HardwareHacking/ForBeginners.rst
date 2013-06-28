
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Kits.html">Kits</a> / <a href="../../Kits/HardwareHacking/HardwareHacking.html">Starter Kit: Hardware Hacking</a> / Hardware Hacking for Beginners 

.. _starter_kit_hardware_hacking_for_beginners:

Hardware Hacking for Beginners
==============================

Hardware hacking with Starter Kit: Hardware Hacking is easy, etc etc!


Using the Industrial Quad Relay Bricklet
----------------------------------------

* what does quad relay?
* how to find pads for quad relay?
 * mechanical switch
 * relay
 * separable wire

Let us start with a simple example schematic. The following schematic
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
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_qr_1500.jpg




Using the Analog in Bricklet
----------------------------

* what does analog in?
* how to find pads for analog in?
 * LED
 * Sensor

Example Schematic: A LED is switched by some kind of circuitry, in this case a
simple switch.

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_off_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch and LED, switched off
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_off_1500.jpg

To read out the state of the hardware, we can use the state of the LED. To read 
it out we connect one port of the Industrial Digital In 4 Bricklet to it. Since 
the minimum high level input voltage is 3V it is not sufficient to connect it 
to the LED. Typically the (forward-) voltage of an red LED is 1.7V so it is not 
high enough to trigger a high level on the input port of the Digital In.
To solve this we connect the Industrial Digital In 4 Bricklet to the LED and the
series resistor. The polarity or, to put it in another way, the way you have 
connected the wires to the Digital In does not matter. If the Digital In does
not show any reaction if the LED is triggered simply substitute the wires of 
the input port. The wiring will look as the following:

.. image:: /Images/Kits/hardware_hacking_for_beginner_schematic_switch_digital_in_350.jpg
   :scale: 100 %
   :alt: Example Schematic with Battery, Switch and LED and Industrial Digital In 4 Bricklet
   :align: center
   :target: ../../_images/Kits/hardware_hacking_for_beginner_schematic_digital_in_1500.jpg


Soldering a wire to a solder pad
--------------------------------

To solder a wire to a pad, you need a 
`soldering iron <https://en.wikipedia.org/wiki/Soldering_iron>`__ 
and `solder <http://en.wikipedia.org/wiki/Solder>`__.

Don't be afraid if you have never soldered something! You only
need to solder a wires to a solder pad if you want to hack
hardware with the Starter Kit: Hardware Hacking.

You can solder a wire to a pad in five steps:

* Heat the solder pad with the soldering iron
* Add solder to the pad while it is hot
* Attach the cable to the pad
* Remove the soldering iron (still hold the cable to the pad)
* Wait until pad is cooled down 

To make it easier, you can also apply some solder to the
stripped part of the cable first.

We also made a small video to show the process:

TODO: Video
