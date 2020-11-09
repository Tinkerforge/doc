
:shoplink: ../../../shop/bricklets/co2-v2-bricklet.html

.. include:: CO2_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _co2_v2_bricklet:

CO2 Bricklet 2.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_co2_v2_tilted_[?|?].jpg           CO2 Bricklet 2.0
	Bricklets/bricklet_co2_v2_tilted2_[?|?].jpg          CO2 Bricklet 2.0
	Bricklets/bricklet_co2_v2_top_[?|?].jpg              CO2 Bricklet 2.0
	Bricklets/bricklet_co2_v2_side_[?|?].jpg             CO2 Bricklet 2.0
	Bricklets/bricklet_co2_v2_brickv_[100|].jpg          CO2 Bricklet 2.0 in Brick Viewer
	Dimensions/co2_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures CO2 concentration from 400 to 10000ppm (parts per million)
* High accuracy of ±30ppm (full-scale) and ±3% (of reading)
* Measures temperature and humidity for compensation
* Ambient air pressure can be applied for additional compensation


.. _co2_v2_bricklet_description:

Description
-----------

The CO2 :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure
`CO2 concentration <https://en.wikipedia.org/wiki/CO2>`__ in the air. The
measured CO2 concentration can be read out in
`ppm <https://en.wikipedia.org/wiki/Parts-per_notation>`__.
With configurable events it is possible to react on changing CO2
concentration without polling.

The Bricklet also measures temperature and humidity. These are
used internally for compensation and can additionally be read out.

It is possible to apply an ambient air pressure value to achieve
further compensation and better CO2 concentration measurement.

The CO2 Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            Sensirion SCD30
Current Consumption (average)     60mW (12mA at 5V)
Current Consumption (peak)        400mW (80mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
CO2 Concentration Resolution      1ppm with range of 400ppm to 10000ppm
Temperature Resolution            0.01°C with range of -40°C to 70°c
Humidity Resolution               0.01%RH with range of 0%RH to 100%RH
--------------------------------  ------------------------------------------------------------
CO2 Concentration Accuracy        ±30ppm (full-scale), ±3% (of reading)
Temperature Accuracy              ± (0.4°C + 0.023 × (T [°C] – 25°C))*
Humidity Accuracy                 ± 3 %RH
--------------------------------  ------------------------------------------------------------
Measurement Frequency             0.5 measurements per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 40 x 18mm (1.38 x 1.57 x 0.71")
Weight                            9g
================================  ============================================================

\* This is the temperature at the exact position of the sensor. If the Bricklet is used inside
of an enclosure, the air around the Bricklet may heat up more than the ambient air. The Bricklet
does have API to calibrate this kind of offset.

Resources
---------

* SCD30 datasheet (`Download <https://github.com/Tinkerforge/co2-v2-bricklet/raw/master/datasheets/SCD30.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/co2-v2-bricklet/raw/master/hardware/co2-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/co2_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/co2-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2VEHtyN>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/co2_v2/co2-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/co2_v2/co2-v2.FCStd>`__)


Air Pressure Compensation and Temperature Offset
------------------------------------------------

The CO2 Bricklet 2.0 has API to set an ambient air pressure value for
additionl internal compensation to achieve increased CO2 concentration
accuracy.

You can use a :ref:`Barometer Bricklet 2.0 <barometer_v2_bricklet>` or 
:ref:`Air Quality Bricklet <air_quality_bricklet>` to measure
the air pressure and update the compensation value periodically.

Additionally, if the Bricklet is used inside of an enclosure, the air 
around the Bricklet may heat up more than the ambient air. This temperature
offset can also be calibrated with the API. 
We recommend that you leave the parts in the enclosure running for at least
24 hours such that a temperature equilibrium can be reached.


.. _co2_v2_bricklet_calibration:
CO2 Calibration
---------------

Gas sensors need to be calibrated from time to time. Typically this is
done by applying a specified amount of CO2 to it. Since this is 
impractical for a CO2 sensor at home, the gas sensor of this 
Bricklet (Sensirion SCD30) do a permanent automatic 
calibration (ASC).

Here is what Sensirion is writing about it:

.. note::

 To work properly SCD30 has to see fresh air on a regular basis. Optimal 
 working conditions are given when the sensor sees fresh air for one hour 
 every day so that ASC can constantly re-calibrate. ASC only works in 
 continuous measurement mode.

That means if the sensor is not seeing fresh air in that period it will
calibrate with the wrong values decreasing the accuracy of the sensor.

.. _co2_v2_bricklet_test:

Test your CO2 Bricklet 2.0
--------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_co2_v2_brickv.jpg
   :scale: 100 %
   :alt: CO2 Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_co2_v2_brickv.jpg

|test_pi_ref|



.. _co2_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: CO2_V2_hlpi.table
