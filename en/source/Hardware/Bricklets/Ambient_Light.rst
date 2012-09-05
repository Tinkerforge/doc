.. include:: Ambient_Light.substitutions


.. _ambient_light_bricklet:

Ambient Light Bricklet
======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_ambient_light_tilted_350.jpg",
	               "Bricklets/bricklet_ambient_light_tilted_600.jpg",
	               "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_vertical_100.jpg",
	             "Bricklets/bricklet_ambient_light_vertical_600.jpg",
	             "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_horizontal_100.jpg",
	             "Bricklets/bricklet_ambient_light_horizontal_600.jpg",
	             "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_master_100.jpg",
	             "Bricklets/bricklet_ambient_light_master_600.jpg",
	             "Ambient Light Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_brickv_100.jpg",
	             "Bricklets/bricklet_ambient_light_brickv.jpg",
	             "Ambient Light Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/ambient_light_bricklet_dimensions_100.png",
	             "Dimensions/ambient_light_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures ambient light up to 900lux
* Output in 0.1lux steps (12bit resolution)


Description
-----------

The Ambient Light :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` with the
capability to measure ambient light. The measured illuminance can be read
out in `lux <http://en.wikipedia.org/wiki/Lux>`__. With configurable events
it is possible to react on changing illuminance without polling.

Typical applications are illuminance dependent switching of
backlights, motors etc.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            TEMT6000
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


.. _ambient_light_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Ambient_Light_hlpi.table
