
:shoplink: ../../../shop/bricklets/dual-button-bricklet.html

.. include:: Dual_Button.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _dual_button_bricklet:

Dual Button Bricklet
====================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dual_button_tilted_[?|?].jpg           Dual Button Bricklet
	Bricklets/bricklet_dual_button_vertical_[?|?].jpg         Dual Button Bricklet
	Bricklets/bricklet_dual_button_horizontal_[?|?].jpg       Dual Button Bricklet
	Bricklets/bricklet_dual_button_tilted_back_[?|?].jpg      Dual Button Bricklet
	Bricklets/bricklet_dual_button_brickv_[100|].jpg          Dual Button Bricklet in Brick Viewer
	Dimensions/dual_button_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Two tactile buttons with built-in blue LEDs
* LED auto-toggle possible


.. _dual_button_bricklet_description:

Description
-----------

The Dual Button :ref:`Bricklet <primer_bricklets>` is equipped with
two buttons and can extend :ref:`Bricks <primer_bricks>`. Both buttons have a 
built-in blue LED. You can read the current state of the button 
(pressed/released) and of the LED (on/off). You can turn the LED on/off yourself 
or enable auto-toggle. In auto-toggle mode the LEDs are toggled between on/off 
with each button press.

It is also possible to use events. This allows to react to button presses
without polling.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               1mA per active LED
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Button Type                       Tactile Button with LED
Button Operating Force            150gf
Button Travel Distance            2.5mm
LED Color                         Blue
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            45 x 20 x 10mm (1.77 x 0.79 x 0.39")
Weight                            6g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/dual-button-bricklet/raw/master/hardware/dual-button-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dual_button_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/dual-button-bricklet/zipball/master>`__)


.. _dual_button_bricklet_test:

Test your Dual Button Bricklet
------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see button presses and
change the state of the LED.

.. image:: /Images/Bricklets/bricklet_dual_button_brickv.jpg
   :scale: 100 %
   :alt: Dual Button Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_button_brickv.jpg

|test_pi_ref|


.. _dual_button_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Dual_Button_hlpi.table
