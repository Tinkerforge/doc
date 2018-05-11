
:shoplink: ../../../shop/bricklets/rotary-encoder-v2-bricklet.html

.. include:: Rotary_Encoder_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _rotary_encoder_v2_bricklet:

Rotary Encoder Bricklet 2.0
===========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rotary_encoder_v2_tilted_[?|?].jpg               Rotary Encoder Bricklet 2.0
	Bricklets/bricklet_rotary_encoder_v2_top_[?|?].jpg                  Rotary Encoder Bricklet 2.0
	Bricklets/bricklet_rotary_encoder_v2_w_knob_[100|600].jpg           Rotary Encoder Bricklet 2.0 and knob
	Bricklets/bricklet_rotary_encoder_v2_side_[?|?].jpg                 Rotary Encoder Bricklet 2.0
	Bricklets/bricklet_rotary_encoder_v2_brickv_[100|].jpg              Rotary Encoder Bricklet 2.0 in Brick Viewer
	Dimensions/rotary_encoder_v2_bricklet_dimensions_[100|600].png      Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 360° rotary encoder
* Counts 24 steps per rotation (step angle 15°)
* Integrated push-button


.. _rotary_encoder_v2_bricklet_description:

Description
-----------

The Rotary Encoder :ref:`Bricklet <primer_bricklets>` extends
:ref:`Bricks <primer_bricks>` and is equipped
with a 360° rotary encoder. It has 24 steps per rotation with a nice clicking
feel. The encoder has an integrated push-button (by pressing on the knob) that
can be used to select a menu item or similar. 

The difference between the :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>`
and the Rotary Encoder Bricklet 2.0 is that the encoder has full rotation without
limits.

The Rotary Encoder Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.


Technical Specifications
------------------------

==================================  ============================================================
Property                            Value
==================================  ============================================================
Current Consumption                 34mW
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Number of Steps per Rotation        24 (step angle 15°)
Maximum Number of Steps detectable  up to 250 steps / second
Button Operating Force              200gf
Button Travel Distance              0.5mm
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)              30 x 25 x 23mm (1.18 x 0.98 x 0.9")*
Weight                              6g*
==================================  ============================================================

\* without knob

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/rotary-encoder-v2-bricklet/raw/master/hardware/rotary-encoder-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rotary_encoder_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rotary-encoder-v2-bricklet/zipball/master>`__)
* 3D model (`View online <http://autode.sk/2EHoGaC>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/rotary_encoder_v2/rotary-encoder-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/rotary_encoder_v2/rotary-encoder-v2.FCStd>`__)



.. _rotary_encoder_v2_bricklet_test:

Test your Rotary Encoder Bricklet 2.0
-------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now turn the encoder and see
the corresponding count.

.. image:: /Images/Bricklets/bricklet_rotary_encoder_v2_brickv.jpg
   :scale: 100 %
   :alt: Rotary Encoder Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_encoder_v2_brickv.jpg

|test_pi_ref|

.. _rotary_encoder_v2_bricklet_case:

Case
----

A `laser-cut case for the Rotary Encoder Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-rotary-poti-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_rotary_poti_case_shallow_350.jpg
   :scale: 100 %
   :alt: Case for Rotary Encoder Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_rotary_poti_case_shallow_1000.jpg

.. include:: Rotary_Encoder_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/rotary_poti_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Rotary Encoder Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/rotary_poti_exploded.png

|bricklet_case_hint|


.. _rotary_encoder_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Rotary_Encoder_V2_hlpi.table
