
.. include:: Humidity.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _humidity_bricklet:

Humidity Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_humidity_tilted_[?|?].jpg           Humidity Bricklet
	Bricklets/bricklet_humidity_vertical_[?|?].jpg         Humidity Bricklet
	Bricklets/bricklet_humidity_horizontal_[?|?].jpg       Humidity Bricklet
	Bricklets/bricklet_humidity_master_[100|600].jpg       Humidity Bricklet with Master Brick
	Cases/bricklet_ambient_light_case_built_up_[?|?].jpg   Humidity Bricklet in Case
	Bricklets/bricklet_humidity_brickv_[100|].jpg          Humidity Bricklet in Brick Viewer
	Dimensions/humidity_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Humidity Bricklet is discontinued and is no longer sold. The
 :ref:`Humidity Bricklet 2.0 <humidity_v2_bricklet>` is the recommended
 replacement.

Features
--------

* Measures relative humidity
* Output in 0.1% RH steps (12bit resolution)


.. _humidity_bricklet_description:

Description
-----------

The Humidity :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure
`relative humidity <https://en.wikipedia.org/wiki/Relative_humidity>`__.
The measured humidity can be read out directly in percent, no conversions are
necessary. With configurable events it is possible to react on changing humidity
without polling.

A weather station is a typical application for this sensor, but it can also be
used in drying applications, environment monitoring etc.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            HIH-5030
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Relative Humidity (RH)            0% RH - 100% RH in 0.1% RH steps, 12bit resolution
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* HIH-5030 datasheet (`Download <https://github.com/Tinkerforge/humidity-bricklet/raw/master/datasheets/hih-5030.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/humidity-bricklet/raw/master/hardware/humidity-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/humidity_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/humidity-bricklet/zipball/master>`__)


.. _humidity_bricklet_test:

Test your Humidity Bricklet
---------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_humidity_master_600.jpg
   :scale: 100 %
   :alt: Humidity Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_humidity_master_1200.jpg

|test_tab|
If everything went as expected you can now see the measured relative humidity
and a graph that shows the humidity over time.
To test the sensor breath over the sensor. The relative humidity should rise
as long as you breath and fall again afterwards.

.. image:: /Images/Bricklets/bricklet_humidity_brickv.jpg
   :scale: 100 %
   :alt: Humidity Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_humidity_brickv.jpg

|test_pi_ref|

.. _humidity_bricklet_case:

Case
----

A `laser-cut case for the Humidity Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for humidity Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Humidity.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Humidity Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


Troubleshooting
---------------

If enough liquid water forms on the sensor under condensing conditions, this
water can create a leakage path. This leads to an erroneous reading of 0% 
humidity. Once this water evaporates the sensor returns to normal functionality.
If you want to use the sensor under heavy condensing conditions mount it top 
side down. If this not suffice protect it e.g by foam.

.. _humidity_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Humidity_hlpi.table
