
:DISABLED_shoplink: ../../../shop/bricklets/industrial-digital-out-4-v2-bricklet.html

.. include:: Industrial_Digital_Out_4_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_digital_out_4_v2_bricklet:

Industrial Digital Out 4 Bricklet 2.0
=====================================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_digital_out_4_v2_tilted_[?|?].jpg           Industrial Digital Out 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_out_4_v2_horizontal_[?|?].jpg       Industrial Digital Out 4 Bricklet 2.0
	Bricklets/bricklet_industrial_digital_out_4_v2_master_[100|600].jpg       Industrial Digital Out 4 Bricklet 2.0 with Master Brick
	Cases/bricklet_industrial_digital_out_4_v2_case_[100|600].jpg             Industrial Digital Out 4 Bricklet 2.0 with case
	Bricklets/bricklet_industrial_digital_out_4_v2_brickv_[100|].jpg          Industrial Digital Out 4 Bricklet 2.0 in Brick Viewer
	Dimensions/industrial_digital_out_4_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 4 channel digital output
* Output voltages up to 36V
* Galvanically isolated
* Status LED per channel


.. _industrial_digital_out_4_v2_bricklet_description:

Description
-----------

The Industrial Digital Out 4 :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend :ref:`Bricks <primer_bricks>` by four galvanically isolated digital outputs.
The outputs have to be supplied externally with a voltage of up to
36 `Volt <https://en.wikipedia.org/wiki/Volt>`__.
Output isolation permits the usage without a direct electric connection, 
such that ground loops can be prevented and an additional degree of safety is added.

Typical applications are the interfacing of industrial controllers, such as PLC's or frequency converters,
or the usage in environments were electrical ground levels can not be connected.

The Industrial Digital Out 4 Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               30mW (6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
External Voltage Supply           Up to 36V
Output Type                       Four operational amplifier outputs
Maximum Output Current            25mA (per output pin)
Isolation                         5000Vrms (optocoupler value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 14mm (1.57 x 1.57 x 0.55")
Weight                            10g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-digital-out-4-v2-bricklet/raw/master/hardware/industrial-digital-out-4-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_digital_out_4_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-digital-out-4-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2v362pN>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/industrial_digital_out_4_v2/industrial-digital-out-4-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/industrial_digital_out_4_v2/industrial-digital-out-4-v2.FCStd>`__)


.. _industrial_digital_out_4_v2_bricklet_connectivity:

Connectivity
------------

The Industrial Digital Out 4 Bricklet 2.0 has an 8 pole terminal.
Please see the picture below for the pinout.

TODO: Update image

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet 2.0 pinout
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_caption_1200.jpg


.. _industrial_digital_out_4_v2_bricklet_leds:

Channel Status LEDs
-------------------

The Bricklet has the standard status LED with four additional LEDs (one
for each output).

By default the channel status LEDs are on if the corresponding channel
is high and off otherwise. You can also turn each LED individually on/off
and show other status information through the API.

.. _industrial_digital_out_4_v2_bricklet_test:

Test your Industrial Digital Out 4 Bricklet 2.0
-----------------------------------------------

|test_intro|

|test_connect|.
Additionally connect a voltage source to power the Bricklet and a load
you want to switch. For testing purposes we have connected a battery
and a LED (see picture below).

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_setup_1200.jpg

|test_tab|
If everything went as expected you can switch the LED by changing the output
state with the Brick Viewer.

.. image:: /Images/Bricklets/bricklet_industrial_digital_out_4_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Digital Out 4 Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_digital_out_4_v2_brickv.jpg

|test_pi_ref|


.. _industrial_digital_out_4_v2_bricklet_case:

Case
----

A `laser-cut case for the Industrial Digital Out 4 Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Digital Out 4 Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Digital_Out_4_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Digital Out 4 Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_digital_out_4_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Digital_Out_4_V2_hlpi.table
