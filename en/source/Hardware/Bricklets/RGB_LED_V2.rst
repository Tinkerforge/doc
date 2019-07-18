
:shoplink: ../../../shop/bricklets/rgb-led-v2-bricklet.html

.. include:: RGB_LED_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_v2_bricklet:

RGB LED Bricklet 2.0
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_v2_tilted_[?|?].jpg           RGB LED Bricklet 2.0
	Bricklets/bricklet_rgb_led_v2_top_[?|?].jpg              RGB LED Bricklet 2.0
	Bricklets/bricklet_rgb_led_v2_bright_vs_dark_[?|?].jpg   RGB LED Bricklet 2.0
	Bricklets/bricklet_rgb_led_v2_brickv_[100|].jpg          RGB LED Bricklet 2.0 in Brick Viewer
	Dimensions/rgb_led_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 1x RGB LED
* 24 bit color resolution
* Luminance output is corrected for human light perception (CIE 1931)

.. _rgb_led_v2_bricklet_description:

Description
-----------

The RGB LED :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to control a RGB LED. Each of the three channels
(red, green, blue) can be controlled individually with 8 bit resolution.

The luminance output of the LED is corrected for human light perception
with accordance to CIE 1931. This means that for every color a fade from 
off to full brightness (value 0 to 255) will appear to be a smooth color 
gradient to the human eye.

The RGB LED Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="400px" height="auto" controls loop>
	  <source src="../../_images/Videos/bricklet_rgb_led_v2_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_rgb_led_v2_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_rgb_led_v2_video.webm" type="video/webm">
	</video>


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
LED                               QBLP679E-RGB
Current Consumption               | Off: 35mW (7mA at 5V)
                                  | White: 180mW (36mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Luminous intensity (R, G, B)      400-630mcd, 1000-1500mcd, 200-285mcd
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            3g
================================  ============================================================


Resources
---------

* QBLP679E-RGB datasheet (`Download <https://github.com/Tinkerforge/rgb-led-v2-bricklet/raw/master/datasheets/QBLP679E-RGB.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/rgb-led-v2-bricklet/raw/master/hardware/rgb-led-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rgb_led_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rgb-led-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/30ouYWQ>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/rgb_led_v2/rgb-led-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/rgb_led_v2/rgb-led-v2.FCStd>`__)


.. _rgb_led_v2_bricklet_test:

Test your RGB LED Bricklet 2.0
------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now control the RGB LED color with
different sliders:

.. image:: /Images/Bricklets/bricklet_rgb_led_v2_brickv.jpg
   :scale: 100 %
   :alt: RGB LED Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_v2_brickv.jpg

|test_pi_ref|



.. _rgb_led_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RGB_LED_V2_hlpi.table
