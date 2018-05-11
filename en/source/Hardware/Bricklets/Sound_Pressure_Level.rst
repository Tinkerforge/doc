
:DISABLED_shoplink: ../../../shop/bricklets/sound-pressure-level-bricklet.html

.. include:: Sound_Pressure_Level.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _sound_pressure_level_bricklet:

Sound Pressure Level Bricklet
=============================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_sound_pressure_level_tilted_[?|?].jpg           Sound Pressure Level Bricklet
	Bricklets/bricklet_sound_pressure_level_horizontal_[?|?].jpg       Sound Pressure Level Bricklet
	Bricklets/bricklet_sound_pressure_level_master_[100|600].jpg       Sound Pressure Level Bricklet with Master Brick
	Cases/bricklet_sound_pressure_level_case_[100|600].jpg             Sound Pressure Level Bricklet with case
	Bricklets/bricklet_sound_pressure_level_brickv_[100|].jpg          Sound Pressure Level Bricklet in Brick Viewer
	Dimensions/sound_pressure_level_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Measures sound pressure level in dB(A/B/C/D/Z) and ITU-R 468
* Measures spectrum with up to 512 bins and up to 80 samples per second
* Frequency range 40Hz to 40960Hz
* Noise floor 30dB, maximum 120dB


.. _sound_pressure_level_bricklet_description:

Description
-----------

The Sound Pressure Level :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the
capability to measure 
`sound pressure level <https://en.wikipedia.org/wiki/Sound_pressure#Sound_pressure_level>`__ and
sound `spectrum <https://en.wikipedia.org/wiki/Spectrogram>`__. The measured sound
pressure level can be returned weighted by the 
`frequency-weighting standards <https://en.wikipedia.org/wiki/A-weighting>`__
A, B, C, D, ITU-R 468 and flat weighting (Z).

The sensor can be used to measure loudness of music, construction sites, street noises and
other environmenstal noises in a variety of weighting standards. It is also possible to
determine the frequency composition (spectrum).

The Sound Pressure Level Bricklet has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               50mW (10mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
dB(X) Accuracy*                   +-5dB, +-5% maximum full-scale error
Measurement Range                 30dB - 120dB
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 25 x 6mm (0.98 x 0.98 x 0.24")
Weight                            2.6g
================================  ============================================================

\* Valid for the range of 100Hz to 8kHz. For details see :ref:`below <sound_pressure_level_bricklet_accuracy>`.

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/sound-pressure-level-bricklet/raw/master/hardware/sound-pressure-level-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/sound_pressure_level_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/sound-pressure-level-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _sound_pressure_level_bricklet_accuracy:

Accuracy and Calibration
------------------------

The Bricklet is calibrated against a sound pressure level meter with
1.5dB accuracy. The utilized MEMS microphone has a non-flat frequency
response with up to 1.5dB deviation in the range of 100Hz to 8kHz.

We add another 2dB for small variations in the mounting and the small
hole in the Bricklet etc to reach the specification of +-5dB.

For frequencies from 8kHz to 20kHz the deviation in frequency response
increases significantly. We compensated this range in accordance to the
ICS43432 datasheet, but we can't give any guarantees in this range. We
were not able to compare this to a "ground truth"-value, since most
professional sound pressure level meters only measure up to 8kHz.

Additionally, the frequency response changes between microphones. To
calibrate this we would have to calibrate in an anechoic chamber for
each Bricklet. This is not economically feasable for a Bricklet.
We account for this with an additional absolute maximum 5% full-scale
error.

In our tests we found that the noise floor of the Bricklet is at about
30dB and we measured values up to 120dB.

The Bricklet is not tested with regards to IEC 61252:1993 class 1 or 2 
or IEC 61672 part 2 and it does not have "Pattern Approval".

As a general rule of thumb: The Bricklet will perform about as well
as other sub-200€ sound pressure level meters. Do not use this Bricklet
for measurements that have important health or safety implications!

.. _sound_pressure_level_bricklet_test:

Test your Sound Pressure Level Bricklet
---------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the spectrum and decibel value.

.. image:: /Images/Bricklets/bricklet_sound_pressure_level_brickv.jpg
   :scale: 100 %
   :alt: Sound Pressure Level Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_sound_pressure_level_brickv.jpg

|test_pi_ref|


.. _sound_pressure_level_bricklet_examples:

Examples
--------

Guitar music:

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls loop>
	  <source src="../../_images/Videos/sound_pressure_level_guitar.mp4" type="video/mp4">
	  <source src="../../_images/Videos/sound_pressure_level_guitar.ogg" type="video/ogg">
	  <source src="../../_images/Videos/sound_pressure_level_guitar.webm" type="video/webm">
	</video>


Moving sine wave:

.. raw:: html
 
	<video class="align-center" max-width="100%" width="100%" height="auto" controls loop>
	  <source src="../../_images/Videos/sound_pressure_level_moving_sine_wave.mp4" type="video/mp4">
	  <source src="../../_images/Videos/sound_pressure_level_moving_sine_wave.ogg" type="video/ogg">
	  <source src="../../_images/Videos/sound_pressure_level_moving_sine_wave.webm" type="video/webm">
	</video>


.. _sound_pressure_level_bricklet_case:

Case
----

..
	A `laser-cut case for the Sound Pressure Level Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-sound-pressure-level-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_sound_pressure_level_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Sound Pressure Level Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_sound_pressure_level_case_1000.jpg

	.. include:: Sound_Pressure_Level.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/sound_pressure_level_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Sound Pressure Level Bricklet
	   :align: center
	   :target: ../../_images/Exploded/sound_pressure_level_exploded.png

	|bricklet_case_hint|


.. _sound_pressure_level_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Sound_Pressure_Level_hlpi.table
