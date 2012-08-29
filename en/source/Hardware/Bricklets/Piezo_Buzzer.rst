.. _piezo_buzzer_bricklet:

Piezo Buzzer Bricklet
=====================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_piezo_buzzer_tilted_350.jpg",
	               "Bricklets/bricklet_piezo_buzzer_tilted_600.jpg",
	               "Piezo Buzzer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_buzzer_vertical_100.jpg",
	             "Bricklets/bricklet_piezo_buzzer_vertical_600.jpg",
	             "Piezo Buzzer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_buzzer_horizontal_100.jpg",
	             "Bricklets/bricklet_piezo_buzzer_horizontal_600.jpg",
	             "Piezo Buzzer Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_buzzer_master_100.jpg",
	             "Bricklets/bricklet_piezo_buzzer_master_600.jpg",
	             "Piezo Buzzer Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_piezo_buzzer_brickv_100.jpg",
	             "Bricklets/bricklet_piezo_buzzer_brickv.jpg",
	             "Piezo Buzzer Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/piezo_buzzer_bricklet_dimensions_100.png",
	             "Dimensions/piezo_buzzer_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Creates 1kHz beep
* Configurable beep duration


Description
-----------

The `Piezo Buzzer <http://en.wikipedia.org/wiki/Buzzer>`__
:ref:`Bricklet <product_overview_bricklets>` ca be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by
the capability to beep. The device can output 1kHz beeps in different
lengths. It is possible to beep for a specified timespan or to transmit a
`Morse Code <http://en.wikipedia.org/wiki/Morse_code>`__ string.

A typical application is to beep on specific events (e.g. "email received").


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Buzzer                            PS1420P02CT
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

To test the Piezo Buzzer Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

For a simple test connect the Piezo Buzzer Bricklet to a
:ref:`Brick <product_overview_bricks>` with the supplied cable
(see picture below).

.. image:: /Images/Bricklets/bricklet_piezo_buzzer_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Piezo Buzzer Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_buzzer_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named
"Piezo Buzzer Bricklet" in the Brick Viewer after you pressed "connect".
Select it.
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_piezo_buzzer_brickv.jpg
   :scale: 100 %
   :alt: Piezo Buzzer Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_piezo_buzzer_brickv.jpg

Generate a beep by pressing "Send Beep". You should hear a beep with the
specified duration.

You can now go on with writing your own application.
See the :ref:`Programming Interface <piezo_buzzer_programming_interfaces>`
section for the API of the Piezo Buzzer Bricklet and examples in your
programming language.


.. _piezo_buzzer_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Piezo_Buzzer_hlpi.table
