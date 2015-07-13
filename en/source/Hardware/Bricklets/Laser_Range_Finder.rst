
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Laser Range Finder Bricklet
:FIXME_shoplink: ../../../shop/bricklets/laser-range-finder-bricklet.html

.. include:: Laser_Range_Finder.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _laser_range_finder_bricklet:

Laser Range Finder Bricklet
===========================

.. note::
 This Bricklet is currently work-in-progress!


Features
--------

* Measures distance and velocity with laser pulses
* Distance range 0-40m, resolution 1cm
* Velocity range up to 0-127m/s, resolution up to 0.1m/s


.. _laser_range_finder_bricklet_description:

Description
-----------

The Laser Range Finder :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure distances and velocity. The distance is measured with
the help of a laser pulse and the `time-of-flight
<https://en.wikipedia.org/wiki/Time_of_flight>`__ principle.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               TBDmA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Distance (Range, Resolution)      * 0-40m, 1cm

Velocity (Range, Resolution)      * 0-12.7m/s, 0.1m/s
                                  * 0-31.75m/s, 0.25m/s
                                  * 0-63.5m/s, 0.5m/s
                                  * 0-127m/s, 1.0m/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            49 x 36 x 48mm (1.93 x 1.42 x 1.89")
Weight                            TBDg
================================  ============================================================

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/raw/master/hardware/laser-range-finder-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/laser_range_finder_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/zipball/master>`__)

.. _laser_range_finder_bricklet_test:

Test your Laser Range Finder Bricklet
-------------------------------------

|test_intro|

|test_connect|.

|test_tab|
Click the "Enable Laser" checkbox to enable the laser.
If everything went as expected you can now see the measured distance
of the sensor and a graph that shows the distance over time. In the image
below we slowly moved a hand away from the sensor and to the sensor again.

.. image:: /Images/Bricklets/bricklet_laser_range_finder_brickv.jpg
   :scale: 100 %
   :alt: Laser Range Finder Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_laser_range_finder_brickv.jpg

|test_pi_ref|


.. _laser_range_finder_bricklet_case:

Case
----


.. _laser_range_finder_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Laser_Range_Finder_hlpi.table
