
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / RGB LED Bricklet
:shoplink: ../../../shop/bricklets/rgb-led-bricklet.html

.. include:: RGB_LED.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_bricklet:

RGB LED Bricklet
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_tilted_[?|?].jpg           RGB LED Bricklet
	Bricklets/bricklet_rgb_led_vertical_[?|?].jpg         RGB LED Bricklet
	Bricklets/bricklet_rgb_led_brickv_[100|].png          RGB LED Bricklet in Brick Viewer
	Dimensions/rgb_led_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}



Features
--------

* 1x RGB LED
* 24 bit color resolution

.. _rgb_led_bricklet_description:

Description
-----------

The RGB LED :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to control a RGB LED. Each of the three channels
(red, green, blue) can be controlled individually with 8 bit resolution.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
LED                               WS2812B
Current Consumption               | Black: 25mW (5mA at 5V)
                                  | White: 225mW (45mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Luminous intensity (R, G, B)      390-420mcd, 660-720mcd, 180-200mcd
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")*
Weight                            2g
================================  ============================================================

\* Because of a lack of attention on our part the RGB LED Bricklet
with hardware version 1.0 was produced with a size of
25 x 17.5 x 5mm (0.98 x 0.69 x 0.19"). It is was unfortunately not in
our standard 5mm grid. This was fixed with version 1.1.

Resources
---------

* WS2812B datasheet (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/raw/master/datasheets/WS2812B.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/raw/master/hardware/rgb-led-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rgb_led_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rgb-led-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2iW4cAV>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/rgb_led/rgb-led.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/rgb_led/rgb-led.FCStd>`__)

.. _rgb_led_bricklet_test:

Test your RGB LED Bricklet
--------------------------

|test_intro|

|test_connect|.

|test_tab|


.. image:: /Images/Bricklets/bricklet_rgb_led_brickv.png
   :scale: 100 %
   :alt: RGB LED Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_brickv.png

If everything went as expected you can now control the RGB LED color with
different sliders:

.. image:: /Images/Bricklets/bricklet_rgb_led_animation.gif
   :scale: 100 %
   :alt: RGB LED Bricklet animation
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_animation.gif


|test_pi_ref|


.. _rgb_led_bricklet_case:

Case
----

Coming soon...

.. _rgb_led_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RGB_LED_hlpi.table
