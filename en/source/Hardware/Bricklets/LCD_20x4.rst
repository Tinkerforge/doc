
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#bricklets">Bricklets</a> / LCD 20x4 Bricklet
:shoplink: ../../../shop/bricklets/lcd20x4-bricklet.html

.. include:: LCD_20x4.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _lcd_20x4_bricklet:

LCD 20x4 Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_lcd12_20x4_tilted_350.jpg",
	               "Bricklets/bricklet_lcd12_20x4_tilted_600.jpg",
	               "LCD 20x4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_lcd12_20x4_top_100.jpg",
	             "Bricklets/bricklet_lcd12_20x4_top_600.jpg",
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
	             "LCD 20x4 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/lcd_20x4_bricklet_dimensions_100.png",
	             "Dimensions/lcd_20x4_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 20x4 character alphanumeric display
* Switchable blue backlight
* 4 push-buttons


Description
-----------

This LCD :ref:`Bricklet <product_overview_bricklets>` is equipped with a
20x4 character alphanumeric display with blue backlight and four push-buttons.
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
LCD                                  Alphanumeric, 20 chars per line, 4 lines
Current Consumption with Backlight   36mA
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Backlight                            Blue, software switchable
Contrast                             Adjustable with potentiometer
-----------------------------------  ------------------------------------------------------------
-----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)               60 x 98 x 22mm (2.36 x 3.86 x 0.86")*
Weight                               96g*
===================================  ============================================================

\* without screws


Resources
---------

* LCD charset (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/standard_charset.pdf>`__)
* KS0066U datasheet (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/KS0066u.pdf>`__)
* MCP23017 datasheet (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/datasheets/MCP23017.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/raw/master/hardware/lcd-20x4-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/lcd_20x4_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/lcd-20x4-bricklet/zipball/master>`__)


.. _lcd_20x4_bricklet_test:

Test your LCD 20x4 Bricklet
---------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_lcd_20x4_master_600.jpg
   :scale: 100 %
   :alt: LCD 20x4 Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_20x4_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_lcd_20x4_brickv.jpg
   :scale: 100 %
   :alt: LCD 20x4 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_lcd_20x4_brickv.jpg

Input a string into the text field.
You can choose the line and the start position at which the text is displayed.
Press "Send Text" to display it. Press "Backlight On" to turn the backlight on.
Play around with the four on-board buttons and look how their values change.

|test_pi_ref|


Change LCD's contrast
---------------------

To modify the contrast you have to
turn the potentiometer on the Bricklet with a screwdriver.
The potentiometer is attached next to the Bricklet connector.


Attach external Buttons
-----------------------

The LCD Bricklet can be equipped with a pin header on the right hand side.
To attach a switch or a button you have to connect on pin
with one input (BTN0 to BTN3) and the other with GND.


.. _lcd_20x4_bricklet_case:

Case
----

A `laser-cut case for the LCD 20x4 Bricklet <https://www.tinkerforge.com/en/shop/cases/case-lcd-20x4-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_lcd_20x4_case_350.jpg
   :scale: 100 %
   :alt: Case for LCD 20x4 Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_lcd_20x4_case_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw LCD to top plate with spacers (10mm) at the bottom and long screws from the top,
* screw Bricklet to LCD with spacers (12mm),
* build up side plates,
* add button extensions to side plate,
* plug side plates into top plate and
* screw bottom plate to bottom spacers.

Below you can see an exploded assembly drawing of the LCD 20x4 Bricklet case:

.. image:: /Images/Exploded/lcd20x4_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für LCD 20x4 Bricklet
   :align: center
   :target: ../../_images/Exploded/lcd20x4_exploded.png

|bricklet_case_hint|

.. _lcd_20x4_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: LCD_20x4_hlpi.table
