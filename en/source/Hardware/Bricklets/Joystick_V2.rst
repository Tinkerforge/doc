
:shoplink: ../../../shop/bricklets/joystick-v2-bricklet.html

.. include:: Joystick_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _joystick_v2_bricklet:

Joystick Bricklet 2.0
=====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_joystick_v2_tilted_[?|?].jpg           Joystick Bricklet 2.0
	Bricklets/bricklet_joystick_v2_top_[?|?].jpg              Joystick Bricklet 2.0
	Bricklets/bricklet_joystick_v2_side_[?|?].jpg             Joystick Bricklet 2.0
	Bricklets/bricklet_joystick_v2_brickv_[100|].jpg          Joystick Bricklet 2.0 in Brick Viewer
	Dimensions/joystick_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 2-axis joystick with push-button


.. _joystick_v2_bricklet_description:

Description
-----------

The Joystick :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by joystick
functionality.

The Joystick is two directional and equipped with a push-button.
You can read out the position of the stick (X/Y coordinates) and
the state of the button. 

With configurable events it is possible to react on
changing positions and on button presses without polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Joystick                          2-axis with push-button
Current Consumption               45mW (9mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
X/Y Position                      -100/100, 0=center
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 45 x 23mm (0.98 x 1.77 x 0.9")*
Weight                            15g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/joystick-v2-bricklet/raw/master/hardware/joystick-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/joystick_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/joystick-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/30pO5Ab>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/joystick_v2/joystick-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/joystick_v2/joystick-v2.FCStd>`__)


.. _joystick_v2_bricklet_test:

Test your Joystick Bricklet 2.0
-------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_joystick_v2_brickv.jpg
   :scale: 100 %
   :alt: Joystick Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_joystick_v2_brickv.jpg

The tab consists of a coordinate system that shows the current position of
the stick and if the button is pressed.
Below this coordinate system you can find a graph that visualizes the
movements over time.
You should be able to reproduce the depicted graph when you move the
stick first up, then down, then right and then end left.

If the Brick Viewer does not show "Position x=0, y=0" when the stick is
in center position, press the "Calibrate Zero" button.

|test_pi_ref|


.. _joystick_v2_bricklet_case:

Case
----

A `laser-cut case for the Joystick Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-joystick-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_joystick_case_350.jpg
   :scale: 100 %
   :alt: Case for Joystick Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_joystick_case_1000.jpg

.. include:: Joystick_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/joystick_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Joystick Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/joystick_exploded.png

|bricklet_case_hint|


.. _joystick_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Joystick_V2_hlpi.table
