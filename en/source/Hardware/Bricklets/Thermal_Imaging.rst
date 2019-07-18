
:shoplink: ../../../shop/bricklets/thermal-imaging-bricklet.html

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


Features
--------

* 80x60 pixel thermal imaging camera
* Measurement range -10°C to 450°C 
* Uses FLIR Lepton **with radiometry and shutter**
* High Contrast Image with 8.6Hz and 8 bit resolution (for display)
* Temperature Image with 4.5Hz and 16 bit resolution (for scientific calculations)
* Definable spotmeter with min, max, mean temperature measurement
* Automatic shutter control


.. _thermal_imaging_bricklet_description:

Description
-----------

The Thermal Imaging :ref:`Bricklet <primer_bricklets>` is equipped with a
80x60 pixel `thermal imaging camera <https://en.wikipedia.org/wiki/Thermographic_camera>`__.
It can be connected to a :ref:`Brick <primer_bricks>`.

The Bricklet uses a FLIR Lepton sensor with radiometry and shutter. It can
measure a temperature range of -10°C up to 450°C with a resolution of 80x60 pixel.

A spotmeter can be set to measure the minimum, mean and maximum temperature
of a user defined region in the image.

The Bricklet supports two image modes: High Contrast Image and Temperature Image.

In High Contrast Image mode the Bricklet provides an image stream with 8.6Hz and 8 bit
resolution. The image data is gray-scale, the high dynamic range of the sensor
is collapsed to be appropriate for display. This mode is used in thermal imaging
cameras that are available on the market. Typically the gray-scale data is converted
in a pseudo-color image by a lookup table.

In Temperature Image mode the Bricklet provides an image stream with 4.5Hz and 16 bit
resolution. In the image data each pixel represents one 16 bit temperature value between
-10°C and 450°C with a resolution of 0.1°C or a value between -10°C and 140°C with a 
resolution of 0.01°C (depending on the resolution configuration). This mode can be
used for scientific calculations and to analyze absolute temperature changes.

The shutter is automatically controlled by the Bricklet.

The Thermal Imaging Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_thermal_imaging_short_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_thermal_imaging_short_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_thermal_imaging_short_video.webm" type="video/webm">
	</video>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               546mW (109.2mA at 5V, running)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        80x60
Frame Rate                        8.6Hz (High Contrast Image), 4.5Hz (Temperature Image)
Field of View                     51° horizontal, 66° diagonal
Depth of Field                    10cm to infinity
Thermal Sensitivity               < 50mK (0.05°C)
Radiometric accuracy              ±5°C or 5% (typical)
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
* 3D model (`View online <https://autode.sk/2BUaYhK>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/thermal_imaging/thermal-imaging.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/thermal_imaging/thermal-imaging.FCStd>`__)


.. _thermal_imaging_bricklet_demo_video:

Demo Video
----------

In the following video you can see the Thermal Imaging Bricklet in action.
We film a kitchen sink with a warm cup of coffee. Then we turn warm water on
and then change from to cold and back to warm.

You can see that first the cup of coffee is the warmest object in the frame.
The water slowly gets warmer then the coffee after we turn on the tap. When 
we turn the tap to cold it gets colder again.

You can also see the vortex between hot and cold water the forms in the sink.

The Thermal part of the video is the :ref:`High Contrast <thermal_imaging_bricklet_high_contrast_vs_temperature>` 
data from the Thermal Imaging Bricklet.

.. raw:: html

 <iframe class="youtube" width="640" height="360" src="https://www.youtube-nocookie.com/embed/xb44krsgmaM" frameborder="0" allowfullscreen></iframe>

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
frame rate of 8.6Hz. Every pixel is a gray-scale representation and
has a resolution of 8 bit.

This mode is used in FLIR based thermal imaging cameras that are 
available on the market. The data can be used for visualizations and it can be 
directly drawn to a display as is.

For the High Contrast Image mode the high dynamic range of the sensor
is collapsed with a histogram-based non-linear mapping function. This filtering
is necessary for visualizations. If the data would be unfiltered, it could 
not be used for visualizations. With a temperature range from 
-10°C and 450°C a common temperature image with small changes in the range of
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

* -10°C to 140°C with a resolution of 0.01°C
* -10°C to 450°C with a resolution of 0.1°C

If you don't need to measure temperatures above 381°C you should always use the first
range to increase the resolution.

The data can be directly used for scientific calculations or to 
analyze absolute temperature changes.

Use this mode if you want to work with actual temperature data.


.. _thermal_imaging_flir:

Thermal by FLIR
---------------
The Tinkerforge Thermal Imaging Bricklet is equipped with a 
`Lepton <https://www.flir.com/cores/lepton/>`__ thermal
imaging sensor. Tinkerforge is part of the Thermal by FLIR
program (please note the logo on the front side of the Bricklet). Thermal by FLIR is a program 
where FLIR is working with leading integrators to support development and 
marketing of products that include FLIR thermal sensors.  The goal of the program 
is aligned with FLIR's mission of innovating the sixth sense to saves lives and 
livelihoods.

FLIR has created a central site at `lepton.flir.com <https://lepton.flir.com/>`__
to support the Lepton maker community.


.. _thermal_imaging_bricklet_case:

Case
----

A `laser-cut case for the Thermal Imaging Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-thermal-imaging-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_thermal_imaging_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Case for Thermal Imaging Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_thermal_imaging_case_built_up1_800.jpg

The assembly is easiest if you follow the following steps:

* screw 12mm screw with nut to the top plate
* Build up side plates,
* plug side plates into top plate,
* screw 10mm spacers to the Bricklet and
* screw bottom plate to spacers.

Below you can see an exploded assembly drawing of the Thermal Imaging Bricklet case:


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
