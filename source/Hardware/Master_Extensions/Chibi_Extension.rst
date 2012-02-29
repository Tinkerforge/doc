.. _chibi_extension:

Chibi Extension
===============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Extensions/extension_chibi_tilted_350.jpg", 
	             "Extensions/extension_chibi_tilted_600.jpg", 
	             "Chibi Extension") 
	}}
	{{ 
	    tfdocimg("Extensions/extension_chibi_tilted_complete_100.jpg", 
	             "Extensions/extension_chibi_tilted_complete_600.jpg", 
	             "Chibi Extension") 
	}}
	{{ 
	    tfdocimg("Extensions/extension_chibi_top_100.jpg", 
	             "Extensions/extension_chibi_top_600.jpg", 
	             "Chibi Extension") 
	}}
	{{ 
	    tfdocimg("Extensions/extension_chibi_bottom_100.jpg", 
	             "Extensions/extension_chibi_bottom_600.jpg", 
	             "Chibi Extension") 
	}}
	{{ tfdocend() }}


Features
--------

 * 700/800/900Mhz radio transceiver
 * Allows wireless interconnection between stacks
 * Configurable frequency and channel
 * Measureable signal strength

Description
-----------

The Chibi Extension is equipped with a 700/800/900Mhz radio transceiver. 
Typically this transceiver is used for long range 
`Zigbee <http://en.wikipedia.org/wiki/Zigbee>`_ networks. Unfortunately
the Zigbee terms of use do forbid a GPL implementation of the
Zigbee protocol stack (see `here <http://freaklabs.org/index.php/Blog/Zigbee/Zigbee-Linux-and-the-GPL.html>`__ for more information).

Thus we decided to port the open source `Chibi Wireless Stack <http://freaklabs.org/index.php/Blog/Embedded/Introducing...Chibi-A-Simple-Small-Wireless-stack-for-Open-Hardware-Hackers-and-Enthusiasts.html>`__ for this extension. It is a
simple and small protocol stack that is perfectly suited for our use cases.

In good conditions a **range of up to 2km** can be achieved outdoors.

To establish a Chibi network with Bricks, two Chibi Extensions and two
Master Bricks are needed. Both Master Bricks can be connected to a
full stack of Bricks and Bricklets, whereas one Master Brick is Battery
powered and one is connected with USB. From a programming perspective
the Chibi network is completely transparent, i.e. the two stacks can
be used exactly the same way as if they were both connected via USB.

It is also possible to create a network with several Chibi Extension where
only one is connected via USB (many-to-one routing).

.. note:: After configuring a chibi network all modules will behave as 
   connected via USB to your PC. Therefore you need no code changes if you 
   change you system from cable based to Chibi. But be aware that you will 
   loose through put since the Chibi transmission speed is slower than USB 
   transmission speed.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Device Current Consumption        ca. 10mA
Range (Outdoor)            		  up to 2km
Maximum Baud Rate                 up to 250kbit/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            13g
================================  ============================================================



Resources
---------
	 
* AT86RF212 datasheet (`Download <https://github.com/Tinkerforge/chibi-extension/raw/master/datasheets/at86rf212.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/chibi-extension/raw/master/hardware/chibi-extension-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/chibi_extension_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/chibi-extension/zipball/master>`__)


Chibi Network Assembly
----------------------

A chibi network constists of one master and multiple slaves. 
Chibi master is the Master Brick which has a USB connection to the PC
running brickd. All the other Master Bricks with Chibi Extension must not have
a USB connection. Each Chibi Extension is identified with
its own address. The addresses have to be unique in the transmission range. 

.. note::
	If you use multiple networks in parallel with identical channel and 
	frequency make sure that every address is unique and not used in different 
	networks in transmission range.

To create a Chibi network, stack the Chibi Extension on top of an Master Brick.
Connect the Master Brick via USB with your PC and start the Brick Viewer 
software. After you have done this you should see the Master Brick view
with the identified Chibi Extension (see image below). Configure the extension
as slave or master (as described :ref:`here <chibi_slave>` and 
:ref:`here <chibi_master>`).

If you have configured all extensions you can build your system. Connect 
Bricks and Bricklets as you like. The master of each stack has to be the 
lowermost board (except if you are using a powersupply). The Chibi Extension 
can be positioned in the stack as you wish.

After you have plugged together your system you have to power ip up.
You have to power up the slaves before the master, since the Chibi master 
searches for slaves only at startup.
You should now be able to see all connected boards in the Brick Viewer.

.. _chibi_slave:

Chibi Slave Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^
To configure a Chibi Extension as slave you have to set an unique address for
the extension

.. image:: /Images/Extensions/extension_chibi_address.jpg
   :scale: 100 %
   :alt: Configuration of Chibi address 
   :align: center
   :target: ../../_images/Extensions/extension_chibi_address.jpg

and you have to define a Master Address. This is the address of the
Chibi master this Chibi slave will talk too.

.. image:: /Images/Extensions/extension_chibi_master_address.jpg
   :scale: 100 %
   :alt: Configuration of Chibi master address 
   :align: center
   :target: ../../_images/Extensions/extension_chibi_master_address.jpg

.. _chibi_master:

Chibi Master Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^
To configure a Chibi Extension as master you have to set an unique address for
the extension

.. image:: /Images/Extensions/extension_chibi_address.jpg
   :scale: 100 %
   :alt: Configuration of Chibi address 
   :align: center
   :target: ../../_images/Extensions/extension_chibi_address.jpg

and you have to give the Chibi master a list of Chibi slaves that it can
talk to:

.. image:: /Images/Extensions/extension_chibi_slave_address.jpg
   :scale: 100 %
   :alt: Configuration of Chibi slave addresses
   :align: center
   :target: ../../_images/Extensions/extension_chibi_slave_address.jpg

There are 32 slots (0-31) available, address 0 means that this slot is not 
used. There should not be any unused slots between used ones.

Modify your Chibi Network
^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to change something in your network, e.g. add new Bricks or 
Bricklets, you have to power down the stack you like to change. Change it 
and repower it. If the node was a Chibi slave, you also have to reset the
Chibi master (it only searches for new Bricks/Bricklets on startup). 
This can be achieved by a powercycle or pressing the reset 
button on the Master Brick.

Chibi Frequency and Channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Chibi Extension supports several frequencies with different channels
and different frequencies are allowed in different countries.

.. image:: /Images/Extensions/extension_chibi_frequency.jpg
   :scale: 100 %
   :alt: Configuration of Chibi frequency and channel
   :align: center
   :target: ../../_images/Extensions/extension_chibi_frequency.jpg

Here is a small list of frequencies with corresponding possible channels:

.. csv-table::
 :header: "Frequency", "Possible Channels"
 :widths: 40, 60
 
 "OQPSK 868Mhz (Europe)", "0"
 "OQPSK 915Mhz (US)", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
 "OQPSK 780Mhz (China)", "0, 1, 2, 3"
 "BPSK40 915Mhz", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"

.. warning::
	The Chibi Extension is sold as an electronic component. You are building
	a system with this component and it is your responsibility that the
	system you are building abides by your local law. Make sure that you
	are allowed to use the frequency you are configuring!
