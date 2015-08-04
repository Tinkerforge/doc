
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Dual Analog In Bricklet
:shoplink: ../../../shop/bricklets/industrial-dual-analog-in-bricklet.html

.. include:: Industrial_Dual_Analog_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_analog_in_bricklet:

Industrial Dual Analog In Bricklet
==================================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_dual_analog_in_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_dual_analog_in_tilted_600.jpg",
	               "Industrial Dual Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_analog_in_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_dual_analog_in_horizontal_600.jpg",
	             "Industrial Dual Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_dual_analog_in_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_dual_analog_in_brickv.jpg",
	             "Industrial Dual Analog In Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_dual_analog_in_bricklet_dimensions_100.png",
	             "Dimensions/industrial_dual_analog_in_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Independently measures two voltages between -35V and +35V (DC)
* 24bit ADC for high resolution
* Calibrated
* Full-scale accuracy of 0.1% / ±4mV
* Up to 976 samples per second


.. _industrial_dual_analog_in_bricklet_description:

Description
-----------

The Industrial Dual Analog In :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to precisely measure voltages.
Both channels of the Bricklet are calibrated. The voltage measurement can
used with an extremely high level of confidence.

With configurable events it is possible to react on changing
voltages without polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
ADC                               MCP3911
Current Consumption               15mW (3mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Channels                          2
Measurement Range                 -35V to +35V (DC)
Resolution                        24bit
Accuracy                          0.1% / ±4mV full scale
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            9g
================================  ============================================================

Resources
---------

* MCP3911 datasheet (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/raw/master/datasheets/MCP3911.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/raw/master/hardware/industrial_dual_analog_in-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_dual_analog_in_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/zipball/master>`__)


Connectivity
------------

The Industrial Dual Analog In Bricklet has an 8 pole terminal.
Please see the picture below for the pinout.

.. image:: /Images/Bricklets/bricklet_industrial_dual_analog_in_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Dual Analog In Bricklet pinout
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_analog_in_caption_1200.jpg


.. _industrial_dual_analog_in_bricklet_test:

Test your Industrial Dual Analog In Bricklet
--------------------------------------------

|test_intro|

|test_connect|.
Additionally connect a DC voltage you want to measure to the Bricklet. For
testing purposes connect the 3.3V output pin to the IN0- pin and connect the
GND pin to the IN0+ pin.

|test_tab|
If everything went as expected you can now see the voltage in Volt
and a graph that shows the voltage over time.

.. image:: /Images/Bricklets/bricklet_industrial_dual_analog_in_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual Analog In Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_analog_in_brickv.jpg

|test_pi_ref|


.. _industrial_dual_analog_in_bricklet_case:

Case
----

A `laser-cut case for the Industrial Dual Analog In Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Dual Analog In Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Dual_Analog_In.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Dual Analog In Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_dual_analog_in_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Dual_Analog_In_hlpi.table
