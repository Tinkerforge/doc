:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / <a href="../../Kits/Blinkenlights/Blinkenlights.html">Starterkit: Blinkenlights</a> / Aufbau des Starterkits: Blinkenlights


.. role:: led-pixel-red

.. role:: led-pixel-green

.. role:: led-pixel-blue

.. role:: led-pixel-white

.. role:: power-red

.. role:: power-black

.. role:: power-white


.. _starter_kit_blinkenlights_construction:

Aufbau des Starterkits: Blinkenlights
=====================================

Das Starterkit: Blinkenlights besteht aus:

* 1x :ref:`Master Brick <master_brick>`,
* 1x :ref:`LED Strip Bricklet <led_strip_bricklet>`,
* 4x LED Pixels (jeweils 50 Stück),
* 1x Gelochte Rückplatte 80x40cm (schwarz)
* 1x Frontplatte 90x50cm (weiß)
* 4x Wandbefestigungsplatte (für Wandharken)
* 1x 5V/8A Stromversorgung
* 1x Brickletkabel 15cm
* 1x 2x2.5mm² Litze (5m)
* 2x Dübel und Wandharken
* 4x 2-Draht Klemmen
* 6x 3-Draht Klemmen
* 4x 5-Draht Klemmen

sowie Kabelbinder, Schrauben, Abstandshalter und andere Teile.

.. image:: /Images/Kits/kit_blinkenlights_content_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Inhalt
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_content_1200.jpg


Notwendige Werkzeuge
--------------------

Ein Kreuzschlitz-Schraubendreher, etwas zum Abisolieren von Drähten (Messer
oder Abisolierzange) und eine Maßband sind notwendig. Es sollte sich genügend
Zeit zum Aufbau des Kits genommen werden.

Erster Schritt
--------------

Es sollte überprüft werden ob alles vorhanden und unbeschädigt ist. Anschließend
sollten die Schutzfolien von Frontplatte (weiß) und Rückplatte (schwarz) 
abgezogen werden. Jeweils auf Vorder- und Rückseite befindet sich eine Folie.

.. image:: /Images/Kits/kit_blinkenlights_remove_protective_foil_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Aufbau Folien entfernen
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_remove_protective_foil_1200.jpg


Pixel in die Rückplatte einsetzen
---------------------------------

Next you can stick the pixels into the perforated board. It is important that
you start with the correct pixel on the correct position. If you start wrong it
is possible that you can't wire the pixels or that your cables will come out on
the top position of the display instead of the bottom side.

Take the first bunch of pixels and insert the pixel with the plug (the end that
will be connected to the LED Strip Bricklet). See the schematic drawing for the
correct position, marked as start.

.. image:: /Images/Kits/kit_blinkenlights_build_step1_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step 1
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step1_1200.jpg

The following drawing shows the back of the perforated board. The pixels
will be plugged in from this side, such that the heads of the LEDs are on the front.
Notice the positions of the small mounting holes and the starting position for
the first LED. After inserting the first pixel continue in the alternating
pattern as show by the red line.

.. image:: /Images/Kits/kit_blinkenlights_led_wiring_600.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Wiring Process Description
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_led_wiring_1200.jpg

If you finished to attach the first 50 pixels take the next pixels and plug
them together with their connectors. Then put the next 50 pixels into the 
perforated board and repeat this procedure.

.. image:: /Images/Kits/kit_blinkenlights_build_step4_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction All Pixels Attached
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step4_1200.jpg


Power Supply Cables and Pixel Cables
------------------------------------

In the next step we will cut and place the power supply cables. 5m of 2x2.5mm² 
wires are included in the kit. Cut the following wire lengths from it:

* 1x 95cm
* 1x 80cm
* 1x 55cm
* 1x 40cm
* 1x 20cm
* 1x 10cm

Strip 10mm of the wires on both ends. 

.. image:: /Images/Kits/kit_blinkenlights_wire_stripped_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Stripped Wires
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wire_stripped_1200.jpg

Additionally strip 8mm on the power supply wires of the LED pixels (blue and
red wires).


Connect the Wires
-----------------

Pay attention to correctly constructing the power supply wiring. Incorrect
wiring can damage the LED pixels.

Start the wiring with the 95cm cable. It will connect the power supply to
the last connected LED pixels. Take two 2-wire clamps and connect one to the
:led-pixel-red:`red` LED pixel wire and one on to the :led-pixel-blue:`blue`
LED pixel wire. The :led-pixel-blue:`blue` wire will be connected with the
:power-black:`black` power supply wire. The :led-pixel-red:`red` wire of
the pixels will be connected with the :power-red:`red` wire of the power
supply. After that install it the 95cm power supply cable as depicted in the
following picture.

.. image:: /Images/Kits/kit_blinkenlights_wago_2x_connected_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step Clamps
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_2x_connected_1200.jpg

.. image:: /Images/Kits/kit_blinkenlights_build_step6_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step with 95cm Cable
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step6_1200.jpg

