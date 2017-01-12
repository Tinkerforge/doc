
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Industrial Quad Relay Bricklet
:shoplink: ../../../shop/bricklets/industrial-quad-relay-bricklet.html

.. include:: Industrial_Quad_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_quad_relay_bricklet:

Industrial Quad Relay Bricklet
==============================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_quad_relay_tilted_[?|?].jpg           Industrial Quad Relay Bricklet
	Bricklets/bricklet_industrial_quad_relay_vertical_[?|?].jpg         Industrial Quad Relay Bricklet
	Bricklets/bricklet_industrial_quad_relay_horizontal_[?|?].jpg       Industrial Quad Relay Bricklet
	Bricklets/bricklet_industrial_quad_relay_setup_[?|?].jpg            Industrial Quad Relay Bricklet setup
	Cases/bricklet_industrial_case_[100|600].jpg                        Industrial Quad Relay Bricklet in Case
	Bricklets/bricklet_industrial_quad_relay_brickv_[100|].jpg          Industrial Quad Relay Bricklet in Brick Viewer
	Dimensions/industrial_quad_relay_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* 4 Channel Solid State Relay
* Switch up to 30V with 1.2A
* Galvanically isolated
* Groupable


.. _industrial_quad_relay_bricklet_description:

Description
-----------

The Industrial Quad Relay :ref:`Bricklet <primer_bricklets>` can be used to
extend :ref:`Bricks <primer_bricks>` by four galvanically isolated solid state relays.
Each channel can switch currents of up to 1.2 `Ampere <https://en.wikipedia.org/wiki/Ampere>`__
with 30 `Volt <https://en.wikipedia.org/wiki/Volt>`__.
Output isolation permits the usage without a direct electric connection, 
such that ground loops can be prevented and an additional degree of safety is added.

Typical applications are the interfacing of industrial control, such as PLC's or frequency converters,
or the usage in environments were electrical ground levels can not be connected.

If you need more then four relays, you can add another Industrial Quad Relay
Bricklet and group these together. If you do this, you have eight relays which can
set simultaneously in contrast to set both Bricklets successively.
Grouping is only possible for Bricklets connected to one Brick.
Thus you can group up to four Industrial Bricklets on a Master Brick or
two on other Bricks.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Solid State Relay                 CPC1020N
Current Consumption               2mA (per Relay)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Output Type                       Four galvanically isolated solid state relays
Maximum Switching Current         1.2A
Maximum Switching Voltage         30V
Isolation                         1500Vrms (datasheet value)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1.57 x 1.57 x 0.43")
Weight                            8g
================================  ============================================================


Resources
---------

* CPC1020N datasheet (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/raw/master/datasheets/CPC1020N.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/raw/master/hardware/industrial-quad-relay-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_quad_relay_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/zipball/master>`__)


Connectivity
------------

The Industrial Quad Relay Bricklet has an 8 pole terminal.
Please see the picture below for the pinout.


.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_caption_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay 4 Bricklet pinout
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_caption_1200.jpg


.. _industrial_quad_relay_bricklet_test:

Test your Industrial Quad Relay Bricklet
-------------------------------------------

|test_intro|

|test_connect|.
For a simple test we will connect a battery and a LED to test the Bricklet
(see picture below).


.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_setup_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet setup
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_setup_1200.jpg

|test_tab|

If everything went as expected you can switch the LED by changing the output
state with the Brick Viewer.

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_brickv.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_brickv.jpg

|test_pi_ref|

.. _industrial_quad_relay_bricklet_case:

Case
----

A `laser-cut case for the Industrial Quad Relay Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-industrial-bricklet.html>`__
is available.

.. image:: /Images/Cases/bricklet_industrial_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_case_1000.jpg

.. include:: Industrial_Quad_Relay.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/industrial_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Quad Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/industrial_exploded.png

|bricklet_case_hint|


.. _industrial_quad_relay_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Quad_Relay_hlpi.table
