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

 * 900Mhz radio transceiver
 * Enable wireless interconnection of Master Bricks
 * Easy usage

Description
-----------

The Chibi Extension is equipped with a 900Mhz radio transceiver. Typically
this transceiver is used for long range 
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

.. note:: Coming soon! 
   The Chibi Extension is not yet available to buy.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Device Current Consumption        TBD
Range (Outdoor/Indoor)            TBD/TBD
Maximum Baud Rate                 TBD
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
a USB connection, only one is allowed. Each Chibi Extension is identified with
its own address, which have to be unique in the transmission range. 

.. note::
	If you use multiple networks in parallel assure that every address is unique
	and not used in different networks.

To create a Chibi Network, stack the Chibi Extension on top of an Master Brick.
Connect the Master Brick via USB with your PC and start the Brick Viewer 
software. After you have done this you should see the Master Brick View
with the identified Chibi Extension (see picture below). Now you have 
to configure the Extension. 


Chibi Master Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

To configure a chibi extension as master you have to tell, it its address
and which slaves (identified by their addresses) should participate to the
network.


Chibi Slave Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

* Picture

First of all you have to set an unique address for this chibi extension.
Enter a number (1-255) and press "Save".

* Picture

After this you have to enter a "Master Address". This is the address of the chibi 
extension which should act as chibi master. If you are currently configuring the
chibi master, you don't have to configure it (address "0").

* Picture

At the end you have to tell the chibi master which addresses should be part of
the network. You have 32 slots (0-31). Each slot can contain an address


