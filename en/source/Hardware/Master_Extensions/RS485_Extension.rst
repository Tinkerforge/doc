
:shoplink: ../../../shop/master-extensions/rs485-master-extension.html

.. _rs485_extension:

RS485 Master Extension
======================

.. raw:: html

	{% tfgallery %}

	Extensions/extension_rs485_v11_tilted_[?|?].jpg  RS485 Extension
	Extensions/extension_rs485_v11_top_[?|?].jpg     RS485 Extension top
	Extensions/extension_rs485_v11_bottom_[?|?].jpg  RS485 Extension bottom

	{% tfgalleryend %}


Features
--------

* Allows cable based interconnection between stacks of Bricks
* Long distance connections (up to 1200m)
* Configurable baud rate, parity and stop bits
* Can be used in existing RS485 networks (:ref:`Modbus RTU <llproto_modbus>`)


Description
-----------

The RS485 Extension can be used for long range cable based
inter-:ref:`stack <primer_stack>` communication. It uses the RS485 differential 
interface standard to achieve ranges of **up to 1200m**.

To establish a RS485 bus with :ref:`Bricks <primer_bricks>`, two RS485 
Extensions and two :ref:`Master Bricks <master_brick>` are needed. Both Master 
Bricks can be connected to a full stack of Bricks and 
:ref:`Bricklets <primer_bricklets>`, whereas one Master Brick is 
battery powered and one is connected with USB, Ethernet or WIFI to a PC. From a
programming perspective
the RS485 bus is completely transparent, i.e. the two stacks can
be used exactly the same way as if they were both connected via USB.

It is also possible to create a bus with several RS485 Extension where
only one is connected via USB, Ethernet or WIFI to a PC (many-to-one routing).

:ref:`Modbus RTU <llproto_modbus>` is used as the
protocol on the RS485 interface. This allows to use a stack of Bricks
and Bricklets with an RS485 Extension to be integrated in existing
Modbus networks. It is also possible to communicate with a stack
directly via Modbus from an embedded device or over a Modbus gateway.

The following combinations with other Extensions in a stack are possible
(regardless of order):

* RS485 Master / Chibi Slave
* RS485 Master / Ethernet
* RS485 Master / WIFI
* RS485 Master / WIFI 2.0
* RS485 Slave / Chibi Master


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
* 3D model (`View online <http://autode.sk/2iTPXMM>`__ | Download: `STEP <http://download.tinkerforge.com/3d/extensions/rs485/rs485-extension.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/extensions/rs485/rs485_extension.FCStd>`__)


Connectivity
------------

The following picture shows the connection possibilities of the RS485-Extension.

.. image:: /Images/Extensions/extension_rs485_v11_caption_600.jpg
   :scale: 100 %
   :alt: RS485 Extension connectivity
   :align: center
   :target: ../../_images/Extensions/extension_rs485_v11_caption_800.jpg


RS485 Bus Assembly
------------------

A RS485 bus consists of one master and multiple slaves.
RS485 master is the Master Brick which has a USB, Ethernet or WIFI connection
to the PC running brickd. All the other Master Bricks with RS485 Extension
must not have a USB, Ethernet or WIFI connection (they can use a USB Power Supply).
Each RS485 slave is identified with its own ID. The IDs have
to be unique on the bus.

To create a RS485 bus, stack the RS485 Extension on top of a Master Brick.
Connect the Master Brick via USB, Ethernet or WIFI with your PC and start the
Brick Viewer software. You should see the Master Brick view
with the identified RS485 Extension (see images below). Configure the extension
as slave or master (as described :ref:`here <rs485_extension_configuration>`).

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

If the bus is only a few meters long then the cable you use should not matter.
If the bus is longer than a few meters then some kind of `twisted pair
<https://en.wikipedia.org/wiki/Twisted_pair>`__ cable is recommended. Common
telephone cable is often twisted. Even better is Ethernet cable, because it is
twisted and often shielded. If you use a twisted pair cable, make sure to use
the same twisted pair for A and B, but use another twisted pair for GND.

You have to power up the slaves before the master, since the RS485 master
searches for slaves only at startup. You should now be able to see all
connected stacks in the Brick Viewer.


.. _rs485_extension_configuration:

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

At the end, press "Save RS485 Configuration" to save the configuration permanently
on the RS485 Extension.
The Master Brick has to be restarted to apply the new configuration.


RS485 Bus Modification
^^^^^^^^^^^^^^^^^^^^^^

If you want to change something in your bus, e.g. add new Bricks or
Bricklets, you have to power down the stack you would like to change,
change it and repower it. 

The following is true with Master Brick firmware version 2.4.6 and above:

* If you restart the RS485 Master, every Brick/Bricklet of the RS485
  network will send the initial enumeration message again.

* If you restart the RS485 Slave, only the Bricks/Bricklets that
  are connected to this stack will send the  initial enumeration 
  message again.


Programming Interface
---------------------

See :ref:`Master Brick documentation <master_brick_programming_interface>`.
