
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Solid State Relay Bricklet 2.0
.. :shoplink: ../../../shop/bricklets/solid-state-relay-v2-bricklet.html

.. include:: Solid_State_Relay_V2.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _solid_state_relay_v2_bricklet:

Solid State Relay Bricklet 2.0
==============================

.. note::
  This Bricklet is currently under development.

..
	.. raw:: html

		{% tfgallery %}

		Bricklets/bricklet_ssr_v2_w_ssr_[100|600].jpg                      Solid State Relay Bricklet 2.0
		Bricklets/bricklet_ssr_v2_w_master_[100|600].jpg                   Solid State Relay Bricklet 2.0 with Master Brick
		Bricklets/bricklet_ssr_v2_vertical_[?|?].jpg                       Solid State Relay Bricklet 2.0
		Bricklets/bricklet_ssr_v2_tilted_[?|?].jpg                         Solid State Relay Bricklet 2.0
		Bricklets/bricklet_ssr_v2_w_cover_[100|600].jpg                    Solid State Relay Bricklet 2.0 with cover
		Bricklets/bricklet_ssr_v2_w_heatsink_tilted_low_[?|?].jpg          Solid State Relay Bricklet 2.0 with heatsink
		Bricklets/bricklet_ssr_v2_w_heatsink_tilted_[?|?].jpg              Solid State Relay Bricklet 2.0 with heatsink
		Bricklets/bricklet_solid_state_relay_v2_brickv_[100|].jpg          Solid State Relay Bricklet 2.0 in Brick Viewer
		Dimensions/solid_state_relay_v2_bricklet_dimensions_[100|600].png  Outline and drilling plan

		{% tfgalleryend %}


Features
--------

* Galvanically isolated switching of large AC or DC loads

  * For example: motors, pumps and lamps

* Bricklet controls Solid State Relays (SSR)

  * The offered SSRs can switch up to 380V/25A AC or 50V/80A DC

* PWM possible (dimming of lamps, control speed of motors)


.. _solid_state_relay_v2_bricklet_description:

Description
-----------

The Solid State Relay :ref:`Bricklet <primer_bricklets>` 2.0 can be used to
extend :ref:`Bricks <primer_bricks>` by the possibility to switch `solid state
relays (SSR) <https://en.wikipedia.org/wiki/Solid-state_relay>`__.

With solid state relays large loads can be switched while being galvanically isolated.
Mechanical relays can create switching sparks and other interferences.
Solid state relays do not. Furthermore solid state relays
are wearless and allow higher switching frequencies.

The maximum switching capacity depends on the connected solid state relay, which
is controlled by the Solid State Relay Bricklet 2.0.

We offer two compatible solid state relays in our shop:

* `AC (Alternating Current) SSR for up to 25A at 380V
  <https://www.tinkerforge.com/en/shop/solid-state-relay-ac-380v-25a.html>`__
* `DC (Direct Current) SSR for up to 80A at 50V
  <https://www.tinkerforge.com/en/shop/solid-state-relay-dc-50v-80a.html>`__


Technical Specification
-----------------------

=====================================  ============================================================
Property                               Value
=====================================  ============================================================
Current Consumption                    TBDmA
-------------------------------------  ------------------------------------------------------------
-------------------------------------  ------------------------------------------------------------
Necessary Contact Space of SSR Input   25.4mm (1")
-------------------------------------  ------------------------------------------------------------
-------------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)                 19 x 33.4 x 5mm (0.75 x 1.31 x 0.2")
Weight                                 TBDg
=====================================  ============================================================


Resources
---------

* SSR AC 380V/25A (KS15/D-38Z25-L) datasheet (`Download <https://github.com/Tinkerforge/solid-state-relay-v2-bricklet/raw/master/datasheets/ks15_ac.pdf>`__)
* SSR DC 50V/80A (KS33/D-50D80-L) datasheet (`Download <https://github.com/Tinkerforge/solid-state-relay-v2-bricklet/raw/master/datasheets/ks33_dc.pdf>`__)
* SSR heatsink (HF92B-120) datasheet (`Download <https://github.com/Tinkerforge/solid-state-relay-v2-bricklet/raw/master/datasheets/hf92b_heatsink.pdf>`__)
* SSR cover datasheet (`Download <https://github.com/Tinkerforge/solid-state-relay-v2-bricklet/raw/master/datasheets/ssr_cover.pdf>`__)
* Schematic (`Download <https://github.com/Tinkerforge/solid-state-relay-v2-bricklet/raw/master/hardware/solid-state-relay-v2-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/solid_state_relay_v2_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/solid-state-relay-v2-bricklet/zipball/master>`__)


Connectivity
------------

The Bricklet has to be connected to the control inputs of a solid state relay.
You have to consider the polarity. Connect the SSR input marked with "+" with
the "+" marked contact of the Bricklet.

The load terminals of the AC solid state relays has no polarity. Typically you
want to switch the phase wire. To do this you cut the phase wire (typically
black or brown) and connect both ends with the relay.

The load terminals of DC solid state relays has a polarity. "+" marks the higher
voltage. For example, if a power supply should be switched, you have to cut
the "+" wire. Each end will be connected to the SSR, whereas the wire directly
connected to the power supply has to be connected to the "+" pole of the SSR.

.. warning:: The handling of alternating currents and high direct currents is
             potential hazardous!

.. _solid_state_relay_v2_bricklet_test:

Test your Solid State Relay Bricklet 2.0
----------------------------------------

|test_intro|

|test_connect| (see picture below).

.. image:: /Images/Bricklets/bricklet_ssr_v2_w_master_600.jpg
   :scale: 100 %
   :alt: Master Brick with connected Solid State Relay Bricklet 2.0
   :align: center
   :target: ../../_images/Bricklets/bricklet_ssr_v2_w_master_1200.jpg

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_solid_state_relay_v2_brickv.jpg
   :scale: 100 %
   :alt: Solid State Relay Bricklet 2.0 in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_solid_state_relay_v2_brickv.jpg

Play around with the buttons, you should see the LED of the relay
switching.

|test_pi_ref|


PWM / Dimming / Speed Control
-----------------------------

With `Pulse-width modulation <https://en.wikipedia.org/wiki/Pulse-width_modulation>`__
the power of loads connected to the solid state relay can be controlled
(e.g. brightness of a lamp, speed of a motor). With a fixed frequency the load
will be switched on for a variable time. Depending on the time the power will be
controlled.

Example:
We want to control a heating device. A heating device has a high inertia so a 
frequency of 1Hz will suffice. By varying the on-time between 0-1 second the power
can be controlled between 0-100%. To do this we write a small program with a
timer that calls the "set_monoflop" function of the Solid State Relay Bricklet 2.0 
every second with an on-time between 0-1 seconds.

.. warning::
   High switching frequencies produce heat in the solid state relay. If these 
   frequencies are too high, and there is not enough cooling, the relay can be
   destroyed. The maximum switching frequency with sufficient cooling is 30Hz.


.. _solid_state_relay_v2_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Solid_State_Relay_V2_hlpi.table
