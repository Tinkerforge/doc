
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Temperature Bricklet
:shoplink: ../../../shop/bricklets/temperature-bricklet.html

.. include:: Temperature.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _temperature_bricklet:

Temperature Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_temperature_tilted_[?|?].jpg           Temperature Bricklet
	Bricklets/bricklet_temperature_vertical_[?|?].jpg         Temperature Bricklet
	Bricklets/bricklet_temperature_horizontal_[?|?].jpg       Temperature Bricklet
	Bricklets/bricklet_temperature_master_[100|600].jpg       Temperature Bricklet with Master Brick
	Cases/bricklet_ambient_light_case_built_up_[?|?].jpg      Temperature Bricklet in Case
	Bricklets/bricklet_temperature_brickv_[100|].jpg          Temperature Bricklet in Brick Viewer
	Dimensions/temperature_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures ambient temperature with **0.5°C** accuracy
* Temperature range from -40°C to 125°C
* Output in 0.1°C steps (12bit resolution)


.. _temperature_bricklet_description:

Description
-----------

The Temperature :ref:`Bricklet <primer_bricklets>` can be used to
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
Sensor                            TMP102
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Ambient Temperature               -40°C to 125°C in 0.1°C steps (12bit resolution)
Accuracy                          0.5°C
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5 mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* TMP102 datasheet (`Download <https://github.com/Tinkerforge/temperature-bricklet/raw/master/datasheets/tmp102.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/temperature-bricklet/raw/master/hardware/temperature-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/temperature_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/temperature-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2gCmYzG>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/temperature/temperature.step>`__,  `FreeCAD <http://download.tinkerforge.com/3d/bricklets/temperature/temperature.FCStd>`__)



.. _temperature_bricklet_test:

Test your Temperature Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_temperature_master_600.jpg
   :scale: 100 %
   :alt: Temperature Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_temperature_brickv.jpg
   :scale: 100 %
   :alt: Temperature Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_brickv.jpg

Put your finger on the sensor to see the
temperature rising (or falling if it is extremely warm in your room).

|test_pi_ref|


.. _temperature_bricklet_case:

Case
----

A `laser-cut case for the Temperature Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Temperature Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Temperature.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Temperature Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _temperature_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Temperature_hlpi.table
