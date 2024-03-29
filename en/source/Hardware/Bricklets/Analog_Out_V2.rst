
.. include:: Analog_Out_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_out_v2_bricklet:

Analog Out Bricklet 2.0
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_analog_out_v2_tilted1_[?|?].jpg          Analog Out Bricklet 2.0
	Bricklets/bricklet_analog_out_v2_tilted2_[?|?].jpg          Analog Out Bricklet 2.0
	Bricklets/bricklet_analog_out_v2_horizontal_[?|?].jpg       Analog Out Bricklet 2.0
	Cases/bricklet_analog_in_v2_case_built_up_[?|?].jpg         Analog Out Bricklet 2.0 in Gehäuse
	Bricklets/bricklet_analog_out_v2_brickv_[100|].jpg          Analog Out Bricklet 2.0 in Brick Viewer
	Dimensions/analog_out_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Analog Out Bricklet 2.0 is discontinued and is no longer sold. The
 :ref:`Analog Out Bricklet 3.0 <analog_out_v3_bricklet>` is the recommended
 replacement.

Features
--------

* Generates a configurable voltage between 0V and 12V*
* Specification in 1mV steps (12bit resolution)


.. _analog_out_v2_bricklet_description:

Description
-----------

The Analog Out :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to generate voltages between 0V and 12V*. It is the successor of the
:ref:`analog_out_bricklet` with a bigger output voltage range.
The voltage can be configured directly in `Volt
<https://en.wikipedia.org/wiki/Volt>`__ without any conversion.
The device is equipped with a 12bit `Digital-to-Analog Converter (DAC)
<https://en.wikipedia.org/wiki/Digital-to-analog_converter>`__.

For output voltages above 5V, it is necessary to add an external supply voltage.
The maximum reachable output voltage will be the value of the supply voltage.
For example, if you want to reach an output voltage of 12V, you need to connect
a supply voltage of at least 12V.
For output voltages below 5V, you can :ref:`connect the 5V and VIN terminals
<analog_out_v2_bricklet_connectivity>`.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
DAC                               MCP4725
Current Consumption               < 5mW (< 1mA at 5V, without load)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Voltage                           0V - 12V* in 1mV steps, 12bit resolution
Maximum Output Current            24mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 30 x 14mm (1.38 x 1.18 x 0.55")
Weight                            8g
================================  ============================================================

\* The maximum output voltage depends on the supply voltage at the VIN terminal.

Resources
---------

* MCP4725 datasheet (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/raw/master/datasheets/MCP4725.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/raw/master/hardware/analog-out-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog_out_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <https://autode.sk/2Bcx3vA>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/analog_out_v2/analog-out-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/analog_out_v2/analog-out-v2.FCStd>`__)

.. _analog_out_v2_bricklet_connectivity:

Connectivity
------------

The Analog Out Bricklet 2.0 has five terminals. A DC voltage source (maximum
15V) has to be connected to the VIN terminal and the adjacent GND terminal.
The Bricklet uses this input voltage to created the configurable output voltage
for the VOUT terminal. The 5V terminal is an additional output with fixed 5V
you can use to power things. It can also be connected to the VIN terminal to
produce output voltages up to 5V at the VOUT terminal without the need for an
additional external power supply.

.. image:: /Images/Bricklets/bricklet_analog_out_v2_horizontal_350.jpg
    :scale: 100 %
    :alt: Analog Out Bricklet 2.0 Terminals
    :align: center
    :target: ../../_images/Bricklets/bricklet_analog_out_v2_horizontal_1200.jpg


.. _analog_out_v2_bricklet_test:

Test your Analog Out Bricklet 2.0
---------------------------------

|test_intro|

|test_connect|.
Additionally connect a DC voltage source to the Bricklet's VIN and GND
terminals. For testing purposes connect the 5V output terminal to the VIN
terminal. The GND terminals are already connected internally.

|test_tab|
In this tab you can configure the voltage on the VOUT terminal. The maximum
VOUT voltage is limited by the connected VIN voltage.
For test purposes, you can measure the VOUT voltage with a voltmeter.
If everything went as expected the voltage on the voltmeter and the voltage
you have configured should be identical.

.. image:: /Images/Bricklets/bricklet_analog_out_v2_brickv.jpg
   :scale: 100 %
   :alt: Analog Out Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_analog_out_v2_brickv.jpg

|test_pi_ref|


.. _analog_out_v2_bricklet_case:

Case
----

A `laser-cut case for the Analog Out Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-analog-in-out-v2-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_analog_in_v2_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Analog Out Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_analog_in_v2_case_built_up_1000.jpg

.. include:: Analog_Out_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/analog_in_v2_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Analog Out Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/analog_in_v2_exploded.png

|bricklet_case_hint|


.. _analog_out_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Analog_Out_V2_hlpi.table
