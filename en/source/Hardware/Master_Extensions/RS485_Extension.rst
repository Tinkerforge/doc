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
	             "RS485 Extension top")
	}}
	{{
	    tfdocimg("Extensions/extension_rs485_bottom_100.jpg",
	             "Extensions/extension_rs485_bottom_600.jpg",
	             "RS485 Extension bottom")
	}}
	{{ tfdocend() }}


Features
--------

* Long distance connections (up to 1200m)
* Allows cable based interconnection between stacks
* Configurable baud rate, parity and stop bits
* Can be used in existing RS485 networks (:ref:`Modbus RTU <llproto_modbus>`)


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

:ref:`Modbus RTU <llproto_modbus>` is used as the
protocol on the RS485 interface. This allows to use a stack of Bricks
and Bricklets with an RS485 Extension to be integrated in existing
Modbus networks. It is also possible to communicate with a stack
directly via Modbus from an embedded device or over a Modbus gateway.

The following combinations with other Extensions in a stack are possible:

* RS485 Master top / WIFI bottom
* RS485 Master top / Chibi Slave bottom
* RS485 Master bottom / WIFI top
* RS485 Master bottom / Chibi Slave top
* RS485 Slave top / Chibi Master bottom
* RS485 Slave bottom / Chibi Master top


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               8mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximum Distance                  1200m
Maximum Baud Rate                 2Mbit/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                            13g
================================  ============================================================


Resources
---------

* ADM3485 datasheet (`Download <https://github.com/Tinkerforge/rs485-extension/raw/master/datasheets/ADM3485.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/rs485-extension/raw/master/hardware/rs485-extension-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/rs485_extension_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/rs485-extension>`__)


.. _rs485_connectivity:

Connectivity
------------

The following picture shows the connection possibilities of the RS485-Extension.

.. image:: /Images/Extensions/extension_rs485_caption_600.jpg
   :scale: 100 %
   :alt: RS485 Extension connectivity
   :align: center
   :target: ../../_images/Extensions/extension_rs485_caption_800.jpg


RS485 Bus Assembly
------------------

A RS485 bus consists of one master and multiple slaves.
RS485 master is the Master Brick which has a USB connection to the PC
running brickd. All the other Master Bricks with RS485 Extension must not have
a USB connection (they can use a USB Power Supply).
Each RS485 slave is identified with its own ID. The IDs have
to be unique on the bus.

To create a RS485 bus, stack the RS485 Extension on top of a Master Brick.
Connect the Master Brick via USB with your PC and start the Brick Viewer
software. You should see the Master Brick view
with the identified RS485 Extension (see images below). Configure the extension
as slave or master (as described :ref:`here <rs485_configuration>`).

If you have configured all extensions you can build your system. Connect
Bricks and Bricklets as you like. The Master Brick of each stack has to be the
lowermost Brick (except if you are using a Power Supply). The RS485 Extension
can be positioned in the stack as you wish. Wire up the RS485 stacks and set
the termination switch on the first and last RS485 Extension in the bus to
"on", as shown below.

.. image:: /Images/Extensions/extension_rs485_assembly.jpg
   :scale: 90 %
   :alt: Assembly of RS485 Extension
   :align: center
   :target: ../../_images/Extensions/extension_rs485_assembly.jpg

You have to power up the slaves before the master, since the RS485 master
searches for slaves only at startup. You should now be able to see all
connected stacks in the Brick Viewer.


.. _rs485_configuration:

RS485 Configuration
^^^^^^^^^^^^^^^^^^^

To configure a RS485 Extension you first have to choose the baud rate,
parity and stop bits.

.. image:: /Images/Extensions/extension_rs485_config.jpg
   :scale: 100 %
   :alt: Configuration of RS485 Extension
   :align: center
   :target: ../../_images/Extensions/extension_rs485_config.jpg

If your bus isn't absolutely huge you should probably
choose "speed: 2000000 (2Mbit/s), parity: None, Stop bits: 1". If you start to
get timeouts and the CRC error counter is rising rapidly, you might want
to lower the baud rate. If you want to use a stack with RS485 Extension in
your existing Modbus network, you have to match the values with the
other bus participants.

For slave configuration choose "Slave" as type and set an address for
the slave (1-255).

.. image:: /Images/Extensions/extension_rs485_slave.jpg
   :scale: 100 %
   :alt: Configuration of RS485 in slave mode
   :align: center
   :target: ../../_images/Extensions/extension_rs485_slave.jpg

For master configuration choose "Master" as type and input the addresses
of the slaves in the RS485 bus as a comma separated list.

.. image:: /Images/Extensions/extension_rs485_master.jpg
   :scale: 100 %
   :alt: Configuration of RS485 in master mode
   :align: center
   :target: ../../_images/Extensions/extension_rs485_master.jpg


RS485 Bus Modification
^^^^^^^^^^^^^^^^^^^^^^

If you want to change something in your bus, e.g. add new Bricks or
Bricklets, you have to power down the stack you would like to change.
Change it and repower it. If the stack was slave in the RS485 bus, you
also have to reset the RS485 master (it only searches for new
Bricks and Bricklets on startup).
This can be achieved by a power cycle or pressing the reset
button on the Master Brick.

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`Master Brick documentation <master_brick_programming_interfaces>`.
