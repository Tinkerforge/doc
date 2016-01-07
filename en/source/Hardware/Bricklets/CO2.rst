
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / CO2 Bricklet
:FIXME_shoplink: ../../../shop/bricklets/co2-bricklet.html

.. include:: CO2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _co2_bricklet:

CO2 Bricklet
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_co2_tilted1_350.jpg",
	               "Bricklets/bricklet_co2_tilted1_600.jpg",
	               "CO2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_co2_tilted2_100.jpg",
	             "Bricklets/bricklet_co2_tilted2_600.jpg",
	             "CO2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_co2_horizontal_100.jpg",
	             "Bricklets/bricklet_co2_horizontal_600.jpg",
	             "CO2 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_co2_brickv_100.jpg",
	             "Bricklets/bricklet_co2_brickv.jpg",
	             "CO2 Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/co2_bricklet_dimensions_100.png",
	             "Dimensions/co2_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}

.. note::
 This Bricklet is currently work-in-progress!

Features
--------

* Measures CO2 concentration from 0 to 10000ppm (parts per million)
* High accuracy of ±30ppm (full-scale) and ±3% (of reading)

.. _co2_bricklet_description:

Description
-----------

The CO2 :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure
`CO2 concentration <https://en.wikipedia.org/wiki/CO2>`__ in the air. The
measured CO2 concentration can be read out in
`ppm <https://en.wikipedia.org/wiki/Parts-per_notation>`__.
With configurable events it is possible to react on changing CO2
concentration without polling.

Typical applications are automated ventilation and environmental
data logging.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            SenseAir K30
Current Consumption               | 200mW (40mA at 5V, idle)
                                  | 1750mW (350mA at 5V, measuring)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Measurement Range                 0ppm - 10000ppm
Accuracy                          ±30ppm (full-scale), ±3% (of reading)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            60 x 65 x 15mm (2.36 x 2.56 x 0.59")
Weight                            29g
================================  ============================================================

Resources
---------

* SenseAir K30 datasheet (`Download <https://github.com/Tinkerforge/co2-bricklet/raw/master/datasheets/K30_Datasheet.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/co2-bricklet/raw/master/hardware/co2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/co2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/co2-bricklet/zipball/master>`__)

.. _co2_bricklet_test:

Test your CO2 Bricklet
----------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_co2_brickv.jpg
   :scale: 100 %
   :alt: CO2 Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_co2_brickv.jpg

|test_pi_ref|


.. _co2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: CO2_hlpi.table
