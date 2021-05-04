:shoplink: ../../../shop/bricklets/industrial-dual-ac-relay-bricklet.html

.. include:: Industrial_Dual_AC_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_ac_relay_bricklet:

Industrial Dual AC Relay Bricklet
=================================

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_ac_relay_tilted_[?|?].jpg           Industrial Dual AC Relay Bricklet
	Bricklets/bricklet_industrial_dual_ac_relay_w_connector_[?|?].jpg      Industrial Dual AC Relay Bricklet
	Bricklets/bricklet_industrial_dual_ac_relay_horizontal_[?|?].jpg       Industrial Dual AC Relay Bricklet
	Bricklets/bricklet_industrial_dual_ac_relay_caption_[?|?].jpg          Industrial Dual AC Relay Bricklet
	Bricklets/bricklet_industrial_dual_ac_relay_brickv_[100|].jpg          Industrial Dual AC Relay Bricklet in Brick Viewer
	Dimensions/industrial_dual_ac_relay_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Two solid state relays for switching AC devices
* Switches up to 240VAC/1.2A (with max 12A surge current)
* Switching done during zero-crossing


.. _industrial_dual_ac_relay_bricklet_description:

Description
-----------

The Industrial Dual AC Relay :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by two
`solid state relays (SSR) <https://en.wikipedia.org/wiki/Solid-state_relay>`__. 
Each relay has two terminals. The state is visualized by a LED. 

You can use this Bricklet to switch power supplies, motors, lamps, etc.
Consider the maximum voltage and current.

.. warning::
 Terminals and contacts are not insulated. If you want
 to switch higher voltages, consider to put the Dual AC Relay Bricklet
 in a casing. Touching the contacts is potentially life-threatening!

The Industrial Dual AC Relay Bricklet has a 7 pole Bricklet connector and
is connected to a Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

==================================  ============================================================
Property                            Value
==================================  ============================================================
Solid State Relay                   Panasonic AQH3213A
Current Consumption                 | 25mW (5mA at 5V)
                                    | + 60mW (12mA at 5V) per activated relay
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximum Voltage/Current             AC 240V/1.2A (with max 12A surge current)
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)              40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Weight                              11g
==================================  ============================================================


Resources
---------

* AQH3213A Solid State Relay (`Download <https://github.com/Tinkerforge/industrial-dual-ac-relay-bricklet/raw/master/hardware/industrial-dual-ac-relay-schematic.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/industrial-dual-ac-relay-bricklet/raw/master/datasheets/AH-Q.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_dual_ac_relay_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-dual-ac-relay-bricklet/zipball/master>`__)
* 3D model (`View online <https://a360.co/3nvkxgh>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_relay/industrial-dual-ac-relay.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricklets/industrial_dual_ac_relay/industrial-dual-ac-relay.FCStd>`__)


Connectivity
------------

The following picture shows the different connection possibilities of the Industrial Dual AC Relay Bricklet.

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_relay_caption_front_and_top_800.jpg
   :scale: 100 %
   :alt: Industrial Dual AC Relay Bricklet connectivity
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_relay_caption_front_and_top_1200.jpg


.. _industrial_dual_ac_relay_bricklet_test:

Test your Industrial Dual AC Relay Bricklet
----------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_industrial_dual_ac_relay_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual AC Relay Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_ac_relay_brickv.jpg

|test_pi_ref|

Play around with the two relay buttons, an LED indicates the current state of each relay.


.. _industrial_dual_ac_relay_bricklet_case:

Case
----

A `laser-cut case for the Industrial Dual Relay Bricklet and Industrial Dual AC Relay Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-industrial-dual-relay-bricklet.html>`__ 
is available (images show Industrial Dual Relay Bricklet).

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Dual AC Relay Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_1000.jpg

The case of the Industrial Dual AC Relay Bricklet is delivered including cable ties
for a cable relief and WAGO connecting clamps to join wires. The case
is big enough to accommodate the cable relief as well as the WAGO
clamps.

The internal construction can look as follows (with one as well as
two relays connected)

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_top1_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Dual AC Relay Bricklet with one relay connected
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_top1_1000.jpg

.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_top2_350.jpg
   :scale: 100 %
   :alt: Case for Industrial Dual AC Relay Bricklet with two relays connected
   :align: center
   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_top2_1000.jpg

The protective conductor (brown) is switched with the Industrial Dual AC Relay Bricklet.
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
drawing of the Industrial Dual AC Relay Bricklet case:

.. image:: /Images/Exploded/dual_relay_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Industrial Dual AC Relay Bricklet
   :align: center
   :target: ../../_images/Exploded/dual_relay_exploded.png

|bricklet_case_hint|


.. _industrial_dual_ac_relay_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Dual_AC_Relay_hlpi.table
