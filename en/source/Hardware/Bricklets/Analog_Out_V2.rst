
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
The device is equipped with a 12bit `Digital-to-Analog Converter (DAC)
<http://en.wikipedia.org/wiki/Digital-to-analog_converter>`__.

For output voltages above 5V, it is necessary to add an external supply voltage.
The maximum reachable voltage will be the value of the supply voltage. For
example, if you want to reach an output voltage of 12V, you need to connect a
supply voltage of at least 12V.
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
Voltage                           0V - 12V* in 1mV steps, 12bit resolution
Maximum Output Current            24mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            35 x 30 x 14mm (1.38 x 1.18 x 0.55")
Weight                            TBDg
================================  ============================================================

\* The maximum output voltage depends on the supply voltage at the VIN terminal.

Resources
---------

* MCP4725 datasheet (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/raw/master/datasheets/MCP4725.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/raw/master/hardware/analog-out-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/analog_out_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/analog-out-v2-bricklet/zipball/master>`__)


Connectivity
------------

The Analog Out Bricklet 2.0 has five terminals. A DC voltage source (maximum
15V) has to be connected to the VIN terminal and the adjacent GND terminal.
The Bricklet uses this input voltage to created the configurable output voltage
for the VOUT terminal. The 5V terminal is an additional output with fixed 5V
you can use to power things. It can also be connected to the VIN terminal.

.. image:: /Images/Bricklets/bricklet_analog_out_v2_vertical_350.jpg
    :scale: 100 %
    :alt: Analog Out Bricklet 2.0 Terminals
    :align: center
    :target: ../../_images/Bricklets/bricklet_analog_out_v2_vertical_1200.jpg


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


.. _analog_out_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Analog_Out_V2_hlpi.table
