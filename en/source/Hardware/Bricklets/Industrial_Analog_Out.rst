
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Analog Out Bricklet
:FIXME_shoplink: ../../../shop/bricklets/industrial-analog-out-bricklet.html

.. include:: Industrial_Analog_Out.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_analog_out_bricklet:

Industrial Analog Out Bricklet
==============================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Simultaneous programmable voltage and current output
* Outputs voltage between 0V and 10V
* Outputs current between 0mA and 24mA
* No external power supply necessary


.. _industrial_analog_out_bricklet_description:

Description
-----------

The Industrial Analog Out :ref:`Bricklet <primer_bricklets>`
can be used to extend the features of :ref:`Bricks <primer_bricks>`
by the capability to output voltage and current.

Voltage and current output are simultaneous. The voltage can
be given in mV and the current in µA.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
DAC                               DAC7760
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        up to 1.2mV / 4.8µA

Voltage Ranges                    * 0V - 5V
                                  * 0V - 10V

Current Ranges                    * 4mA - 20mA
                                  * 0mA - 20mA
                                  * 0mA - 24mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            TBDg
================================  ============================================================

Resources
---------

* DAC7760 Datasheet (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/raw/master/datasheets/dac7760.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/raw/master/hardware/industrial-analog-out-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_analog_out_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-analog-out-bricklet/zipball/master>`__)


.. _industrial_analog_out_bricklet_test:

Test your Industrial Analog Out Bricklet
----------------------------------------


.. _industrial_analog_out_bricklet_case:

Case
----


.. _industrial_analog_out_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Analog_Out_hlpi.table
