
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Solid State Relay Bricklet
:shoplink: ../../../shop/bricklets/solid-state-relay-bricklet.html

.. include:: Solid_State_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _solid_state_relay_bricklet:

Solid State Relay Bricklet
==========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_solid_state_relay_tilted_350.jpg",
	               "Bricklets/bricklet_solid_state_relay_tilted_600.jpg",
	               "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_solid_state_relay_horizontal_100.jpg",
	             "Bricklets/bricklet_solid_state_relay_horizontal_600.jpg",
	             "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_solid_state_relay_front_100.jpg",
	             "Bricklets/bricklet_solid_state_relay_front_600.jpg",
	             "Solid State Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_solid_state_relay_master_100.jpg",
	             "Bricklets/bricklet_solid_state_relay_master_600.jpg",
	             "Solid State Relay Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_solid_state_relay_case_100.jpg",
	             "Cases/bricklet_solid_state_relay_case_600.jpg",
	             "Solid State Relay Bricklet Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_solid_state_relay_brickv_100.jpg",
	             "Bricklets/bricklet_solid_state_relay_brickv.jpg",
	             "Solid State Relay Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/solid_state_relay_bricklet_dimensions_100.png",
	             "Dimensions/solid_state_relay_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


.. note::
 This Bricklet is currently work-in-progress.

Features
--------

* TODO


Description
-----------

TODO


Technical Specifications
------------------------

==================================  ============================================================
Property                            Value
==================================  ============================================================
Current Consumption                 TBDmA
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximum Voltage/Current             TBD
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)              TBD: 45 x 45 x 25mm (1.77 x 1.77 x 0.98")
Weight                              TBDg
==================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/raw/master/hardware/solid-state-relay-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/solid_state_relay_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/solid-state-relay-bricklet/zipball/master>`__)


Connectivity
------------

TODO

.. _solid_state_relay_bricklet_test:

Test your Solid State Relay Bricklet
------------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_solid_state_relay_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Solid State Relay Bricklet
   :align: center
   :target: ../../_images/Bricklets/bricklet_solid_state_relay_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_solid_state_relay_brickv.jpg
   :scale: 100 %
   :alt: Solid State Relay Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_solid_state_relay_brickv.jpg

Play around with the buttons, you should see the LED of the relay
switching.

|test_pi_ref|


.. _solid_state_relay_bricklet_case:

Case
----

TODO: FIXME

A `laser-cut case for the Solid State Relay Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-solid_state-relay-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_solid_state_relay_case_350.jpg
   :scale: 100 %
   :alt: Case for Solid State Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_solid_state_relay_case_1000.jpg

The case of the Solid State Relay Bricklet is delivered including cable ties
for a cable relief and WAGO connecting clamps to join wires. The case
is big enough to accommodate the cable relief as well as the WAGO
clamps.

The internal construction can look as follows (with one as well as
two relays connected)

.. image:: /Images/Cases/bricklet_solid_state_relay_case_top_open_1_350.jpg
   :scale: 100 %
   :alt: Case for Solid State Relay Bricklet with one relay connected
   :align: center
   :target: ../../_images/Cases/bricklet_solid_state_relay_case_top_open_1_1000.jpg

.. image:: /Images/Cases/bricklet_solid_state_relay_case_top_open_2_350.jpg
   :scale: 100 %
   :alt: Case for Solid State Relay Bricklet with two relays connected
   :align: center
   :target: ../../_images/Cases/bricklet_solid_state_relay_case_top_open_2_1000.jpg

The protective conductor (brown) is switched with the Solid State Relay Bricklet.
The external conductor (green-yellow) and the neutral conductor (blue)
are coupled with the WAGO connecting clamps.

It is important that the external conductor is longer then the other cables.
This way it is assured that the external conductor will be pulled of at last
if the cable relief is overstrained or defect. We recommend the following 
length for the cables and the stripping:

.. image:: /Images/Cases/bricklet_solid_state_relay_case_cables_350.jpg
   :scale: 100 %
   :alt: Recommended lengths
   :align: center
   :target: ../../_images/Cases/bricklet_solid_state_relay_case_cable_1000.jpg

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
drawing of the Solid State Relay Bricklet case:

.. image:: /Images/Exploded/solid_state_relay_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Solid State Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/solid_state_relay_exploded.png

|bricklet_case_hint|


.. _solid_state_relay_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Solid_State_Relay_hlpi.table
