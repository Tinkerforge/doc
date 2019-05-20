
:DISABLED_shoplink: ../../../shop/bricklets/piezo-speaker-v2-bricklet.html

.. include:: Piezo_Speaker_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _piezo_speaker_v2_bricklet:

Piezo Speaker Bricklet 2.0
==========================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_piezo_speaker_v2_tilted_[?|?].jpg           Piezo Speaker Bricklet 2.0
	Bricklets/bricklet_piezo_speaker_v2_top_[?|?].jpg              Piezo Speaker Bricklet 2.0
	Bricklets/bricklet_piezo_speaker_v2_side_[?|?].jpg             Piezo Speaker Bricklet 2.0
	Bricklets/bricklet_piezo_speaker_v2_brickv_[100|].jpg          Piezo Speaker Bricklet 2.0 in Brick Viewer
	Dimensions/piezo_speaker_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Can beep with configurable frequency of 50Hz to 15000Hz
* Can output fully configurable alarm/siren sound
* Loudness configurable between 85dB(A) and 110dB(A)


.. _piezo_speaker_v2_bricklet_description:

Description
-----------

The Piezo Speaker :ref:`Bricklet <primer_bricklets>` can be used to extend
:ref:`Bricks <primer_bricks>` by the possibility to generate beeps with 
different frequencies and volume. 

The available frequency range is 50Hz to 15000Hz. You can control the volume
with a sound pressure level range of 85dB(A) to 110dB(A).

Additionally the Bricklet has support for alarm/siren sounds. In this mode 
it will sweep through a frequency range with configurable range, step size and
duration.

The Piezo Speaker Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Below you can find an audio file with samples of different sounds and alarams 
that have been generated with a Piezo Speaker Bricklet 2.0:

.. raw:: html
 
	<audio controls>
	  <source src="../../_images/Videos/bricklet_piezo_speaker_v2_audio.ogg" type="audio/ogg">
	  <source src="../../_images/Videos/bricklet_piezo_speaker_v2_audio.mp3" type="audio/mp3">
	</audio>


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Buzzer                            PT-4532PLQ
Current Consumption               55mW (11mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Frequency Range                   50Hz - 15000Hz (configurable)
Sound Pressure                    85dB(A) - 110dB(A) @50cm/1kHz (configurable)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            55 x 45 x 20mm (2.2 x 1.8 x 0.8")
Weight                            20g
================================  ============================================================


Resources
---------

* PT-4532PLQ datasheet (`Download <https://github.com/Tinkerforge/piezo-speaker-v2-bricklet/raw/master/datasheets/PT-4532PLQ.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/piezo-speaker-v2-bricklet/raw/master/hardware/piezo-speaker-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/piezo_speaker_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/piezo-speaker-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/30jdwD4>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/piezo_speaker_v2/piezo-speaker-v2.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/piezo_speaker_v2/piezo-speaker-v2.FCStd>`__)


.. _piezo_speaker_v2_bricklet_test:

Test your Piezo Speaker Bricklet 2.0
------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now generate beep and alarm sounds.

.. image:: /Images/Bricklets/bricklet_piezo_speaker_v2_brickv.jpg
   :scale: 100 %
   :alt: Piezo Speaker Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_v2_brickv.jpg

|test_pi_ref|


Volume and Sound Pressure Level
-------------------------------

The Bricklet has 11 different volume levels (volume value 0 to 10).

We measured the sound pressure level with the test setup below.
We used the average of three different sound pressure level meters at
50cm distance. The frequency of the Piezo Speaker Bricklet 2.0 was
set to 1kHz.

.. image:: /Images/Bricklets/bricklet_piezo_speaker_v2_spl1_800.jpg
   :scale: 100 %
   :alt: Piezo Speaker Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_v2_spl1_1200.jpg

The result is a range of 85dB(A) to 110dB(A):

.. image:: /Images/Bricklets/bricklet_piezo_speaker_v2_spl_bargraph.png
   :scale: 100 %
   :alt: Piezo Speaker Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_v2_spl_bargraph.png

You can use the volume range of 0-4 for different notification beep loudness levels
and the volume range of 5-10 for loud and annoying alarm sounds.

.. warning::
	Please note: At 110 dB(A) the recommended permissible exposure time (according to
	`NIOSH and CDC <https://www.cdc.gov/niosh/topics/noise/chart-lookatnoise.html>`__) 
	is only about 1.5 minutes.


.. _piezo_speaker_v2_bricklet_case:

Case
----

Comming soon...

..
	A `laser-cut case for the Piezo Speaker Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-piezo-speaker-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_piezo_speaker_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Piezo Speaker Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_piezo_speaker_v2_case_1000.jpg

	.. include:: Piezo_Speaker_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/piezo_speaker_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Piezo Speaker Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/piezo_speaker_v2_exploded.png

	|bricklet_case_hint|


.. _piezo_speaker_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Piezo_Speaker_V2_hlpi.table
