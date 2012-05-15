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
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/ambient_light_bricklet_dimensions_100.png", 
	             "Dimensions/ambient_light_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * Measures ambient Light
 * Outputs ambient light in lux, unit 0.1 lux
 * 12bit resolution


Description
-----------

The Ambient Light :ref:`Bricklet <product_overview_bricklets>` can be used to 
extend the features of :ref:`Bricks <product_overview_bricks>` with the 
capability to measure ambient light. The measured illuminance can be read 
out in `lux <http://en.wikipedia.org/wiki/Lux>`_. With configurable events
it is possible to react on changing illuminance without polling.

Typical applications are illuminance dependent switching of 
backlights, motors etc.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions                        15mm x 25mm (0.59" x 0.98")
Weight                            1.5g
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Sensor                            TEMT6000
Output: Illumination              0-900 lux, unit 0.1 lux, resolution 12bit
================================  ============================================================

Resources
---------

* TEMT6000 datasheet (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/raw/master/datasheets/TEMT6000.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/raw/master/hardware/ambient-light-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/ambient_light_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/zipball/master>`__)


.. _ambient_light_bricklet_test:

Test your Ambient Light Bricklet
--------------------------------

To test the Ambient Light Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming 
language API bindings, the latter is for testing purposes.

Now you can connect the Ambient Light Bricklet to any
:ref:`Brick <product_overview_bricks>`. You should have received a suitable
cable with the Bricklet. 

.. image:: /Images/Bricklets/bricklet_ambient_light_master_600.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_master_1200.jpg

If you then connect the Brick to the PC over USB,
you should see a tab named "Ambient Light Bricklet" in the Brick Viewer after 
you pressed "connect". Select it.

If everything went as expected you can now see the illuminance in lux,
a graphical representation of the illuminance and a graph that shows the
illuminance over time. A good test for the sensor is to darken the room and
slowly move a flashlight over the sensor, the graph should then look
approximately as in the screenshot shown below.

.. image:: /Images/Bricklets/bricklet_ambient_light_brickv.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet view in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_brickv.jpg

After this test you can go on with writing your own application.
See the :ref:`Programming Interface <ambl_programming_interfaces>` section for 
the API of the Current12 Bricklet and examples in different programming languages.

.. _ambl_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Ambient_Light_hlpi.table
