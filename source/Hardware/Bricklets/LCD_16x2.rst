.. _lcd_16x2_bricklet:

LCD 16x2
========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_16x2_tilted_350.jpg", 
	             "Bricklets/bricklet_lcd_16x2_tilted_100.jpg", 
	             "Bricklets/bricklet_lcd_16x2_tilted_800.jpg", 
	             "LCD 16x2 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_16x2_apart_350.jpg", 
	             "Bricklets/bricklet_lcd_16x2_apart_100.jpg", 
	             "Bricklets/bricklet_lcd_16x2_apart_800.jpg", 
	             "LCD 16x2 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_16x2_display_350.jpg", 
	             "Bricklets/bricklet_lcd_16x2_display_100.jpg", 
	             "Bricklets/bricklet_lcd_16x2_display_800.jpg", 
	             "LCD 16x2 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_16x2_master_350.jpg", 
	             "Bricklets/bricklet_lcd_16x2_master_100.jpg", 
	             "Bricklets/bricklet_lcd_16x2_master_800.jpg", 
	             "LCD 16x2 Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_16x2_brickv_350.jpg", 
	             "Bricklets/bricklet_lcd_16x2_brickv_100.jpg", 
	             "Bricklets/bricklet_lcd_16x2_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/lcd_16x2_bricklet_dimensions_350.png", 
	             "Dimensions/lcd_16x2_bricklet_dimensions_100.png", 
	             "Dimensions/lcd_16x2_bricklet_dimensions.png", 
	             "Outline and drilling plan") 
	}}
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

===================================  ============================================================
Property                             Value
===================================  ============================================================
Dimensions                           80mm x 31mm (3.15" x 1.22")
Weight                               51.4g (w/o screws)
Current Consumption with Backlight   28mA
LCD                                  Alphanummeric, 16 chars per line, 2 lines
Backlight                            Blue, software switchable on/off
Contrast                             Contrast voltage adjustable with potentiometer
===================================  ============================================================

Resources
---------

* LCD Datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/el1602a.pdf>`__)
* LCD Controller KS0066U Datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/KS0066u.pdf>`__)
* MCP23017 Datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/hardware/lcd-16x2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/lcd_16x2_bricklet_dimensions.png>`__)
* Project (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__



Change LCD's contrast
---------------------

Depending on your power supply it might be possible that the contrast
of the LCD is not as you wish. To modify it you have to take
a screwdriver and turn the potentiometer on the bricklet.
The potentiometer is attached beside the Bricklet connector.


.. _lcd_16x2_bricklet_test:

Test your LCD 16x2 Bricklet
---------------------------

To test your LCD 16x2 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(see :ref:`here <tools_installation_brickdv>` for an installation tutorial).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect your LCD 16x2 Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable 
(see picture below).

.. image:: /Images/Bricks/Servo_Brick/servo_brick_test.jpg
   :scale: 100 %
   :alt: Master Brick with connected LCD 16x2 Bricklet
   :align: center
   :target: ../../_images/Bricklets/current12_brickv.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"LCD 16x2 Bricklet" in the Brick Viewer after you pressed "connect", select it.
If everything went as expected you the Brick Viewer should look like
depicted below.

.. image:: /Images/Bricklets/lcd_16x2_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the LCD 16x2 Bricklet
   :align: center
   :target: ../../_images/Bricklets/lcd_16x2_brickv.jpg

Input an string to the text field.
You can choose the line and the start position at which the text is displayed.
Press "Send Text" to display it. Press "Backlight On" such that you can read
the LCD easier. Play around with the three onboard buttons and look 
how their values changes.

After this short test you can go on with writing your own application.
See :ref:`Interface and Coding <lcd_16x2_programming_interfaces>` section for the API of
the LCD 16x2 Bricklet and examples in your programming language.



.. _lcd_16x2_programming_interfaces:

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



