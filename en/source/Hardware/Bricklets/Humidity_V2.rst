:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Humidity Bricklet 2.0
:FIXME_shoplink: ../../../shop/bricklets/humidity-v2-bricklet.html

.. include:: Humidity_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _humidity_v2_bricklet:

Humidity Bricklet 2.0
=====================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_humidity_v2_tilted_[?|?].jpg           Humidity Bricklet 2.0
	Bricklets/bricklet_humidity_v2_horizontal_[?|?].jpg       Humidity Bricklet 2.0
	Bricklets/bricklet_humidity_v2_master_[100|600].jpg       Humidity Bricklet 2.0 with Master Brick
	Cases/bricklet_humidity_v2_case_[100|600].jpg             Humidity Bricklet 2.0 with case
	Bricklets/bricklet_humidity_v2_brickv_[100|].jpg          Humidity Bricklet 2.0 in Brick Viewer
	Dimensions/humidity_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures relative humidity and temperature
* Output in 0.01%RH / 0.01°C steps (14 bit resolution)
* Internal heater and internal compensation


.. _humidity_v2_bricklet_description:

Description
-----------

The Humidity :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure
`relative humidity <https://en.wikipedia.org/wiki/Relative_humidity>`__ and
`temperature <https://en.wikipedia.org/wiki/Temperature>`__. The measured
humidity can be read out directly in percent and the temperature directly in °C.
With configurable events it is possible to react on changing humidity or temperature
without polling.

The sensor compensates the measured humidity internaly with the current temperature.
A heater is integrated into the sensor and it can be turned on through the API. It
can be used to dry the sensor in extremly wet environments.

A weather station is a typical application for this sensor. It can also be
used in drying applications, environment monitoring etc.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            HDC1080
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Relative Humidity (RH)            0% RH - 100%RH in 0.01%RH steps, 14 bit resolution
Temperature                       -20°C- 85°C in 0.01°C steps, 14 bit resolution
Accuracy                          +-2% (typical) for humidity
                                  +-0.2°C (typical) for temperature
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            3g
================================  ============================================================



Resources
---------

* HDC1080 Datenblatt (`Download <https://github.com/Tinkerforge/humidity-v2-bricklet/raw/master/datasheets/hdc1080.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/humidity-v2-bricklet/raw/master/hardware/humidity-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/humidity_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/humidity-v2-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2yBMQ5P>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/humidity_v2/humidity.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/humidity_v2/humidity.FCStd>`__)


.. _humidity_v2_bricklet_test:

Test your Humidity Bricklet 2.0
-------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the measured relative humidity
and temperatures as well as a graph that shows both values over time.
To test the sensor breath over the sensor. The relative humidity should rise
and fall again.

.. image:: /Images/Bricklets/bricklet_humidity_v2_brickv.jpg
   :scale: 100 %
   :alt: Humidity Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_humidity_v2_brickv.jpg

|test_pi_ref|

.. _humidity_v2_bricklet_case:

Case
----

A `laser-cut case for the Humidity Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Humidity Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Temperature.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Humidity Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|



.. _humidity_v2_bricklet_programming_interface:


Troubleshooting
---------------

If enough liquid water forms on the sensor under condensing conditions, this
water can create a leakage path. This leads to erroneous readings.
Once this water evaporates the sensor returns to normal functionality. You
can use the integrated heater to dry the sensor.

If you want to use the sensor under heavy condensing conditions mount it top 
side down. If this not suffice protect it e.g by foam.

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Humidity_V2_hlpi.table
