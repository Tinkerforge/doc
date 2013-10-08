
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Sound Intensity Bricklet
:FIXME_shoplink: ../../../shop/bricklets/sound-intensity-bricklet.html

.. include:: Sound_Intensity.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _sound_intensity_bricklet:

Sound Intensity Bricklet
========================

.. note::
 This Bricklet is currently in the prototype stage and the software/hardware
 as well as the documentation is in an incomplete state.

.. FIXME raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_sound_intensity_tilted_350.jpg",
	               "Bricklets/bricklet_sound_intensity_tilted_600.jpg",
	               "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_vertical_100.jpg",
	             "Bricklets/bricklet_sound_intensity_vertical_600.jpg",
	             "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_horizontal_100.jpg",
	             "Bricklets/bricklet_sound_intensity_horizontal_600.jpg",
	             "Sound Intensity Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_master_100.jpg",
	             "Bricklets/bricklet_sound_intensity_master_600.jpg",
	             "Sound Intensity Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_sound_intensity_brickv_100.jpg",
	             "Bricklets/bricklet_sound_intensity_brickv.jpg",
	             "Sound Intensity Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/sound_intensity_bricklet_dimensions_100.png",
	             "Dimensions/sound_intensity_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures sound intensity
* 12 bit resolution

Description
-----------



Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Resolution                        12bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 30 x 9mm (0.98 x 1.18 x 0.35")
Weight                            4g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/sound-intensity-bricklet/raw/master/hardware/sound-intensity-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/sound_intensity_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/sound-intensity-bricklet/zipball/master>`__)


.. _sound_intensity_bricklet_test:

Test your Sound Intensity Bricklet
----------------------------------

|test_intro|

|test_connect| (see picture below).

.. FIXME image:: /Images/Bricklets/bricklet_sound_intensity_master_600.jpg
   :scale: 100 %
   :alt: Sound Intensity Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_sound_intensity_master_1200.jpg

|test_tab|
If everything went as expected you can now ... FIXME.

.. FIXME image:: /Images/Bricklets/bricklet_sound_intensity_brickv.jpg
   :scale: 100 %
   :alt: Sound Intensity Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_sound_intensity_brickv.jpg

|test_pi_ref|

.. _sound_intensity_bricklet_case:

Case
----

A `laser-cut case for the Sound Intensity Bricklet <https://www.tinkerforge.com/en/shop/cases/case-sound-intensity-bricklet.html>`__ is available.

.. FIXME image:: /Images/Cases/bricklet_sound_intensity_case_built_up_350.jpg
   :scale: 100 %
   :alt: Case for Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_sound_intensity_case_built_up_1000.jpg

.. include:: Sound_Intensity.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. FIXME image:: /Images/Exploded/sound_intensity_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Exploded/sound_intensity_exploded.png

|bricklet_case_hint|


.. _sound_intensity_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Sound_Intensity_hlpi.table
