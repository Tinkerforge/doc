:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/Blinkenlights/Blinkenlights.html">Starter Kit: Blinkenlights</a> / Construction of Starter Kit: Blinkenlights

.. _starter_kit_blinkenlights_construction:

Construction of Starter Kit: Blinkenlights
==========================================

The Starter Kit: Blinkenlights comes with:
1x :ref:`Master Brick <master_brick>`,
1x :ref:`LED Strip Bricklet <led_strip_bricklet>`,
4x LED Pixels (50 pieces each),
1x Perforated Board 80x40cm (black)
1x Front Panel (white)
1x 5V/8A Power Supply
1x Bricklet Cable 15cm
1x 2x2.5mm^2 wires
4x 2-wire clamps
6x 3-wire clamps
4x 5-wire clamps
and cable straps, screws, spacers and some other parts.


Necessary Tools
---------------

You will need a phillips screwdriver, something to dismantle wires 
(knife or cable stripper), and a tape measure. Allow some extra time to build
the kit.


First Step
----------

Check if everything was delivered correctly. You can remove the protective foil 
of the front and back of front plate (white).

(TODO: remove foil of perforated board (black), too?)
	

Attach Pixels to Perforated Board
---------------------------------

Next we will stick the pixels into the perforated boards. It is absolutely 
important that you will start with the right pixel (begin with led pixel chain
input) on the right position. If you start wrong it is possible that you can't
wire the pixels or that your cables will come out on the top position of the
display instead on the bottom side.

Let's start with the build up process.

First take the first bunch of pixels and take the pixel with the 
plug (TODO check me).


TODO Image with first pixel and plug

Stick this pixel into the perforated board. The following image shows
the right position. After that stick in the next pixels like depicted.

TODO Image with mounting holes and marked pixel1 position

If you have finished to attach the first bunch take the next bunch and plug 
together the last pixel of the attached pixels with the first pixel of the new
bunch. 

TODO Image pixels connected?

After that plug these pixels into the perforated board and repeat this 
procedure until you have attached the four bunches.

TODO Image all pixels attached


Make Power Supply Cables and Dismantle Pixel Cables
---------------------------------------------------

In the next step we will make the power supply cables.  Some 2x2.5mm^2 cables
should be delivered with the kit. Cut the following cables from it:

 * 1x 95cm
 * 1x 80cm
 * 1x 55cm
 * 1x 40cm
 * 1x 20cm
 * 1x 10cm

Dismantle 10mm of the wires on both ends. Additionally dismantle 8mm on the 
power supply wires of the led pixels (blue and red wires).


Connect the Wires
-----------------

We will start the wiring with the 95cm cable. It will wire the power supply to
the end of the connected led pixels. Take two 2-wire camps and connect
one to the red led pixel wire and one on the blue led pixel wire. The blue wire
will be connected with the black power supply wire. The red wire of the pixels
will be connected with the red wire of the power supply.
After that connect your produced 95cm cable and install it as depicted in the 
following picture.

TODO Image with wired 95cm cable

After that we will wire the 80cm cable. It will be connected to the last but one
power supply point. Take two 3-wire clamps and connect the two blue wires of the
pixels with the black wire and the two red wires with the red wire. Install it
as depicted below.


TODO Image with wired 95cm + 80cm cable

Next we will also wire the 55cm cable as before with two 3-wire clamps.

TODO Image with wired 95cm + 80cm + 55cm cable

Repeat this step also with the 40cm cable.

TODO Image with wired 95cm + 80cm + 55cm + 40cm cable

As last step take two 2-wire clamps and wire the first power supply point with
the 20cm cable and install the cable as depicted:

TODO Image with wired 95cm + 80cm + 55cm + 40cm + 20cm cable


Prepare the 5V Power Supply
---------------------------

In this step we will make the wiring to power all these cables.
At first connect the 5V power supply to two 5-wire clamps as depicted below.

TODO Image 5V Power Supply + 2x 5-wire clamp

The white wire of the power supply is the 5V wire and will later be connected to
the red wires. the black wire is GND and will be connected to the black wires.

Next take two additional 5-wire clamps and connect these clamps with the
previous 5-wire clamps.

TODO Image 4x 5-wire clamps with 5V


Connect everything
------------------

Next connect the previous installed power supply cables with the clamps.
Install it as depicted in the following picture:

TODO Image Power Supply Wiring finished


Attach LED Strip Bricklet and Master Brick
------------------------------------------

After that we have to attach the LED Strip Bricklet and the Master Brick.
To do this start by dismantling the LED Strip Bricklet connection wires. 7mm 
will suffice. Connect it with the Bricklet and install everything as depicted
below

TODO Image LED Stip Bricklet + Master Brick + Cable

Connect this circuitry with the first pixel and install it as depicted below:

TODO Image all wired

Attach the mounting plates
--------------------------

In this step we will attach the mounting plates to the perforated board. Use
two 10mm spacers (thread inside/inside) and two M3 screws for each mounting plate
to generate the following plates:

TODO Image mounting plate with 2x 10mm spacers

After that mount these plates to the back of the perforated board with M3 
screws. On six positions (see the following image) we will not use M3 screws to 
attach it. We will use 12mm spacers (thread inside/outside) to mount it.

TODO Image with 6 marked positions

After this step the board will looks like the following

TODO Image board with mounting plates


Attach Front Panel (Optional)
-----------------------------

This step is optional. You can attach the delivered front panel to the board,
dependend on your application you don't have to. 

If you wan't to use the kit to display pixel based things like text, games or
something else you can attach the front panel directly to the six 12mm spacers.
For diffuse applications like our fire example it is necessary to increase the
distance between front panel and the pixels. To do this simply put more spacers
between them. We use two 9mm spacers and one 12mm spacer additionally to the 
mounted 12mm spacer on each of the six mounting points.






