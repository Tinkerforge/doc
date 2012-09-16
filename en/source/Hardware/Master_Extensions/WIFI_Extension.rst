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
External Antenna Connector        RP-SMA Female (with pin inside) and U.FL
Security Protocols                WEP, WPA, WPA2 (Personal and Enterprise), EAP-FAST, EAP-TLS, EAP-TTLS, PEAP
Operating Temperature             -40°C to +85°C
--------------------------------  -----------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Weight                            18g
================================  =============================================================================


Resources
---------

* GS1011MEES Homepage (`here <http://www.gainspan.com/gs1011mees>`__)
* Schematic (`Download <https://github.com/Tinkerforge/wifi-extension/raw/master/hardware/wifi-extension-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/wifi_extension_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/wifi-extension/zipball/master>`__)

.. _wifi_network_assembly:

WIFI Network
------------

With this Master Extension you will be able to create a connection to
a Master Brick and all of its connected Bricks and Bricklets.
No Brick Deamon is necessary if you use this Extension.

If you want to connect the Brick Viewer with your WIFI setup,
you have to enter the IP of the WIFI Extension and the configured port
in the Setup Tab. After pressing "Connect" you will not connect to your local
running Brick Daemon but to your WIFI Extension.

.. note::
 TODO Screenshot

For your own code modify the passed host and port
at your IPConnection call, e.g. change:

.. code-block:: python

 ipcon = IPConnection("localhost", 4223)

to

.. code-block:: python

 ipcon = IPConnection("192.168.0.25", 4223)



TODO: Icon of Tablet/Smart phone controlling wireless stack
TODO: USB power supply test (how big is stack possible?)

.. _wifi_configuration:

WIFI Configuration
------------------

.. note::

 Currently Adhoc Mode is not supported.

First of all you have to enter the SSID of your wireless network
and if the device should use DHCP or a static IP.

In case of you want to use DHCP simply select DHCP and configure the port.

.. image:: /Images/Extensions/extension_wifi_connection_dhcp.jpg
   :scale: 100 %
   :alt: Configure connection as DHCP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_dhcp.jpg

If you want to use a static IP you have to configure that IP and the port.
Additionally configure the subnet mask and gateway address.

.. image:: /Images/Extensions/extension_wifi_connection_static.jpg
   :scale: 100 %
   :alt: Configure connection as static IP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_static.jpg


We suggest that you use an encrypted network. You can choose between
WPA/WPA2, WPA Enterprise (EAP-FAST, EAP-TLS, EAP-TTLS, PEAP) and WEP.

For WPA enter the key in hex notation.

.. image:: /Images/Extensions/extension_wifi_encryption_wpa.jpg
   :scale: 100 %
   :alt: Configure encryption as WPA
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wpa.jpg

For WPA Enterprise configure outer auth (FAST, TLS, TTLS, PEAP), 
inner auth (MSCHAP, GTC), type (ca cert, client cert, private key),
user, pass and certificate.

.. image:: /Images/Extensions/extension_wifi_encryption_wpa_enterprise.jpg
   :scale: 100 %
   :alt: Configure encryption as WPA Enterprise
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wpa_enterprise.jpg

For WEP enter the key and the key index. If the key index is unknown it is likely 1.

.. image:: /Images/Extensions/extension_wifi_encryption_wep.jpg
   :scale: 100 %
   :alt: Configure encryption as WEP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wep.jpg

If you don't want encryption select "No Encryption". 


Finally you have to configure the Power Mode. There are two Power Modes:
Full Speed and Low Power. In Full Speed mode the device consumes more power,
but you will be able to transmit much more messages. This will be the typical
configuration. If you only need to transmit only a few messages (e.g. if you want to 
measure temperatures wirelessly, than you might to use the Low Power Mode
and save energy.

.. image:: /Images/Extensions/extension_wifi_power_mode.jpg
   :scale: 100 %
   :alt: Configure Power Mode
   :align: center
   :target: ../../_images/Extensions/extension_wifi_power_mode.jpg

At the end, press "Save WIFI Configuration" to save the configuration and
restart the Master Brick to load it. After restart you should be able to
reach the Master Brick by entering the IP and port of the Brick in the
Brick Viewer.


.. _extension_wifi_connectivity:

Connectivity
------------

The following picture depicts the different connection possibilities of the 
WIFI Extension.

.. image:: /Images/Extensions/extension_wifi_caption_600.jpg
   :scale: 100 %
   :alt: WIFI Extension with caption
   :align: center
   :target: ../../_images/Extensions/extension_wifi_caption_800.jpg

The blue power LED will be on permanently if the device is powered.
The green LED is the status LED (permanently off=error, blink=associating, on=associated).

The WIFI module is equipped with an U.FL connector and an 75 Ohm RP-SMA pigtail cable.
Dependend on your application it is possible to disconnect the pigtail cable
and connect your own cable. 

