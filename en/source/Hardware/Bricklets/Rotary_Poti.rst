
:shoplink: ../../../shop/bricklets/rotary-poti-bricklet.html

.. include:: Rotary_Poti.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _rotary_poti_bricklet:

Rotary Poti Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_rotary_poti_tilted_[?|?].jpg           Rotary Poti Bricklet
	Bricklets/bricklet_rotary_poti_front_[?|?].jpg            Rotary Poti Bricklet
	Bricklets/bricklet_rotary_poti_vertical_[?|?].jpg         Rotary Poti Bricklet
	Bricklets/bricklet_rotary_poti_horizontal_[?|?].jpg       Rotary Poti Bricklet
	Bricklets/bricklet_rotary_poti_knob_[100|600].jpg         Rotary Poti Bricklet
	Bricklets/bricklet_rotary_poti_master_[100|600].jpg       Rotary Poti Bricklet with Master Brick
	Cases/bricklet_rotary_poti_case_shallow_[100|600].jpg     Rotary Poti Bricklet im Gehäuse
	Bricklets/bricklet_rotary_poti_brickv_[100|].jpg          Rotary Poti Bricklet in Brick Viewer
	Dimensions/rotary_poti_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 300° rotary potentiometer
* Outputs position from -150° to 150° in 1° steps


.. _rotary_poti_bricklet_description:

Description
-----------

The Rotary Poti :ref:`Bricklet <primer_bricklets>` is equipped with
a 1-turn rotary `potentiometer <https://en.wikipedia.org/wiki/Potentiometer>`__.
It can be connected to a
:ref:`Brick <primer_bricks>`, with which the position of the
slider can be read out. With configurable events it is possible to react on
changing positions without polling.

You can use this Bricklet for speed, volume control or similar purposes.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Rotary Potentiometer              1-turn, 300°
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          -150° to 150° (left to right) in 1° steps
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            30 x 25 x 23mm (1.18 x 0.98 x 0.9")*
Weight                            5g*
================================  ============================================================

\* without knob


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/raw/master/hardware/rotary-poti-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rotary_poti_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rotary-poti-bricklet/zipball/master>`__)


.. _rotary_poti_bricklet_test:

Test your Rotary Poti Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_rotary_poti_master_600.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_rotary_poti_brickv.jpg
   :scale: 100 %
   :alt: Rotary Poti Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_rotary_poti_brickv.jpg

Turn the potentiometer.
You should be able to create a similar graph by turning the potentiometer
from left left to right and back to left.

|test_pi_ref|

.. _rotary_poti_bricklet_case:

Case
----

A `laser-cut case for the Rotary Poti Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-rotary-poti-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_rotary_poti_case_350.jpg
   :scale: 100 %
   :alt: Case for Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_rotary_poti_case_1000.jpg

.. include:: Rotary_Poti.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/rotary_poti_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Rotary Poti Bricklet
   :align: center
   :target: ../../_images/Exploded/rotary_poti_exploded.png

|bricklet_case_hint|


.. _rotary_poti_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Rotary_Poti_hlpi.table
