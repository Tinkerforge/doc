
:shoplink: ../../../shop/bricklets/industrial-digital-in-4-v2-bricklet.html

.. include:: Industrial_Digital_In_4_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_digital_in_4_v2_bricklet:

Industrial Digital In 4 Bricklet 2.0
====================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_digital_in_4_v2_tilted_[?|?].jpg           Industrial Digital In 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_in_4_v2_tilted2_[?|?].jpg          Industrial Digital In 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_in_4_v2_side_[?|?].jpg             Industrial Digital In 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_in_4_v2_top_[?|?].jpg              Industrial Digital In 4 Bricklet 2.0
	Cases/bricklet_industrial_digital_in_4_v2_case_[?|?].jpg                 Industrial Digital In 4 Bricklet 2.0 with case
	Cases/bricklet_industrial_digital_in_4_v2_case2_[?|?].jpg                Industrial Digital In 4 Bricklet 2.0 with case
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

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls autoplay loop>
	  <source src="../../_images/Videos/bricklet_industrial_digital_in_4_video.mp4" type="video/mp4">
	  <source src="../../_images/Videos/bricklet_industrial_digital_in_4_video.ogg" type="video/ogg">
	  <source src="../../_images/Videos/bricklet_industrial_digital_in_4_video.webm" type="video/webm">
	</video>

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               28mW (5.6mA at 5V)
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
* 3D model (`View online <https://autode.sk/2rG0jVB>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_digital_in_4_v2/industrial-digital-in-4-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_digital_in_4_v2/industrial-digital-in-4-v2.FCStd>`__)


.. _industrial_digital_in_4_v2_bricklet_connectivity:

Connectivity
------------

The Industrial Digital In 4 Bricklet 2.0 has an 8 pole terminal. With it you can 
access the four inputs. Each input is connected to one LED inside the 
optocoupler.

To use one input connect it as depicted below:

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_v2_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet 2.0 Terminals
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_v2_caption_1200.jpg


.. _industrial_digital_in_4_v2_bricklet_leds:

Channel Status LEDs
-------------------

The Bricklet has the standard status LED with four additional LEDs (one
for each input).

By default the channel status LEDs are on if the corresponding channel
is high and off otherwise. You can also turn each LED individually on/off
and show other status information through the API.


.. _industrial_digital_in_4_v2_bricklet_test:

Test your Industrial Digital In 4 Bricklet 2.0
----------------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the current state of the inputs should be displayed. If nothing is
connected to the Bricklet all inputs should be logical low.

.. image:: /Images/Bricklets/bricklet_industrial_digital_in_4_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital In 4 Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_in_4_v2_brickv.jpg

|test_pi_ref|


.. _industrial_digital_in_4_v2_bricklet_case:

Case
----

A `laser-cut case for the Industrial Digital In 4 Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_digital_in_4_v2_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Digital In 4 Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_digital_in_4_v2_case_1000.jpg

.. include:: Industrial_Digital_In_4.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Digital In 4 Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_digital_in_4_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Digital_In_4_V2_hlpi.table
