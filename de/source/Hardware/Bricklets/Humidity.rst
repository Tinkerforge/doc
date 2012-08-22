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
	             "Brick Viewer screenshot") 
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
* Outputs 0-100% RH, unit 0.1% RH
* Resolution 12bit


Description
-----------

The Humidity :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by the 
capability to measure 
`relative humidity <http://en.wikipedia.org/wiki/Relative_humidity>`_. 
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
Dimensions                        15mm x 25mm (0.59" x 0.98")
Weight                            1.6g
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            HIH-5030
Output: Relative Humidity (RH)    0-100% RH, unit 0.1% RH, resolution 12bit
================================  ============================================================

Resources
---------

* HIH-5030 Datasheet (`Download <https://github.com/Tinkerforge/humidity-bricklet/raw/master/datasheets/hih-5030.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/humidity-bricklet/raw/master/hardware/humidity-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/humidity_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/humidity-bricklet/zipball/master>`__)


.. _humidity_bricklet_test:


Test your Humidity Bricklet
---------------------------

To test the Humidity Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Humidity Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable 
(see picture below).

.. image:: /Images/Bricklets/bricklet_humidity_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Humidity Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_humidity_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Humidity Bricklet" in the Brick Viewer after you pressed "connect".
Select it.
If everything went as expected you can now see the measured relative humidity
and a graph that shows the humidity over time.

To test the sensor breath over the sensor. The relative humidity should rise
as long as you breath and fall again afterwards.

.. image:: /Images/Bricklets/bricklet_humidity_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Humidity Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_humidity_brickv.jpg


After this test you can go on with writing your own application.
See the :ref:`Programming Interface <humidity_programming_interfaces>` 
section for the API of the Humidity Bricklet and examples in different 
programming languages.


.. _humidity_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Humidity_hlpi.table
