
:DISABLED_shoplink: ../../../shop/bricklets/dual-button-v2-bricklet.html

.. include:: Dual_Button_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dual_button_v2_bricklet:

Dual Button Bricklet 2.0
========================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dual_button_v2_tilted_[?|?].jpg           Dual Button Bricklet 2.0
	Bricklets/bricklet_dual_button_v2_horizontal_[?|?].jpg       Dual Button Bricklet 2.0
	Bricklets/bricklet_dual_button_v2_master_[100|600].jpg       Dual Button Bricklet 2.0 with Master Brick
	Cases/bricklet_dual_button_v2_case_[100|600].jpg             Dual Button Bricklet 2.0 with case
	Bricklets/bricklet_dual_button_v2_brickv_[100|].jpg          Dual Button Bricklet 2.0 in Brick Viewer
	Dimensions/dual_button_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Two tactile buttons with built-in blue LEDs
* LED auto-toggle possible


.. _dual_button_v2_bricklet_description:

Description
-----------

The Dual Button :ref:`Bricklet <primer_bricklets>` 2.0 is equipped with
two buttons and can extend :ref:`Bricks <primer_bricks>`. Both buttons have a 
built-in blue LED. You can read the current state of the button 
(pressed/released) and of the LED (on/off). You can turn the LED on/off yourself 
or enable auto-toggle. In auto-toggle mode the LEDs are toggled between on/off 
with each button press.

It is also possible to use events. This allows to react to button presses
without polling.

The Dual Button Bricklet 2.0 has a 7 pole Bricklet connector and is connected to a
Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               27mW (5.4mA at 5V) + 3mW per active LED
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Button Type                       Tactile Button with LED
Button Operating Force            150gf
Button Travel Distance            2.5mm
LED Color                         Blue
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            45 x 20 x 10mm (1.77 x 0.79 x 0.39")
Weight                            5.5g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/dual-button-v2-bricklet/raw/master/hardware/dual-button-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dual_button_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/dual-button-v2-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _dual_button_v2_bricklet_test:

Test your Dual Button Bricklet 2.0
----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see button presses and
change the state of the LED.

.. image:: /Images/Bricklets/bricklet_dual_button_v2_brickv.jpg
   :scale: 100 %
   :alt: Dual Button Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_button_v2_brickv.jpg

|test_pi_ref|


.. _dual_button_v2_bricklet_case:

Case
----

..
	A `laser-cut case for the Dual Button Bricklet 2.0
	<https://www.tinkerforge.com/en/shop/cases/case-dual-button-v2-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_dual_button_v2_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Dual Button Bricklet 2.0
	   :align: center
	   :target: ../../_images/Cases/bricklet_dual_button_v2_case_1000.jpg

	.. include:: Dual_Button_V2.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/dual_button_v2_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Dual Button Bricklet 2.0
	   :align: center
	   :target: ../../_images/Exploded/dual_button_v2_exploded.png

	|bricklet_case_hint|


.. _dual_button_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Dual_Button_V2_hlpi.table
