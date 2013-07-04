
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#bricklets">Bricklets</a> / Industrial Dual 0-20mA Bricklet
:shoplink: ../../../shop/bricklets/industrial-dual-0-20-ma-bricklet.html

.. include:: Industrial_Dual_020mA.substitutions


.. _industrial_dual_0_20_ma_bricklet:

Industrial Dual 0-20mA Bricklet
===============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_dual_0_20ma_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_dual_0_20ma_tilted_600.jpg",
	               "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20ma_vertical_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20ma_vertical_600.jpg",
	             "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20ma_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20ma_horizontal_600.jpg",
	             "Industrial Dual 0-20mA Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20ma_sensor_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20ma_sensor_600.jpg",
	             "Industrial Dual 0-20mA Bricklet with Ambient Light Sensor")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_0_20ma_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_dual_0_20ma_brickv.jpg",
	             "Industrial Dual 0-20mA Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_dual_0_20ma_dimensions_100.png",
	             "Dimensions/industrial_dual_0_20ma_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}

Features
--------

* Precision current sensor, measures `currents between 0 and 22.5mA <http://en.wikipedia.org/wiki/Current_loop>`__
* Can read out any IEC 60381-1 type 2 and type 3 sensor 
* High accuracy (0.15%), resolution (up to 0.172µA) and sample rate (up to 240 SPS)
* It is possible to detect if a sensor is connected/faulty


Description
-----------

The Industrial Dual 0-20mA :ref:`Bricklet <product_overview_bricklets>` 
can be used to extend the features of :ref:`Bricks <product_overview_bricks>` 
by the capability to measure currents between 0 and 22.5mA.

This Bricklet can be used to read out up to two IEC 60381-1 type 2 and 
type 3 sensor. 

The measured current can be read out in nA. 
With configurable events it is possible to react on changing
currents without polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MCP3423
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Measurement Range                 0mA - 22.5mA
Supported Sensors                 IEC 60381-1 type 2 and type 3
Accuracy                          0.15% with 40ppm/°C
Resolution                        up to 0.172µA (18bit)
Sample Rate                       up to 240 samples per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            8g
================================  ============================================================


Resources
---------

* MCP3423 Datasheet (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/datasheets/mcp3423.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/hardware/industrial-dual-0-20ma-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_dual_0_20ma_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/zipball/master>`__)


Connectivity
------------

See below for connection diagrams for type 2/3 sensor.

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_connectivity_600.jpg
   :scale: 100 %
   :alt: Connection diagram for type 2/3 sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_connectivity_1200.jpg

Both sensor ports ("Sensor 0" and "Sensor 1") can be used independently.

.. _industrial_dual_0_20_ma_bricklet_test:

Test your Industrial Dual 0-20mA Bricklet
-----------------------------------------

|test_intro|

|test_connect| and attach a current source (see picture below).
In this example we use a 4-20mA ambient light sensor.

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_sensor_600.jpg
   :scale: 100 %
   :alt: Industrial Dual 0-20mA Bricklet connected to ambient light sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_sensor_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual 0-20mA Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_brickv.jpg

Interact with the sensor to see the current changing in the Brick Viewer.

|test_pi_ref|

.. _industrial_dual_0_20_ma_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Industrial_Dual_020mA_hlpi.table
