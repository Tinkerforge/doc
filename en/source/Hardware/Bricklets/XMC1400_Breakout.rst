
:DISABLED_shoplink: ../../../shop/bricklets/xmc1400-breakout-bricklet.html

.. include:: XMC1400_Breakout.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _xmc1400_breakout_bricklet:

XMC1400 Breakout Bricklet
=========================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_xmc1400_breakout_tilted_[?|?].jpg           XMC1400 Breakout Bricklet
	Bricklets/bricklet_xmc1400_breakout_horizontal_[?|?].jpg       XMC1400 Breakout Bricklet
	Bricklets/bricklet_xmc1400_breakout_master_[100|600].jpg       XMC1400 Breakout Bricklet with Master Brick
	Cases/bricklet_xmc1400_breakout_case_[100|600].jpg             XMC1400 Breakout Bricklet with case
	Bricklets/bricklet_xmc1400_breakout_brickv_[100|].jpg          XMC1400 Breakout Bricklet in Brick Viewer
	Dimensions/xmc1400_breakout_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Bricklet development board
* Used for development of new Bricklets


.. _xmc1400_breakout_bricklet_description:

Description
-----------

The XMC1400 Breakout :ref:`Bricklet <primer_bricklets>` is a breakout board for
the XMC1400 microcontroller from Infineon in the Bricklet form factor.

It can be used as a basis for prototypes of new Bricklets.

It has the standard Bricklet connector, status LED and boot pad. The bootloader
as well as an example firmware is already flashed. All available pins are routed out
and can be accessed through a pin header.

If you want to develop your own Bricklet, you can use this to get started without
having to develop your own custom hardware first.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               55mW (11mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Number of available IOs           42                           
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            50 x 45 x 15mm (1.97 x 1.77 x 0.59")
Weight                            12g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/xmc1400-breakout-bricklet/raw/master/hardware/xmc1400-breakout-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/xmc1400_breakout_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/xmc1400-breakout-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


.. _xmc1400_breakout_bricklet_test:

Test your XMC1400 Breakout Bricklet
-----------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the example plugin.

.. image:: /Images/Bricklets/bricklet_xmc1400_breakout_brickv.jpg
   :scale: 100 %
   :alt: XMC1400 Breakout Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_xmc1400_breakout_brickv.jpg

|test_pi_ref|


.. _xmc1400_breakout_bricklet_tutorial:

Tutorial: Add Getter Function
-----------------------------

.. note::

 This tutorial is unfortunately not yet ready. It is on our TODO list.
 If you are interested in it write us an email to info@tinkerforge.com,
 so we know that there is a demand for it.


We plan to write a tutorial that goes through the whole process
of adding functions to the API, implementing them in the firmware
and adding a GUI element for it in Brick Viewer through the
following steps:

* Add getter function to generator
* Generate/copy stubs
* Implement functionality of stub in firmware
* Generate bindings
* Write program with new bindings that uses new getter
* Add GUI element to Brick Viewer that uses new getter


.. _xmc1400_breakout_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: XMC1400_Breakout_hlpi.table
