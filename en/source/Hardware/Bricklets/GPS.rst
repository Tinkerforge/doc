
:shoplink: ../../../shop/bricklets/gps-bricklet.html

.. include:: GPS.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _gps_bricklet:

GPS Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_gps_tilted_[?|?].jpg           GPS Bricklet
	Bricklets/bricklet_gps_horizontal_[?|?].jpg       GPS Bricklet
	Bricklets/bricklet_gps_battery_[100|600].jpg      GPS Bricklet
	Cases/bricklet_gps_case_[100|600].jpg             GPS Bricklet in Case
	Bricklets/bricklet_gps_brickv_[100|].jpg          GPS Bricklet in Brick Viewer
	Dimensions/gps_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

Features
--------

* Receives movement-, position-, altitude and time data
* Internal antenna, external antenna optional
* 66 channels, 10Hz update rate
* High sensitivity and accuracy, interference canceller


.. _gps_bricklet_description:

Description
-----------

The GPS :ref:`Bricklet <primer_bricklets>` can be used to extend
:ref:`Bricks <primer_bricks>` by the possibility to
determine their position via 
`GPS <https://en.wikipedia.org/wiki/GPS>`__.
Additionally it is possible to receive movement (direction and velocity),
altitude (altitude and `geodial separation
<https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84>`__),
as well as high precise time and date information.

The used GPS module is optimized to get a fast fix, has a high input
sensitivity (-165dBm) and a update rate of 10Hz suitable for drones or the like.
Internal interference canceller rejects RF interference from other devices
like Bluetooth or Wi-Fi.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
GPS Module Chipset                MTK MT3339 (PA6H module)
Current Consumption               35mA (acquisition), 30mA (tracking)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensitivity                       -148dBm (acquisition), -165dBm (tracking)*
Position Accuracy                 3.0m (50% CEP)*
Time to first Fix                 < 35s (without battery), < 1s (with battery)*
Update Rate                       10Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 35 x 12mm (1.57 x 1.38 x 0.47")
Weight                            12g (without battery)
================================  ============================================================

\* datasheet values

Resources
---------

* PA6H datasheet (`Download <https://github.com/Tinkerforge/gps-bricklet/raw/master/datasheets/FGPMMOPA6H.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/gps-bricklet/raw/master/hardware/gps-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/gps_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/gps-bricklet/zipball/master>`__)


External Antenna
----------------

With an `U.FL <https://en.wikipedia.org/wiki/Hirose_U.FL>`__ connector
external antennas can be attached. This is makes sense if it should be
mounted at another position than the Bricklet or if the reception should
be improved. The module detects automatically an external antenna
and switches over.

The connector is short-circuit protected and supplies the antenna with 
3.3V/28mA. The external antenna should fulfill the following requirements:

================================  ============================================================
Property                          Value
================================  ============================================================
Polarization                      Right-hand circular polarized
Frequency Received                1.57542GHz ± 1.023MHz
Power Supply                      3.0V to 3.6V with 4mA to 20mA
Gain                              > +15dBi
Impedance                         50Ω
Noise Figure                      < 1.5dB
================================  ============================================================



.. _gps_bricklet_test:

Test your GPS Bricklet
----------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_gps_brickv.jpg
 :scale: 100 %
 :alt: GPS Bricklet in Brick Viewer
 :align: center
 :target: ../../_images/Bricklets/bricklet_gps_brickv.jpg

|test_pi_ref|


.. _gps_bricklet_fix_led:

Fix LED
-------

The blue LED labeled "Fix" indicates that status of the position data. If
there is no fix (position data is not valid) the LED is blinking with a 1
second pattern. Once a fix is achieved the blue LED is turned of and the
position data is valid.


.. _gps_bricklet_case:

Case
----

A `laser-cut case for the GPS Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-gps-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_gps_case_350.jpg
   :scale: 100 %
   :alt: Case for GPS Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_gps_case_1000.jpg

.. include:: GPS.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/gps_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for GPS Bricklet
   :align: center
   :target: ../../_images/Exploded/gps_exploded.png

|bricklet_case_hint|


.. _gps_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: GPS_hlpi.table
