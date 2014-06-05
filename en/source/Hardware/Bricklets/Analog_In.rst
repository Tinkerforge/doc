
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Analog In Bricklet
:shoplink: ../../../shop/bricklets/analog-in-bricklet.html

.. include:: Analog_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_in_bricklet:

Analog In Bricklet
==================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_analog_in_tilted_350.jpg",
	               "Bricklets/bricklet_analog_in_tilted_600.jpg",
	               "Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_in_vertical_100.jpg",
	             "Bricklets/bricklet_analog_in_vertical_600.jpg",
	             "Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_in_horizontal_100.jpg",
	             "Bricklets/bricklet_analog_in_horizontal_600.jpg",
	             "Analog In Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_in_master_100.jpg",
	             "Bricklets/bricklet_analog_in_master_600.jpg",
	             "Analog In Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_analog_in_case_build_up_100.jpg",
	             "Cases/bricklet_analog_in_case_build_up_600.jpg",
	             "Analog In Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_analog_in_brickv_100.jpg",
	             "Bricklets/bricklet_analog_in_brickv.jpg",
	             "Analog In Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/analog_in_bricklet_dimensions_100.png",
	             "Dimensions/analog_in_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}

.. note::

 The Analog In Bricklet is discontinued. The more precise
 :ref:`Voltage/Current Bricklet <voltage_current_bricklet>` is the recommended
 replacement.


Features
--------

* Measures voltages up to 45V (DC)
* Output in 1mV steps (12bit resolution)
* High resolution up to 1.48mV


Description
-----------

The Analog In :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure voltages.
The voltage can be read out in `Volt
<http://en.wikipedia.org/wiki/Volt>`__ directly without conversions necessary.
The device has 4 different measurement ranges.
Each range is measured with 12bit resolution such that lower voltages can be
measured more accurate than larger voltages (see technical specifications below).
The device switches between these ranges automatically.
With configurable events it is possible to react on changing
voltages without polling.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            Automatically switched voltage divider
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Voltage                           0V - 45V (DC) in 1mV steps, 12bit resolution
Measurement Range                 Automatically switched

                                  * 0V - 6.05V, ~1.48mV resolution
                                  * 0V - 10.32V, ~2.52mV resolution
                                  * 0V - 36.30V, ~8.86mV resolution
                                  * 0V - 45.00V, ~11.25mV resolution

                                  In addition, manually selectable

                                  * 0V - 3.30V, ~0.81mV resolution
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 25 x 14mm (1.18 x 0.98 x 0.55")
Weight                            6g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/analog-in-bricklet/raw/master/hardware/analog-in-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog_in_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/analog-in-bricklet/zipball/master>`__)


Connectivity
------------

The Analog In Bricklet has four terminals. With these terminals you can access
the following output signals: 5V, 3.3V as well as GND. The voltage you want
to measure can be applied between the VIN and the GND terminal.
See picture below.

.. image:: /Images/Bricklets/bricklet_analog_in_vertical_350.jpg
   :scale: 100 %
   :alt: Analog In Bricklet Terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_vertical_1200.jpg


.. _analog_in_bricklet_test:

Test your Analog In Bricklet
----------------------------

|test_intro|

|test_connect|.
Additionally connect a DC voltage source to the Bricklet.
For testing purposes the positive pole of a battery can be connected to the VIN
terminal and the negative pole to the GND terminal.

.. image:: /Images/Bricklets/bricklet_analog_in_master_600.jpg
   :scale: 100 %
   :alt: Analog In Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_master_1200.jpg

|test_tab|
If everything went as expected you can now see the voltage in Volt
and a graph that shows the voltage over time.

.. image:: /Images/Bricklets/bricklet_analog_in_brickv.jpg
   :scale: 100 %
   :alt: Analog In Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_in_brickv.jpg

|test_pi_ref|

.. _analog_in_bricklet_case:

Case
----

A `laser-cut case for the Analog In Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-analog-in-out-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_analog_in_case_build_up_350.jpg
   :scale: 100 %
   :alt: Case for Analog In Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_analog_in_case_build_up_1000.jpg

.. include:: Analog_In.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/analog_in_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Analog In Bricklet
   :align: center
   :target: ../../_images/Exploded/analog_in_exploded.png

|bricklet_case_hint|


.. _analog_in_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Analog_In_hlpi.table
