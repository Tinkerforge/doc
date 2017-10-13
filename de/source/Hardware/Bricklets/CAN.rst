
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / CAN Bricklet
:shoplink: ../../../shop/bricklets/can-bricklet.html

.. include:: CAN.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _can_bricklet:

CAN Bricklet
============

.. raw:: html

	{% tfgallery %}

	Bricklets/bricklet_can_tilted_[?|?].jpg           CAN Bricklet
	Bricklets/bricklet_can_horizontal_[?|?].jpg       CAN Bricklet
	Cases/bricklet_can_case_built_up1_[?|?].jpg       CAN Bricklet im Gehäuse
	Cases/bricklet_can_case_built_up2_[?|?].jpg       CAN Bricklet im Gehäuse
	Bricklets/bricklet_can_brickv_[100|].jpg          CAN Bricklet im Brick Viewer
	Dimensions/can_bricklet_dimensions_[100|600].png  Umriss und Bohrplan

	{% tfgalleryend %}


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

Die Baudrate kann zwischen 10kbit/s und 1Mbit/s konfiguriert werden. Es
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
Maximaler Durchsatz               1000 Frames pro Sekunden*
Filter                            Disabled / Accept All / Match / Match Data / Match Extended
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           45 x 35 x 14mm (1,77 x 1,38 x 0,55")
Gewicht                           9g
================================  ============================================================

\* 1000 Frames pro Sekunden entspricht 44kbit/s bis 128kbit/s abhängig von der Größe der Frames.

Ressourcen
----------

* MCP2515 (CAN Controller) Datenblatt (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/datasheets/MCP2515.pdf>`__)
* MCP2562 (CAN Transceiver) Datenblatt (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/datasheets/MCP2562.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/can-bricklet/raw/master/hardware/can-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/can_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/can-bricklet/zipball/master>`__)
* 3D Modell (`Online ansehen <http://a360.co/2vslBZp>`__ | Download: `STEP <http://download.tinkerforge.com/3d/bricklets/can/can.step>`__, `FreeCAD <http://download.tinkerforge.com/3d/bricklets/can/can.FCStd>`__)


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

Ein `laser-geschnittenes Gehäuse für das CAN Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-can-bricklet.html>`__
ist verfügbar.

.. image:: /Images/Cases/bricklet_can_case_built_up1_350.jpg
   :scale: 100 %
   :alt: Gehäuse für CAN Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_can_case_built_up1_1000.jpg

.. include:: CAN.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/can_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für CAN Bricklet
   :align: center
   :target: ../../_images/Exploded/can_exploded.png

|bricklet_case_hint|


.. _can_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: CAN_hlpi.table
