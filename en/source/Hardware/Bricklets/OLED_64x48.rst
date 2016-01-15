
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / OLED 64x48 Bricklet
:shoplink: ../../../shop/bricklets/oled-64x48-bricklet.html

.. include:: OLED_64x48.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _oled_64x48_bricklet:

OLED 64x48 Bricklet
===================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_oled_64x48_tilted_[?|?].jpg           OLED 64x48 Bricklet
	Bricklets/bricklet_oled_64x48_front_[?|?].jpg            OLED 64x48 Bricklet
	Bricklets/bricklet_oled_64x48_horizontal_[?|?].jpg       OLED 64x48 Bricklet
	Bricklets/bricklet_oled_64x48_bottom_[?|?].jpg           OLED 64x48 Bricklet
	Bricklets/bricklet_oled_64x48_brickv_[100|].jpg          OLED 64x48 Bricklet in Brick Viewer
	Bricklets/bricklet_oled_font_[100|314].png               OLED 64x48 Bricklet font
	Dimensions/oled_64x48_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Black/white OLED
* Size of 1.68cm (0.66") with a resolution of 64x48

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

A `demo <https://github.com/Tinkerforge/oled-128x64-bricklet/blob/master/software/examples/python/example_draw_servo_poti.py>`__
with the 128x64 pixel version, a Servo Brick and a Rotary Poti Bricklet
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
Size                              1.68cm (0.66")
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
also possible to show the available character set on the OLED.

.. image:: /Images/Bricklets/bricklet_oled_64x48_brickv.jpg
   :scale: 100 %
   :alt: OLED 64x48 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_oled_64x48_brickv.jpg

|test_pi_ref|

Usage
-----

Unfortunately Bricklets only have a very limited amount of RAM (256 Byte)
and flash (4096 Byte) available. This is not enough to for example cache a
whole 64x48 b/w image. Therefore we can not offer convenient APIs like
``draw_line(x1, y1, x2, y2)``.

To draw to the display we recommend that you use an image library that is
native to your programming language (for example PIL for Python). This
way you can use all of the available drawing primitives and fonts of the
library and then copy the image buffer to the Bricklet.

We provide examples for

* `C# <https://raw.githubusercontent.com/Tinkerforge/oled-64x48-bricklet/master/software/examples/csharp/ExampleScribble.cs>`__,
* `Java <https://raw.githubusercontent.com/Tinkerforge/oled-64x48-bricklet/master/software/examples/java/ExampleScribble.java>`__,
* `JavaScript (Node.js) <https://raw.githubusercontent.com/Tinkerforge/oled-64x48-bricklet/master/software/examples/javascript/ExampleScribble.js>`__
  (with `gm <https://www.npmjs.com/package/gm>`__ and `get-pixels <https://www.npmjs.com/package/get-pixels>`__) and
* `Python <https://raw.githubusercontent.com/Tinkerforge/oled-64x48-bricklet/master/software/examples/python/example_scribble.py>`__
  (with `PIL <https://python-pillow.github.io/>`__).

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
