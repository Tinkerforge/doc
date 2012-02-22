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
 * Enable wireless interconnection of Master Bricks
 * Easy usage
 * Configurable frequency and channel
 * Measureable signal strength

Description
-----------

The Chibi Extension is equipped with a 700/800/900Mhz radio transceiver. Typically
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

.. note:: After configuring a chibi network all modules will behave as 
   connected via USB to your PC. Therefore you need no code changes if you change 
   you system from cable based to chibi. But be aware that you will loose some
   speed since the transmission range is slower than USB speed.


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
	If you use multiple networks in parallel with identical channel and frequency
        assure that every address is unique and not used in different networks in
        transmission range.

To create a Chibi Network, stack the Chibi Extension on top of an Master Brick.
Connect the Master Brick via USB with your PC and start the Brick Viewer 
software. After you have done this you should see the Master Brick view
with the identified Chibi Extension (see picture below). Configure the extension
as slave or master (see followin descriptions).

If you have configured all extensions you can build you system. Connect Bricks
and Bricklets as you like. The master of each stack has to be the lowermost board
(except if you are using a powersupply). The Chibi Extension can be positioned in 
the stack as you wish.

After you have plugged together your system you have to power up it.
Power up the slaves first after some seconds connect the master with the PC.
You should now see all the connected boards in the Brick Viewer.


Chibi Slave Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^
To configure a Chibi Extension as slave you have to do the following steps:

First of all you have to set an unique address for this chibi extension.
Enter a number (1-255) and press "Save".

* Picture

After this you have to enter a "Master Address". This is the address of the chibi 
extension which should act as chibi master. 


Chibi Master Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

To configure a chibi extension as master you have to tell it, its address
and which slaves (identified by their addresses) should participate at the
network.

First you have to set a unique address for the extension.

* Picture

You don't have to set the "Master Address", this address is not used
if there exist a USB connection to a PC (chibi master).

* Picture

At the end you have to tell the chibi master which addresses should be part of
the network. You have 32 slots (0-31). Each slot can contain an address.
Address "0" means this slot is not used. Please arrange the slots such that
you have no unused slots between used ones.

Modify your Chibi Network
^^^^^^^^^^^^^^^^^^^^^^^^^

If you like to change something in your network, e.g. add new Bricks or 
Bricklets, you have to powerdown the node you like to change. Change it 
and repower it. If the node was a chibi slave, you have to reset the
chibi master, too. This can be achieved by a powercycle or pressing the reset 
button on the Master Brick.

Chibi Frequency and Channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You have to configure the transmission frequency and channel depending on your
location. 

.. warning:: A wrong configured frequency and channel can bring you trouble 

To configure the frequency and channel open the Brick Viewer software
and select the appropriate settings

* Picture
