
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Piezo Speaker Bricklet
:shoplink: ../../../shop/bricklets/piezo-speaker-bricklet.html

.. include:: Piezo_Speaker.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _piezo_speaker_bricklet:

Piezo Speaker Bricklet
========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_piezo_speaker_tilted_350.jpg",
	               "Bricklets/bricklet_piezo_speaker_tilted_600.jpg",
	               "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_vertical_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_vertical_600.jpg",
	             "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_horizontal_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_horizontal_600.jpg",
	             "Piezo Speaker Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_piezo_speaker_case_tilted_100.jpg",
	             "Cases/bricklet_piezo_speaker_case_tilted_600.jpg",
	             "Piezo Speaker Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_speaker_brickv_100.jpg",
	             "Bricklets/bricklet_piezo_speaker_brickv.jpg",
	             "Piezo Speaker Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/piezo_speaker_bricklet_dimensions_100.png",
	             "Dimensions/piezo_speaker_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Creates beeps with configurable frequency of 585Hz to 7100Hz
* Configurable beep duration
* Morse code output supported

Description
-----------

The Piezo Speaker :ref:`Bricklet <product_overview_bricklets>` can be used to
generate beeps with different frequencies. The available frequency range is
585Hz to 7100Hz. A beep has a configurable length and it is possible to transmit
a `Morse Code <http://en.wikipedia.org/wiki/Morse_code>`__ string.

A typical application is to beep on specific events (e.g. "email received").

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Buzzer                            PS1420P02CT
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Frequency Range                   585 - 7100Hz (configurable)
Sound Pressure                    60 - 82dB/10cm (depends on frequency)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 30 x 13mm (0.98 x 1.18 x 0.51")
Weight                            5g
================================  ============================================================


Resources
---------

* PS1420P02CT datasheet (`Download <https://github.com/Tinkerforge/piezo-speaker-bricklet/raw/master/datasheets/ef532_ps.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/piezo-speaker-bricklet/raw/master/hardware/piezo-speaker-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/piezo_speaker_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/piezo-speaker-bricklet/zipball/master>`__)


.. _piezo_speaker_bricklet_test:

Test your Piezo Speaker Bricklet
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now generate beeps.

.. image:: /Images/Bricklets/bricklet_piezo_speaker_brickv.jpg
   :scale: 100 %
   :alt: Piezo Speaker Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_speaker_brickv.jpg

|test_pi_ref|

.. _piezo_speaker_bricklet_case:

Case
----

A `laser-cut case for the Piezo Speaker Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-piezo-speaker-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_piezo_speaker_case_tilted_350.jpg
   :scale: 100 %
   :alt: Case for Piezo Speaker Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_piezo_speaker_case_tilted_1000.jpg

.. include:: Piezo_Speaker.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/piezo_speaker_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Piezo Speaker Bricklet
   :align: center
   :target: ../../_images/Exploded/piezo_speaker_exploded.png

|bricklet_case_hint|


.. _piezo_speaker_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Piezo_Speaker_hlpi.table
