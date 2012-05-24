.. _dual_relay_bricklet:

Dual Relay Bricklet
===================


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ 
	    tfdocstart("Bricklets/bricklet_dual_relay_tilted_350.jpg", 
	             "Bricklets/bricklet_dual_relay_tilted_600.jpg", 
	             "Dual Relay Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_horizontal_100.jpg", 
	             "Bricklets/bricklet_dual_relay_horizontal_600.jpg", 
	             "Dual Relay Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_vertical_100.jpg", 
	             "Bricklets/bricklet_dual_relay_vertical_600.jpg", 
	             "Dual Relay Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_front_100.jpg", 
	             "Bricklets/bricklet_dual_relay_front_600.jpg", 
	             "Dual Relay Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_master_100.jpg", 
	             "Bricklets/bricklet_dual_relay_master_600.jpg", 
	             "Dual Relay Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_brickv_100.jpg", 
	             "Bricklets/bricklet_dual_relay_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/dual_relay_bricklet_dimensions_100.png", 
	             "Dimensions/dual_relay_bricklet_dimensions_600.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}


Features
--------

 * 2 relays to switch AC/DC devices
 * Switches up to 250V/10A


Description
-----------

The Dual Relay :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by two 
`relays <http://en.wikipedia.org/wiki/Relay>`_. Each relay has three
terminals such that the terminal in the middle is electrically connected to 
the terminal left or right depending on the state. 
The state is visualized by a LED.

You can use this Bricklet to switch power supplies, motors, lamps, etc.
Consider the maximum voltage and current.

If you want to switch inductive loads, please see: 
:ref:`Inductive Load Switching <dual_relay_inductive_load_switching>`.

.. warning::

   Terminals and contacts are not insulated. If you want
   to switch higher voltages, consider to put the Dual Relay Bricklet
   in a casing. Touching the contacts is potentially life-threatening!!!

Technical Specifications
------------------------

==================================  ============================================================
Property                            Value
==================================  ============================================================
Dimensions                          45mm x 45mm (1.77" x 1.77")
Weight                              29.1g
Current Consumption per Relay       60mA 
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximum Voltage/Current             250V/10A or 125V/15A
==================================  ============================================================

Resources
---------

* Relay Datasheet (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/datasheets/ORWH-SH.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/hardware/dual-relay-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dual_relay_bricklet_dimensions.png>`__)
* Project source code and design files (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/zipball/master>`__)


Connectivity
------------

Each relay has three connectors A, SW and B. SW can be connected to A or B 
depending on the state of the relay. 

* If the relay is switched off, then SW is connected to B
* If the relay is switched on, then SW is connected to A


.. image:: /Images/Bricklets/bricklet_dual_relay_connection_350.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet, visualization of the switch
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_connection_700.jpg


.. _dual_relay_inductive_load_switching:

Inductive Load Switching
------------------------

Without external components the switching of inductive loads can
cause noise in the system and can lead to malfunctions or destroyed 
components. Typical examples for inductive loads are motors and solenoids,
but these problems can also occur when switching e.g. fluorescent lamps.

If you want to switch an inductive load you need external components,
e.g. a `Varistor <http://en.wikipedia.org/wiki/Varistor>`_
or a combination of a resistor and a capacitor parallel to the load.

More information about protection circuitries can be found
`here <http://www.jkmicro.com/inductive_loads.pdf>`_.



.. _dual_relay_bricklet_test:

Test your Dual Relay Bricklet
-----------------------------

To test the Dual Relay Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For installation guides click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings, the latter is for testing purposes.

Connect the Dual Relay Bricklet to a 
:ref:`Brick <product_overview_bricks>` with the supplied cable (see picture below).

.. image:: /Images/Bricklets/bricklet_dual_relay_master_600.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet with connected Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Dual Relay Bricklet" in the Brick Viewer after you pressed "connect". 
Select it.
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_dual_relay_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Dual Relay
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_brickv.jpg

Play around with the two relay buttons,
you should hear the relay switching when toggling the buttons.

After this you can go on with writing your own application.
See the :ref:`Programming Interface <dualrelay_programming_interfaces>` section 
for the API of the Dual Relay Bricklet and examples in different programming 
languages.


.. _dualrelay_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Dual_Relay_hlpi.table
