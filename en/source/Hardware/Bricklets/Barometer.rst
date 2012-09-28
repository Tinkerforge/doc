.. include:: Barometer.substitutions


.. _barometer_bricklet:

Barometer Bricklet
==================


Features
--------

* Measures barometric pressure and altitude changes
* Resolution 0.012mbar / 0.1m
* Range 10 to 1200mbar

Description
-----------

The Barometer Bricklet can be used to extend the features of Bricks by the capability to
measure barometric pressure in range of 10 to 1200mbar with a resolution of 0.012mbar. 
An internal temperature sensor corrects the measured values. 
The device is equipped with a MS5611-01BA01 sensor which is designed to be used as
altimeter. Since the barometric pressure is changing significantly during the day 
this have to be compensated in case of usage as altimeter. One possibility
is to make sensor fusion with `IMU Brick <brick_imu>` data.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MS5611-01BA01
Pressure Range                    10 - 1200mbar
Resolution                        0.012mbar / 0.1m
Accuracy (25°C, 750mbar)          +- 1.5mbar

Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* MS5611 Datasheet (`Download <https://github.com/Tinkerforge/barometer-bricklet/raw/master/datasheets/ms5611-01ba01.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/barometer-bricklet/raw/master/hardware/barometer-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/barometer_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/barometer-bricklet/zipball/master>`__)


.. _barometer_bricklet_test:

Test your Barometer Bricklet
----------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_barometer_master_600.jpg
   :scale: 100 %
   :alt: Barometer Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_barometer_master_1200.jpg

|test_tab|
If everything went as expected you can now see the air pressure in mbar
and a graph that shows the air pressure over time.

.. image:: /Images/Bricklets/bricklet_barometer_brickv.jpg
   :scale: 100 %
   :alt: Barometer Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_barometer_brickv.jpg

|test_pi_ref|


.. _barometer_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Barometer_hlpi.table
