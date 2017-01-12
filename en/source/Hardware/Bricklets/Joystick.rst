
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Joystick Bricklet
:shoplink: ../../../shop/bricklets/joystick-bricklet.html

.. include:: Joystick.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _joystick_bricklet:

Joystick Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_joystick_tilted_[?|?].jpg           Joystick Bricklet
	Bricklets/bricklet_joystick_front_[?|?].jpg            Joystick Bricklet
	Bricklets/bricklet_joystick_horizontal_[?|?].jpg       Joystick Bricklet
	Bricklets/bricklet_joystick_master_[100|600].jpg       Joystick Bricklet with Master Brick
	Cases/bricklet_joystick_case_[100|600].jpg             Joystick Bricklet in Case
	Bricklets/bricklet_joystick_brickv_[100|].jpg          Joystick Bricklet in Brick Viewer
	Dimensions/joystick_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 2-axis joystick with push-button


.. _joystick_bricklet_description:

Description
-----------

The Joystick :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by joystick
functionality.

The Joystick is two directional and equipped with a push-button.
You can read out the position of the stick (X/Y coordinates) and
the state of the button. With configurable events it is possible to react on
changing positions and an button presses without polling.

You can use this device to control robots, games etc.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Joystick                          2-axis with push-button
Current Consumption               2mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
X/Y Position                      -100/100, 0=center
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 45 x 23mm (0.98 x 1.77 x 0.9")*
Weight                            12g*
================================  ============================================================

\* without knob


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/joystick-bricklet/raw/master/hardware/joystick-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/joystick_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/joystick-bricklet/zipball/master>`__)


.. _joystick_bricklet_test:

Test your Joystick Bricklet
---------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_joystick_master_600.jpg
   :scale: 100 %
   :alt: Joystick Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_joystick_brickv.jpg
   :scale: 100 %
   :alt: Joystick Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_brickv.jpg

The tab consists of a coordinate system that shows the current position of
the stick and if the button is pressed.
Below this coordinate system you can find a graph that visualizes the
movements over time.
You should be able to reproduce the depicted graph when you move the
stick first up, then down, then right and then end left.

If the Brick Viewer does not show "Position (0,0)" when the stick is
in center position, press the "Calibrate (0,0)" button.

|test_pi_ref|

.. _joystick_bricklet_case:

Case
----

A `laser-cut case for the Joystick Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-joystick-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_joystick_case_350.jpg
   :scale: 100 %
   :alt: Case for Joystick Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_joystick_case_1000.jpg

.. include:: Joystick.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/joystick_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Joystick Bricklet
   :align: center
   :target: ../../_images/Exploded/joystick_exploded.png

|bricklet_case_hint|


.. _joystick_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Joystick_hlpi.table
