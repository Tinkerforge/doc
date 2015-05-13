
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Dual Analog In Bricklet
:FIXME_shoplink: ../../../shop/bricklets/industrial-dual-analog-in-bricklet.html

.. include:: Industrial_Dual_Analog_In.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_analog_in_bricklet:

Industrial Dual Analog In Bricklet
==================================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Independently measures two voltages between -45V and 45V
* 24 bit resolution
* Calibrated to calibration standard at room temperature
* Full-scale accuracy of 0.1% / ±4mV
* Up to 976 samples per second

.. _industrial_dual_analog_in_bricklet_description:

Description
-----------

The Industrial Dual Analog In :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure voltages.
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
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Channels                          2
Measurement Range                 -45V - 45V
Resolution                        24bit resolution
Accuracy                          0.1% / ±4mV full scale
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            TBDg
================================  ============================================================

Resources
---------

* MCP3911 Datasheet (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/raw/master/datasheets/MCP3911.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/raw/master/hardware/industrial-dual-analog-in-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_dual_analog_in_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-dual-analog-in-bricklet/zipball/master>`__)

.. _industrial_dual_analog_in_bricklet_test:

Test your Industrial Dual Analog In Bricklet
--------------------------------------------


.. _industrial_dual_analog_in_bricklet_case:

Case
----


.. _industrial_dual_analog_in_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Dual_Analog_In_hlpi.table
