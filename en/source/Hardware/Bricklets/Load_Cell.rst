
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Load Cell Bricklet
:FIXME_shoplink: ../../../shop/bricklets/load-cell-bricklet.html

.. include:: Load_Cell.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _load_cell_bricklet:

Load Cell Bricklet
==================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Measures output of load cells
* Integrates 24bit ADC for high resolution
* Up to 80 weight measurements per second

.. _load_cell_bricklet_description:

Description
-----------

The Load Cell :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure load cells.

A load cell that is connected to the Bricklet can be easily calibrated
with only one known weight. It is possible to measure
weight differences of few grams in objects that weigh many kilograms.

Load cells with different weight ranges are available in the shop:

* `x - y kg <TBD>`
* `x - y kg <TBD>`
* `x - y kg <TBD>`
* `x - y kg <TBD>`

The Bricklet does have an LED that can be turned on trough the API,
e.g. to show that a weight measurement is in range.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            HX711
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        24bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 30 x 14mm (1.18 x 1.18 x 0.55")
Weight                            TBDg
================================  ============================================================

Resources
---------

* HX711 datasheet (`Download <https://github.com/Tinkerforge/load-cell-bricklet/raw/master/datasheets/hx711.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/load-cell-bricklet/raw/master/hardware/load-cell-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/load_cell_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/load-cell-bricklet/zipball/master>`__)


Connectivity
------------


.. _load_cell_bricklet_test:

Test your Load Cell Bricklet
----------------------------


Calibration
-----------


.. _load_cell_bricklet_case:

Case
----


.. _load_cell_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Load_Cell_hlpi.table
