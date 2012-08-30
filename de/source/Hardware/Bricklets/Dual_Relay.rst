.. include:: Dual_Relay.substitutions


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
	             "Dual Relay Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_dual_relay_brickv_100.jpg",
	             "Bricklets/bricklet_dual_relay_brickv.jpg",
	             "Dual Relay Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/dual_relay_bricklet_dimensions_100.png",
	             "Dimensions/dual_relay_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Zwei Relais um AC/DC Geräte zu schalten
* Schaltet bis zu 240VAC/10A und 24VDC/10A


Beschreibung
------------

Mit dem Dual Relay :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` um zwei
`Relais <http://de.wikipedia.org/wiki/Relais>`__ erweitert werden.
Jedes Relais besitzt drei Anschlüsse, der mittlere wird zwischen den beiden
äußeren umgeschaltet. Der Schaltzustand wird jeweils durch eine LED angezeigt.

Dieses Bricklet kann benutzt werden um Stromversorgungen, Motoren, Lampen etc.
zu schalten.

Das Schalten induktiver Lasten kann besondere Vorkehrungen erfordern, siehe:
:ref:`Schalten Induktiver Lasten <dual_relay_inductive_load_switching>`.

.. warning::
 Anschlussklemmen und Kontakte sind nicht isoliert. Beim Schalten von hohen
 Spannungen sollte das Dual Relay Bricklet in ein Gehäuse verbaut werden.
 Das Berühren der Kontakte ist potentiell lebensgefährlich!


Technische Spezifikation
------------------------

==================================  ============================================================
Eigenschaft                         Wert
==================================  ============================================================
Stromverbrauch pro Relais           60mA
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Maximale Spannung/Strom             AC: 240V/10A
                                    DC:  24V/10A
----------------------------------  ------------------------------------------------------------
----------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)             45 x 45 x 25mm (1,77 x 1,77 x 0,98")
Gewicht                             37g
==================================  ============================================================


Ressourcen
----------

* T7CS5D-05 Datenblatt (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/datasheets/T7CS5D-05.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/raw/master/hardware/dual-relay-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/dual_relay_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/dual-relay-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Jedes Relais hat drei Anschlüsse: A, SW und B. SW ist mit A oder B verbunden
abhängig vom Schaltzustand des Relais.

* Wenn das Relais ausgeschaltet ist, dann ist SW mit B verbunden
* Wenn das Relais eingeschaltet ist, dann ist SW mit A verbunden

.. image:: /Images/Bricklets/bricklet_dual_relay_connection_350.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet Schaltzustand
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_connection_700.jpg


.. _dual_relay_bricklet_test:

Teste dein Dual Relay Bricklet
------------------------------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_dual_relay_master_600.jpg
   :scale: 100 %
   :alt: Dual Relay verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_master_1200.jpg

|test_tab|

If everything went as expected the Brick Viewer should look as
depicted below.

.. image:: /Images/Bricklets/bricklet_dual_relay_brickv.jpg
   :scale: 100 %
   :alt: Dual Relay Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_dual_relay_brickv.jpg

Play around with the two relay buttons,
you should hear the relay switching when toggling the buttons.

|test_pi_ref|


.. _dual_relay_inductive_load_switching:

Schalten Induktiver Lasten
--------------------------

Without external components the switching of inductive loads can
cause noise in the system and can lead to malfunctions or destroyed
components. Typical examples for inductive loads are motors and solenoids,
but these problems can also occur when switching e.g. fluorescent lamps.

If you want to switch an inductive load you need external components,
e.g. a `Varistor <http://en.wikipedia.org/wiki/Varistor>`__
or a combination of a resistor and a capacitor parallel to the load.

More information about protection circuitries can be found
`here <http://www.jkmicro.com/inductive_loads.pdf>`__.


.. _dual_relay_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: Dual_Relay_hlpi.table
