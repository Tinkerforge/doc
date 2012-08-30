.. include:: Humidity.substitutions


.. _humidity_bricklet:

Humidity Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_humidity_tilted_350.jpg",
	               "Bricklets/bricklet_humidity_tilted_600.jpg",
	               "Humidity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_humidity_vertical_100.jpg",
	             "Bricklets/bricklet_humidity_vertical_600.jpg",
	             "Humidity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_humidity_horizontal_100.jpg",
	             "Bricklets/bricklet_humidity_horizontal_600.jpg",
	             "Humidity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_humidity_master_100.jpg",
	             "Bricklets/bricklet_humidity_master_600.jpg",
	             "Humidity Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_humidity_brickv_100.jpg",
	             "Bricklets/bricklet_humidity_brickv.jpg",
	             "Humidity Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/humidity_bricklet_dimensions_100.png",
	             "Dimensions/humidity_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures relative humidity
* Output in 0.1% RH steps (12bit resolution)


Description
-----------

The Humidity :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by the
capability to measure
`relative humidity <http://en.wikipedia.org/wiki/Relative_humidity>`__.
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


.. _humidity_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Humidity_hlpi.table
