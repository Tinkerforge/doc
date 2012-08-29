.. _temperature_ir_bricklet:

Temperature IR Bricklet
=======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_temperature_ir_tilted_350.jpg",
	               "Bricklets/bricklet_temperature_ir_tilted_600.jpg",
	               "Temperature IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_ir_vertical_100.jpg",
	             "Bricklets/bricklet_temperature_ir_vertical_600.jpg",
	             "Temperature IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_ir_horizontal_100.jpg",
	             "Bricklets/bricklet_temperature_ir_horizontal_600.jpg",
	             "Temperature IR Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_ir_master_100.jpg",
	             "Bricklets/bricklet_temperature_ir_master_600.jpg",
	             "Temperature IR Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_temperature_ir_brickv_100.jpg",
	             "Bricklets/bricklet_temperature_ir_brickv.jpg",
	             "Temperature IR Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/temperature_ir_bricklet_dimensions_100.png",
	             "Dimensions/temperature_ir_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures contactless object temperature from -70°C to 380°C
* Configurable emissivity
* Measures ambient temperature from -40°C to 85°C
* Output in 0.1°C steps (16bit resolution)


Description
-----------

The Temperature IR :ref:`Bricklet <product_overview_bricklets>` is equipped
with a `infrared thermometer <http://en.wikipedia.org/wiki/Infrared_thermometer>`__.
It can extend the features of a Brick with the capability to contactlessly
measure temperature.

You can read out object temperature and ambient temperature in
`°C <http://en.wikipedia.org/wiki/Degree_Celsius>`__.
It is possible to define the
`emissivity <http://en.wikipedia.org/wiki/Emissivity>`__ of the object you
want to measure (most infrared thermometers can't do this) .
With configurable events it is possible to react on changing
temperatures without polling.


Technical Specifications
------------------------

===================================  =====================================================================
Property                             Value
===================================  =====================================================================
Sensor                               MLX90614ESF-BAA
-----------------------------------  ---------------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------------
Object Temperature                   -70°C to 380°C in 0.1°C steps (16bit resolution)
Ambient Temperature                  -40°C to 85°C in 0.1°C steps (16bit resolution)
Accuracy                             0.5°C over wide temperature range
-----------------------------------  ---------------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------------
Dimensions (W x D x H)               25 x 20 x 7mm (0.98 x 0.79 x 0.27")
Weight                               3g
===================================  =====================================================================


Resources
---------

* MLX90614 datasheet (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/blob/master/datasheets/MLX90614.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/raw/master/hardware/temperature-ir-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/temperature_ir_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/zipball/master>`__)


.. _temperature_ir_bricklet_test:

Test your Temperature IR Bricklet
---------------------------------

To test the Temperature IR Bricklet you need to have the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
(for installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`) and the Brick Viewer has to be connected
to the Brick Daemon.

Connect the Temperature IR Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable
(see picture below).

.. image:: /Images/Bricklets/bricklet_temperature_ir_master_600.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_master_1200.jpg

If you connect the Brick to the PC over USB, you should see a new tab named
"Temperature IR Bricklet" in the Brick Viewer after a moment. Select this tab.

If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_temperature_ir_brickv.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_brickv.jpg

Point the Bricklet in different
directions. The Brick Viewer will show the ambient temperature (the
temperature of the room) and the object temperature you point at.

It is possible to configure the emissivity of the material you
point at.
Enter 0xFFFF = 65535 for an emissivity of 1.0.
The default is an emissivity of 0.98 (0.98 * 0xFFFF = 64224).

After this test you can go on with writing your own application.
See the :ref:`Programming Interface <temperatureir_programming_interfaces>`
section for the API of the Temperature IR Bricklet and examples in different
programming language.


.. _temperatureir_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Temperature_IR_hlpi.table
