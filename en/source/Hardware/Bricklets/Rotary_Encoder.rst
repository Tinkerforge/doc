
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Rotary Encoder Bricklet
:FIXME_shoplink: ../../../shop/bricklets/rotary-encoder-bricklet.html

.. include:: Rotary_Encoder.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _rotary_encoder_bricklet:

Rotary Encoder Bricklet
=======================

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_rotary_encoder_tilted_350.jpg",
	               "Bricklets/bricklet_rotary_encoder_tilted_600.jpg",
	               "Rotary Encoder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_encoder_vertical_100.jpg",
	             "Bricklets/bricklet_rotary_encoder_vertical_600.jpg",
	             "Rotary Encoder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_encoder_horizontal_100.jpg",
	             "Bricklets/bricklet_rotary_encoder_horizontal_600.jpg",
	             "Rotary Encoder Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_encoder_master_100.jpg",
	             "Bricklets/bricklet_rotary_encoder_master_600.jpg",
	             "Rotary Encoder Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_rotary_encoder_brickv_100.jpg",
	             "Bricklets/bricklet_rotary_encoder_brickv.jpg",
	             "Rotary Encoder Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/rotary_encoder_bricklet_dimensions_100.png",
	             "Dimensions/rotary_encoder_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 360° rotary encoder
* Counts 24 steps per rotation (step angle 15°)
* Integrated push-button

Description
-----------

The Rotary Encoder :ref:`Bricklet <product_overview_bricklets>` is equipped
with a 360° rotary encoder. It has 24 steps per rotation with a nice clicking
feel. The encoder has an integrated push-button (by pressing on the knob) that
can be used to select a menu item or similar.

The difference between the :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>`
and the Rotary Encoder Bricklet is that the encoder has full rotation without
limits.


Technical Specifications
------------------------

==================================  ============================================================
Property                            Value
==================================  ============================================================
Number of Steps per Rotation        24 (step angle 15°)
Maximum Number of Steps detectable  up to 250 steps / second
Button Operating Force              200gf
Button Travel Distance              0.5mm
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)              30 x 25 x 23mm (1.18 x 0.98 x 0.9")*
Weight                              5g*
==================================  ============================================================

\* without knob

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/rotary-encoder-bricklet/raw/master/hardware/rotary-encoder-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rotary_encoder_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rotary-encoder-bricklet/zipball/master>`__)


.. _rotary_encoder_bricklet_test:

Test your Rotary Encoder Bricklet
---------------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_rotary_encoder_master_600.jpg
   :scale: 100 %
   :alt: Rotary Encoder Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_encoder_master_1200.jpg

|test_tab|
If everything went as expected you can now turn the encoder and see
the corresponding count.

.. image:: /Images/Bricklets/bricklet_rotary_encoder_brickv.jpg
   :scale: 100 %
   :alt: Rotary Encoder Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_encoder_brickv.jpg

|test_pi_ref|

.. _rotary_encoder_bricklet_case:

Case
----

A `laser-cut case for the Rotary Encoder Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-rotary-poti-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_rotary_encoder_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Rotary Encoder Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_rotary_encoder_case_built_up_1000.jpg

.. include:: Rotary_Encoder.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/rotary_poti_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Rotary Encoder Bricklet
   :align: center
   :target: ../../_images/Exploded/rotary_poti_exploded.png

|bricklet_case_hint|


.. _rotary_encoder_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Rotary_Encoder_hlpi.table
