
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Multi Touch Bricklet
:FIXME_shoplink: ../../../shop/bricklets/multi-touch-bricklet.html

.. include:: Multi_Touch.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _multi_touch_bricklet:

Multi Touch Bricklet
====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_multi_touch_tilted_350.jpg",
	               "Bricklets/bricklet_multi_touch_tilted_600.jpg",
	               "Multi Touch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_multi_touch_vertical_100.jpg",
	             "Bricklets/bricklet_multi_touch_vertical_600.jpg",
	             "Multi Touch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_multi_touch_horizontal_100.jpg",
	             "Bricklets/bricklet_multi_touch_horizontal_600.jpg",
	             "Multi Touch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_multi_touch_tilted_back_100.jpg",
	             "Bricklets/bricklet_multi_touch_tilted_back_600.jpg",
	             "Multi Touch Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_multi_touch_brickv_100.jpg",
	             "Bricklets/bricklet_multi_touch_brickv.jpg",
	             "Multi Touch Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/multi_touch_bricklet_dimensions_100.png",
	             "Dimensions/multi_touch_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Capacitive Touch Sensor
* Can handle up to 12 electrodes used as touch locations
* Touch can be detected through a thin layer of glass/plastic/paper
* Size and placement of touch area can be user defined
* Can be used to build custom touch panel

Description
-----------

The Multi Touch :ref:`Bricklet <product_overview_bricklets>` is equipped with
the MPR121 capacitive touch sensor. It can be used to sense touch at 12
different locations.

The thing that is actually touched is called an "electrode". The electrode can
be a cable, electrically conductive tape or a copper surface of a circuit board.
Electrodes can sense touch through a thin layer of glass, plastic, paper or
similar.

With the Multi Touch Bricklet it is possible to build custom touch panels
by gluing a cover onto the electrodes.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Sensor                            MPR121
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

* MPR121 datasheet (`Download <https://github.com/Tinkerforge/multi-touch-bricklet/raw/master/datasheets/MPR121.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/multi-touch-bricklet/raw/master/hardware/multi-touch-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/multi_touch_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/multi-touch-bricklet/zipball/master>`__)


.. _multi_touch_bricklet_test:

Test your Multi Touch Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_multi_touch_master_600.jpg
   :scale: 100 %
   :alt: Multi Touch Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_multi_touch_master_1200.jpg

|test_tab|
If everything went as expected you can now see the current state.

.. image:: /Images/Bricklets/bricklet_multi_touch_brickv.jpg
   :scale: 100 %
   :alt: Multi Touch Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_multi_touch_brickv.jpg

|test_pi_ref|

Create own Touch Pads / Adjust Sensitivity
------------------------------------------

TODO Image

You can create simple touch pads by using stripped wires. To create real pads
you can use `self-adhesive aluminum tape
<https://www.tinkerforge.com/en/shop/accessories/sensors/aluminum-tape-1m.html>`__
to create the pad and connect the wire to it. Since it is a capacitive 
technology you can cover your self created touch panel with thin non-conductive 
materials. If your self created touch pad is too sensitive you can
remove some of the aluminum tape.

Dependent on your touch pads it might be necessary to adjust the sensitivity.
Use the Brick Viewer Software to play around with it by changing the value until
you have found a satisfying sensitivity. To accept the entered value press
"Recalibrate".


.. _multi_touch_bricklet_case:

Case
----

A `laser-cut case for the Multi Touch Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-multi-touch-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_multi_touch_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Multi Touch Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_multi_touch_case_built_up_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* build up side plates and put them around Bricklet,
* screw bottom plate to bottom spacers,
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the Multi Touch Bricklet case:

.. image:: /Images/Exploded/multi_touch_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Multi Touch Bricklet
   :align: center
   :target: ../../_images/Exploded/multi_touch_exploded.png

|bricklet_case_hint|


.. _multi_touch_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Multi_Touch_hlpi.table
