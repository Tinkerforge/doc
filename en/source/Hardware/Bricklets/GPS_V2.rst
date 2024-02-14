
:shoplink: ../../../shop/bricklets/gps-v2-bricklet.html

.. include:: GPS_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _gps_v2_bricklet:

GPS Bricklet 2.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_gps_v2_tilted_[?|?].jpg           GPS Bricklet 2.0
	Bricklets/bricklet_gps_v2_tilted_back_[?|?].jpg      GPS Bricklet 2.0
	Bricklets/bricklet_gps_v2_top_[?|?].jpg              GPS Bricklet 2.0 top
	Bricklets/bricklet_gps_v2_bottom_[?|?].jpg           GPS Bricklet 2.0 bottom
	Cases/bricklet_gps_v2_case_built_up1_[?|?].jpg       GPS Bricklet 2.0 in Case
	Cases/bricklet_gps_v2_case_built_up2_[?|?].jpg       GPS Bricklet 2.0 in Case
	Cases/bricklet_gps_v2_case_built_up3_[?|?].jpg       GPS Bricklet 2.0 in Case
	Bricklets/bricklet_gps_v2_brickv_[100|].jpg          GPS Bricklet 2.0 in Brick Viewer
	Dimensions/gps_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Supports GPS and GLONASS simultaneously
* Receives movement-, position-, altitude, time data and PPS signal
* Elevation, azimuth and SNR for each GPS/GLONASS satellite accessible
* 99 channels, 10Hz update rate
* High sensitivity and accuracy, interference canceller


.. _gps_v2_bricklet_description:

Description
-----------

The GPS :ref:`Bricklet <primer_bricklets>` 2.0 can be used to extend
:ref:`Bricks <primer_bricks>` by the possibility to
determine their position via 
`GPS <https://en.wikipedia.org/wiki/GPS>`__.
Additionally it is possible to receive movement (direction and velocity),
altitude (altitude and `geodial separation
<https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84>`__),
as well as high precise time/date information and PPS signal.

Current values for elevation, azimuth and SNR for each of the GPS and GLONASS satellites
can be read out.

The GPS module is optimized to get a fast fix, has a high input
sensitivity (-165dBm) and a update rate of 10Hz suitable for drones or the like.
Internal interference canceller rejects RF interference from other devices
like Bluetooth or Wi-Fi.

A 25 x 25mm active patch antenna with high gain is permanently attached to the bottom side
of the Bricklet and connected by a U.FL connector. You can remove the connector and
connect your own external antenna.

A CR1025 coin cell battery is also included. It is used as a battery backup for
the last satellite position data. With this information a fix can be obtained faster
if the power was lost.

.. note::

 Hardware version 2.0 does not work properly with a HAT (Zero) Brick, due to a
 hardware design flaw on the Bricklet. This flaw is fixed in hardware version 2.1.
 Existing hardware version 2.0 GPS Bricklets can be successfully connected to a
 HAT (Zero) Brick using an :ref:`Isolator Bricklet <isolator_bricklet>`.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
GPS Module Chipset                GlobalTop Firefly X1
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensitivity                       -148dBm (acquisition), -165dBm (tracking)*
Position Accuracy                 3.0m (50% CEP)*
Time to first Fix                 < 35s (without battery), < 1s (with battery)*
Update Rate                       10Hz
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 35 x 12mm (1.57 x 1.38 x 0.47")
Weight                            20g (with battery and antenna)
Current Consumption               approx. 73mA
================================  ============================================================

\* datasheet values

Resources
---------

* FireFly X1 datasheet (`Download <https://github.com/Tinkerforge/gps-v2-bricklet/raw/master/datasheets/FireFly_X1.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/gps-v2-bricklet/raw/master/hardware/gps-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/gps_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/gps-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2BgLPRK>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/gps_v2/gps-v2.1.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/gps_v2/gps-v2.1.FCStd>`__)

External Antenna
----------------

The GPS Bricklet 2.0 does not have an internal antenna. An external antenna has to be connected to the 
`U.FL <https://en.wikipedia.org/wiki/Hirose_U.FL>`__ connector.

The connector is short-circuit protected and supplies the antenna with 
3.3V/20mA. 

A compatible 25 x 25mm patch antenna is included with the Bricklet and attached to the bottom. You can
disconnect the U.FL connector and connect your own antenna. A compatible antenna with a long
lead is `available in the shop <https://www.tinkerforge.com/en/shop/gps-antenna-sma-300cm.html>`__.

The antenna should always look upwards, so if you use the antenna that is attached to the bottom
you need to mount the Bricklet accordingly.

.. _gps_v2_bricklet_test:

Test your GPS Bricklet 2.0
--------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_gps_v2_brickv.jpg
 :scale: 100 %
 :alt: GPS Bricklet 2.0 in Brick Viewer
 :align: center
 :target: ../../_images/Bricklets/bricklet_gps_v2_brickv.jpg

|test_pi_ref|


.. _gps_v2_bricklet_fix_led:

Fix LED
-------

The green LED labeled "Fix" indicates the status of the position data. The
LED blinks during fix acquisition and is turned on if a fix is achieved.

If the GPS module is battery powered the LED is turned off to save power.

.. _gps_v2_bricklet_case:

Case
----

A `laser-cut case for the GPS Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-gps-v2-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_gps_v2_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Case for GPS Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_gps_v2_case_built_up1_1000.jpg

.. include:: GPS_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/gps_v2_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for GPS Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/gps_v2_exploded.png

|bricklet_case_hint|

The case has a hole for a `U.FL to SMA adapter cable <https://www.tinkerforge.com/en/shop/gps-pigtail-cable.html>`__
that can be used to connect an `external SMA antenna <https://www.tinkerforge.com/en/shop/gps-antenna-sma-300cm.html>`__ instead of the antenna
that is glued to the bottom of the Bricklet.

.. image:: /Images/Bricklets/bricklet_gps_v2_case_with_sma_antenna_600.jpg
   :scale: 100 %
   :alt: GPS Bricklet 2.0 with SMA connector and antenna
   :align: center
   :target: ../../_images/Bricklets/bricklet_gps_v2_case_with_sma_antenna_1200.jpg

.. _gps_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: GPS_V2_hlpi.table
