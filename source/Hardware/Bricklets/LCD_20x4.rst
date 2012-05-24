.. _lcd_20x4_bricklet:

LCD 20x4 Bricklet
=================


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricklets/bricklet_lcd_20x4_tilted_350.jpg", 
	             "Bricklets/bricklet_lcd_20x4_tilted_600.jpg", 
	             "LCD 20x4 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_20x4_apart_100.jpg", 
	             "Bricklets/bricklet_lcd_20x4_apart_600.jpg", 
	             "LCD 20x4 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_20x4_display_100.jpg", 
	             "Bricklets/bricklet_lcd_20x4_display_600.jpg", 
	             "LCD 20x4 Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_20x4_master_100.jpg", 
	             "Bricklets/bricklet_lcd_20x4_master_600.jpg", 
	             "LCD 20x4 Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_lcd_20x4_brickv_100.jpg", 
	             "Bricklets/bricklet_lcd_20x4_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/lcd_20x4_bricklet_dimensions_100.png", 
	             "Dimensions/lcd_20x4_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * Alphanumeric character display with 20x4 characters
 * Switchable blue backlight
 * 3 push buttons

Description
-----------

This LCD :ref:`Bricklet <product_overview_bricklets>` is equipped with a
20x4 alphanumeric character display with blue backlight and three push buttons.
It can be controlled with :ref:`Bricks <product_overview_bricks>`.
The API allows to write characters to the LCD, get the state of the buttons,
switch the backlight on or off and configure events for the buttons.

You can use this Bricklet to display text, for example a name of
a song that is played on your PC or measurements from other Bricklets.

Technical Specifications
------------------------

===================================  ============================================================
Property                             Value
===================================  ============================================================
Dimensions                           98mm x 60mm (3.86" x 2.36")
Weight                               96.0g (w/o screws)
Current Consumption with Backlight   36mA
LCD                                  Alphanumeric, 20 chars per line, 4 lines
Backlight                            Blue, software switchable on/off
Contrast                             Contrast voltage adjustable with potentiometer
===================================  ============================================================

Resources
---------

* LCD Charset (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/standard_charset.pdf>`__)
* LCD Controller KS0066U Datasheet (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/KS0066u.pdf>`__)
* MCP23017 Datasheet (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/hardware/lcd-20x4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/lcd_20x4_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/zipball/master>`__)


Change LCD's contrast
---------------------

To modify the contrast you have to 
turn the potentiometer on the Bricklet with a screwdriver.
The potentiometer is attached next to the Bricklet connector.


.. _lcd_20x4_bricklet_test:

Test your LCD 20x4 Bricklet
---------------------------

To test the LCD 20x4 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the LCD 20x4 Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable 
(see picture below).

.. image:: /Images/Bricklets/bricklet_lcd_20x4_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected LCD 20x4 Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_20x4_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"LCD 20x4 Bricklet" in the Brick Viewer after you pressed "connect". Select it.
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_lcd_20x4_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of the LCD 20x4 Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_20x4_brickv.jpg

Input a string into the text field.
You can choose the line and the start position at which the text is displayed.
Press "Send Text" to display it. Press "Backlight On" to turn the backlight on.
Play around with the three on-board buttons and look how their values change.

After this test you can go on with writing your own application.
See the :ref:`Programming Interface <lcd_20x4_programming_interfaces>` section 
for the API of the LCD 20x4 Bricklet and examples in different 
programming languages.



.. _lcd_20x4_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: LCD_20x4_hlpi.table
