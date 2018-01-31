
:DISABLED_shoplink: ../../../shop/bricklets/temperature-ir-v2-bricklet.html

.. include:: Temperature_IR_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _temperature_ir_v2_bricklet:

Temperature IR Bricklet 2.0
===========================

.. note::
  This Bricklet is currently under development.

..
	.. raw:: html

		{% tfgallery %}

		Bricklets/bricklet_temperature_ir_v2_tilted_[?|?].jpg           Temperature IR Bricklet 2.0
		Bricklets/bricklet_temperature_ir_v2_vertical_[?|?].jpg         Temperature IR Bricklet 2.0
		Bricklets/bricklet_temperature_ir_v2_horizontal_[?|?].jpg       Temperature IR Bricklet 2.0
		Bricklets/bricklet_temperature_ir_v2_master_[100|600].jpg       Temperature IR Bricklet 2.0 with Master Brick
		Cases/bricklet_temperature_ir_v2_case_[100|600].jpg             Temperature IR Bricklet 2.0 in Case
		Bricklets/bricklet_temperature_ir_v2_brickv_[100|].jpg          Temperature IR Bricklet 2.0 in Brick Viewer
		Dimensions/temperature_ir_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

		{% tfgalleryend %}


Features
--------

* Measures contactless object temperature from -70°C to 380°C
* Configurable emissivity
* Measures ambient temperature from -40°C to 85°C
* Output in 0.1°C steps (16bit resolution)


.. _temperature_ir_v2_bricklet_description:

Description
-----------

The Temperature IR :ref:`Bricklet <primer_bricklets>` 2.0 is equipped
with a `infrared thermometer <https://en.wikipedia.org/wiki/Infrared_thermometer>`__.
It can extend the features of a :ref:`Brick <primer_bricks>` with the capability 
of contactless temperature measurement.

You can read out object temperature and ambient temperature in
`°C <https://en.wikipedia.org/wiki/Degree_Celsius>`__.
It is possible to define the
`emissivity <https://en.wikipedia.org/wiki/Emissivity>`__ of the object you
want to measure (most infrared thermometers can't do this) .
With configurable events it is possible to react on changing
temperatures without polling.

The Temperature IR Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

===================================  =====================================================================
Property                             Value
===================================  =====================================================================
Sensor                               MLX90614ESF-BAA
Current Consumption                  TBDmA
-----------------------------------  ---------------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------------
Object Temperature                   -70°C to 380°C in 0.1°C steps (16bit resolution)
Ambient Temperature                  -40°C to 85°C in 0.1°C steps (16bit resolution)
Accuracy                             0.5°C over wide temperature range
-----------------------------------  ---------------------------------------------------------------------
-----------------------------------  ---------------------------------------------------------------------
Dimensions (W x D x H)               25 x 20 x 7mm (0.98 x 0.79 x 0.27")
Weight                               TBDg
===================================  =====================================================================


Resources
---------

* MLX90614 datasheet (`Download <https://github.com/Tinkerforge/temperature-ir-v2-bricklet/raw/master/datasheets/MLX90614.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/temperature-ir-v2-bricklet/raw/master/hardware/temperature-ir-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/temperature_ir_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/temperature-ir-v2-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2Euzglf>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/temperatur_ir_v2/temperatur_ir.step>`__,  `FreeCAD <http://download.tinkerforge.com/3d/bricklets/temperatur_ir_v2/temperatur_ir.FCStd>`__)


.. _temperature_ir_v2_bricklet_test:

Test your Temperature IR Bricklet 2.0
-------------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_temperature_ir_v2_master_600.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet 2.0 connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_v2_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_temperature_ir_v2_brickv.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_v2_brickv.jpg

Point the Bricklet in different
directions. The Brick Viewer will show the ambient temperature (the
temperature of the room) and the object temperature of the object you point at.

For accurate object temperature measurements it is possible to configure the
emissivity of the material you point at.
Enter 0xFFFF = 65535 for an emissivity of 1.0.

|test_pi_ref|


.. _temperature_ir_v2_bricklet_case:

Case
----

..
	A `laser-cut case for the Temperature IR Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-temperature-ir-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_temperature_ir_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Temperature IR Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_temperature_ir_v2_case_1000.jpg

	The assembly is easiest if you follow the following steps:

	* Screw Bricklet to top plate with spacers at the bottom and long screws from the top,
	* build up side plates,
	* plug side plates into top plate and
	* screw bottom plate to bottom spacers.

	Below you can see an exploded assembly drawing of the Temperature IR Bricklet 2.0 case:

	.. image:: /Images/Exploded/temperature_ir_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Temperature IR Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/temperature_ir_v2_exploded.png

	|bricklet_case_hint|


.. _temperature_ir_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Temperature_IR_V2_hlpi.table
