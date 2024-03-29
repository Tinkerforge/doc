
:shoplink: ../../../shop/bricklets/air-quality-bricklet.html

.. include:: Air_Quality.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _air_quality_bricklet:

Air Quality Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_air_quality_tilted_[?|?].jpg           Air Quality Bricklet
	Bricklets/bricklet_air_quality_top_[?|?].jpg              Air Quality Bricklet
	Cases/bricklet_air_quality_case_[100|600].jpg             Air Quality Bricklet with case
	Bricklets/bricklet_air_quality_brickv_[100|].jpg          Air Quality Bricklet in Brick Viewer
	Dimensions/air_quality_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures IAQ (indoor air quality) index, air pressure, humidity and temperature
* IAQ index and humidity values are temperature compensated
* Configurable temperature compensation for use cases in enclosures


.. _air_quality_bricklet_description:

Description
-----------

The Air Quality :ref:`Bricklet <primer_bricklets>` can measure

* IAQ (indoor air quality) index,
* Air pressure in hPa,
* Humidity in %RH and
* Temperature in °C.

The IAQ index is a measurement for the quality of air. To calculate the IAQ
index the Bricklet detects ethane, isoprene (2-methylbuta-1,3-diene), ethanol,
acetone and carbon monoxide (often called VOC, volatile organic components) by
adsorption. These gas measurements are combined with the measurements of air
pressure, humidity and temperature to calculate the final IAQ index.

The IAQ index has a range of 0-500:

.. image:: /Images/Misc/bricklet_air_quality_iaq_index.png
   :scale: 100 %
   :alt: IAQ index scale
   :align: center
   :target: ../../_images/Misc/bricklet_air_quality_iaq_index.png

Typical applications for this Bricklet are the monitoring of air quality,
environmental statistics, home automation and similar.

.. raw:: html

	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_air_quality_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_air_quality_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_air_quality_video.webm" type="video/webm">
	</video>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            BME680
Current Consumption               100mW (20mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
IAQ Index Resolution              1
Air Pressure Resolution           0.0018hPa
Humidity Resolution               0.008%RH
Temperature Resolution            0.01°C
--------------------------------  ------------------------------------------------------------
IAQ Index Accuracy                ±15 and ±15% of reading
Air Pressure Accuracy             ±0.12hPa (700-900hPa at 25-40°C), ±0.6hPa (full scale)
Humidity Accuracy                 ±3%RH (20-80%RH at 25°C)
Temperature Accuracy              ±0.5°C (at 25°C), ±1.0°C (0-65°C)*
--------------------------------  ------------------------------------------------------------
Measurement Frequency             0.3 measurements per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            2.1g
================================  ============================================================

\* This is the temperature at the exact position of the sensor. If the Bricklet is used inside
of an enclosure, the air around the Bricklet may heat up more than the ambient air. The Bricklet
does have API to calibrate this kind of offset.

Calibration of the temperature value is recommended, since the temperature value is used
to compensate the IAQ index and humidity values.

Resources
---------

* BME680 datasheet (`Download <https://github.com/Tinkerforge/air-quality-bricklet/raw/master/datasheets/BME680.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/air-quality-bricklet/raw/master/hardware/air-quality-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/air_quality_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/air-quality-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2NTYEnR>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/air_quality/air-quality.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/air_quality/air-quality.FCStd>`__)


IAQ Accuracy and Automatic Calibration
--------------------------------------

The Bricklet is building a database of measurements and uses this data to do an
automatic background calibration and calculate an accurate IAQ index over time.
It will take a few days until the IAQ index has a high reliability.

..
 Please also remove the note from the openhab configuration when removing it here.

The IAQ accuracy is reflects the current state of the background calibration process.

* Accuracy 0: The Bricklet was just started and the sensor is stabilizing.
* Accuracy 1: The background history is uncertain. This typically means the gas sensor data was too stable for the calibration algorithm to clearly define its references.
* Accuracy 2: The Bricklet found new calibration data and is currently calibrating.
* Accuracy 3: The Bricklets is calibrated successfully.

The effective duration of the calibration process depends on the stimuli observed by
the sensor. An IAQ accuracy going back and fourth between 2 and 3 is expected, the
Bricklet is recalibrating itself.

The Bricklet saves the current database of values and calculated coefficients
every 12 hours in its internal flash memory. If the Bricklet loses power it will
not take as long to receive reliable data again.

Starting with firmware version 2.0.3 the automatic background calibration considers 
28 days of data. We recommend that you run the Bricklet for 28 full days before you
consider the data as completely reliable. It is possible to reduce the calibration
window to 4 days with the API.


.. _air_quality_bricklet_test:

Test your Air Quality Bricklet
------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the values for
IAQ index, air pressure, humidity and temperature.

.. image:: /Images/Bricklets/bricklet_air_quality_brickv.jpg
   :scale: 100 %
   :alt: Air Quality Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_air_quality_brickv.jpg

|test_pi_ref|


.. _air_quality_bricklet_case:

Case
----

A `laser-cut case for the Air Quality Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-air-quality-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_air_quality_case_350.jpg
   :scale: 100 %
   :alt: Case for Air Quality Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_air_quality_case_1000.jpg

.. include:: Air_Quality.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/air_quality_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Air Quality Bricklet
   :align: center
   :target: ../../_images/Exploded/air_quality_exploded.png

|bricklet_case_hint|


.. _air_quality_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Air_Quality_hlpi.table
