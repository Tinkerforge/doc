
:DISABLED_shoplink: ../../../shop/bricklets/color-v2-bricklet.html

.. include:: Color_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _color_v2_bricklet:

Color Bricklet 2.0
==================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_color_v2_tilted_[?|?].jpg           Color Bricklet 2.0
	Bricklets/bricklet_color_v2_horizontal_[?|?].jpg       Color Bricklet 2.0
	Bricklets/bricklet_color_v2_master_[100|600].jpg       Color Bricklet 2.0 with Master Brick
	Cases/bricklet_color_v2_case_[100|600].jpg             Color Bricklet 2.0 with case
	Bricklets/bricklet_color_v2_brickv_[100|].jpg          Color Bricklet 2.0 in Brick Viewer
	Dimensions/color_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures color (RGB), color temperature and illuminance (16bit resolution each)
* Equipped with switchable LED for defined illumination and color temperature


.. _color_v2_bricklet_description:

Description
-----------

The Color :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure `color <https://en.wikipedia.org/wiki/Color>`__,
`color temperature <https://en.wikipedia.org/wiki/Color_temperature>`__ and
`illuminance <https://en.wikipedia.org/wiki/Illuminance>`__ of a light source.
Thus the Bricklet can measure the color of an object via its reflected light.
To create a defined illumination and color temperature the Bricklet is equipped 
with a API switchable LED.

The Bricklet can be used for many purposes, e.g. sorting of objects by their
color.

.. image:: /Images/Bricklets/bricklet_color_wavelength_chart_350.jpg
   :scale: 100 %
   :alt: Chart Responsivity / Wavelength
   :align: center
   :target: ../../_images/Bricklets/bricklet_color_wavelength_chart_600.jpg

The Sensor is equipped with color filters for the colors red, green and blue 
(RGB). In the chart above the responsivity of the sensor in the given color 
range is shown. Additional to the color information (RGB) a fourth value is 
measured called "clear value" (C). This is the sensors value without any color
filter. Each value of RGB and C is measured as 16bit value. From these sensor
values the Bricklet computes two additional values: illuminance and color 
temperature each with 16bit resolution.

The Color Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            TCS34725
Current Consumption               TBD (LED off), TBD (LED on)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dynamic Range                     3800000:1
Color Resolution (R,G,B,C)        16bit each (0-65535)
Color Temperature Resolution      16bit (0-65535)
Illuminance Resolution            16bit (0-65535)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            TBDg
================================  ============================================================


Resources
---------

* TCS3472 datasheet (`Download <https://github.com/Tinkerforge/color-v2-bricklet/raw/master/datasheets/TCS34725.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/color-v2-bricklet/raw/master/hardware/color-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/color_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/color-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _color_v2_bricklet_test:

Test your Color Bricklet 2.0
----------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected ... TBD.

..
	.. image:: /Images/Bricklets/bricklet_color_v2_brickv.jpg
	   :scale: 100 %
	   :alt: Color Bricklet 2.0 in Brick Viewer
	   :align: center
	   :target: ../../_images/Bricklets/bricklet_color_v2_brickv.jpg

|test_pi_ref|


Usage and Configuration
-----------------------

The sensor of the Bricklet can be configured. Gain and integration time can
be changed. Dark environments need a higher gain or a longer integration time.
If you use long integration times the sensor will react slower. If you need fast
measurements use a high gain and short integration times.

The desired configuration depends on the application. Depending on the 
illumination and distance to the measured object other parameters have to be chosen.
The Brick Viewer can be used to find proper values.

If you want to use the Bricklet in sorting applications it should be mounted in 
a fixed distance, with a fixed source of light (e.g. the equipped LED) and 
it should also be protected from interfering light.



.. _color_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Color_V2_hlpi.table
