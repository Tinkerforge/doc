
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / CAN Bricklet
:shoplink: ../../../shop/bricklets/can-bricklet.html

.. include:: CAN.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _can_bricklet:

CAN Bricklet
============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_can_tilted_350.jpg",
	               "Bricklets/bricklet_can_tilted_600.jpg",
	               "CAN Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_can_horizontal_100.jpg",
	             "Bricklets/bricklet_can_horizontal_600.jpg",
	             "CAN Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_can_brickv_100.jpg",
	             "Bricklets/bricklet_can_brickv.jpg",
	             "CAN Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/can_bricklet_dimensions_100.png",
	             "Dimensions/can_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Sendet und empfängt Daten über einen CAN-Bus.
* Konfigurierbare Baudrate, Modi und Filter

.. _can_bricklet_description:

Beschreibung
------------

Mit dem CAN :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` Daten auf einem CAN-Bus
senden und empfangen.

Die Bandrate kann zwischen 10kbit/s und 1Mbit/s konfiguriert werden. Es
ist möglich Filter anzuwenden um nur Frames mit einem spezifischen
Identifier zu empfangen.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    30mW (6mA bei 5V, Idle)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Baudrate                          10kbit/s - 1Mbit/s
Filter                            Disabled / Accept All / Match / Match Data / Match Extended
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           45 x 35 x 14mm (1,77 x 1,38 x 0,55")
Gewicht                           9g
================================  ============================================================

Ressourcen
----------

* CAN Controller Datenblatt (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/datasheets/MCP2515.pdf>`__)
* CAN Transceiver Datenblatt (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/datasheets/MCP2562.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/hardware/can-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/can_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/can-bricklet/zipball/master>`__)


.. _can_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
Verbinde ein CAN Gerät mit den CAN-L, CAN-H und GND Schraubklemmen.

|test_tab|
Wenn alles wie erwartet funktioniert werden jetzt die Frames die über
den CAN-Bus geschickt werden in der Frame-Tabelle des Brick Viewer angezeigt.

.. image:: /Images/Bricklets/bricklet_can_brickv.jpg
   :scale: 100 %
   :alt: CAN Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_can_brickv.jpg

|test_pi_ref|

.. _can_bricklet_case:

Gehäuse
-------

Coming soon...

.. _can_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: CAN_hlpi.table
