
:DISABLED_shoplink: ../../../shop/bricklets/industrial-dual-relay-bricklet.html

.. include:: Industrial_Dual_Relay.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _industrial_dual_relay_bricklet:

Industrial Dual Relay Bricklet
==============================

.. note::
  This Bricklet is currently work-in-progress!

..
    .. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_industrial_dual_relay_tilted_[?|?].jpg           Industrial Dual Relay Bricklet
	Bricklets/bricklet_industrial_dual_relay_horizontal_[?|?].jpg       Industrial Dual Relay Bricklet
	Bricklets/bricklet_industrial_dual_relay_master_[100|600].jpg       Industrial Dual Relay Bricklet with Master Brick
	Cases/bricklet_industrial_dual_relay_case_[100|600].jpg             Industrial Dual Relay Bricklet with case
	Bricklets/bricklet_industrial_dual_relay_brickv_[100|].jpg          Industrial Dual Relay Bricklet in Brick Viewer
	Dimensions/industrial_dual_relay_bricklet_dimensions_[100|600].png  Outline and drilling plan

	{% tfgalleryend %}


Features
--------

* Two relays for switching AC/DC devices
* Switches up to 240VAC/10A and 30VDC/7A


.. _industrial_dual_relay_bricklet_description:

Description
-----------

The Industrial Dual Relay :ref:`Bricklet <primer_bricklets>` can be used to
extend the features of :ref:`Bricks <primer_bricks>` by two
`relays <https://en.wikipedia.org/wiki/Relay>`__. Each relay has three
terminals such that the terminal in the middle is electrically connected to
the terminal left or right depending on the state.
The state is visualized by a LED. The Bricklet is equipped with 

You can use this Bricklet to switch power supplies, motors, lamps, etc.
Consider the maximum voltage and current.

If you want to switch inductive loads, please see:
:ref:`Inductive Load Switching <dual_relay_inductive_load_switching>`.

.. warning::
 Terminals and contacts are not insulated. If you want
 to switch higher voltages, consider to put the Dual Relay Bricklet
 in a casing. Touching the contacts is potentially life-threatening!

The Industrial Dual Relay Bricklet has a 7 pole Bricklet connector and
is connected to a Brick with a ``7p-10p`` Bricklet cable.

Technical Specifications
------------------------

==================================  ============================================================
Property                            Value
==================================  ============================================================
Relay                               AZ943-1CH-5DE
Current Consumption                 | 27mw (5.4mA at 5V) 
                                    | + 350mw (70mA at 5V) per activated relay
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximum Voltage/Current             | AC: 240V/10A
                                    | DC: 30V/7A
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)              40 x 40 x 25mm (1.57 x 1.57 x 0.98")
Weight                              29.4g
==================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-dual-relay-bricklet/raw/master/hardware/industrial-dual-relay-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial_dual_relay_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-dual-relay-bricklet/zipball/master>`__)
* 3D model (`View online <TBD>`__ | Download: `STEP <http://download.tinkerforge.com/3d/TBD/TBD.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/TBD/TBD.FCStd>`__)


Connectivity
------------

Each relay has three connectors: A, SW and B. SW is connected to A or B
depending on the switching state of the relay.

* If the relay is switched off, then SW is connected to B
* If the relay is switched on, then SW is connected to A

TODO: Update image

.. image:: /Images/Bricklets/bricklet_dual_relay_connection_350.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet, visualization of the switch
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_connection_700.jpg


.. _industrial_dual_relay_bricklet_test:

Test your Industrial Dual Relay Bricklet
----------------------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_industrial_dual_relay_brickv.jpg
   :scale: 100 %
   :alt: Industrial Dual Relay Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_dual_relay_brickv.jpg

|test_pi_ref|

Play around with the two relay buttons,
you should hear the relay switching when toggling the buttons. An LED indicates
the current state of each relay.


.. _industrial_dual_relay_inductive_load_switching:

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


.. _industrial_dual_relay_bricklet_case:

Case
----

..
	A `laser-cut case for the Industrial Dual Relay Bricklet
	<https://www.tinkerforge.com/en/shop/cases/case-industrial-dual-relay-bricklet.html>`__ is available.

	.. image:: /Images/Cases/bricklet_industrial_dual_relay_case_350.jpg
	   :scale: 100 %
	   :alt: Case for Industrial Dual Relay Bricklet
	   :align: center
	   :target: ../../_images/Cases/bricklet_industrial_dual_relay_case_1000.jpg

	.. include:: Industrial_Dual_Relay.substitutions
	   :start-after: >>>bricklet_case_steps
	   :end-before: <<<bricklet_case_steps

	.. image:: /Images/Exploded/industrial_dual_relay_exploded_350.png
	   :scale: 100 %
	   :alt: Exploded assembly drawing for Industrial Dual Relay Bricklet
	   :align: center
	   :target: ../../_images/Exploded/industrial_dual_relay_exploded.png

	|bricklet_case_hint|


.. _industrial_dual_relay_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Industrial_Dual_Relay_hlpi.table
