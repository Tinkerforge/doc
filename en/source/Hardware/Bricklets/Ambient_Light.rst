

.. include:: Ambient_Light.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _ambient_light_bricklet:

Ambient Light Bricklet
======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_ambient_light_tilted_[?|?].jpg           Ambient Light Bricklet
	Bricklets/bricklet_ambient_light_vertical_[?|?].jpg         Ambient Light Bricklet
	Bricklets/bricklet_ambient_light_horizontal_[?|?].jpg       Ambient Light Bricklet
	Bricklets/bricklet_ambient_light_master_[100|600].jpg       Ambient Light Bricklet with Master Brick
	Cases/bricklet_ambient_light_case_built_up_[?|?].jpg        Ambient Light Bricklet in case
	Bricklets/bricklet_ambient_light_brickv_[100|].jpg          Ambient Light Bricklet in Brick Viewer
	Dimensions/ambient_light_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Ambient Light Bricklet is discontinued and is no longer sold. The
 :ref:`Ambient Light Bricklet 2.0 <ambient_light_v2_bricklet>` is the recommended
 replacement.


Features
--------

* Measures ambient light up to 900lux
* Output in 0.1lux steps (12bit resolution)


.. _ambient_light_bricklet_description:

Description
-----------

The Ambient Light :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` with the
capability to measure ambient light. The measured illuminance can be read
out in `lux <https://en.wikipedia.org/wiki/Lux>`__. With configurable events
it is possible to react on changing illuminance without polling.

Typical applications are illuminance dependent switching of
backlights, motors etc.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            TEMT6000
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Illumination                      0lux - 900lux in 0.1lux steps, 12bit resolution
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 5mm (0.98 x 0.59 x 0.19")
Weight                            2g
================================  ============================================================


Resources
---------

* TEMT6000 datasheet (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/raw/master/datasheets/TEMT6000.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/raw/master/hardware/ambient-light-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/ambient_light_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/zipball/master>`__)


.. _ambient_light_bricklet_test:

Test your Ambient Light Bricklet
--------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_ambient_light_master_600.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_master_1200.jpg

|test_tab|
If everything went as expected you can now see the illuminance in lux,
a graphical representation of the illuminance and a graph that shows the
illuminance over time.

A good test for the sensor is to darken the room and
slowly move a flashlight over the sensor, the graph should then look
approximately as in the screenshot shown below.

.. image:: /Images/Bricklets/bricklet_ambient_light_brickv.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_brickv.jpg

|test_pi_ref|


.. _ambient_light_bricklet_case:

Case
----

A `laser-cut case for the Ambient Light Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Ambient Light Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Ambient_Light.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Ambient Light Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _ambient_light_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Ambient_Light_hlpi.table
