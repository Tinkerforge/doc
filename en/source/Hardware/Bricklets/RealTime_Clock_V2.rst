
:shoplink: ../../../shop/bricklets/real-time-clock-v2-bricklet.html

.. include:: RealTime_Clock_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _real_time_clock_v2_bricklet:

Real-Time Clock Bricklet 2.0
============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_real_time_clock_v2_tilted_[?|?].jpg           Real-Time Clock Bricklet 2.0
	Bricklets/bricklet_real_time_clock_v2_top_[?|?].jpg              Real-Time Clock Bricklet 2.0
	Cases/bricklet_real_time_clock_v2_case_[?|?].jpg                 Real-Time Clock Bricklet 2.0 in case
	Bricklets/bricklet_real_time_clock_v2_brickv_[100|].jpg          Real-Time Clock Bricklet 2.0 in Brick Viewer
	Dimensions/real_time_clock_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Battery-backed real-time clock
* Hundredth of a second time resolution
* Low power consumption in battery mode


.. _real_time_clock_v2_bricklet_description:

Description
-----------

The battery-backed Real-Time Clock :ref:`Bricklet <primer_bricklets>` 2.0 can be
used to extend the features of :ref:`Bricks <primer_bricks>` with the
capability to accurately keep date and time over long time periods even if
the Brick is not constantly powered.

This Bricklet can also be used to keep the system time of a :ref:`RED Brick
<red_brick>` (using this `example program <https://github.com/Tinkerforge/red-brick/tree/master/programs/rtc_time>`__)
or a :ref:`Raspberry Pi <embedded_raspberry_pi>`.

The Real-Time Clock Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            PCF85263A
Current Consumption               | 40mW (8mA at 5V)
                                  | 1.05µW (680nA at 1.55V) in battery mode*
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Date Format                       2000-01-01 to 2099-12-31 including weekday and leap years
Time Format                       24h with hundredths of a second
Accuracy                          | ±20ppm (±52.6 seconds per month) non-calibrated
                                  | down to ±1ppm (±2.6 seconds per month) calibrated*
Battery Type                      SR621SW / 364 / SR60 / S621 / SG1 or LR60 / L621 / AG1
Battery Dimensions                6.8 x 2.2mm (0.27 x 0.09")
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 25 x 5mm (0.98 x 0.98 x 0.19")
Weight                            3g
================================  ============================================================

\* datasheet value

Resources
---------

* PCF85263A datasheet (`Download <https://github.com/Tinkerforge/real-time-clock-bricklet/raw/master/datasheets/PCF85263A.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/real-time-clock-v2-bricklet/raw/master/hardware/real-time-clock-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/real_time_clock_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/real-time-clock-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2HQg0zb>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/real_time_clock_v2/real-time-clock-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/real_time_clock_v2/real-time-clock-v2.FCStd>`__)


.. _real_time_clock_v2_bricklet_test:

Test your Real-Time Clock Bricklet 2.0
--------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the Bricklet's and the local
date and time counting up.

You can set the Bricklet's date and time you your local time by clicking the
"Save Local" button.

.. image:: /Images/Bricklets/bricklet_real_time_clock_v2_brickv.jpg
   :scale: 100 %
   :alt: Real-Time Clock Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_real_time_clock_v2_brickv.jpg

|test_pi_ref|


.. _real_time_clock_v2_bricklet_case:

Case
----

A `laser-cut case for the Real-Time Clock Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-real-time-clock-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_real_time_clock_v2_case_350.jpg
   :scale: 100 %
   :alt: Case for Real-Time Clock Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_real_time_clock_v2_case_1000.jpg

.. include:: RealTime_Clock_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/real_time_clock_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Real-Time Clock Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/real_time_clock_exploded.png

|bricklet_case_hint|


.. _real_time_clock_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RealTime_Clock_V2_hlpi.table
