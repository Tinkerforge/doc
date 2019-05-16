
:DISABLED_shoplink: ../../../shop/bricklets/laser-range-finder-v2-bricklet.html

.. include:: Laser_Range_Finder_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _laser_range_finder_v2_bricklet:

Laser Range Finder Bricklet 2.0
===============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_laser_range_finder_v2_tilted_[?|?].jpg           Laser Range Finder Bricklet 2.0
	Bricklets/bricklet_laser_range_finder_v2_tilted2_[?|?].jpg          Laser Range Finder Bricklet 2.0
	Bricklets/bricklet_laser_range_finder_v2_top_[?|?].jpg              Laser Range Finder Bricklet 2.0
	Bricklets/bricklet_laser_range_finder_v2_bottom_[?|?].jpg           Laser Range Finder Bricklet 2.0
	Bricklets/bricklet_laser_range_finder_v2_brickv_[100|].jpg          Laser Range Finder Bricklet 2.0 in Brick Viewer
	Dimensions/laser_range_finder_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures distance and velocity with laser pulses
* Distance range 0-40m, resolution 1cm
* Measurement frequency up to 500Hz


.. _laser_range_finder_v2_bricklet_description:

Description
-----------

The Laser Range Finder :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure distances and velocity. The distance is measured with
the help of a laser pulse and the `time-of-flight
<https://en.wikipedia.org/wiki/Time_of_flight>`__ principle.

The Laser Range Finder Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            LIDAR-Lite (V3)
Current Consumption               | 230mW (46mA at 5V, Laser off)
                                  | 455mW (91mA at 5V, Laser on)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Distance (Range, Resolution)      0-40m, 1cm
Sample Rate                       up to 500Hz (depends on measured range)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            49 x 45 x 36mm (1.93 x 1.77 x 1.42")
Weight                            30g
================================  ============================================================


Resources
---------

* LIDAR-Lite V3 datasheet (`Download <https://github.com/Tinkerforge/laser-range-finder-v2-bricklet/raw/master/datasheets/lidar-lite-v3.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/laser-range-finder-v2-bricklet/raw/master/hardware/laser-range-finder-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/laser_range_finder_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/laser-range-finder-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2Hx8J8y>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/laser_range_finder_v2/laser-range-finder-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/laser_range_finder_v2/laser-range-finder-v2.FCStd>`__)


.. _laser_range_finder_v2_bricklet_test:

Test your Laser Range Finder Bricklet 2.0
-----------------------------------------

|test_intro|

|test_connect|.

|test_tab|
Click the "Enable Laser" checkbox to enable the laser.
If everything went as expected you can now see the measured distance
of the sensor and a graph that shows the distance over time. In the image
below we slowly moved a hand away from the sensor and to the sensor again.

.. image:: /Images/Bricklets/bricklet_laser_range_finder_v2_brickv.jpg
   :scale: 100 %
   :alt: Laser Range Finder Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_laser_range_finder_v2_brickv.jpg

|test_pi_ref|


.. _laser_range_finder_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Laser_Range_Finder_V2_hlpi.table
