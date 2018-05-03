
:DISABLED_shoplink: ../../../shop/bricklets/industrial-digital-in-4-v2-bricklet.html

.. include:: Industrial_Digital_In_4_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_digital_in_4_v2_bricklet:

Industrial Digital In 4 Bricklet 2.0
====================================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_digital_in_4_v2_tilted_[?|?].jpg           Industrial Digital In 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_in_4_v2_horizontal_[?|?].jpg       Industrial Digital In 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_in_4_v2_master_[100|600].jpg       Industrial Digital In 4 Bricklet 2.0 with Master Brick
	Cases/bricklet_industrial_digital_in_4_v2_case_[100|600].jpg             Industrial Digital In 4 Bricklet 2.0 with case
	Bricklets/bricklet_industrial_digital_in_4_v2_brickv_[100|].jpg          Industrial Digital In 4 Bricklet 2.0 in Brick Viewer
	Dimensions/industrial_digital_in_4_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 4 channel digital input 
* Input voltages up to 36V (DC)
* Galvanically isolated


.. _industrial_digital_in_4_v2_bricklet_description:

Description
-----------

The Industrial Digital In 4 :ref:`Bricklet <primer_bricklets>` 2.0 can 
be used to extend :ref:`Bricks <primer_bricks>` by four galvanically 
isolated digital inputs. The input voltage can be up to 36 
`volts <https://en.wikipedia.org/wiki/Volt>`__ (DC).

Input isolation permits the usage without a direct electrical connection, 
such that ground loops can be prevented and an additional degree of safety is 
added.

Typical applications are the interfacing of industrial controllers, such as 
PLC's or frequency converters, or the usage in environments were electrical 
ground levels can not be connected.

The Industrial Digital In 4 Bricklet 2.0 has a 7 pole Bricklet connector and
is connected to a Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               28mw (5.6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Input Type                        Four optocoupled inputs (including 4.7kΩ series resistor)
Input Current                     Depending on input voltage, ca. 1mA/5V, ca. 5mA/24V
Maximum Input Voltage             36V (DC)
Low Level Voltage                 0-2V
High Level Voltage                3-36V
Isolation                         5000Vrms (optocoupler value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            8.6g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-v2-bricklet/raw/master/hardware/industrial-digital-in-4-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_digital_in_4_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-digital-in-4-v2-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _industrial_digital_in_4_v2_bricklet_connectivity:

Connectivity
------------

The Industrial Digital In 4 Bricklet 2.0 has an 8 pole terminal. With it you can 
access the four inputs. Each input is connected to one LED inside the 
optocoupler.

To use one input connect it as depicted below:

TODO: Make photo with new Bricklet.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet 2.0 Terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_caption_1200.jpg


.. _industrial_digital_in_4_v2_bricklet_leds:

Channel Status LEDs
-------------------

The Bricklet has the standard status LED with four additional LEDs (one
for each channel).

By default the channel status LEDs are on if the corresponding channel
is high and off otherwise. You can also turn each LED individually on/off
and show other status information through the API.


.. _industrial_digital_in_4_v2_bricklet_test:

Test your Industrial Digital In 4 Bricklet 2.0
----------------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected ... TBD.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_v2_brickv.jpg

|test_pi_ref|


.. _industrial_digital_in_4_v2_bricklet_case:

Case
----

..
	A `laser-cut case for the Industrial Digital In 4 Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-industrial-digital-in-4-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_industrial_digital_in_4_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Industrial Digital In 4 Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_industrial_digital_in_4_v2_case_1000.jpg

	.. include:: Industrial_Digital_In_4_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/industrial_digital_in_4_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Industrial Digital In 4 Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/industrial_digital_in_4_v2_exploded.png

	|bricklet_case_hint|


.. _industrial_digital_in_4_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Digital_In_4_V2_hlpi.table
