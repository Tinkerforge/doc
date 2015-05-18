
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Analog Out Bricklet 2.0
:FIXME_shoplink: ../../../shop/bricklets/analog-out-v2-bricklet.html

.. include:: Analog_Out_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _analog_out_v2_bricklet:

Analog Out Bricklet 2.0
=======================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Generates a configurable voltage between 0V and 12V

.. _analog_out_v2_bricklet_description:

Description
-----------

The Analog Out :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to generate voltages between 0V and 12V.
The voltage can be configured directly in `Volt
<http://en.wikipedia.org/wiki/Volt>`__ without any conversion.
The device is equipped with a 12-bit `Digital-to-Analog Converter (DAC)
<http://en.wikipedia.org/wiki/Digital-to-analog_converter>`__.

For output voltages above 5V, it is necessary to add an external supply voltage.
The maximum reachable voltage will be the value of the supply voltage. I.e.
if you want to reach an output voltage of 12V, you need to connect a supply
voltage of at least 12V.
For output voltages below 5V, you can `connect "5V Out" to "VIN" <TBD>`__.



Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
DAC                               MCP4725
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Voltage                           0V - 12V*, 12bit resolution
Maximum Output Current            24mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 30 x 14mm (1.38 x 1.18 x 0.55")
Weight                            TBDg
================================  ============================================================

\* The maximum output voltage depends on the supply voltage.

Resources
---------

* MCP4725 datasheet (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/raw/master/datasheets/MCP4725.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/raw/master/hardware/analog-out-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog_out_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/zipball/master>`__)

.. _analog_out_v2_bricklet_test:

Test your Analog Out Bricklet 2.0
---------------------------------


.. _analog_out_v2_bricklet_case:

Case
----


.. _analog_out_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Analog_Out_V2_hlpi.table
