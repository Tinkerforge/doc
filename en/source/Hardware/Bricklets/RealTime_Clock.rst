
:shoplink: ../../../shop/bricklets/real-time-clock-bricklet.html

.. include:: RealTime_Clock.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _real_time_clock_bricklet:

Real-Time Clock Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_real_time_clock_tilted_[?|?].jpg           Real-Time Clock Bricklet
	Bricklets/bricklet_real_time_clock_horizontal_[?|?].jpg       Real-Time Clock Bricklet
	Bricklets/bricklet_real_time_clock_red_master_[100|600].jpg   Real-Time Clock Bricklet with RED Brick and Master Brick
	Cases/bricklet_real_time_clock_case_built_up_[?|?].jpg        Real-Time Clock Bricklet in Case
	Bricklets/bricklet_real_time_clock_brickv_[100|].jpg          Real-Time Clock Bricklet in Brick Viewer
	Dimensions/real_time_clock_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Real-Time Clock Bricklet is discontinued. We are selling our remaining stock. The
 :ref:`Real-Time Clock Bricklet 2.0 <real_time_clock_v2_bricklet>` is the recommended
 replacement.


Features
--------

* Battery-backed real-time clock
* Hundredth of a second time resolution
* Low power consumption in battery mode


.. _real_time_clock_bricklet_description:

Description
-----------

The battery-backed Real-Time Clock :ref:`Bricklet <primer_bricklets>` can be
used to extend the features of :ref:`Bricks <primer_bricks>` with the
capability to accurately keep date and time over long time periods even if
the Brick is not constantly powered.

This Bricklet can also be used to keep the system time of a :ref:`RED Brick
<red_brick>` (using this `example program <https://github.com/Tinkerforge/red-brick/tree/master/programs/rtc_time>`__)
or a :ref:`Raspberry Pi <embedded_raspberry_pi>`.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            PCF85263A
Current Consumption               | < 5mW (< 1mA at 5V)
                                  | 1.05µW (680nA at 1.55V) im battery mode*
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
* Schematic (`Download <https://github.com/Tinkerforge/real-time-clock-bricklet/raw/master/hardware/real-time-clock-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/real_time_clock_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/real-time-clock-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2BFtoCC>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/real_time_clock/real-time-clock.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/real_time_clock/real-time-clock.FCStd>`__)

.. _real_time_clock_bricklet_test:

Test your Real-Time Clock Bricklet
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the Bricklet's and the local
date and time counting up.

You can set the Bricklet's date and time you your local time by clicking the
"Save Local" button.

.. image:: /Images/Bricklets/bricklet_real_time_clock_brickv.jpg
   :scale: 100 %
   :alt: Real-Time Clock Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_real_time_clock_brickv.jpg

|test_pi_ref|


.. _real_time_clock_bricklet_case:

Case
----

A `laser-cut case for the Real-Time Clock Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-real-time-clock-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_real_time_clock_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Real-Time Clock Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_real_time_clock_case_built_up_1000.jpg

.. include:: RealTime_Clock.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/real_time_clock_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Real-Time Clock Bricklet
   :align: center
   :target: ../../_images/Exploded/real_time_clock_exploded.png

|bricklet_case_hint|

.. _real_time_clock_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: RealTime_Clock_hlpi.table
