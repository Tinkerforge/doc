
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#kits">Kits</a> / Starter Kit: Internet of Things
:shoplink: ../../../shop/kits/starter-kit-internet-of-things.html


.. _starter_kit_iot:

Starter Kit: Internet of Things
===============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
		tfdocstart("Kits/iot_on_table_350.jpg",
				   "Kits/iot_on_table_800.jpg",
				   "Starter Kit: Internet of Things")
	}}
	{{
		tfdocimg("Kits/iot_front_350.jpg",
				 "Kits/iot_front_800.jpg",
				 "Starter Kit: Internet of Things")
	}}
	{{
		tfdocimg("Kits/iot_back_ethernet_100.jpg",
				 "Kits/iot_back_ethernet_800.jpg",
				 "Internet of Things: Back side with Ethernet")
	}}
	{{
		tfdocimg("Kits/iot_rpi_100.jpg",
				 "Kits/iot_rpi_800.jpg",
				 "Internet of Things: Connected to Raspberry PI")
	}}
	{{
		tfdocimg("Kits/iot_half_open_100.jpg",
				 "Kits/iot_half_open_800.jpg",
				 "Internet of Things: Open")
	}}
	{{
		tfdocimg("Kits/iot_half_open_ethernet_100.jpg",
				 "Kits/iot_half_open_ethernet_800.jpg",
				 "Internet of Things: Open with Ethernet")
	}}
	{{
		tfdocimg("Kits/iot_content_100.jpg",
				 "Kits/iot_content_800.jpg",
				 "Internet of Things: Content")
	}}
	{{
		tfdocimg("Kits/iot_packaging_open_100.jpg",
				 "Kits/iot_packaging_open_800.jpg",
				 "Internet of Things: Packaging")
	}}
	{{ tfdocend() }}

Features
--------

* Allows to control devices over the Internet 
* Supports 433MHz actuators
* External antenna, big range
* Controllable by `www.iot-remote.com <http://www.iot-remote.com/>`__


Description
-----------

The `Internet of Things <http://en.wikipedia.org/wiki/Internet_of_Things>`__
is an evolution of the Internet. It interconnects not only human and computer
as before but also physical objects (things).

The *Starter Kit: Internet of Things* offers an easy access into the
world of the Internet of Things. It allows to control many devices
over the internet. For that the kit is equipped with a 
:ref:`Remote Switch Bricklet <remote_switch_bricklet>`. It can be
used to remotely control 433MHz mains switches, dimmers and home automation
:ref:`list of supported actuators <remote_switch_supported_devices>` in the
documentation of the Bricklet.

With the :ref:`API Bindings <api_bindings>` it is possible to control the
wireless actuators with any (Embedded-)PC, smart phone or tablet over the
Internet.

With the kit nothing stands in the way of turning your coffee maker on
while you are headed home or to dim your living room illumination
with your own cloud or with a Raspberry Pi. The website 
`www.iot-remote.com <http://www.iot-remote.com/>`__ gives you direct
access to wireless actuators from any web-enabled device.

The kit basically consists of a :ref:`Master Brick <master_brick>` and a
:ref:`Remote Switch Bricklet <remote_switch_bricklet>` which is
equipped with a 433MHz transceiver. Over the USB connection of the
Master Brick you can control remote control mains switches or similar.
An (Embedded-)PC (e.g. Raspberry Pi) either do the switching itself
or it can serve as a gateway. With an additional 
:ref:`Ethernet Master Extension <ethernet_extension>` it is possible
to go without a gateway.

With additional modules from the Tinkerforge building blocks you can
extend the kit. It is for example possible to measure temperature
(:ref:`Temperature <temperature_bricklet>`,
:ref:`Temperature IR <temperature_ir_bricklet>` or
:ref:`PTC Bricklet <ptc_bricklet>`) or to react on movements
(:ref:`Motion Detector Bricklet <motion_detector_bricklet>`).

Technical Specifications
------------------------

========================================  ============================================================
Property                                  Value
========================================  ============================================================
Radio Module                              RFM69HW
Current Consumption                       10mA (idle), 40mA (sending)
Radio Frequency                           433MHz
----------------------------------------  ------------------------------------------------------------
----------------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)                    11cm x 6.5cm x 4.5cm (assembled kit)
Weight                                    130g (assembled kit)
========================================  ============================================================

