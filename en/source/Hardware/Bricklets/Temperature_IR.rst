
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Temperature IR Bricklet
:shoplink: ../../../shop/bricklets/temperature-ir-bricklet.html

.. include:: Temperature_IR.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _temperature_ir_bricklet:

Temperature IR Bricklet
=======================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_temperature_ir_tilted_[?|?].jpg           Temperature IR Bricklet
	Bricklets/bricklet_temperature_ir_vertical_[?|?].jpg         Temperature IR Bricklet
	Bricklets/bricklet_temperature_ir_horizontal_[?|?].jpg       Temperature IR Bricklet
	Bricklets/bricklet_temperature_ir_master_[100|600].jpg       Temperature IR Bricklet with Master Brick
	Cases/bricklet_temperature_ir_case_[100|600].jpg             Temperature IR Bricklet in Case
	Bricklets/bricklet_temperature_ir_brickv_[100|].jpg          Temperature IR Bricklet in Brick Viewer
	Dimensions/temperature_ir_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures contactless object temperature from -70°C to 380°C
* Configurable emissivity
* Measures ambient temperature from -40°C to 85°C
* Output in 0.1°C steps (16bit resolution)


.. _temperature_ir_bricklet_description:

Description
-----------

The Temperature IR :ref:`Bricklet <primer_bricklets>` is equipped
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


Technical Specifications
------------------------

===================================  =====================================================================
Property                             Value
===================================  =====================================================================
Sensor                               MLX90614ESF-BAA
Current Consumption                  2mA
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

* MLX90614 datasheet (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/raw/master/datasheets/MLX90614.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/raw/master/hardware/temperature-ir-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/temperature_ir_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/temperature-ir-bricklet/zipball/master>`__)


.. _temperature_ir_bricklet_test:

Test your Temperature IR Bricklet
---------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_temperature_ir_master_600.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_temperature_ir_brickv.jpg
   :scale: 100 %
   :alt: Temperature IR Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_temperature_ir_brickv.jpg

Point the Bricklet in different
directions. The Brick Viewer will show the ambient temperature (the
temperature of the room) and the object temperature of the object you point at.

For accurate object temperature measurements it is possible to configure the
emissivity of the material you point at.
Enter 0xFFFF = 65535 for an emissivity of 1.0.

|test_pi_ref|


.. _temperature_ir_bricklet_case:

Case
----

A `laser-cut case for the Temperature IR Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-temperature-ir-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_temperature_ir_case_350.jpg
   :scale: 100 %
   :alt: Case for Temperature IR Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_temperature_ir_case_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw Bricklet to top plate with spacers at the bottom and long screws from the top,
* build up side plates,
* plug side plates into top plate and
* screw bottom plate to bottom spacers.

Below you can see an exploded assembly drawing of the Temperature IR Bricklet case:

.. image:: /Images/Exploded/temperature_ir_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Temperature IR Bricklet
   :align: center
   :target: ../../_images/Exploded/temperature_ir_exploded.png

|bricklet_case_hint|


.. _temperature_ir_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Temperature_IR_hlpi.table
