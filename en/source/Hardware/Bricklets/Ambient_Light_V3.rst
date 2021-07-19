
:shoplink: ../../../shop/bricklets/ambient-light-v3-bricklet.html

.. include:: Ambient_Light_V3.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ambient_light_v3_bricklet:

Ambient Light Bricklet 3.0
==========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ambient_light_v3_tilted_[?|?].jpg           Ambient Light Bricklet 3.0
	Bricklets/bricklet_ambient_light_v3_top_[?|?].jpg              Ambient Light Bricklet 3.0
	Bricklets/bricklet_ambient_light_v3_brickv_[100|].jpg          Ambient Light Bricklet 3.0 in Brick Viewer
	Dimensions/ambient_light_v3_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures ambient light up to 64000lux
* Full dynamic range from 0.01lux to 64000lux
* Output in 0.01lux steps (16bit effective resolution)


.. _ambient_light_v3_bricklet_description:

Description
-----------

The Ambient Light :ref:`Bricklet <primer_bricklets>` 3.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure ambient light. It is the successor of the
:ref:`ambient_light_bricklet` with an about 70x bigger measurement range.
The measured
illuminance can be read out in `lux <https://en.wikipedia.org/wiki/Lux>`__.
With configurable events it is possible to react on changing illuminance
without polling.

Typical applications are illuminance dependent switching of backlights, motors
etc.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            LTR329ALS
Current Consumption               10mW (2mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Illumination                      0lux - 64000lux in 0.01lux steps, 16bit resolution
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* LTR329ALS datasheet (`Download <https://github.com/Tinkerforge/ambient-light-v3-bricklet/raw/master/datasheets/LTR329ALS.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/ambient-light-v3-bricklet/raw/master/hardware/ambient-light-v3-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/ambient_light_v3_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/ambient-light-v3-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2WsqooM>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/ambient_light_v3/ambient-light-v3.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/ambient_light_v3/ambient-light-v3.FCStd>`__)


.. _ambient_light_v3_bricklet_test:

Test your Ambient Light Bricklet 3.0
------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the illuminance in lux,
a graphical representation of the illuminance and a graph that shows the
illuminance over time.

A good test for the sensor is to darken the room and
slowly move a flashlight over the sensor, the graph should then look
approximately as in the screenshot shown below.

.. image:: /Images/Bricklets/bricklet_ambient_light_v3_brickv.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet 3.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_v3_brickv.jpg

|test_pi_ref|


.. _ambient_light_v3_bricklet_case:

Case
----

A `laser-cut case for the Ambient Light Bricklet 3.0
<https://www.tinkerforge.com/en/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Ambient Light Bricklet 3.0
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Ambient_Light_V3.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Ambient Light Bricklet 3.0
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _ambient_light_v3_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Ambient_Light_V3_hlpi.table
