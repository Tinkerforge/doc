
:shoplink: ../../../shop/bricklets/industrial-quad-relay-v2-bricklet.html

.. include:: Industrial_Quad_Relay_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_quad_relay_v2_bricklet:

Industrial Quad Relay Bricklet 2.0
==================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_quad_relay_v2_tilted_[?|?].jpg           Industrial Quad Relay Bricklet 2.0
	Bricklets/bricklet_industrial_quad_relay_v2_tilted2_[?|?].jpg          Industrial Quad Relay Bricklet 2.0
	Bricklets/bricklet_industrial_quad_relay_v2_side_[?|?].jpg             Industrial Quad Relay Bricklet 2.0
	Bricklets/bricklet_industrial_quad_relay_v2_top_[?|?].jpg              Industrial Quad Relay Bricklet 2.0
	Bricklets/bricklet_industrial_quad_relay_v2_brickv_[100|].jpg          Industrial Quad Relay Bricklet 2.0 in Brick Viewer
	Dimensions/industrial_quad_relay_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 4 Channel Solid State Relay
* Switch up to 30V with 1.2A
* Galvanically isolated


.. _industrial_quad_relay_v2_bricklet_description:

Description
-----------

The Industrial Quad Relay :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend :ref:`Bricks <primer_bricks>` by four galvanically isolated solid state relays.
Each channel can switch currents of up to 1.2 `Ampere <https://en.wikipedia.org/wiki/Ampere>`__
with 30 `Volt <https://en.wikipedia.org/wiki/Volt>`__.
Output isolation permits the usage without a direct electric connection, 
such that ground loops can be prevented and an additional degree of safety is added.

Typical applications are the interfacing of industrial control, such as PLC's or frequency converters,
or the usage in environments were electrical ground levels can not be connected.

The Industrial Quad Relay Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               | 31mW (6.2mA at 5V)
                                  | + 3mW (0.6mA at 5V) per activated relay
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Output Type                       Four galvanically isolated solid state relays
Maximum Switching Current         1.2A
Maximum Switching Voltage         30V
Isolation                         1500Vrms (datasheet value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            9g
================================  ============================================================


Resources
---------

* CPC1020N datasheet (`Download <https://github.com/Tinkerforge/industrial-quad-relay-v2-bricklet/raw/master/datasheets/CPC1020N.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-quad-relay-v2-bricklet/raw/master/hardware/industrial-quad-relay-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_quad_relay_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-quad-relay-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2JSDnZI>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_quad_relay_v2/industrial-quad-relay-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_quad_relay_v2/industrial-quad-relay-v2.FCStd>`__)


Connectivity
------------

The Industrial Quad Relay Bricklet has an 8 pole terminal.
Please see the picture below for the pinout.

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_v2_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay 4 Bricklet 2.0 connectivity
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_v2_caption_1200.jpg

.. _industrial_quad_relay_v2_bricklet_test:

Channel Status LEDs
-------------------

The Bricklet has the standard status LED with four additional LEDs (one
for each channel).

By default the channel status LEDs are on if the corresponding channel
is switched on and off otherwise. You can also turn each LED individually on/off
and show other status information through the API.

Test your Industrial Quad Relay Bricklet 2.0
--------------------------------------------

|test_intro|

|test_connect|.
For a simple test we will connect a battery and a LED to test the Bricklet
(see picture below).

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_setup_1200.jpg

|test_tab|

If everything went as expected you can switch the LED by changing the output
state with the Brick Viewer.

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_v2_brickv.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_v2_brickv.jpg

|test_pi_ref|


.. _industrial_quad_relay_v2_bricklet_case:

Case
----

A `laser-cut case for the Industrial Quad Relay Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Quad_Relay.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_quad_relay_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Quad_Relay_V2_hlpi.table
