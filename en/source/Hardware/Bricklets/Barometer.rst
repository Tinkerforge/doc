.. include:: Barometer.substitutions


.. _barometer_bricklet:

Barometer Bricklet
==================


Features
--------

* Measures air pressure and altitude changes
* Resolution 0.012mbar / 0.1m
* Range 10 to 1200mbar


Description
-----------

The Barometer Bricklet can be used to extend the features of Bricks by the
capability to measure air pressure in range of 10 to 1200mbar with a resolution
of 0.012mbar. The measurement is temperature compensated internally.
The Bricklet is equipped with a MS5611-01BA01 sensor which is designed to be
used as an altimeter, too. But since the air pressure is changing significantly
even over a short period time the achievable accuracy is limited. One possible
solution to achieve higher accuracy and stability of the altitude measurement is
to perform sensor fusion with the sensor data of an :ref:`IMU Brick <imu_brick>`.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MS5611-01BA01
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Pressure Range                    10 - 1200mbar
Resolution                        0.012mbar / 0.1m
Accuracy (25°C, 750mbar)          +- 1.5mbar
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
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
