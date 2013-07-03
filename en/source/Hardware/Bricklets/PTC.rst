
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#bricklets">Bricklets</a> / PTC Bricklet
:shoplink: ../../../shop/bricklets/ptc-bricklet.html

.. include:: PTC.substitutions


.. _ptc_bricklet:

PTC Bricklet
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_ptc_tilted_350.jpg",
	               "Bricklets/bricklet_ptc_tilted_600.jpg",
	               "PTC Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ptc_vertical_100.jpg",
	             "Bricklets/bricklet_ptc_vertical_600.jpg",
	             "PTC Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ptc_horizontal_100.jpg",
	             "Bricklets/bricklet_ptc_horizontal_600.jpg",
	             "PTC Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ptc_sensor_100.jpg",
	             "Bricklets/bricklet_ptc_sensor_600.jpg",
	             "PTC Bricklet with 3-wire Pt100 RTD")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ptc_jumper_100.jpg",
	             "Bricklets/bricklet_ptc_jumper_600.jpg",
	             "PTC Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ptc_brickv_100.jpg",
	             "Bricklets/bricklet_ptc_brickv.jpg",
	             "PTC Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/ptc_bricklet_100.png",
	             "Dimensions/ptc_bricklet_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}

Features
--------

* Supports Pt100 and Pt1000 sensors
* Supports 2-wire, 3-wire and 4-wire type
* Measures temperature with 0.5% accuracy at the full scale of -246 to 849°C
* Resolution of 0.03125°C (15bit), output in 0.01°C steps


Description
-----------

The PTC :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by the
capability to measure temperature with Pt100 and Pt1000 sensors.

The Pt100 and Pt1000 sensors can be of 2-wire, 3-wire or 4-wire type.

The measured temperature can be read out in `°C
<http://en.wikipedia.org/wiki/Degree_Celsius>`__.
With configurable events it is possible to react on changing
temperatures without polling.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MAX31865
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Supported Pt-Sensor Types         Pt100 and Pt1000 with 2-wire, 3-wire or 4-wire
Accuracy                          min 0.5% full scale
Input Protection                  +-50V
Temperature Resolution            0.03125°C (15bit)
Conversion Time                   21ms
Fault Detection                   Open RTD element, RTD value out-of-range, short across RTD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 30 x 15mm (1.38 x 1.18 x 0.59")
Weight                            TBDg
================================  ============================================================

Resources
---------

* MAX31865 datasheet (`Download <https://github.com/Tinkerforge/ptc-bricklet/raw/master/datasheets/MAX31865.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/ptc-bricklet/raw/master/hardware/ptc-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/ptc_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/ptc-bricklet/zipball/master>`__)


.. _ptc_bricklet_jumper_configuration:

Jumper Configuration
--------------------

Configure the jumper for Pt100/Pt1000 sensor and 2/3/4-wire type as
shown below.

.. image:: /Images/Bricklets/bricklet_ptc_pt_wire_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet jumper configurations
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_pt_wire_1000.jpg

.. _ptc_bricklet_connectivity:

Connectivity
------------

See below for connection diagrams for 2/3/4-wire type resistance temperature
device.

.. image:: /Images/Bricklets/bricklet_ptc_connectivity_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet connection diagram
   :align: center
   :target: ../../_images/Bricklets/bricklet_connectivity_1000.jpg

Additonally the number of wires has to be set with the API.

.. _ptc_bricklet_test:

Test your PTC Bricklet
----------------------

|test_intro|

|test_connect| and attach a Pt100/1000 sensor (see picture below).
In this example we use a 3-wire Pt100 sensor.

.. image:: /Images/Bricklets/bricklet_ptc_sensor_600.jpg
   :scale: 100 %
   :alt: PTC Bricklet connected to 3-wire Pt100 sensor.
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_sensor_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_ptc_brickv.jpg
   :scale: 100 %
   :alt: PTC Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ptc_brickv.jpg

Put the sensor in your hand to see the
temperature rising (or falling if it is extremely warm in your room).

|test_pi_ref|

.. _ptc_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: PTC_hlpi.table
