.. _lcd_16x2_bricklet:

LCD 16x2
========


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

This LCD :ref:`Bricklet <product_overview_bricklets>` is equipped with a
16x2 alphanummeric chars display with blue backlight and three push buttons. 
You can control it by connecting it to a :ref:`Brick <product_overview_bricks>`.
The API lets you write chars or lines to the LCD, get the state of each button,
switch the backlight on or off and configure events for each button.

You can use this bricklet to display any information you like to.
For example you can use it to display song information on your PC or 
measured values from other bricklets.



Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        80mm x 31mm (3.15" x 1.22")
Weight
LCD                               Alphanummeric, 16 chars per line, 2 lines
Backlight                         Blue, software switchable on/off
Contrast                          Contrast voltage adjustable with potentiometer
================================  ============================================================

Resources
---------

* LCD Datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/el1602a.pdf>`__)
* LCD Controller KS0066U Datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/KS0066u.pdf>`__)
* MCP23017 Datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/hardware/lcd-16x2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/lcd_16x2_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



.. _lcd_16x2_bricklet_test:

Test your LCD 16x2 Bricklet
---------------------------

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

Contrast



.. _lcd16x2_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <lcd_16x2_bricklet_c_api>`", ":ref:`Examples <lcd_16x2_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <lcd_16x2_bricklet_csharp_api>`", ":ref:`Examples <lcd_16x2_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <lcd_16x2_bricklet_java_api>`", ":ref:`Examples <lcd_16x2_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <lcd_16x2_bricklet_python_api>`", ":ref:`Examples <lcd_16x2_bricklet_python_examples>`", "Installation"



