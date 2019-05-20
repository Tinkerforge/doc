
:shoplink: ../../../shop/bricklets/linear-poti-bricklet.html

.. include:: Linear_Poti.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _linear_poti_bricklet:

Linear Poti Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_linear_poti_tilted_[?|?].jpg           Linear Poti Bricklet
	Bricklets/bricklet_linear_poti_front_[?|?].jpg            Linear Poti Bricklet
	Bricklets/bricklet_linear_poti_vertical_[?|?].jpg         Linear Poti Bricklet
	Bricklets/bricklet_linear_poti_horizontal_[?|?].jpg       Linear Poti Bricklet
	Bricklets/bricklet_linear_poti_knob_[100|600].jpg         Linear Poti Bricklet
	Bricklets/bricklet_linear_poti_master_[100|600].jpg       Linear Poti Bricklet with Master Brick
	Cases/bricklet_linear_poti_case_[100|600].jpg             Linear Poti Bricklet in Case
	Bricklets/bricklet_linear_poti_brickv_[100|].jpg          Linear Poti Bricklet in Brick Viewer
	Dimensions/linear_poti_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Linear Poti Bricklet is discontinued. We are selling our remaining stock. The
 :ref:`Linear Poti Bricklet 2.0 <linear_poti_v2_bricklet>` is the recommended
 replacement.


Features
--------

* 59mm linear potentiometer
* Outputs position from 0% to 100% in 1% steps


.. _linear_poti_bricklet_description:

Description
-----------

The Linear Poti :ref:`Bricklet <primer_bricklets>` is equipped with
a linear `potentiometer <https://en.wikipedia.org/wiki/Potentiometer>`__
("fader", "slider"). It can be connected to a
:ref:`Brick <primer_bricks>`, with which the position of the
slider can be read out.
With configurable events it is possible to react on changing positions
without polling.

You can use this Bricklet for speed, volume control or similar purposes.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Linear Potentiometer              59mm (2.32") adjustable length
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Position                          0% - 100% (slider down - slider up) in 1% steps
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 85 x 20mm (0.98 x 3.35 x 0.78")*
Weight                            14g*
================================  ============================================================

\* without knob


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/raw/master/hardware/linear-poti-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/linear_poti_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/linear-poti-bricklet/zipball/master>`__)


.. _linear_poti_bricklet_test:

Test your Linear Poti Bricklet
------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_linear_poti_master_600.jpg
   :scale: 100 %
   :alt: Linear Poti Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_linear_poti_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_linear_poti_brickv.jpg
   :scale: 100 %
   :alt: Linear Poti Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_linear_poti_brickv.jpg

Move the potentiometer.
You should be able to create a similar graph
by moving the potentiometer from bottom to top and back to bottom.

|test_pi_ref|


.. _linear_poti_bricklet_case:

Case
----

A `laser-cut case for the Linear Poti Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-linear-poti-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_linear_poti_case_350.jpg
   :scale: 100 %
   :alt: Case for Linear Poti Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_linear_poti_case_1000.jpg

.. include:: Linear_Poti.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/linear_poti_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Linear Poti Bricklet
   :align: center
   :target: ../../_images/Exploded/linear_poti_exploded.png

|bricklet_case_hint|


.. _linear_poti_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Linear_Poti_hlpi.table
