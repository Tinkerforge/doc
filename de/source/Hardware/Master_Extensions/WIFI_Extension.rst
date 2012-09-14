.. _wifi_extension:

WIFI Extension
==============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Extensions/extension_wifi_tilted_350.jpg",
	               "Extensions/extension_wifi_tilted_600.jpg",
	               "WIFI Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_stack_100.jpg",
	             "Extensions/extension_wifi_stack_600.jpg",
	             "WIFI Extension with Master Brick in a stack")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_horizontal_100.jpg",
	             "Extensions/extension_wifi_horizontal_600.jpg",
	             "WIFI Extension from top")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_bottom_100.jpg",
	             "Extensions/extension_wifi_bottom_600.jpg",
	             "WIFI Extension from bottom")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_caption_100.jpg",
	             "Extensions/extension_wifi_caption_600.jpg",
	             "WIFI Extension with caption")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_ufl_100.jpg",
	             "Extensions/extension_wifi_ufl_600.jpg",
	             "U.FL connector of WIFI Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_front_100.jpg",
	             "Extensions/extension_wifi_front_600.jpg",
	             "WIFI Extension from front")
	}}
	{{ tfdocend() }}


Features
--------

* Control Bricks/Bricklets wirelessly over your mobile phone or tablet
* Operates with 802.11b/g/n access points, WEP, WPA, WPA2 Personal and Enterprise
* Equipped with 18dBm power amplifier for extended range
* External RP-SMA and U.FL antenna connector


Description
-----------

With this WIFI Extension you can control :ref:`Bricks <product_overview_bricks>` and
:ref:`Bricklets <product_overview_bricklets>` wirelessly over your
mobile phone, tablet or your PC. For the Master Extension concept please take a look at the general
:ref:`description <product_overview_master_extensions>`. The Extension is equipped with a `GainSpan <http://www.gainspan.com>`__
`GS1011MEES <http://www.gainspan.com/gs1011mees>`__ WIFI module with an internal power amplifier
which allows for superior range compared to other WIFI modules.

The devices supports two modes. In Full Speed Mode the device WIFI transceiver is always on.
New incoming data will be immediately handled. In Low Power Mode the devices is not always on,
the transceiver enters sleep mode after each message. This leads to a significantly lower power
consumption and data throughput.

Since the device itself handles TCP/IP packages it is possible to connect directly from your controling
device (mobile phone, tablet, (embedded) PC). A :ref:`brick daemon <brickd>` is not necessary.

To use this WIFI Extension a :ref:`Master Brick <master_brick>` is mandatory.
If you want to use other Bricks, you can build a stack and plug them also on top
of the Master Brick. If you want to use Bricklets you can attach them to the Master Brick or
to other Bricks in the stack. From the programming perspective
this is completely transparent, i.e. all Bricks and Bricklets can
be used exactly the same way as if they were connected to your controlling device via USB.


Technical Specifications
------------------------

================================  =============================================================================
Property                          Value
================================  =============================================================================
Current Consumption               110mA (transmit), 23mA (during sleep)
--------------------------------  -----------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------
Maximum Range (Outdoor)           TBD
Maximum Transfer Rate             TBD
--------------------------------  -----------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------
RF Output Power (Typical)         18dBm
External Antenna Connector        RP-SMA Female (with pin inside)
Security Protocols                WEP, WPA, WPA2 (Personal and Enterprise), EAP-FAST, EAP-TLS, EAP-TTLS, PEAP
Operating Temperature             -40°C to +85°C
--------------------------------  -----------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            18g
================================  =============================================================================


Resources
---------

* GS1011MEES datasheet (`Download <https://github.com/Tinkerforge/wifi-extension/raw/master/datasheets/GS1011M_Datasheet.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/wifi-extension/raw/master/hardware/wifi-extension-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/wifi_extension_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/wifi-extension/zipball/master>`__)

.. _wifi_network_assembly:

WIFI Network Assembly
---------------------

TODO

.. _wifi_configuration:

WIFI Configuration
------------------

Connection TODO

.. image:: /Images/Extensions/extension_wifi_connection_dhcp.jpg
   :scale: 100 %
   :alt: Configure connection as DHCP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_dhcp.jpg

TODO

.. image:: /Images/Extensions/extension_wifi_connection_static.jpg
   :scale: 100 %
   :alt: Configure connection as static IP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_static.jpg

Encryption TODO

.. image:: /Images/Extensions/extension_wifi_encryption_wpa.jpg
   :scale: 100 %
   :alt: Configure encryption as WPA
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wpa.jpg

TODO

.. image:: /Images/Extensions/extension_wifi_encryption_wpa_enterprise.jpg
   :scale: 100 %
   :alt: Configure encryption as WPA Enterprise
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wpa_enterprise.jpg

TODO

.. image:: /Images/Extensions/extension_wifi_encryption_wep.jpg
   :scale: 100 %
   :alt: Configure encryption as WEP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wep.jpg

Power Mode TODO

.. image:: /Images/Extensions/extension_wifi_power_mode.jpg
   :scale: 100 %
   :alt: Configure encryption as WEP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_power_mode.jpg


.. _extension_wifi_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the 
WIFI Extension.

.. image:: /Images/Extensions/extension_wifi_caption_600.jpg
   :scale: 100 %
   :alt: WIFI Extension with caption
   :align: center
   :target: ../../_images/Bricks/extension_wifi_caption_800.jpg
