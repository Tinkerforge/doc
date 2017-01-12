
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Piezo Buzzer Bricklet

.. include:: Piezo_Buzzer.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _piezo_buzzer_bricklet:

Piezo Buzzer Bricklet
=====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_piezo_buzzer_tilted_[?|?].jpg           Piezo Buzzer Bricklet
	Bricklets/bricklet_piezo_buzzer_vertical_[?|?].jpg         Piezo Buzzer Bricklet
	Bricklets/bricklet_piezo_buzzer_horizontal_[?|?].jpg       Piezo Buzzer Bricklet
	Bricklets/bricklet_piezo_buzzer_master_[100|600].jpg       Piezo Buzzer Bricklet with Master Brick
	Bricklets/bricklet_piezo_buzzer_brickv_[100|].jpg          Piezo Buzzer Bricklet in Brick Viewer
	Dimensions/piezo_buzzer_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Piezo Buzzer Bricklet is discontinued and is no longer sold. The
 :ref:`Piezo Speaker Bricklet <piezo_Speaker_bricklet>` is the recommended
 replacement.


Features
--------

* Creates 1kHz beep
* Configurable beep duration


.. _piezo_buzzer_bricklet_description:

Description
-----------

The `Piezo Buzzer <https://en.wikipedia.org/wiki/Buzzer>`__
:ref:`Bricklet <primer_bricklets>` ca be used to
extend the features of :ref:`Bricks <primer_bricks>` by
the capability to beep. The device can output 1kHz beeps in different
lengths. It is possible to beep for a specified timespan or to transmit a
`Morse Code <https://en.wikipedia.org/wiki/Morse_code>`__ string.

A typical application is to beep on specific events (e.g. "email received").


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Buzzer                            PS1420P02CT
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Beep                              Frequency 1kHz, configurable duration
Sound Pressure                    63 dB/10cm (according to datasheet)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 25 x 14mm (0.98 x 0.98 x 0.55")
Weight                            4g
================================  ============================================================


Resources
---------

* PS1420P02CT datasheet (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/raw/master/datasheets/ef532_ps.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/raw/master/hardware/piezo-buzzer-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/piezo_buzzer_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/piezo-buzzer-bricklet/zipball/master>`__)


.. _piezo_buzzer_bricklet_test:

Test your Piezo Buzzer Bricklet
-------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_piezo_buzzer_master_600.jpg
   :scale: 100 %
   :alt: Piezo Buzzer Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_buzzer_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_piezo_buzzer_brickv.jpg
   :scale: 100 %
   :alt: Piezo Buzzer Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_buzzer_brickv.jpg

Generate a beep by pressing "Send Beep". You should hear a beep with the
specified duration.

|test_pi_ref|


.. _piezo_buzzer_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Piezo_Buzzer_hlpi.table
