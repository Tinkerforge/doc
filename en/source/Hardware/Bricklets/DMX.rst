
:shoplink: ../../../shop/bricklets/dmx-bricklet.html

.. include:: DMX.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dmx_bricklet:

DMX Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dmx_tilted1_[?|?].jpg          DMX Bricklet
	Bricklets/bricklet_dmx_tilted2_[?|?].jpg          DMX Bricklet
	Bricklets/bricklet_dmx_front_[?|?].jpg            DMX Bricklet
	Bricklets/bricklet_dmx_back_[?|?].jpg             DMX Bricklet
	Bricklets/bricklet_dmx_top_[?|?].jpg              DMX Bricklet
	Bricklets/bricklet_dmx_brickv_[100|].jpg          DMX Bricklet in Brick Viewer
	Dimensions/dmx_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Supports DMX slave and master
* Has male and female XLR connector
* All 512 DMX channels available
* Can be used to monitor existing DMX network without interference 
* Switchable 120 Ohm termination


.. _dmx_bricklet_description:

Description
-----------

The DMX :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the capability of a
DMX slave or master.

In master mode the Bricklet can control up to 512 channels with the maximum
possible DMX speed. Frames can be send with a fixed frame rate to achieve smooth
animations. Frames are double buffered to increase performance.

In slave mode the Bricklet can receive all 512 channels. It can react to any of
the channels or also be used for monitoring in an existing DMX network without
any interference.

The Bricklet comes with a male and female connector as well as a user switchable
120 ohm termination.

This Bricklet ist not galvanically isolated to the Tinkerforge system. 
This means that there is a direct electrical connection between the terminals 
of the Bricklet and the rest of the system. Dependent of the application 
this can lead to undesired connections, ground loops or short circuits. 
These problems can be prevented by using the Bricklet together with a :ref:`Isolator Bricklet <isolator_bricklet>`.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               180mW (36mA at 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Modes                             Master / Slave
Channels                          512
Frame Rate                        Up to 44Hz at 512 channels (higher with less channels)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            60 x 50 x 30mm (2.36 x 1.97 x 1.18")
Weight                            30g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/dmx-bricklet/raw/master/hardware/dmx-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dmx_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/dmx-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2C4Vatz>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/dmx/dmx.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/dmx/dmx.FCStd>`__)


.. _dmx_bricklet_test:

Test your DMX Bricklet
----------------------

|test_intro|

|test_connect|.

|test_tab|
You can now change between master/slave mode and send/receive DMX data.

.. image:: /Images/Bricklets/bricklet_dmx_brickv.jpg
   :scale: 100 %
   :alt: DMX Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dmx_brickv.jpg

|test_pi_ref|


.. _dmx_bricklet_case:

Case
----

A `laser-cut case for the DMX Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-dmx-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_dmx_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Case for DMX Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_dmx_case_built_up1_800.jpg

The assembly is easiest if you follow the following steps:

* Build up side plates,
* plug side plates into bottom plate,
* screw 12mm screw with nut to the bottom plate
* screw spacers to the Bricklet and
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the DMX Bricklet case:

.. image:: /Images/Exploded/dmx_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for DMX Bricklet
   :align: center
   :target: ../../_images/Exploded/dmx_exploded.png

|bricklet_case_hint|


.. _dmx_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: DMX_hlpi.table
