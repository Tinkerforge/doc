.. _dual_relay_bricklet:

Dual Relay
===========


.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{ tfdocstart() }}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_tilted_350.jpg", 
	             "Bricklets/bricklet_dual_relay_tilted_100.jpg", 
	             "Bricklets/bricklet_dual_relay_tilted_800.jpg", 
	             "Dual Relay Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_horizontal_350.jpg", 
	             "Bricklets/bricklet_dual_relay_horizontal_100.jpg", 
	             "Bricklets/bricklet_dual_relay_horizontal_800.jpg", 
	             "Dual Relay Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_vertical_350.jpg", 
	             "Bricklets/bricklet_dual_relay_vertical_100.jpg", 
	             "Bricklets/bricklet_dual_relay_vertical_800.jpg", 
	             "Dual Relay Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_front_350.jpg", 
	             "Bricklets/bricklet_dual_relay_front_100.jpg", 
	             "Bricklets/bricklet_dual_relay_front_800.jpg", 
	             "Dual Relay Bricklet") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_master_350.jpg", 
	             "Bricklets/bricklet_dual_relay_master_100.jpg", 
	             "Bricklets/bricklet_dual_relay_master_1200.jpg", 
	             "Dual Relay Bricklet with Master Brick") 
	}}
	{{ 
	    tfdocimg("Bricklets/bricklet_dual_relay_brickv_350.jpg", 
	             "Bricklets/bricklet_dual_relay_brickv_100.jpg", 
	             "Bricklets/bricklet_dual_relay_brickv.jpg", 
	             "Brick Viewer screenshot") 
	}}
	{{ 
	    tfdocimg("Dimensions/dual_relay_bricklet_dimensions_350.png", 
	             "Dimensions/dual_relay_bricklet_dimensions_100.png", 
	             "Dimensions/dual_relay_bricklet_dimensions.png", 
	             "Outline and drilling plan") 
	}}
	{{ tfdocend() }}

Description
-----------

With the Dual Relay :ref:`Bricklet <product_overview_bricklets>` the features of
every :ref:`Brick <product_overview_bricks>` can be extended by two 
`relays <http://en.wikipedia.org/wiki/Relay>`_. Each relay has three
terminals such that the terminal in the middle is electrically connected to 
the terminal left or right depending on the state. 
The state is visualized by a LED.

You can use this Bricklet to switch power-supplies, motors, lamps, etc.
Consider the maximum voltage and current.

.. warning::

   Be aware that handling of higher voltages is potentially dangerous!

   Note that terminals and contacts are not insulated. 
   Do not touch when switching higher voltages. 
   Doing so might cause electric shock.

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
* Project (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/zipball/master>`__)
* `Kicad Project Page <http://kicad.sourceforge.net/>`__


.. _dual_relay_bricklet_test:

Test your Dual Relay Bricklet
-----------------------------

To test your Dual Relay Bricklet you have to start by installing the
:ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>`
(For an installation guide click :ref:`here <brickd_installation>`
and :ref:`here <brickv_installation>`).
The former is a bridge between the Bricks/Bricklets and the programming
language API bindings (you need this in any case if you want to use the
Bricks/Bricklets). The latter is only for testing purposes.

Connect your Dual Relay Bricklet to an arbitrary 
:ref:`Brick <product_overview_bricks>` over the supplied cable (see picture below).

.. image:: /Images/Bricklets/bricklet_dual_relay_master_600.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet with connected Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_master_1200.jpg

If you then connect the Brick to the PC over USB, you should see a tab named 
"Dual Relay Bricklet" in the Brick Viewer after you pressed "connect", 
select it.
If everything went as expected you the Brick Viewer should look like
depicted below.

.. image:: /Images/Bricklets/bricklet_dual_relay_brickv.jpg
   :scale: 100 %
   :alt: Brickv view of Dual Relay
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_brickv.jpg

Play around with the two relay buttons,
you should hear the relay switching when toggeling the buttons.

After this you can go on with writing your own application.
See :ref:`Interface and Coding <dualrelay_programming_interfaces>` section for the API of
the Dual Relay Bricklet and examples in your programming language.


.. _dualrelay_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 8, 15, 12

   "C/C++", ":ref:`API <dual_relay_bricklet_c_api>`", ":ref:`Examples <dual_relay_bricklet_c_examples>`", "Installation"
   "C#", ":ref:`API <dual_relay_bricklet_csharp_api>`", ":ref:`Examples <dual_relay_bricklet_csharp_examples>`", "Installation"
   "Java", ":ref:`API <dual_relay_bricklet_java_api>`", ":ref:`Examples <dual_relay_bricklet_java_examples>`", "Installation"
   "Python", ":ref:`API <dual_relay_bricklet_python_api>`", ":ref:`Examples <dual_relay_bricklet_python_examples>`", "Installation"

