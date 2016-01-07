
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / OLED 64x48 Bricklet
:shoplink: ../../../shop/bricklets/oled-64x48-bricklet.html

.. include:: OLED_64x48.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _oled_64x48_bricklet:

OLED 64x48 Bricklet
===================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_oled_64x48_tilted_350.jpg",
	               "Bricklets/bricklet_oled_64x48_tilted_600.jpg",
	               "OLED 64x48 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_64x48_front_100.jpg",
	             "Bricklets/bricklet_oled_64x48_front_600.jpg",
	             "OLED 64x48 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_64x48_horizontal_100.jpg",
	             "Bricklets/bricklet_oled_64x48_horizontal_600.jpg",
	             "OLED 64x48 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_64x48_bottom_100.jpg",
	             "Bricklets/bricklet_oled_64x48_bottom_600.jpg",
	             "OLED 64x48 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_64x48_brickv_100.jpg",
	             "Bricklets/bricklet_oled_64x48_brickv.jpg",
	             "OLED 64x48 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_oled_font_100.png",
	             "Bricklets/bricklet_oled_font_314.png",
	             "OLED 64x48 Bricklet font")
	}}
	{{
	    tfdocimg("Dimensions/oled_64x48_bricklet_dimensions_100.png",
	             "Dimensions/oled_64x48_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Black/white OLED
* Size of 0.66" with a resolution of 64x48

.. _oled_64x48_bricklet_description:

Description
-----------

The OLED 64x48 :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to display information on a small 64x48
`OLED display <https://en.wikipedia.org/wiki/OLED>`__.

Because each pixel can be set individually, the display can do graphics. This
allows for more versatile and detailled drawings on the display, compared to
the :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>` with its fixed character
display.

Additionally, text can easily be drawn onto the display with the embedded
:ref:`font <oled_64x48_bricklet_font>` of the Bricklet.

High update rates of up to 100Hz are possible.

A demo with the 128x64 pixel version, a Servo Brick and a Rotary Poti Bricklet
is available on Youtube:

.. raw:: html

 <center><iframe width="640" height="360" src="http://www.youtube-nocookie.com/embed/8RSEs6cKwXc" frameborder="0" allowfullscreen></iframe></center>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               | 10mW (2mA at 5V, all pixels black)
                                  | 110mW (22mA at 5V, all pixels white)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        64x48 pixel, 13x6 characters
Size                              0.66"
Colors                            Black/White
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 20 x 7mm (1.38 x 0.79 x 0.28")
Weight                            4g
================================  ============================================================


Resources
---------

* Display datasheet (`Download <https://github.com/Tinkerforge/oled-64x48-bricklet/raw/master/datasheets/OLED_64X48_Datasheet.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/oled-64x48-bricklet/raw/master/hardware/oled-64x48-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/oled_64x48_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/oled-64x48-bricklet/zipball/master>`__)


.. _oled_64x48_bricklet_test:

Test your OLED 64x48 Bricklet
-----------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

You can draw and write text to the display. With the slider it is
also possible to show the available character set on the the OLED.

.. image:: /Images/Bricklets/bricklet_oled_64x48_brickv.jpg
   :scale: 100 %
   :alt: OLED 64x48 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_oled_64x48_brickv.jpg

|test_pi_ref|

.. _oled_64x48_bricklet_font:

Font
----

The Bricklet has an embedded font (ASCII subset in green) that allows fast and
easy text rendering (up to 13x6 characters):

.. image:: /Images/Bricklets/bricklet_oled_font.png
   :scale: 100 %
   :alt: OLED 64x48 Bricklet font
   :align: center
   :target: ../../_images/Bricklets/bricklet_oled_font.png

.. _oled_64x48_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: OLED_64x48_hlpi.table
