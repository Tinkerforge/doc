
.. _tutorial_eeprom_vs_co_processor:

Tutorial - Bricklets with EEPROM vs Co-Processor 
================================================

Early 2017 we started to replace all of the existing Bricklets with new
versions. These new versions have a co-processor instead of an EEPROM and
they have a different connector.

To re-design and replace about 50 Bricklets is of course a mammoth task.
So why did we do it?


Old Bricklet with EEPROM
------------------------

The old Bricklets with EEPROM had parts like sensors, analog-digital 
converters, LEDs, interface extensions etc. These parts were directly 
connected to the processor on the Bricks (through a Bricklet cable). 
This concept has the advantage, that simple Bricklets only need few parts.
Every Bricklet had an EEPROM that saved the code for the Brick. 
This code was loaded by the Brick, written into its own flash and 
executed periodically. Because of this a Brick did not have to know each 
individual Bricklet. This allowed for a big variety of different building 
blocks.

A disadvantage was, that the processor of the Brick had to run all of the
Bricklet code as well as the code for the Brick functionality itself. 
Applications like a frequency counter or similar, that need to react 
permanently to a signal, were not possible to realize. Another disadvantage 
was that the code of the Bricklets was only compatible to the SAM3 and SAM4 
processors from Atmel. After Microchip bought Atmel it was not clear anymore
how long these processors will be available.


Because of these problems we decided to replace all of these Bricklets
with new ones that have a co-processor.


New Bricklet with Co-Processor
------------------------------

The new Bricklets have their own co-processors that only have two tasks:

* To implement the Bricklet functionality and
* to communicate with a Brick.

Compared to the old Bricklets with EEPROM, the new Bricklets with co-processor
now have a fixed protocol that can be implemented by any processor. So
the Bricks do not need to use a specific kind of processor anymore.

Additionally, we can now have Bricklets that

* process big amounts of data (e.g. `Thermal Imaging Bricklet <https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Thermal_Imaging.html>`__),
* react in real-time to edge-transitions (e.g. `Industrial Counter Bricklet <https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Industrial_Counter.html>`__) or
* do complicated calculations on board (e.g. `Sound Pressure Level Bricklet <https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Sound_Pressure_Level.html>`__).

While the old Bricklets with EEPROM could only be connected to a Brick, the
new Bricklets can in theory be read out by any device that can speak SPI.

This allowed us to develop the Isolator Bricklet as well as the Bricklet HAT
(comming soon) and Bricklet HAT Zero (comming soon).

There are many other small technical advantages that increase the
performance and robustness of the new Bricklets compared to the old ones.

And last but not least, we were able to replace the old 10 pole connector
with a new more robust and user-friendly 7 pole connector. A detailed
explanation about the connector change can be found
:ref:`here <tutorial_bricklet_cables>`.

It took us about 2.5 years and many many engineering man-hours to design
the new Bricklets and replace all of the old ones. Nevertheless, in
hindsight we are very happy with the result and we are certain that the 
efforts were worthwhile.
