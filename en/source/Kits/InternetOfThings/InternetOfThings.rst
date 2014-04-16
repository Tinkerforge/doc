
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

* TODO
* TODO
* TODO
* TODO


Description
-----------

The *Starter Kit: Internet of Things* is ...


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

* TODO
* TODO
* TODO
* TODO

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

