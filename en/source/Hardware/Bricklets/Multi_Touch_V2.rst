
:shoplink: ../../../shop/bricklets/multi-touch-v2-bricklet.html

.. include:: Multi_Touch_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _multi_touch_v2_bricklet:

Multi Touch Bricklet 2.0
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_multi_touch_v2_tilted_[?|?].jpg           Multi Touch Bricklet 2.0
	Bricklets/bricklet_multi_touch_v2_top_[?|?].jpg              Multi Touch Bricklet 2.0
	Cases/bricklet_multi_touch_case_tilted_[?|?].jpg             Multi Touch Bricklet in Case
	Bricklets/button_pad_w_multi_touch_tilted_[?|?].jpg          Multi Touch Bricklet with Button Pads
	Bricklets/cursor_pad_w_cable_[100|600].jpg                   Cursor Pad with Cable
	Bricklets/key_pad_w_multi_touch_[100|600].jpg                Multi Touch Bricklet with Key Pad
	Bricklets/slider_pad_w_multi_touch_[100|600].jpg             Multi Touch Bricklet with Slider Pad
	Bricklets/bricklet_multi_touch_v2_brickv_[100|].jpg          Multi Touch Bricklet 2.0 in Brick Viewer
	Dimensions/multi_touch_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Capacitive touch sensor
* Can handle up to 12 electrodes used as touch locations
* Touch can be detected through a thin layer of glass/plastic/paper
* Size and placement of touch area can be user defined
* Can be used to build custom touch panels


.. _multi_touch_v2_bricklet_description:

Description
-----------

The Multi Touch :ref:`Bricklet <primer_bricklets>` 2.0 is equipped with
the MPR121 capacitive touch sensor. It can be used to extend 
:ref:`Bricks <primer_bricks>` to sense touch at 12 different locations.

The thing that is actually touched is called an "electrode". The electrode can
be a cable, electrically conductive tape or a copper surface of a circuit board.
Electrodes can sense touch through a thin layer of glass, plastic, paper or
similar.

With the Multi Touch Bricklet it is possible to build custom touch panels
by gluing a cover onto the electrodes.

The Multi Touch Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MPR121
Current Consumption               30mW (6mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Number of Electrodes              12 + simulated 13th electrode for proximity
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 25 x 7mm (1.18 x 0.98 x 0.28")
Weight                            4g
================================  ============================================================


Resources
---------

* MPR121 datasheet (`Download <https://github.com/Tinkerforge/multi-touch-v2-bricklet/raw/master/datasheets/MPR121.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/multi-touch-v2-bricklet/raw/master/hardware/multi-touch-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/multi_touch_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/multi-touch-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/31GkD8A>`__ | Download: `STEP <https://download.tinkerforge.com/3d/multi_touch_v2/multi_touch_v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/multi_touch_v2/multi_touch_v2.FCStd>`__)


.. _multi_touch_v2_bricklet_test:

Test your Multi Touch Bricklet 2.0
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
Touch single pins of the Multi Touch Bricklet and you should see their
state changing in the Brick Viewer:

.. image:: /Images/Bricklets/bricklet_multi_touch_v2_brickv.jpg
   :scale: 100 %
   :alt: Multi Touch Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_multi_touch_v2_brickv.jpg

|test_pi_ref|


Create own Touch Pads / Adjust Sensitivity
------------------------------------------

You can create simple touch pads by using stripped wires. tape the wires with
`self-adhesive aluminum tape
<https://www.tinkerforge.com/en/shop/accessories/sensors/aluminum-tape-1m.html>`__
to a surface. Since it is a capacitive technology you can cover your
touch panel with thin non-conductive materials. If your pad is too sensitive you 
can remove some of the aluminum tape or reduce the sensitivity in software.

The following image shows the basic setup of a touch pad:

.. image:: /Images/Bricklets/bricklet_multi_touch_custom_pad2_350.jpg
   :scale: 100 %
   :alt: Self Made Touch Pad for Multi Touch Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_multi_touch_custom_pad2_1200.jpg

Depending on your touch pads it might be necessary to adjust the sensitivity.
Use the Brick Viewer Software to play around with it by changing the value until
you found a satisfying sensitivity. To transfer new values press "Recalibrate".


.. _multi_touch_v2_bricklet_circuit_board_pads:

Circuit Board Pads
------------------

.. image:: /Images/Bricklets/cursor_pad_w_cable_350.jpg
   :scale: 100 %
   :alt: Cursor Pad with Cable
   :align: center
   :target: ../../_images/Bricklets/cursor_pad_w_cable_1200.jpg

There are several circuit boards offered in the shop which can be used as
inputs for the Multi Touch Bricklet without the need of creating own pads.

 * `Cursor Pad <https://www.tinkerforge.com/en/shop/cursor-pad.html>`__
 * `Key Pad 3x4 <https://www.tinkerforge.com/en/shop/key-pad-3x4.html>`__
 * `Slider Pad <https://www.tinkerforge.com/en/shop/slider-pad.html>`__
 * `Button Pad <https://www.tinkerforge.com/en/shop/button-pad.html>`__

Additionally there is a pad kit especially for gaming applications:

 * `Giant Game Pad (see below) <https://www.tinkerforge.com/en/shop/giant-game-pad.html>`__


.. _multi_touch_v2_bricklet_giant_game_pad:

Usage of the Giant Game Pad
---------------------------

.. image:: /Images/Kits/ggp_table_top_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad on Table
   :align: center
   :target: ../../_images/Kits/ggp_table_top_1200.jpg


The Giant Game Pad consists of different pads made out of 3mm PMMA.
Besides the pads there is 10m of stranded wire, two 1m pieces of aluminum tape
and a 12 pole IDC connector included in the kit. 

.. image:: /Images/Kits/ggp_content_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad Kit Content
   :align: center
   :target: ../../_images/Kits/ggp_content_1200.jpg

To create working pads you have to cut the 10m wire in 12 sections as you need 
them. Dismantle 5cm of the isolation on one side of the wires.
Stick the wire with the aluminum tape to the bottom side of the pads.
For a first test only use a small section of the aluminum foil.

.. image:: /Images/Kits/ggp_pad_bottom_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad Bottom View
   :align: center
   :target: ../../_images/Kits/ggp_pad_bottom_1200.jpg

After that insert the wires in the IDC connector. You can use a vise or similar
to press the connector together.

.. image:: /Images/Kits/ggp_connector_crimp_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad IDC connector
   :align: center
   :target: ../../_images/Kits/ggp_connector_crimp_1200.jpg


After that your Giant Game Pad is finished. To ensure that the pads don't slide
around can stick the adhesive rubber feet to the bottom of the pads.

.. image:: /Images/Kits/ggp_table_front_350.jpg
   :scale: 100 %
   :alt: Giant Game Pad on Table
   :align: center
   :target: ../../_images/Kits/ggp_table_front_1200.jpg


The sensitivity has to be adapted depending on the wire length. This can be
done for all pads by software and for each panel by adjusting the size of the 
aluminum plane.


.. _multi_touch_v2_bricklet_case:

Case
----

A `laser-cut case for the Multi Touch Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-multi-touch-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_multi_touch_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for Multi Touch Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_multi_touch_case_tilted_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* build up side plates and put them around Bricklet,
* screw bottom plate to bottom spacers,
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the Multi Touch Bricklet 2.0 case:

.. image:: /Images/Exploded/multi_touch_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Multi Touch Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/multi_touch_exploded.png

|bricklet_case_hint|


.. _multi_touch_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Multi_Touch_V2_hlpi.table
