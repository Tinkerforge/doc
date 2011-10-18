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

..
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
	 
	* AT86RF212 datasheet (Download)
	* Schematic (Download)
	* Outline and drilling plan (`Download <../../_images/Dimensions/chibi_extensions_dimensions.png>`__)
	* Project source code and design files (Download)


.. Chibi Network Assembly
  ----------------------
  * Picture Network
  * explain creation and configuration
  * explain usage



.. Connectivity
   ------------
  The following picture depicts the different connection possibilities of the 
  Chibi-Extension.
  .. image:: /Images/Bricks/Servo_Brick/servo_brick_anschluesse.jpg
   :scale: 100 %
   :alt: alternate text
   :align: center

.. Troubleshoot
   ------------

