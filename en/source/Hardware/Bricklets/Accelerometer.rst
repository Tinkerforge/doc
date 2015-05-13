
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Accelerometer Bricklet
:FIXME_shoplink: ../../../shop/bricklets/accelerometer-bricklet.html

.. include:: Accelerometer.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _accelerometer_bricklet:

Accelerometer Bricklet
======================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------
* 3-axis accelerometer
* 0.001G steps with 16bit resolution
* Up to ±16g full-scale range
* Full 1kHz data rate with callbacks

.. _accelerometer_bricklet_description:

Description
-----------

The Accelerometer :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure acceleration in x-, y- and z-axis. 
The measured acceleration can be read out in 
`G <http://en.wikipedia.org/wiki/G-force#Unit_and_measurement>`__. 
With configurable events it is possible to react on changing acceleration
without polling.

The Bricklet does have an LED that can be turned on trough the API,
e.g. to show that a specific acceleration was reached.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            LIS3DSH
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Acceleration                      0.001G steps, 16bit resolution
Shock survivability               10000g
full-scale range                  ±2g / ±4g / ±6g / ±8g / ±16g dynamically selectable
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            TBDg
================================  ============================================================

Resources
---------

* LIS3DSH datasheet (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/raw/master/datasheets/LIS3DSH.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/raw/master/hardware/accelerometer-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/accelerometer_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/zipball/master>`__)

.. _accelerometer_bricklet_test:

Test your Accelerometer Bricklet
--------------------------------


.. _accelerometer_bricklet_case:

Case
----


.. _accelerometer_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Accelerometer_hlpi.table
