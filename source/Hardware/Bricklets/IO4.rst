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
Update frequency                  
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

* attach led and switch

For a simple test connect your Ambient Light Sensor to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

After installing our software (Brickd, Brickv) you can see the connected Ambient
Light Bricklet in the Brickv.

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

Click on the Ambient Light tab and see how the measured values change dependend 
on device illumination. You can now go on with writing your own application.
See :ref:`Interface and Coding <ambl_programming_interfaces>` section for the API of
the Ambient Light Bricklet and examples in your programming language.


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


