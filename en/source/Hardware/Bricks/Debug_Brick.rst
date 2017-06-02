
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Debug Brick
:shoplink: ../../../shop/bricks/debug-brick.html

.. _debug_brick:

Debug Brick
===========

.. raw:: html

	{% tfgallery %}

	Bricks/brick_debug12_tilted_[?|?].jpg         Debug Brick
	Bricks/brick_debug12_w_headers_[100|800].jpg  Debug Brick with headers soldered in
	Bricks/brick_debug12_top_[?|?].jpg            Debug Brick top
	Bricks/brick_debug12_bottom_[?|?].jpg         Debug Brick bottom
	Bricks/brick_debug12_stack_[?|?].jpg          Debug Brick on stack

	{% tfgalleryend %}

.. FIXME: outdated
	{{
	    tfdocimg("Dimensions/debug_brick_dimensions_100.png",
	             "Dimensions/debug_brick_dimensions_600.png",
	             "Outline and drilling plan")
	}}

Features
--------

* For Firmware Developers
* JTAG and serial console


.. _debug_brick_description:

Description
-----------

The Debug Brick can be used to add JTAG and serial console debug capabilities
to :ref:`Bricks <primer_bricks>`,
:ref:`Bricklets <primer_bricklets>` and :ref:`stacks <primer_stack>`.

You only need the Debug Brick if you want to debug the low level C firmware
of Bricks or Bricklets. It does not add any features for PC based programming.

In hardware version 1.2 the D-Sub 9 connector got replaced with a Mini-USB
connector and a Silicon Labs CP2104 USB-to-serial converter. This
converter requires an extra driver that can be downloaded from the
`Silicon Labs <https://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx>`__
website.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions (W x D x H)            40 x 40 x 8mm (1.57 x 1.57 x 0.31")
Weight                            8g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/debug-brick/raw/master/hardware/debug-schematic.pdf>`__)
* Design files (`Download <https://github.com/Tinkerforge/debug-brick/zipball/master>`__)
* 3D model (`Download STEP <http://download.tinkerforge.com/3d/bricks/debug/debug.step>`__ | `Download FreeCAD <http://download.tinkerforge.com/3d/bricks/debug/debug.FCStd>`__)

.. FIXME: outdated. originally belongs between Schematic and Design files
	* Outline and drilling plan (`Download <../../_images/Dimensions/debug_brick_dimensions.png>`__)


Known Bugs
----------

The (now obsolete) Debug Brick Hardware Version 1.1 has a design flaw. 
GND pins of the JTAG connector are not connected. 
This can lead to debug problems when using the JTAG interface. 
The serial console is not affected. The problem can be fixed
by soldering a wire from a GND pin of the JTAG connector to a GND pad on the
board. This issue will be fixed with the next hardware version. 

.. image:: /Images/Bricks/brick_debug_wire_fix_350.jpg
   :scale: 100 %
   :alt: Debug Brick with Wire
   :align: center
   :target: ../../_images/Bricks/brick_debug_wire_fix_1000.jpg
