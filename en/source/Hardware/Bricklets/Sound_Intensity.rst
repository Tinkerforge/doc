
:shoplink: ../../../shop/bricklets/sound-intensity-bricklet.html

.. include:: Sound_Intensity.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _sound_intensity_bricklet:

Sound Intensity Bricklet
========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_sound_intensity_tilted_[?|?].jpg           Sound Intensity Bricklet
	Bricklets/bricklet_sound_intensity_vertical_[?|?].jpg         Sound Intensity Bricklet
	Bricklets/bricklet_sound_intensity_horizontal_[?|?].jpg       Sound Intensity Bricklet
	Bricklets/bricklet_sound_intensity_tilted_back_[?|?].jpg      Sound Intensity Bricklet
	Cases/bricklet_sound_intensity_case_tilted_[?|?].jpg          Sound Intensity Bricklet in Case
	Bricklets/bricklet_sound_intensity_brickv_[100|].jpg          Sound Intensity Bricklet in Brick Viewer
	Dimensions/sound_intensity_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Sound Intensity Bricklet is discontinued. The
 :ref:`Sound Pressure Level Bricklet <sound_pressure_level_bricklet>` is the recommended
 replacement.


Features
--------

* Measures sound intensity
* 12bit resolution
* Usable as clapping switch, alarm system sensor, etc.


.. _sound_intensity_bricklet_description:

Description
-----------

The Sound Intensity :ref:`Bricklet <primer_bricklets>` is equipped
with a microphone capsule and can be used to measure loudness by
:ref:`Bricks <primer_bricks>`. The returned value corresponds to the 
`upper envelop <https://en.wikipedia.org/wiki/Envelope_(waves)>`__
of the signal of the microphone capsule.

It is possible to configure events that are triggered if a specified
threshold of loudness is exceeded.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
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

|test_connect|.

|test_tab|
If everything went as expected you can now see the changing sound
intensity.

.. image:: /Images/Bricklets/bricklet_sound_intensity_brickv.jpg
   :scale: 100 %
   :alt: Sound Intensity Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_sound_intensity_brickv.jpg

|test_pi_ref|

.. _sound_intensity_bricklet_case:

Case
----

A `laser-cut case for the Sound Intensity Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-sound-intensity-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_sound_intensity_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_sound_intensity_case_tilted_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw Bricklet to top plate with spacers at the bottom and long screws from the top,
* build up side plates,
* plug side plates into top plate and
* screw bottom plate to bottom spacers.

Below you can see an exploded assembly drawing of the Temperature IR Bricklet case:

.. image:: /Images/Exploded/sound_intensity_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Sound Intensity Bricklet
   :align: center
   :target: ../../_images/Exploded/sound_intensity_exploded.png

|bricklet_case_hint|


.. _sound_intensity_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Sound_Intensity_hlpi.table
