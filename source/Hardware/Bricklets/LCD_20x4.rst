.. _lcd_20x4_bricklet:

LCD 20x4
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
20x4 alphanummeric chars display with blue backlight and three push buttons. 
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
Dimensions                        98mm x 60mm (3.86" x 2.36")
Weight
LCD                               Alphanummeric, 20 chars per line, 4 lines
Backlight                         Blue, software switchable on/off
Contrast                          Contrast voltage adjustable with potentiometer
================================  ============================================================

Resources
---------

* LCD Controller KS0066U Datasheet (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/KS0066u.pdf>`__)
* MCP23017 Datasheet (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/hardware/lcd-20x4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/lcd_20x4_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__


Change LCD's contrast
---------------------

Depending on your power supply it might be possible that the contrast
of the LCD is not as you wish. To modify it you have to take
a screwdriver and turn the potentiometer on the bricklet.
The potentiometer is attached beside the Bricklet connector.


.. _lcd_20x4_bricklet_test:

Test your LCD 20x4 Bricklet
---------------------------

For a simple test connect your LCD 20x4 Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Master Brick with connected LCD 20x4 Bricklet
   :align: center

After installing our software (Brickd, Brickv) you can see the connected LCD
20x4 Bricklet in the Brickv.

.. image:: /Images/Bricklets/lcd_20x4_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the LCD 20x4 Bricklet
   :align: center

Click on the LCD 20x4 tab and input an string to the text field.
You can choose the line and the start position at which the text is displayed.
Press "Send Text" to display it. Press "Backlight On" such that you can read
the LCD easier. Play around with the three onboard buttons and look 
how their values changes.

After this short test you can go on with writing your own application.
See :ref:`Interface and Coding <lcd20x4_programming_interfaces>` section for the API of
the LCD 20x4 Bricklet and examples in your programming language.


.. _lcd20x4_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <lcd_20x4_bricklet_c_api>`", ":ref:`Examples <lcd_20x4_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <lcd_20x4_bricklet_csharp_api>`", ":ref:`Examples <lcd_20x4_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <lcd_20x4_bricklet_java_api>`", ":ref:`Examples <lcd_20x4_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <lcd_20x4_bricklet_python_api>`", ":ref:`Examples <lcd_20x4_bricklet_python_examples>`", "Installation"


