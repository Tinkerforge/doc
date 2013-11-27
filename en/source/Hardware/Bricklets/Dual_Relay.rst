
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../Product_Overview.html#bricklets">Bricklets</a> / Dual Relay Bricklet
:shoplink: ../../../shop/bricklets/dual-relay-bricklet.html

.. include:: Dual_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

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
	    tfdocimg("Cases/bricklet_dual_relay_case_100.jpg",
	             "Cases/bricklet_dual_relay_case_600.jpg",
	             "Dual Relay Bricklet Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_relay_brickv_100.jpg",
	             "Bricklets/bricklet_dual_relay_brickv.jpg",
	             "Dual Relay Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/dual_relay_bricklet_dimensions_100.png",
	             "Dimensions/dual_relay_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Two relays to switch AC/DC devices
* Switches up to 240VAC/10A and 24VDC/10A


Description
-----------

The Dual Relay :ref:`Bricklet <product_overview_bricklets>` can be used to
extend the features of :ref:`Bricks <product_overview_bricks>` by two
`relays <http://en.wikipedia.org/wiki/Relay>`__. Each relay has three
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
 in a casing. Touching the contacts is potentially life-threatening!


Technical Specifications
------------------------

==================================  ============================================================
Property                            Value
==================================  ============================================================
Relay                               T7CS5D-05
Current Consumption                 60mA (per Relay)
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Frequency Of Operation              360 per hour
Maximum Voltage/Current             | AC: 240V/10A
                                    | DC: 24V/10A
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)              45 x 45 x 25mm (1.77 x 1.77 x 0.98")
Weight                              37g
==================================  ============================================================


Resources
---------

* T7CS5D-05 datasheet (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/datasheets/T7CS5D-05.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/hardware/dual-relay-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dual_relay_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/zipball/master>`__)


Connectivity
------------

Each relay has three connectors: A, SW and B. SW is connected to A or B
depending on the switching state of the relay.

* If the relay is switched off, then SW is connected to B
* If the relay is switched on, then SW is connected to A

.. image:: /Images/Bricklets/bricklet_dual_relay_connection_350.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet, visualization of the switch
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_connection_700.jpg


.. _dual_relay_bricklet_test:

Test your Dual Relay Bricklet
-----------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_dual_relay_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Dual Relay Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_dual_relay_brickv.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_brickv.jpg

..
  FIXME: update screenshot and description for monoflop

Play around with the two relay buttons,
you should hear the relay switching when toggling the buttons. An LED indicates
the current state of each relay.

|test_pi_ref|


.. _dual_relay_inductive_load_switching:

Inductive Load Switching
------------------------

Without external components the switching of inductive loads can
cause interference in the system that can lead to malfunctions or destroyed
components. Typical examples for inductive loads are motors and solenoids,
but these problems can also occur when switching e.g. fluorescent lamps.

If you want to switch an inductive load you need external components,
e.g. a `Varistor <http://en.wikipedia.org/wiki/Varistor>`__
or a combination of a resistor and a capacitor parallel to the load.

More information about protection circuitries can be found
`here <http://www.jkmicro.com/inductive_loads.pdf>`__.


.. _dual_relay_bricklet_case:

Case
----

A `laser-cut case for the Dual Relay Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-dual-relay-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_dual_relay_case_350.jpg
   :scale: 100 %
   :alt: Case for Dual Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_1000.jpg

The case of the Dual Relay Bricklet is delivered including cable ties
for a cable relief and WAGO connecting clamps to join wires. The case
is big enough to accommodate the cable relief as well as the WAGO
clamps.

The internal construction can look as follows (with one as well as
two relays connected)

.. image:: /Images/Cases/bricklet_dual_relay_case_top_open_1_350.jpg
   :scale: 100 %
   :alt: Case for Dual Relay Bricklet with one relay connected
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_top_open_1_1000.jpg

.. image:: /Images/Cases/bricklet_dual_relay_case_top_open_2_350.jpg
   :scale: 100 %
   :alt: Case for Dual Relay Bricklet with two relays connected
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_top_open_2_1000.jpg

The protective conductor (brown) is switched with the Dual Relay Bricklet.
The external conductor (green-yellow) and the neutral conductor (blue)
are coupled with the WAGO connecting clamps.

It is important that the external conductor is longer then the other cables.
This way it is assured that the external conductor will be pulled of at last
if the cable relief is overstrained or defect. We recommend the following 
length for the cables and the stripping:

.. image:: /Images/Cases/bricklet_dual_relay_case_cables_350.jpg
   :scale: 100 %
   :alt: Recommended lengths
   :align: center
   :target: ../../_images/Cases/bricklet_dual_relay_case_cable_1000.jpg

The assembly is easiest if you follow the following steps:

* screw spacers to Bricklet
* screw Bricklet to bottom plate with spacers
* build up side plates (including cable relief)
* plug side plates into bottom plate
* add cabling and WAGO clamps
* tie cable ties to cables
* screw top plate to top spacers

.. warning:: Never work inside the case when components are carrying voltage!

The exact position of each part can be seen in the following exploded assembly 
drawing of the Dual Relay Bricklet case:

.. image:: /Images/Exploded/dual_relay_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Dual Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/dual_relay_exploded.png

|bricklet_case_hint|


.. _dual_relay_bricklet_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Dual_Relay_hlpi.table
