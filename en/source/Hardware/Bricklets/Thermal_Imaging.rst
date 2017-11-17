:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Thermal Imaging Bricklet
:FIXME_shoplink: ../../../shop/bricklets/thermal-imaging-bricklet.html

.. include:: Thermal_Imaging.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _thermal_imaging_bricklet:

Thermal Imaging Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_thermal_imaging_tilted_[?|?].jpg           Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_horizontal_[?|?].jpg       Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_lepton_[?|?].jpg           Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_brickv_[100|].jpg          Thermal Imaging Bricklet in Brick Viewer
	Dimensions/thermal_imaging_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 Shop entry as well as Brick Viewer and Bindings support for the Thermal Imaging Bricklet
 will be released on Tuesday, November 21st at the latest. Thank you for your 
 patience!

Features
--------

* 80x60 pixel thermal imaging camera
* Measurement range -273°C to 6279°C 
* Uses FLIR Lepton **with radiometry and shutter**
* High Contrast Image with 8.6Hz and 8 bit resolution (for display)
* Temperature Image with 4.5Hz and 16 bit resolution (for scientific calculations)
* Definable spotmeter with min, max, mean temperature measurement
* Automatic shutter control


.. _thermal_imaging_bricklet_description:

Description
-----------

The Thermal Imaging :ref:`Bricklet <primer_bricklets>` is equipped with a
60x80 pixel `thermal imaging camera <https://en.wikipedia.org/wiki/Thermographic_camera>`__.
It can be connected to a :ref:`Brick <primer_bricks>`.

The Bricklet uses a FLIR Lepton sensor with radiometry and shutter. It can
measure a temperature range of -273°C up to 6279°C with a resolution of 80x60 pixel.

A spotmeter can be set to measure the minimum, mean and maximum temperature
of a user defined region in the image.

The Bricklet supports two image modes: High Contrast Image and Temperature Image.

In High Contrast Image mode the Bricklet provides an image stream with 8.6Hz and 8 bit
resolution. The image data is grey-scale, the high dynamic range of the sensor
is collapsed to be appropriate for display. This mode is used in thermal imaging
cameras that are available on the market. Typically the grey-scale data is converted
in a pseudo-color image by a lookup table.

In Temperature Image mode the Bricklet provides an image stream with 4.5Hz and 16 bit
resolution. In the image data each pixel represents one 16 bit temperature value between
-273°C and 6279°C with a resolution of 0.1°C or a value between -273°C and 381°C with a 
resolution of 0.01°C (depending on the resolution configuration). This mode can be
used for scientific calculations and to analyze absolute temperature changes.

The shutter is automatically controlled by the Bricklet.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        60x80
Frame Rate                        8.6Hz (High Contrast Image), 4.5Hz (Temperature Image)
Field of View                     51° horizontal, 66° diagonal
Depth of Field                    10cm to infinity
Thermal Sensitivity               < 50mK (0.05°C)
Radiometric accuracy              +/-5°C or 5% (typical)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 9mm (1.57 x 1.57 x 0.35")
Weight                            8g
================================  ============================================================



Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/thermal-imaging-bricklet/raw/master/hardware/thermal-imaging-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/thermal_imaging_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/thermal-imaging-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)

.. _thermal_imaging_bricklet_test:

Test your Thermal Imaging Bricklet
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the thermal image and configure the Bricklet.

.. image:: /Images/Bricklets/bricklet_thermal_imaging_brickv.jpg
   :scale: 100 %
   :alt: Thermal Imaging Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_thermal_imaging_brickv.jpg

|test_pi_ref|


.. _thermal_imaging_bricklet_high_contrast_vs_temperature:

High Contrast Image vs Temperature Image
----------------------------------------

The Thermal Imaging Bricklet supports two type of image stream modes with
different use cases.

**High Contrast Image**:

In High Contrast Image mode the Bricklet provides a 60x80 pixel image with a
frame rate of 8.6Hz. Every pixel is a grey-scale representation and
has a resolution of 8 bit.

This mode is used in FLIR based thermal imaging cameras that are 
available on the market. The data can be used for visualizations and it can be 
directly drawn to a display as is.

For the High Contrast Image mode the high dynamic range of the sensor
is collapsed with a histogram-based non-linear mapping function. This filtering
is necessary for visualizations. If the data would be unfiltered, it could 
not be used for visualizations. With a temperature range from 
-273°C and 6279°C a common temperature image with small changes in the range of
20°C-30°C the changes would not be visible at all.

The 8 bit data of each pixel does not contain any temperature information anymore.
However, even in High Contrast Image mode you can still use the spotmeter.

For the spotmeter you can define a region within the 60x80 pixel matrix. For this
region you can then get the minimum, maximum and mean temperature for every frame.
You can also define the spotmeter region to be only one pixel (to get the exact
temperature of this pixel).

In this mode you can configure different parameters:

* **Dampening Factor**: This parameter is the amount of temporal dampening applied to the HEQ 
  (history equalization) transformation function. An IIR filter of the form 
  (N/256) * previous + ((256-N)/256) * current is applied, and the HEQ dampening factor 
  represents the value N in the equation, i.e., a value that applies to the amount of
  influence the previous HEQ transformation function has on the current function. The 
  lower the value of N the higher the influence of the current video frame whereas
  the higher the value of N the more influence the previous damped transfer function has.

* **Clip Limit Low**: This parameter defines an artificial population that is added to 
  every non-empty histogram bin. In other words, if the Clip Limit Low is set to L, a bin 
  with an actual population of X will have an effective population of L + X. Any empty bin 
  that is nearby a populated bin will be given an artificial population of L. The effect of
  higher values is to provide a more linear transfer function; lower values provide a more
  non-linear (equalized) transfer function.

* **Clip Limit High**: This parameter defines the maximum number of pixels allowed 
  to accumulate in any given histogram bin. Any additional pixels in a given bin are clipped.
  The effect of this parameter is to limit the influence of highly-populated bins on the 
  resulting HEQ transformation function.

* **Empty Counts**: This parameter specifies the maximum number of pixels in a bin that will be 
  interpreted as an empty bin. Histogram bins with this number of pixels or less will be 
  processed as an empty bin.

Additionally a region of interest can be defined. The algorithms configured by the above
parameters will only be applied for the specified region. This region can be defined
to exclude parts of the image that are not to be analyzed and would otherwise distort
the data. As an example it might be interesting to exclude a hot spot in the image.

Use this mode if you need any form of visualization of the data.

**Temperature Image**:

In Temperature Image mode the Bricklet provides a 60x80 pixel image with a
frame rate of 4.5Hz. Every pixel in this image is a temperature measurement with a
resolution of 16 bit.

The Thermal Imaging Bricklet has two configurable temperature ranges for the
Temperature Image mode:

* -273°C to 381°C with a resolution of 0.01°C
* -273°C to 6279°C with a resolution of 0.1°C

If you don't need to measure temperatures above 381°C you should always use the first
range to increase the resolution.

The data can be directly used for scientific calculations or to 
analyze absolute temperature changes.

Use this mode if you want to work with actual temperature data.


.. _thermal_imaging_bricklet_case:

Case
----

Coming soon...

..
	A `laser-cut case for the Thermal Imaging Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-thermal-imaging-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_thermal_imaging_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Thermal Imaging Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_thermal_imaging_case_1000.jpg

	.. include:: Thermal_Imaging.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/thermal_imaging_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Thermal Imaging Bricklet
	   :align: center
	   :target: ../../_images/Exploded/thermal_imaging_exploded.png

	|bricklet_case_hint|


.. _thermal_imaging_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Thermal_Imaging_hlpi.table
