.. _io4_bricklet:

IO4 Bricklet
============


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricklets/bricklet_io4_11_tilted_350.jpg", 
	             "Bricklets/bricklet_io4_11_tilted_600.jpg", 
	             "IO-4 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_io4_11_vertical_100.jpg", 
	             "Bricklets/bricklet_io4_11_vertical_600.jpg", 
	             "IO-4 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_io4_11_horizontal_100.jpg", 
	             "Bricklets/bricklet_io4_11_horizontal_600.jpg", 
	             "IO-4 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_io4_11_master_100.jpg", 
	             "Bricklets/bricklet_io4_11_master_600.jpg", 
	             "IO-4 Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_io4_brickv_100.jpg", 
	             "Bricklets/bricklet_io4_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/io4_bricklet_dimensions_100.png", 
	             "Dimensions/io4_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * 4 inputs and outputs
 * Fixed 3.3V logic voltage
 * Configurable pullups and interrupts


Description
-----------

The IO4 :ref:`Bricklet <product_overview_bricklets>` can be used to extend the 
features of :ref:`Bricks <product_overview_bricks>` by external digital inputs 
and outputs.

The Bricklet features 4 pins that can be independently configured as
digital inputs or outputs. Each input pin can additionally be configured with
pullups or as interrupt source.

Via terminal blocks all signals can be accessed.
Two additional terminal blocks deliver the output voltage and GND. 

Human interfaces, such as switches, push-buttons and LEDs are typical 
applications of this Bricklet.

Hardware version 1.1 adds GND pins nearby the 4 signal pins to allow easier
access between signal pins and GND.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight                            6.7g
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Number of I/Os                    4
I/O voltages                      Fixed 3.3V
Maximum API Calls*                set_value (1khz), get_value(0.5khz), callback (1khz)
================================  ============================================================

\* depends on your system(OS, CPU etc.)

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/io4-bricklet/raw/master/hardware/io-4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/io4_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/io4-bricklet/zipball/master>`__)




.. _io4_bricklet_test:

Test your IO4 Bricklet
----------------------

To test the IO4 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the IO4 Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable.
In our test we connected an LED with series resistor to the board
by attaching the anode to pin 3 and the cathode to a GND pin.
Additionally we connected a button that can short pin 0 to GND
(see picture below). Starting from hardware version 1.1 you can also
use the GND pins directly beside the data pins.

.. image:: /Images/Bricklets/bricklet_io4_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected IO4 Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"IO4 Bricklet" in the Brick Viewer after you pressed “connect”. Select it.

.. image:: /Images/Bricklets/bricklet_io4_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the IO4 Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_brickv.jpg


In this tab you can change the "Debounce Period", 
it is the debounce time for interrupt callbacks. 
For example: If you set this value to 100, you will get interrupts
maximal every 100ms. This is necessary if something that bounces is
connected to the IO4 Bricklet, such as a button. You can test the optimal
value in the Brick Viewer and use it later in your own program.
  
Below the debounce period configuration you can configure the pins.
Each pin can be configured as input/output and in case of an input pin 
as pullup. The current state is depicted in the tabular below.

To test the LED we configure pin 3 as output and change 
the value. When the pin is high the LED should light up. To test the button 
configure pin 0 as input pullup. We need the pullup to define a stable
state when the button is not pressed. Now look in the tabular, you should
see that you can change the value of the pin by toggling the button.

If you don't have a button or a LED you can try to measure voltages with
a voltage meter or connect a pin with GND or VCC to see changes in the
Brick Viewer.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <io4_programming_interfaces>` section for 
the API of the IO4 Bricklet and examples in different programming languages.

.. _io4_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: IO4_hlpi.table
