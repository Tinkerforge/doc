
:DISABLED_shoplink: ../../../shop/bricklets/industrial-dual-0-20ma-v2-bricklet.html

.. include:: Industrial_Dual_020mA_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_0_20ma_v2_bricklet:

Industrial Dual 0-20mA Bricklet 2.0
===================================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_0_20ma_v2_tilted_[?|?].jpg           Industrial Dual 0-20mA Bricklet 2.0
	Bricklets/bricklet_industrial_dual_0_20ma_v2_horizontal_[?|?].jpg       Industrial Dual 0-20mA Bricklet 2.0
	Bricklets/bricklet_industrial_dual_0_20ma_v2_master_[100|600].jpg       Industrial Dual 0-20mA Bricklet 2.0 with Master Brick
	Cases/bricklet_industrial_dual_0_20ma_v2_case_[100|600].jpg             Industrial Dual 0-20mA Bricklet 2.0 with case
	Bricklets/bricklet_industrial_dual_0_20ma_v2_brickv_[100|].jpg          Industrial Dual 0-20mA Bricklet 2.0 in Brick Viewer
	Dimensions/industrial_dual_0_20ma_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Precision current sensor, measures `currents between 0 and 22.5mA
  <https://en.wikipedia.org/wiki/Current_loop>`__
* Can read out any IEC 60381-1 type 2 and type 3 sensor
* High accuracy (0.15%), resolution (up to 0.172µA) and sample rate (up to 240 SPS)
* It is possible to detect if a sensor is connected/faulty


.. _industrial_dual_0_20ma_v2_bricklet_description:

Description
-----------

The Industrial Dual 0-20mA :ref:`Bricklet <primer_bricklets>` 2.0
can be used to extend the features of :ref:`Bricks <primer_bricks>`
by the capability to measure currents between 0 and 22.5mA.

This Bricklet can be used to read out up to two IEC 60381-1 type 2 and
type 3 sensor.

The measured current can be read out in nA.
With configurable events it is possible to react on changing
currents without polling.

The Industrial Dual 0-20mA Bricklet 2.0 has a 7 pole Bricklet connector and is
connected to a Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MCP3423
Current Consumption               50mw (10mA at 5V)
Maximum Input Voltage             48V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Measurement Range                 0mA - 22.5mA
Supported Sensors                 IEC 60381-1 type 2 and type 3
Accuracy                          0.15% with 40ppm/°C
Resolution                        up to 0.172µA (18bit)
Sample Rate                       up to 240 samples per second
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            8g
================================  ============================================================


Resources
---------

* MCP3423 datasheet (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-bricklet/raw/master/datasheets/mcp3423.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-v2-bricklet/raw/master/hardware/industrial-dual-0-20ma-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_dual_0_20ma_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-dual-0-20ma-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2LQMbnm>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_dual_0_20ma_v2/industrial-dual-0-20ma-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_dual_0_20ma_v2/industrial-dual-0-20ma-v2.FCStd>`__)


Connectivity
------------

See below for connection diagrams for type 2/3 sensor.

..
  TODO: Update image?

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_connectivity_600.jpg
   :scale: 100 %
   :alt: Connection diagram for type 2/3 sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_connectivity_1200.jpg

Both sensor ports ("Sensor 0" and "Sensor 1") can be used independently.
Notice the battery symbol in the picture above.
Over the external power supply input of the Bricklet (up to 48V) the sensors can
be powered.


.. _industrial_dual_0_20ma_v2_bricklet_test:

Test your Industrial Dual 0-20mA Bricklet 2.0
---------------------------------------------

|test_intro|

|test_connect| and attach a current source (see picture below).
In this example we use a 4-20mA ambient light sensor.

..
  TODO: Update image?

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_sensor_600.jpg
   :scale: 100 %
   :alt: Industrial Dual 0-20mA Bricklet connected to ambient light sensor
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_sensor_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_industrial_dual_0_20ma_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual 0-20mA Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_0_20ma_v2_brickv.jpg

Interact with the sensor to see the current changing in the Brick Viewer.

|test_pi_ref|


.. _industrial_dual_0_20ma_v2_bricklet_case:

Case
----

A `laser-cut case for the Industrial Dual 0-20mA Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Dual 0-20mA Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Dual_020mA_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Dual 0-20mA Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_dual_0_20ma_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Dual_020mA_V2_hlpi.table
