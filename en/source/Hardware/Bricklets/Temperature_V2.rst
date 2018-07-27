
:DISABLED_shoplink: ../../../shop/bricklets/temperature-v2-bricklet.html

.. include:: Temperature_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _temperature_v2_bricklet:

Temperature Bricklet 2.0
========================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_temperature_v2_tilted_[?|?].jpg           Temperature Bricklet 2.0
	Bricklets/bricklet_temperature_v2_horizontal_[?|?].jpg       Temperature Bricklet 2.0
	Bricklets/bricklet_temperature_v2_master_[100|600].jpg       Temperature Bricklet 2.0 with Master Brick
	Cases/bricklet_temperature_v2_case_[100|600].jpg             Temperature Bricklet 2.0 with case
	Bricklets/bricklet_temperature_v2_brickv_[100|].jpg          Temperature Bricklet 2.0 in Brick Viewer
	Dimensions/temperature_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures ambient temperature with **0.2°C** accuracy
* Temperature range from -40°C to 125°C
* Output in 0.01°C steps


.. _temperature_v2_bricklet_description:

Description
-----------

The Temperature :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure temperature.
The measured temperature can be read out in `°C
<https://en.wikipedia.org/wiki/Degree_Celsius>`__.
With configurable events it is possible to react on changing
temperatures without polling.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            STS3x
Current Consumption               28mW (5.6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Ambient Temperature               -40°C to 125°C in 0.01°C steps
Accuracy                          typical 0.2°C in the range of 0°C to 65°C
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5 mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* STS3x datasheet (`Download <https://github.com/Tinkerforge/temperature-bricklet/raw/master/datasheets/STS3x.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/temperature-v2-bricklet/raw/master/hardware/temperature-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/temperature_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/temperature-v2-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _temperature_v2_bricklet_test:

Test your Temperature Bricklet 2.0
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_temperature_v2_brickv.jpg
   :scale: 100 %
   :alt: Temperature Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_v2_brickv.jpg

Put your finger on the sensor to see the
temperature rising (or falling if it is extremely warm in your room).

|test_pi_ref|


.. _temperature_v2_bricklet_case:

Case
----


A `laser-cut case for the Temperature Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Temperature Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Temperature_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Temperature Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _temperature_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Temperature_V2_hlpi.table
