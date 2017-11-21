:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / RGB LED Matrix Bricklet
:shoplink: ../../../shop/bricklets/rgb-led-matrix-bricklet.html

.. include:: RGB_LED_Matrix.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rgb_led_matrix_bricklet:

RGB LED Matrix Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rgb_led_matrix_tilted_[?|?].jpg           RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_w_cable_[?|?].jpg          RGB LED Matrix Bricklet with cable
	Bricklets/bricklet_rgb_led_matrix_rainbow_[?|?].jpg          RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_horizontal_[?|?].jpg       RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_detail_[?|?].jpg           RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_w_power_[?|?].jpg          RGB LED Matrix Bricklet
	Bricklets/bricklet_rgb_led_matrix_brickv_[100|].jpg          RGB LED Matrix Bricklet in Brick Viewer
	Dimensions/rgb_led_matrix_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 8x8 RGB LED Matrix
* Each pixel individually controllable
* Each pixel has 8 bit resolution for red, green and blue
* Input voltage can be monitored


.. _rgb_led_matrix_bricklet_description:

Description
-----------

The RGB LED Matrix :ref:`Bricklet <primer_bricklets>` is equipped with
a 8x8 RGB LED matrix. It can extend :ref:`Bricks <primer_bricks>`.

The red, green and blue value of each LED can be individually controlled with
a resolution of 8 bit.

A frame rate of 120 Hz can be achieved. Frames can be send with a fixed frame 
rate to achieve smooth animations. They are double buffered to increase
performance and avoid flicker.

The Bricklet is equipped with a 15cm cable, which has to be connected to an 
external 5V power supply. The LEDs can not be powered through the Bricklet 
connector.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               39mW (7.8mA at 5V) plus external 5V input for LEDs
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Matrix Size                       8x8
LED Resolution                    8 bit per channel
Cable Length                      15cm

Input Voltage                     5V
Max Input Current                 Each RGB LED can pull up to 20mA per color,
                                  this results in 3.83A if all LEDs are set to white.
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            75 x 55 x 14mm (2.95 x 2.17 x 0.55")
Weight                            23g
================================  ============================================================



Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/rgb-led-matrix-bricklet/raw/master/hardware/rgb-led-matrix-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rgb_led_matrix_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rgb-led-matrix-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2xZlMJ4>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/rgb_led_matrix/rgb-led-matrix.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/rgb_led_matrix/rgb-led-matrix.FCStd>`__)

.. _rgb_led_matrix_bricklet_test:

Test your RGB LED Matrix Bricklet
---------------------------------

|test_intro|

|test_connect| and a 5V power supply to the RGB LED Matrix Bricklet terminal blocks.

|test_tab|
If everything went as expected you can now control the RGB LED Matrix.

.. image:: /Images/Bricklets/bricklet_rgb_led_matrix_brickv.jpg
   :scale: 100 %
   :alt: RGB LED Matrix Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rgb_led_matrix_brickv.jpg

|test_pi_ref|


.. _rgb_led_matrix_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RGB_LED_Matrix_hlpi.table
