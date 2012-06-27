.. _rs485_extension:

RS485 Extension
===============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Extensions/extension_rs485_tilted_350.jpg", 
	             "Extensions/extension_rs485_tilted_600.jpg", 
	             "RS485 Extension") 
	}}
	{{ 
	    tfdocimg("Extensions/extension_rs485_top_100.jpg", 
	             "Extensions/extension_rs485_top_600.jpg", 
	             "RS485 Extension") 
	}}
	{{ 
	    tfdocimg("Extensions/extension_rs485_bottom_100.jpg", 
	             "Extensions/extension_rs485_bottom_600.jpg", 
	             "RS485 Extension") 
	}}
	{{ tfdocend() }}


Features
--------

 * Long distance connections (up to 1200m)
 * Allows wired interconnection between stacks
 * Configurable baud rate, parity and stop bits
 * Can be used in existing RS485 networks (Modbus RTU)

Description
-----------

The RS485 Extension can be used for long range cable based
inter-stack communication. It uses the RS485 differential interface
standard to achieve ranges of **up to 1200m**.

To establish a RS485 bus with Bricks, two RS485 Extensions and two
Master Bricks are needed. Both Master Bricks can be connected to a
full stack of Bricks and Bricklets, whereas one Master Brick is Battery
powered and one is connected with USB. From a programming perspective
the RS485 bus is completely transparent, i.e. the two stacks can
be used exactly the same way as if they were both connected via USB.

It is also possible to create a bus with several RS485 Extension where
only one is connected via USB (many-to-one routing).

`Modbus RTU <http://en.wikipedia.org/wiki/Modbus>`__ is used as the
protocol on the RS485 interface. This allows to use a stack of Bricks
and Bricklets with an RS485 Extension to be integrated in existing
Modbus networks. It is also possible to communicate with a stack
directly via Modbus from an embedded device or over a Modbus gateway.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Device Current Consumption        TBD
Maximum Baud Rate                 2Mbit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            13g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/rs485-extension/raw/master/hardware/rs485-extension-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rs485_extension_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/rs485-extension>`__)
* RS485 IC Datasheet (`Download <https://github.com/Tinkerforge/rs485-extension/blob/master/datasheets/ADM3485.pdf>`__)


RS485 Bus Assembly
------------------

* Coming Soon


Connectivity
------------
The following picture depicts the different connection possibilities of the 
485-Extension.

* Coming Soon
