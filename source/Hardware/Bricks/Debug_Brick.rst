.. _debug_brick:

Debug
=====

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricks/brick_debug_tilted_front_350.jpg", 
	             "Bricks/brick_debug_tilted_front_600.jpg", 
	             "Debug Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_debug_tilted_back_100.jpg", 
	             "Bricks/brick_debug_tilted_back_600.jpg", 
	             "Debug Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_debug_top_100.jpg", 
	             "Bricks/brick_debug_top_600.jpg", 
	             "Debug Brick") 
	}}
	{{ 
	    tfdocimg("Bricks/brick_debug_bottom_100.jpg", 
	             "Bricks/brick_debug_bottom_600.jpg", 
	             "Debug Brick") 
	}}
	{{ 
	    tfdocimg("Dimensions/debug_brick_dimensions_100.png", 
	             "Dimensions/debug_brick_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}

Features
--------

 * For Firmware Developers
 * JTAG and serial interface


Description
-----------

The Debug Brick can be used to add JTAG and serial console debug capabilities
to :ref:`Bricks <product_overview_bricks>`, 
:ref:`Bricklets <product_overview_bricklets>` and stacks.

.. note:: You only need the Debug Brick if you want to debug the low level
 C firmware of Bricks or Bricklets. It does not add any features for PC
 based programming.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions (WxLxH)                40mm x 40mm x 8mm (1.57" x 1.57" x 0.31")*
Weight                            18.4g
================================  ============================================================

* without connectors

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/debug-brick/raw/master/hardware/debug-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/debug_brick_dimensions.png>`__)
* Project design files (`Download <https://github.com/Tinkerforge/debug-brick/zipball/master>`__)
