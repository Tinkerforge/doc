
:DISABLED_shoplink: ../../../shop/bricklets/air-quality-bricklet.html

.. include:: Air_Quality.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _air_quality_bricklet:

Air Quality Bricklet
====================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_air_quality_tilted_[?|?].jpg           Air Quality Bricklet
	Bricklets/bricklet_air_quality_horizontal_[?|?].jpg       Air Quality Bricklet
	Bricklets/bricklet_air_quality_master_[100|600].jpg       Air Quality Bricklet with Master Brick
	Cases/bricklet_air_quality_case_[100|600].jpg             Air Quality Bricklet with case
	Bricklets/bricklet_air_quality_brickv_[100|].jpg          Air Quality Bricklet in Brick Viewer
	Dimensions/air_quality_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures air quality (IAQ index), humidity, air pressure and temperature
* IAQ index and humidity values are temperature compensated
* Configurable temperature compensation for use cases in enclosures


.. _air_quality_bricklet_description:

Description
-----------

The Air Quality Bricklet :ref:`Bricklet <primer_bricklets>` can measure

* IAQ (indoor air quality) Index,
* Air Pressure in hPa,
* Humidity in %RH and
* Temperature in °C.

The IAQ Index is a measurement for the quality of air. To calculate the IAQ Index the
Bricklet detects Ethane, Isoprene/2-methyl-1,3 Butadiene, Ethanol, Acetone and
Carbon Monoxide (often called VOC, volatile components) by adsorption. These gas 
measurements are combined with the measurements of air pressure, humidity and 
temperature to calculate the air IAQ Index. 

The index has a range of 0-500:

.. image:: /Images/Misc/bricklet_air_quality_iaq_index.png
   :scale: 100 %
   :alt: Air Quality Index description
   :align: center
   :target: ../../_images/Misc/bricklet_air_quality_iaq_index.png

Typical applications for this Bricklet are the monitoring of air quality, environmental 
statistics, home automation and similar.

The Air Quality Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            BME680
Current Consumption               100mW (20mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
IAQ Index resolution              1
Air Pressure resolution           0.18Pa
Humidity resolution               0.008%RH
Temperature resolution            0.01°C
--------------------------------  ------------------------------------------------------------
IAQ Index accuracy                ±15 and ±15% of reading
Air Pressure accuracy             ±0.12hPa (700-900hPa at 25-40°C), ±0.6hPa (full range)
Humidity accuracy                 ±3%RH (20-80%RH at 25°C)
Temperature accuracy              ±0.5°C (at 25°C), ±1.0°C (0-65°C)*
--------------------------------  ------------------------------------------------------------
Measurement frequency             1 measurement per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            2.1g
================================  ============================================================

\*: This is the temperature at the exact posisiton of the sensor. If the Bricklet is used inside
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
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


IAQ Index accuracy
------------------

The Bricklet is building a database of measurements and uses this data to calculate an accurate
IAQ Index over time. It will take 1-2 days until the IAQ Index has a high reliability. The API
of the Bricklet returns a best guess about the accuracy (ranging from unreliable to high).

The current database of values and calculated coefficients are saved to the flash of the Bricklet
every 12 hours, so if you loose power it will not take as long to receive reliable data again.


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

..
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
