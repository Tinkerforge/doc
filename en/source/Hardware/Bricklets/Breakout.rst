
:shoplink: ../../../shop/bricklets/breakout-bricklet.html

.. _breakout_bricklet:

Breakout Bricklet
=================

.. raw:: html

	{% tfgallery %}

	Bricklets/breakout_bricklet_tilted_[?|?].jpg                Breakout Bricklet
	Bricklets/breakout_bricklet_horizontal_pinheader_[?|?].jpg  Breakout Bricklet
	Bricklets/breakout_bricklet_connected_[100|600].jpg         Breakout Bricklet with Rotary Poti

	{% tfgalleryend %}


Features
--------

* Makes all Bricklet signals available
* Not detected by Bricks


.. _breakout_bricklet_description:

Description
-----------

The Breakout Bricklet is a breakout board for Bricklets. It makes all signals
of the :ref:`Bricklet connector <connector_bricklet>` available.

This allows the use of Bricklets as breakout boards for the sensor on the
Bricklet. For example: If you want to use an ambient light sensor in
your embedded project but you don't want to solder the tiny SMD IC,
you can buy the Ambient Light Bricklet together with the Breakout Bricklet
and solder cables on the big pads of the Breakout Bricklet.

You can also use a standard pin header to make an easy connect and
disconnect of the sensor possible.

.. note::
 The Breakout Bricklet is an adapter, it can not be recognized by Bricks.
 There is no API for the Bricklet available.
 You have to write your own firmware on the Bricks to use this Bricklet.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Dimensions (W x D x H)            25 x 25 x 5mm (0.98 x 0.98 x 0.19")*
Weight                            2g
================================  ============================================================

\* without pin header

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/breakout-bricklet/raw/master/hardware/breakout-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/breakout_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/breakout-bricklet/zipball/master>`__)
