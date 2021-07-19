
:shoplink: ../../../shop/bricklets/compass-bricklet.html

.. include:: Compass.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _compass_bricklet:

Compass Bricklet
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_compass_tilted_[?|?].jpg           Compass Bricklet
	Bricklets/bricklet_compass_top_[?|?].jpg              Compass Bricklet
	Bricklets/bricklet_compass_brickv_[100|].jpg          Compass Bricklet in Brick Viewer
	Dimensions/compass_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 3-axis compass
* Measures heading with resolution of 0.1° and accuracy up to 1°
* Measures magnetic flux density with 0.01µT (microtesla) resolution
* Update rate of up to 600Hz

.. _compass_bricklet_description:

Description
-----------

The Compass :ref:`Bricklet <primer_bricklets>` is equipped with a
3-axis ±8 Gauss magnetic sensor. It can measure the magnetic flux density
for all three axis as well as the heading with a resolution of 0.1° and 
accuracy up to 1°.

The update rate is configurable and can go as high as 600Hz.

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_compass_video.mp4"  type="video/mp4">
	  <source src="../../_images/Videos/bricklet_compass_button_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_compass_button_video.webm" type="video/webm">
	</video>


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MMC5883MA
Current Consumption               40mW (8mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Magnetic Flux Density Range       -800µT to 800µT (microtesla)
Magnetic Flux Density Resolution  0.01µT (microtesla)
Heading Range                     0° to 360°
Heading Resolution                0.1°
Heading Accuracy                  Up to 1° at 100Hz update rate*
Update Rate                       100Hz-600Hz (configurable)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            2g
================================  ============================================================

\*: Depends on the quality of the calibration for the specific environment the Bricklet is used in.

Resources
---------

* MMC5883MA datasheet (`Download <https://github.com/Tinkerforge/compass-bricklet/raw/master/datasheets/MMC5883MA-RevC.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/compass-bricklet/raw/master/hardware/compass-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/compass_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/compass-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/33AQJo8>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/compass/compass.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/compass/compass.FCStd>`__)


.. _compass_bricklet_test:

Test your Compass Bricklet
--------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the measured magnetic flux density as well as
the heading and inclination.

.. image:: /Images/Bricklets/bricklet_compass_brickv.jpg
   :scale: 100 %
   :alt: Compass Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_compass_brickv.jpg

|test_pi_ref|


.. _compass_bricklet_case:

Case
----

A `laser-cut case for the Compass Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-accelerometer-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_accelerometer_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Compass Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_accelerometer_case_built_up_1000.jpg

.. include:: Compass.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/accelerometer_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Compass Bricklet
   :align: center
   :target: ../../_images/Exploded/accelerometer_exploded.png

|bricklet_case_hint|


.. _compass_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Compass_hlpi.table
