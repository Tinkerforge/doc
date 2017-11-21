:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / RGB LED Button Bricklet
:FIXME_shoplink: ../../../shop/bricklets/rgb-led-button-bricklet.html

.. include:: RGB_LED_Button.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_button_bricklet:

RGB LED Button Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_button_tilted_[?|?].jpg           RGB LED Button Bricklet
	Bricklets/bricklet_rgb_led_button_bottom_[?|?].jpg           RGB LED Button Bricklet bottom
	Bricklets/bricklet_rgb_led_button_top_[?|?].jpg              RGB LED Button Bricklet top
	Bricklets/bricklet_rgb_led_button_finger_[?|?].jpg           RGB LED Button Bricklet with finger
	Bricklets/bricklet_rgb_led_button_brickv_[100|].jpg          RGB LED Button Bricklet in Brick Viewer
	Dimensions/rgb_led_button_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 Shop entry as well as Brick Viewer and Bindings support for the RGB LED Button Bricklet
 will be released on Tuesday, November 21st at the latest. Thank you for your 
 patience!

Features
--------

* High quality 15mm x 15mm button
* Adjustable RGB LED backlight
* Replacable/user-printable cap inlay 


.. _rgb_led_button_bricklet_description:

Description
-----------

The RGB LED :ref:`Bricklet <primer_bricklets>` is eqiupped with an adjustable
RGB backlit button. It can extend :ref:`Bricks <primer_bricks>`.

You can read the current state of the button (pressed/released) and
adjust the color of the LED. The red, green and blue part of the LED can be 
controlled with 8 bit resolution each.

A white inlay is attached below the cap. This paper inlay can be replaced by a
custom printed inlay (for example a power sign or an arrow or similar).

It is also possible to use events. This allows to react to button presses
without polling.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_rgb_led_button_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_rgb_led_button_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_rgb_led_button_video.webm" type="video/webm">
	</video> 

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption (LEDs off)    31mW (6.2mA at 5V)
Current Consumption (LEDs on)     207mW (41.4mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
LED Resolution                    8 bit
Inlay size                        14 x 14mm
Button size                       15 x 15mm
Cap size                          17.4 x 17.4mm
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 25 x 30mm (0.98 x 0.98 x 1.18")
Weight                            7g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/rgb-led-button-bricklet/raw/master/hardware/rgb-led-button-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rgb_led_button_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rgb-led-button-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2zqJEtU>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/rgb_led_button/rgb-button-bricklet.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/rgb_led_button/rgb-button-bricklet.FCStd>`__)


Button Inlay
------------

The RGB LED Button Bricklet consists of four parts:

* Bricklet with button and RGB LED,
* White cap,
* Inlay (optional, 14x14mm) and
* Transparent cap.

.. image:: /Images/Bricklets/bricklet_rgb_led_button_disassembled_800.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklet disassembled
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_button_disassembled_1200.jpg

You can easily print your own inlays (size for perfect fit is 14x14mm). Put them between the 
white and the transparent cap.

For best results you can print the inlay on a transparent foil. A simple piece
of white paper works too, but the LED brightness decreases a little bit.

Below you can find an example of three RGB LED Button Bricklets with different inlays with
and without ambient light. The symbol inlays were printed by a laser printer on 
transparent foil.

.. image:: /Images/Bricklets/bricklet_rgb_led_button_3on_bright_600.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklets with inlays
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_button_3on_bright_1000.jpg

.. image:: /Images/Bricklets/bricklet_rgb_led_button_3on_dark_600.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklets with inlays in darkness
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_button_3on_dark_1000.jpg


.. _rgb_led_button_bricklet_test:

Test your RGB LED Button Bricklet
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
You can now see button presses in the GUI and control the backlight RGB LED.

.. image:: /Images/Bricklets/bricklet_rgb_led_button_brickv.jpg
   :scale: 100 %
   :alt: RGB LED Button Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_button_brickv.jpg

|test_pi_ref|


.. _rgb_led_button_bricklet_case:

Case
----

Coming soon...

..
	A `laser-cut case for the RGB LED Button Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-rgb-led-button-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_rgb_led_button_case_350.jpg
	   :scale: 100 %
	   :alt: Case for RGB LED Button Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_rgb_led_button_case_1000.jpg

	.. include:: RGB_LED_Button.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/rgb_led_button_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for RGB LED Button Bricklet
	   :align: center
	   :target: ../../_images/Exploded/rgb_led_button_exploded.png

	|bricklet_case_hint|


.. _rgb_led_button_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RGB_LED_Button_hlpi.table
