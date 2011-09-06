.. _io4_bricklet:

IO4
===


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #0") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #1") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #2") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #3") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #4") }}
	{{ tfdocimg("Bricklets/test.jpg", "test_k.jpg", "Bricklets/test.jpg", "Title #5") }}
	{{ tfdocend() }}


Description
-----------

With the IO4 :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by external digital inputs 
and outputs.

The bricklet features 1x4 pins which can be independently configured as
digital inputs or outputs. Each input pin can additionally be configured with
pullups or as interrupt source. 
Via terminal blocks all signals can be accessed.
A single terminal block deliver the switched output voltage and GND. 

Human interfaces are typical applications of this bricklet since switches, push-bottons and
LEDs can be easily connected.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        25mm x 25mm (0.98" x 0.98")
Weight
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Number of I/Os                    1x8
I/O voltages                      Fixed 3.3V
================================  ============================================================

Resources
---------

* MCP23017 Datasheet (`Download <https://github.com/Tinkerforge/io16-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/io4-bricklet/raw/master/hardware/io-4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/io4_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/io4-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



.. _io4_bricklet_test:

Test your IO4 Bricklet
----------------------

To test your IO4 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect your IO4 Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable.
Connect an LED with series resistor to the board
by attaching the anode to pin 0 and the cathode to one GND pin.
Additonally connect a button which can short pin 1 to GND
(see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Master Brick with connected IO4 Bricklet
   :align: center
   :target: ../../_images/Bricklets/current12_brickv.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"IO4 Bricklet" in the Brick Viewer after you pressed “connect”, select it.

.. image:: /Images/Bricklets/io4_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the IO4 Bricklet
   :align: center
   :target: ../../_images/Bricklets/io4_brickv.jpg


in this tab you can change the "Debounce Period", 
it is the period for interrupt callbacks. 
For example: If you set this value to 100, you will get interrupts
maximal every 100ms. This is necessary if something that bounces is
connected to the IO4 Bricklet, such as a button. You can test the optimal
value in the Brick Viewer such that you can use this value later in your
own program.

Below the debounce period configuration you can configure the pins.
Each pin can be configured as input/output and in case of an input pin 
the pullup option.
Simply choose a port and a pin configure the direction and value and press 
save. The current state is depicted in the tabular below.

For example lets test the LED. Configure pin 0 as output and change 
the value. When the pin is high the LED should light. To test the button 
configure pin 1 as input pullup. We need the pullup to define a stable
state when the button is not pressed. Now look in the tabular, you should
see that you can change the value of the pin by pressing the button.

After this you can go on with writing your own application.
See :ref:`Interface and Coding <io4_programming_interfaces>` section for the API of
the IO4 Bricklet and examples in your programming language.

.. _io4_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <io4_bricklet_c_api>`", ":ref:`Examples <io4_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <io4_bricklet_csharp_api>`", ":ref:`Examples <io4_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <io4_bricklet_java_api>`", ":ref:`Examples <io4_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <io4_bricklet_python_api>`", ":ref:`Examples <io4_bricklet_python_examples>`", "Installation"


