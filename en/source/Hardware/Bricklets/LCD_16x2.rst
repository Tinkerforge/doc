
.. include:: LCD_16x2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _lcd_16x2_bricklet:

LCD 16x2 Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_lcd_16x2_tilted_[?|?].jpg           LCD 16x2 Bricklet
	Bricklets/bricklet_lcd_16x2_apart_[100|600].jpg        LCD 16x2 Bricklet
	Bricklets/bricklet_lcd_16x2_display_[100|600].jpg      LCD 16x2 Bricklet
	Bricklets/bricklet_lcd_16x2_master_[100|600].jpg       LCD 16x2 Bricklet with Master Brick
	Bricklets/bricklet_lcd_16x2_brickv_[100|].jpg          LCD 16x2 Bricklet in Brick Viewer
	Dimensions/lcd_16x2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The LCD 16x2 Bricklet is discontinued and is no longer sold. The
 :ref:`LCD 128x64 Bricklet <lcd_128x64_bricklet>` is the recommended replacement.


Features
--------

* 16x2 character alphanumeric display
* Switchable blue backlight
* 3 push-buttons


.. _lcd_16x2_bricklet_description:

Description
-----------

This LCD :ref:`Bricklet <primer_bricklets>` is equipped with a
16x2 character alphanumeric display with blue backlight and three push-buttons.
It can be controlled with :ref:`Bricks <primer_bricks>`.
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


.. _lcd_16x2_bricklet_test:

Test your LCD 16x2 Bricklet
---------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_lcd_16x2_master_600.jpg
   :scale: 100 %
   :alt: LCD 16x2 Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_16x2_master_1200.jpg

|test_tab|
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

|test_pi_ref|


Change LCD's contrast
---------------------

To modify the contrast you have to
turn the potentiometer on the Bricklet with a screwdriver.
The potentiometer is attached next to the Bricklet connector.

.. _lcd_16x2_bricklet_font:

Font
----

The Bricklet has an embedded font (ASCII subset in green) that allows fast and
easy text rendering (up to 16x2 characters):

.. image:: /Images/Bricklets/bricklet_lcd_16x2_font.png
   :scale: 100 %
   :alt: LCD 16x2 Bricklet font
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_16x2_font.png


.. _lcd_16x2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: LCD_16x2_hlpi.table
