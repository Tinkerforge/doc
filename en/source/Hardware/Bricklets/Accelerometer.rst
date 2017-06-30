
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Accelerometer Bricklet
:shoplink: ../../../shop/bricklets/accelerometer-bricklet.html

.. include:: Accelerometer.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _accelerometer_bricklet:

Accelerometer Bricklet
======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_accelerometer_tilted_[?|?].jpg           Accelerometer Bricklet
	Bricklets/bricklet_accelerometer_horizontal_[?|?].jpg       Accelerometer Bricklet
	Cases/bricklet_accelerometer_case_built_up_[?|?].jpg        Accelerometer Bricklet in Case
	Bricklets/bricklet_accelerometer_brickv_[100|].jpg          Accelerometer Bricklet in Brick Viewer
	Dimensions/accelerometer_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 3-axis accelerometer
* 0.001g steps with 16bit resolution
* Up to ±16g full-scale range
* Full 1kHz data rate with callbacks

.. _accelerometer_bricklet_description:

Description
-----------

The Accelerometer :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure acceleration in x-, y- and z-axis.
The measured acceleration can be read out in
`g <https://en.wikipedia.org/wiki/G-force#Unit_and_measurement>`__.
With configurable events it is possible to react on changing acceleration
without polling.

The Bricklet has an LED that can be turned on trough the API, e.g. to show
that a specific acceleration was reached.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            LIS3DSH
Current Consumption               5mW (1mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Acceleration                      0.001g steps, 16bit resolution
Shock survivability               10000g
Full-scale range                  ±2g / ±4g / ±6g / ±8g / ±16g selectable with API
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            2g
================================  ============================================================

Resources
---------

* LIS3DSH datasheet (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/raw/master/datasheets/LIS3DSH.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/raw/master/hardware/accelerometer-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/accelerometer_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/accelerometer-bricklet/zipball/master>`__)
* 3D model (`View online <http://a360.co/2surksj>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/accelerometer/accelerometer.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/accelerometer/accelerometer.FCStd>`__)

.. _accelerometer_bricklet_test:

Test your Accelerometer Bricklet
--------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the acceleration in g,
pitch and roll and a graph that shows the acceleration over time.

Point the Bricklet downwards along its x-, y- and z-axis one by one. The
acceleration should be around 1g for the axis pointing downwards and around 0g
for the other axes.

.. image:: /Images/Bricklets/bricklet_accelerometer_brickv.jpg
   :scale: 100 %
   :alt: Accelerometer Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_accelerometer_brickv.jpg

|test_pi_ref|


.. _accelerometer_bricklet_case:

Case
----

A `laser-cut case for the Accelerometer Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-accelerometer-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_accelerometer_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Accelerometer Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_accelerometer_case_built_up_1000.jpg

.. include:: Accelerometer.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/accelerometer_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Accelerometer Bricklet
   :align: center
   :target: ../../_images/Exploded/accelerometer_exploded.png

|bricklet_case_hint|


.. _accelerometer_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Accelerometer_hlpi.table
