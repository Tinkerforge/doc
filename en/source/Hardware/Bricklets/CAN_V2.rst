
:shoplink: ../../../shop/bricklets/can-v2-bricklet.html

.. include:: CAN_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _can_v2_bricklet:

CAN Bricklet 2.0
================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_can_v2_tilted_[?|?].jpg           CAN Bricklet 2.0
	Bricklets/bricklet_can_v2_tilted2_[?|?].jpg          CAN Bricklet 2.0
	Bricklets/bricklet_can_v2_top_[?|?].jpg              CAN Bricklet 2.0
	Bricklets/bricklet_can_v2_brickv_[100|].jpg          CAN Bricklet 2.0 in Brick Viewer
	Dimensions/can_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Sends and receives data through CAN bus
* Configurable baudrate, modes and filters


.. _can_v2_bricklet_description:

Description
-----------

The CAN :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the capability to send
and receive CAN data in a `CAN bus <https://en.wikipedia.org/wiki/CAN_bus>`__.

The baudrate can be configured between 10kbit/s and 1Mbit/s. It is possible
to apply filters to match for frames with a specific identifier.

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
Current Consumption               72mW (14.4mA at 5V, idle)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Baudrate                          10kbit/s - 1Mbit/s
Maximum Throughput                1000 frames per second*
Filters                           Disabled / Accept all / Match / Match data / Match extended
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            45 x 35 x 14mm (1.77 x 1.38 x 0.55")
Weight                            8.6g
================================  ============================================================

\* 1000 frames per second equals to 44kbit/s to 128kbit/s depending on the size of the frames.

Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/can-v2-bricklet/raw/master/hardware/can-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/can_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/can-v2-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2KeTiSi>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/can_v2/can-v2.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/can_v2/can-v2.FCStd>`__)


.. _can_v2_bricklet_test:

Test your CAN Bricklet 2.0
--------------------------

|test_intro|

|test_connect|.
Connect a CAN device to the CAN-L, CAN-H and GND terminals.

|test_tab|
If everything went as expected you can now see the data that
is send over the connected CAN bus.

.. image:: /Images/Bricklets/bricklet_can_v2_brickv.jpg
   :scale: 100 %
   :alt: CAN Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_can_v2_brickv.jpg

|test_pi_ref|


.. _can_v2_bricklet_case:

Case
----

A `laser-cut case for the CAN Bricklet 2.0
<https://www.tinkerforge.com/en/shop/cases/case-can-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_can_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Case for CAN Bricklet 2.0
   :align: center
   :target: ../../_images/Cases/bricklet_can_case_built_up1_1000.jpg

.. include:: CAN_V2.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/can_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for CAN Bricklet 2.0
   :align: center
   :target: ../../_images/Exploded/can_exploded.png

|bricklet_case_hint|


.. _can_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: CAN_V2_hlpi.table