.. _starter_kit_iot_resources:

Resources
---------

* Internet of Things kit case FreeCAD CAD files (`Download <https://github.com/Tinkerforge/internet-of-things/tree/master/case>`__)
* iot-remote.com web site (`Download <https://github.com/Tinkerforge/internet-of-things/tree/master/web>`__)
* iot-remote.com server Implementation (`Download <https://github.com/Tinkerforge/internet-of-things/tree/master/server>`__)

Firmware updating and first tests
---------------------------------

As a very first step you should try out and update your Bricks and Bricklets.

For that you need to install the :ref:`Brick Daemon <brickd_installation>` and
the :ref:`Brick Viewer <brickv_installation>`. Connect the Remote Switch Bricklet 
to the Master Brick and connect it via USB to your PC. Afterwards use Brick 
Viewer to check if all of the firmwares are up to date (Updates / Flashing 
button). If not, you can :ref:`update the Bricks <brickv_flash_firmware>` and
:ref:`update the Bricklets <brickv_flash_plugin>` with the Brick
Viewer too:

.. image:: /Images/Kits/iot_update.jpg
   :scale: 100 %
   :alt: Internet of Things update in Brick Viewer
   :align: center

As the next step test the Remote Switch Bricklet with a remotely controlled
mains switch. After that you can start to assemble the kit!


Construction
------------

The Starter Kit: Internet of Things comes with :ref:`Master Brick <master_brick>`,
:ref:`Remote Switch Bricklet <remote_switch_bricklet>`, a 6cm Bricklet cable,
two mounting kits and self-adhesive non-slip rubber feet.

Building the case can be done in four easy steps.

.. image:: /Images/Kits/iot_construction_exploded_w_lines_500.jpg
   :scale: 100 %
   :alt: Exploded assembly drawing
   :align: center
   :target: ../../_images/Kits/iot_construction_exploded_w_lines.png


Step 0: Remove protective foils
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At first the protective foils on all case parts have to be removed.
There is a foil on the front and back side. In some cases the protective
foils may be hard to remove, you can use a cutter or similar as a
lever to get to the foil.

Step 1: Use mounting kit
^^^^^^^^^^^^^^^^^^^^^^^^

Screw the 10mm spacers (thread inside/inside) to the Master Brick
and the Remote Switch Bricklet.

.. image:: /Images/Kits/iot_construction_step1_350.jpg
   :scale: 100 %
   :alt: Construction Step 1
   :align: center
   :target: ../../_images/Kits/iot_construction_step1.png

If you want to use the Ethernet Extension, you should attach it to the
Master Brick with 9mm spacers (thread inside/outside).

.. image:: /Images/Kits/iot_construction_ethernet_step1_350.jpg
   :scale: 100 %
   :alt: Construction Step 1 (Ethernet Extension)
   :align: center
   :target: ../../_images/Kits/iot_construction_ethernet_step1.png

Step 2: Screw to bottom
^^^^^^^^^^^^^^^^^^^^^^^

Now screw the Master Brick (with or without Ethernet Extension) and the 
Remote Switch Bricklet to the bottom part of the case. You should use 
the following sequence:

* Plug front part of case into bottom part
* Screw Master Brick and Remote Switch Bricklet to bottom part
* Add self-adhesive non-slip rubber feet to bottom part
* Add Bricklet cable between Master Brick and Remote Switch Bricklet
* Screw antenna to Remote Switch Bricklet

.. image:: /Images/Kits/iot_construction_step2_350.jpg
   :scale: 100 %
   :alt: Construction Step 2
   :align: center
   :target: ../../_images/Kits/iot_construction_step2.png

Step 3: Attach dome
^^^^^^^^^^^^^^^^^^^

In the last step you just have to plug the back part of the case into
the bottom part. After that bend and attach the top part. Thats it, we
are done already!

.. image:: /Images/Kits/iot_construction_step3_350.jpg
   :scale: 100 %
   :alt: Construction Step 3
   :align: center
   :target: ../../_images/Kits/iot_construction_step3.png


Applications
------------

With your own tablet, smart phone or PC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