After that wire the 80cm cable. It will be connected to the last but one
power supply point. Take two 3-wire clamps and connect the two
:led-pixel-blue:`blue` wires of the pixels with the :power-black:`black` wire
and the two :led-pixel-red:`red wires with the :power-red:`red wire. Install it
as depicted below.

.. image:: /Images/Kits/kit_blinkenlights_wago_3x_connected_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step Clamps
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_3x_connected_1200.jpg


.. image:: /Images/Kits/kit_blinkenlights_build_step7_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step with 80cm Cable
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step7_1200.jpg


Next we will wire the 55cm cable as before with two 3-wire clamps.

.. image:: /Images/Kits/kit_blinkenlights_build_step8_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step with 55cm Cable
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step8_1200.jpg

Repeat this step also for the 40cm cable.

.. image:: /Images/Kits/kit_blinkenlights_build_step9_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step with 40cm Cable
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step9_1200.jpg


As the last wiring step take two 2-wire clamps and wire the last power supply
point with the 20cm cable and install the cable as depicted:

.. image:: /Images/Kits/kit_blinkenlights_build_step10_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Step with 20cm Cable
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step10_1200.jpg


Prepare the 5V Power Supply
---------------------------

Now the wiring of the power cables needs to be joined.
Connect the 5V power supply to two 5-wire clamps as depicted below.

.. image:: /Images/Kits/kit_blinkenlights_wago_power_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Power Supply Connection
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_power_1200.jpg

The white wire of the power supply is the :power-white:`5V` wire and will later
be connected to the :power-red:`red` wires. the black wire is
:power-black:`ground` and will be connected to the :power-black:`black` wires.

Next take two additional 5-wire clamps and connect these clamps with the
previous 5-wire clamps.


.. image:: /Images/Kits/kit_blinkenlights_wago_5x_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Power Wiring
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_5x_1200.jpg

Connect everything
------------------

Connect the previously installed power supply cables with the clamps.
Install it as depicted in the following picture:

.. image:: /Images/Kits/kit_blinkenlights_wago_5x_connected_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Power Wiring Installed
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_wago_5x_connected_1200.jpg


Attach LED Strip Bricklet and Master Brick
------------------------------------------

After that attach the LED Strip Bricklet and the Master Brick.
To do this start by stripping the LED pixel connection wires. 7mm will suffice.
Connect it with the Bricklet and install everything as depicted below.

.. image:: /Images/Kits/kit_blinkenlights_master_led_strip_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Master Brick with LED Strip
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_master_led_strip_1200.jpg

Connect this circuitry with the first pixel and install it as shown below:

.. image:: /Images/Kits/kit_blinkenlights_build_step13_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Master Brick Installed
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_build_step13_1200.jpg


Attach Wall Mounting Plates
---------------------------

Attach the wall mounting plates to the perforated board. Use
two 10mm spacers (thread inside/inside) and two M3 screws for each mounting plate:

.. image:: /Images/Kits/kit_blinkenlights_holder_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit mounting plate
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_holder_1200.jpg

Mount these plates to the back of the perforated board with M3 screws. 

.. image:: /Images/Kits/kit_blinkenlights_holder_on_board_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit mounting plate on board
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_holder_on_board_1200.jpg

After this step the board will look as the following:

.. image:: /Images/Kits/kit_blinkenlights_on_wall_wo_frontpanel_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit on Wall without Front Panel
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_on_wall_wo_frontpanel_1200.jpg

The distance between the mounting holes is 32cm for both, vertical
and horizontal mounting.

Attach Front Panel (Optional)
-----------------------------

This step is optional. You can attach the front panel to the board,
dependent on your application you don't have to. The pixels without
front panel are **very bright**.

The following image is from the Tetris example without front panel:

.. image:: /Images/Kits/kit_blinkenlights_tetris_wo_frontpanel_600.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Tetris w/o front panel
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_tetris_wo_frontpanel_1200.jpg

To mount the front panel, add 12mm spacers (thread inside/outside) to
six positions

.. image:: /Images/Kits/kit_blinkenlights_mounting_600.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit Construction Front Panel Mounting
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_mounting_1200.jpg

and attach the front panel to them with screws:

.. image:: /Images/Kits/kit_blinkenlights_on_wall_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit on Wall
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_on_wall_1200.jpg

If you want to use the kit to display pixel based things like text or games 
you can attach the front panel directly to the six 12mm spacers.
For diffuse applications like our fire example it is necessary to increase the
distance between front panel and the pixels. To do this simply put more spacers
between them. In our examples we used two 9mm spacers and one 12mm spacer 
additionally to the mounted 12mm spacer on each of the six mounting points.

Below you can see the rainbow example with 12mm spacer in daylight, 
with 2x12mm + 2x9mm spacer in daylight and with 2x12mm + 2x9mm spacer in
darkness:

.. image:: /Images/Kits/kit_blinkenlights_rainbow_near_far_dark_350.jpg
   :scale: 100 %
   :alt: Blinkenlights Kit rainbow
   :align: center
   :target: ../../_images/Kits/kit_blinkenlights_rainbow_near_far_dark_1200.jpg
