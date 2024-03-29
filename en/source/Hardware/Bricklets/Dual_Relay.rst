
.. include:: Dual_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _dual_relay_bricklet:

Dual Relay Bricklet
===================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_dual_relay_12_tilted_[?|?].jpg        Dual Relay Bricklet
	Bricklets/bricklet_dual_relay_12_horizontal_[?|?].jpg    Dual Relay Bricklet
	Bricklets/bricklet_dual_relay_12_front_[?|?].jpg         Dual Relay Bricklet
	Bricklets/bricklet_dual_relay_master_[100|600].jpg       Dual Relay Bricklet with Master Brick
	Cases/bricklet_dual_relay_case_[100|600].jpg             Dual Relay Bricklet Case
	Bricklets/bricklet_dual_relay_brickv_[100|].jpg          Dual Relay Bricklet in Brick Viewer
	Dimensions/dual_relay_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}

.. note::

 The Dual Relay Bricklet is discontinued and is no longer sold. The
 :ref:`Industrial Dual Relay Bricklet <industrial_dual_relay_bricklet>` is the recommended
 replacement.


Features
--------

* Two relays to switch AC/DC devices
* Switches up to 240VAC/10A and 30VDC/7A


.. _dual_relay_bricklet_description:

Description
-----------

The Dual Relay :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by two
`relays <https://en.wikipedia.org/wiki/Relay>`__. Each relay has three
terminals such that the terminal in the middle is electrically connected to
the terminal left or right depending on the state.
The state is visualized by a LED. The new hardware version 1.2 is equipped with 
extensive protection circuitry against interference of inductive load switching. 

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
Relay                               AZ943-1CH-5DE
Current Consumption                 75mA (per Relay)
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximum Voltage/Current             | AC: 240V/10A
                                    | DC: 30V/7A
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)              45 x 45 x 25mm (1.77 x 1.77 x 0.98")
Weight                              29g
==================================  ============================================================


Resources
---------

* AZ943-1CH-5DE datasheet (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/datasheets/az943.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/hardware/dual-relay-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/dual_relay_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/zipball/master>`__)
* 3D model (`View online <https://autode.sk/2pLtx4b>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/dual_relay/dual-relay.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/dual_relay/dual-relay.FCStd>`__)



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
e.g. a `varistor <https://en.wikipedia.org/wiki/Varistor>`__
or a combination of a resistor and a capacitor parallel to the load.

More information about protection circuitries can be found
`here <http://www.jkmicro.com/inductive_loads.pdf>`__.


.. _dual_relay_bricklet_case:

Case
----

A `laser-cut case for the Dual Relay Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-industrial-dual-relay-bricklet.html>`__ is available.

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
   :target: ../../_images/Cases/bricklet_dual_relay_case_cables_1000.jpg

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


.. _dual_relay_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Dual_Relay_hlpi.table
