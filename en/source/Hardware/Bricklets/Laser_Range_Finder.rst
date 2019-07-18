
.. include:: Laser_Range_Finder.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _laser_range_finder_bricklet:

Laser Range Finder Bricklet
===========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_laser_range_finder_tilted1_[?|?].jpg          Laser Range Finder Bricklet
	Bricklets/bricklet_laser_range_finder_tilted2_[?|?].jpg          Laser Range Finder Bricklet
	Bricklets/bricklet_laser_range_finder_bottom_[?|?].jpg           Laser Range Finder Bricklet
	Bricklets/bricklet_laser_range_finder_brickv_[100|].jpg          Laser Range Finder Bricklet in Brick Viewer
	Dimensions/laser_range_finder_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Laser Range Finder Bricklet is discontinued and is no longer sold. The
 :ref:`Laser Range Finder Bricklet 2.0 <laser_range_finder_v2_bricklet>` is the recommended
 replacement.


Features
--------

* Measures distance and velocity with laser pulses
* Distance range 0-40m, resolution 1cm
* Measurement frequency up to 500Hz


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
Sensor                            LIDAR-Lite (V3)
Current Consumption               | 450mW (90mA at 5V, Laser off)
                                  | 520mW (104mA at 5V, Laser on)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Distance (Range, Resolution)      0-40m, 1cm
Sample Rate                       up to 500Hz (depends on measured range)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            49 x 45 x 36mm (1.93 x 1.77 x 1.42")
Weight                            39g
================================  ============================================================


Resources
---------

* LIDAR-Lite datasheet (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/raw/master/datasheets/LIDAR-Lite-v1.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/raw/master/hardware/laser-range-finder-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/laser_range_finder_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/laser-range-finder-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2BG9vj2>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/laser_range_finder/laser-range-finder.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/laser_range_finder/laser-range-finder.FCStd>`__)


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


.. _laser_range_finder_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Laser_Range_Finder_hlpi.table
