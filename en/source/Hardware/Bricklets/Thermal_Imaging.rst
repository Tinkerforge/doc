:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Thermal Imaging Bricklet
:FIXME_shoplink: ../../../shop/bricklets/thermal-imaging-bricklet.html

.. include:: Thermal_Imaging.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _thermal_imaging_bricklet:

Thermal Imaging Bricklet
========================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_thermal_imaging_tilted_[?|?].jpg           Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_horizontal_[?|?].jpg       Thermal Imaging Bricklet
	Bricklets/bricklet_thermal_imaging_master_[100|600].jpg       Thermal Imaging Bricklet with Master Brick
	Cases/bricklet_thermal_imaging_case_[100|600].jpg             Thermal Imaging Bricklet with case
	Bricklets/bricklet_thermal_imaging_brickv_[100|].jpg          Thermal Imaging Bricklet in Brick Viewer
	Dimensions/thermal_imaging_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


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
cameras that are available on the market.

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
Frame Rate                        High Contrast Image: 8.6Hz
                                  Temperature Image: 4.5Hz
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

TODO: Explain AGC, binning, spotmeter, dampening factor, clip limit, empty counts (with ROI)


.. _thermal_imaging_bricklet_case:

Case
----

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
