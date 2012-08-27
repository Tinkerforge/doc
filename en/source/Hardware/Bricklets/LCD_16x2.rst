.. _lcd_16x2_bricklet:

LCD 16x2 Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_lcd_16x2_tilted_350.jpg",
	               "Bricklets/bricklet_lcd_16x2_tilted_600.jpg",
	               "LCD 16x2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_16x2_apart_100.jpg",
	             "Bricklets/bricklet_lcd_16x2_apart_600.jpg",
	             "LCD 16x2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_16x2_display_100.jpg",
	             "Bricklets/bricklet_lcd_16x2_display_600.jpg",
	             "LCD 16x2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_16x2_master_100.jpg",
	             "Bricklets/bricklet_lcd_16x2_master_600.jpg",
	             "LCD 16x2 Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd_16x2_brickv_100.jpg",
	             "Bricklets/bricklet_lcd_16x2_brickv.jpg",
	             "LCD 16x2 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/lcd_16x2_bricklet_dimensions_100.png",
	             "Dimensions/lcd_16x2_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 16x2 alphanumeric display
* Switchable blue backlight
* 3 push-buttons


Description
-----------

This LCD :ref:`Bricklet <product_overview_bricklets>` is equipped with a
16x2 alphanumeric character display with blue backlight and three push-buttons.
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
LCD                                  Alphanumeric, 16 chars per line, 2 lines
Current Consumption with Backlight   28mA
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Backlight                            Blue, software switchable
Contrast                             Adjustable with potentiometer
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Dimensions                           31 x 80 x 22mm (1.22 x 3.15 x 0.86")*
Weight                               51g*
===================================  ============================================================
\* without screws


Resources
---------

* LCD charset (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/standard_charset.pdf>`__)
* LCD datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/el1602a.pdf>`__)
* KS0066U datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/KS0066u.pdf>`__)
* MCP23017 datasheet (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/raw/master/hardware/lcd-16x2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/lcd_16x2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/lcd-16x2-bricklet/zipball/master>`__)


Change LCD's contrast
---------------------

To modify the contrast you have to
turn the potentiometer on the Bricklet with a screwdriver.
The potentiometer is attached next to the Bricklet connector.


.. _lcd_16x2_bricklet_test:

Test your LCD 16x2 Bricklet
---------------------------

To test the LCD 16x2 Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the LCD 16x2 Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable
(see picture below).

.. image:: /Images/Bricklets/bricklet_lcd_16x2_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected LCD 16x2 Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_16x2_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named
"LCD 16x2 Bricklet" in the Brick Viewer after you pressed "connect". Select it.
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_lcd_16x2_brickv.jpg
   :scale: 100 %
   :alt: LCD 16x2 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_16x2_brickv.jpg

Input a string into the text field.
You can choose the line and the start position at which the text is displayed.
Press "Send Text" to display it. Press "Backlight On" to turn the backlight on.
Play around with the three on-board buttons and look how their values change.

After this test you can go on with writing your own application.
See the :ref:`Programming Interface <lcd_16x2_programming_interfaces>` section
for the API of the LCD 16x2 Bricklet and examples in different
programming languages.



.. _lcd_16x2_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: LCD_16x2_hlpi.table
