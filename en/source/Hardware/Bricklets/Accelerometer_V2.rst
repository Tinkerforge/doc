
:shoplink: ../../../shop/bricklets/accelerometer-v2-bricklet.html

.. include:: Accelerometer_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _accelerometer_v2_bricklet:

Accelerometer Bricklet 2.0
==========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_accelerometer_v2_tilted_[?|?].jpg           Accelerometer Bricklet 2.0
	Bricklets/bricklet_accelerometer_v2_top_[?|?].jpg              Accelerometer Bricklet 2.0
	Bricklets/bricklet_accelerometer_v2_brickv_[100|].jpg          Accelerometer Bricklet 2.0 in Brick Viewer
	Dimensions/accelerometer_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 3-axis accelerometer
* 0.0001g steps with 16bit resolution
* Up to ±8g full-scale range
* Date rate of up to 25.6kHz


.. _accelerometer_v2_bricklet_description:

Description
-----------

The Accelerometer :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure acceleration in x-, y- and z-axis.
The measured acceleration can be read out in
`g <https://en.wikipedia.org/wiki/G-force#Unit_and_measurement>`__.
With configurable events it is possible to react on changing acceleration
without polling.

A continuous acceleration callback can be used to transfer the acceleration
data with the full rate of up to 25.6kHz. This high data rate is well suited
for predictive maintenance applications.

The Bricklet has an LED that can be turned on trough the API, e.g. to show
that a specific acceleration was reached.



Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            KX122
Current Consumption               30mW (6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        0.0001g steps, 16bit resolution
Shock survivability               5000g for 0.5ms / 10000g for 0.2ms
Full-scale range                  ±2g / ±4g / ±8g (selectable with API)
Data Rate                         0.781Hz - 25.6kHz (selectable with API)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 20 x 5mm (0.98 x 0.79 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* KX122 datasheet (`Download <https://github.com/Tinkerforge/accelerometer-bricklet-v2/raw/master/datasheets/KX122.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/accelerometer-v2-bricklet/raw/master/hardware/accelerometer-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/accelerometer_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/accelerometer-v2-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _accelerometer_v2_bricklet_test:

Test your Accelerometer Bricklet 2.0
------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the acceleration in g,
pitch and roll and a graph that shows the acceleration over time.

Point the Bricklet downwards along its x-, y- and z-axis one by one. The
acceleration should be around 1g for the axis pointing downwards and around 0g
for the other axes.

.. image:: /Images/Bricklets/bricklet_accelerometer_v2_brickv.jpg
   :scale: 100 %
   :alt: Accelerometer Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_accelerometer_v2_brickv.jpg

|test_pi_ref|


.. _accelerometer_v2_bricklet_case:

Case
----

A `laser-cut case for the Accelerometer Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-accelerometer-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_accelerometer_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Accelerometer Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_accelerometer_case_built_up_1000.jpg

.. include:: Accelerometer.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/accelerometer_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Accelerometer Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/accelerometer_exploded.png

|bricklet_case_hint|


.. _accelerometer_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Accelerometer_V2_hlpi.table
