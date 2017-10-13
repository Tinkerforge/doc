
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / CAN Bricklet
:shoplink: ../../../shop/bricklets/can-bricklet.html

.. include:: CAN.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _can_bricklet:

CAN Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_can_tilted_[?|?].jpg           CAN Bricklet
	Bricklets/bricklet_can_horizontal_[?|?].jpg       CAN Bricklet
	Cases/bricklet_can_case_built_up1_[?|?].jpg       CAN Bricklet in Case
	Cases/bricklet_can_case_built_up2_[?|?].jpg       CAN Bricklet in Case
	Bricklets/bricklet_can_brickv_[100|].jpg          CAN Bricklet in Brick Viewer
	Dimensions/can_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Sends and receives data through CAN bus
* Configurable baudrate, modes and filters

.. _can_bricklet_description:

Description
-----------

The CAN :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by the capability to send
and receive CAN data in a `CAN bus <https://en.wikipedia.org/wiki/CAN_bus>`__.

The baudrate can be configured between 10kbit/s and 1Mbit/s. It is possible
to apply filters to match for frames with a specific identifier.


Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               30mW (6mA at 5V, idle)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Baudrate                          10kbit/s - 1Mbit/s
Maximum Throughput                1000 frames per second*
Filters                           Disabled / Accept all / Match / Match data / Match extended
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            45 x 35 x 14mm (1.77 x 1.38 x 0.55")
Weight                            9g
================================  ============================================================

\* 1000 frames per second equals to 44kbit/s to 128kbit/s depending on the size of the frames.

Resources
---------

* MCP2515 (CAN controller) datasheet (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/datasheets/MCP2515.pdf>`__)
* MCP2562 (CAN transceiver) datasheet (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/datasheets/MCP2562.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/hardware/can-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/can_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/can-bricklet/zipball/master>`__)
* 3D model (`View online <http://a360.co/2vslBZp>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/can/can.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/can/can.FCStd>`__)



.. _can_bricklet_test:

Test your CAN Bricklet
----------------------

|test_intro|

|test_connect|.
Connect a CAN device to the CAN-L, CAN-H and GND terminals.

|test_tab|
If everything went as expected you can now see the data that
is send over the connected CAN bus.

.. image:: /Images/Bricklets/bricklet_can_brickv.jpg
   :scale: 100 %
   :alt: CAN Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_can_brickv.jpg

|test_pi_ref|


.. _can_bricklet_case:

Case
----

A `laser-cut case for the CAN Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-can-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_can_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Case for CAN Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_can_case_built_up1_1000.jpg

.. include:: CAN.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/can_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for CAN Bricklet
   :align: center
   :target: ../../_images/Exploded/can_exploded.png

|bricklet_case_hint|


.. _can_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: CAN_hlpi.table
