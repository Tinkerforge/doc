
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Ambient Light Bricklet 2.0
:FIXME_shoplink: ../../../shop/bricklets/ambient-light-v2-bricklet.html

.. include:: Ambient_Light_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ambient_light_v2_bricklet:

Ambient Light Bricklet 2.0
==========================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Measures ambient light up to 64000 lux
* Full dynamic range from 0.01 lux to 64000 lux
* Output in 0.01 lux steps (16 bit effective resolution)

.. _ambient_light_v2_bricklet_description:

Description
-----------

The Ambient Light :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure ambient light. It is the successor of the
:ref:`Ambient Light Bricklet <ambient_light_bricklet>`. The measured
illuminance can be read out in `lux <http://en.wikipedia.org/wiki/Lux>`__.
With configurable events it is possible to react on changing illuminance
without polling.

Typical applications are illuminance dependent switching of
backlights, motors etc.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            LTR329ALS
Current Consumption               TBD
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Illumination                      0lux - 64000lux in 0.01lux steps, 16bit resolution
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            TBDg
================================  ============================================================


Resources
---------

* LTR329ALS datasheet (`Download <https://github.com/Tinkerforge/ambient-light-v2-bricklet/raw/master/datasheets/LTR329ALS.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/ambient-light-v2-bricklet/raw/master/hardware/ambient-light-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/ambient_light_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/ambient-light-v2-bricklet/zipball/master>`__)

.. _ambient_light_v2_bricklet_test:

Test your Ambient Light Bricklet 2.0
------------------------------------


.. _ambient_light_v2_bricklet_case:

Case
----


.. _ambient_light_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Ambient_Light_V2_hlpi.table
