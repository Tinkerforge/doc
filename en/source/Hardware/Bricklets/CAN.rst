
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
Filters                           Disabled / Accept all / Match / Match data / Match extended
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            45 x 35 x 14mm (1.77 x 1.38 x 0.55")
Weight                            9g
================================  ============================================================


Resources
---------

* MCP2515 (CAN controller) datasheet (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/datasheets/MCP2515.pdf>`__)
* MCP2562 (CAN transceiver) datasheet (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/datasheets/MCP2562.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/hardware/can-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/can_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/can-bricklet/zipball/master>`__)


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

Coming soon...


.. _can_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: CAN_hlpi.table
