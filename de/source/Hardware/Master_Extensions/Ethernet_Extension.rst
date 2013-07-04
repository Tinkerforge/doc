
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#master-extensions">Master Extensions</a> / Ethernet Extension
:shoplink: ../../../shop/master-extensions/ethernet-master-extension.html

.. _ethernet_extension:

Ethernet Extension
==================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Extensions/extension_ethernet_tilted_350.jpg",
	               "Extensions/extension_ethernet_tilted_600.jpg",
	               "Ethernet Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_ethernet_cable_100.jpg",
	             "Extensions/extension_ethernet_cable_600.jpg",
	             "Ethernet Extension mit Ethernetkabel")
	}}
	{{
	    tfdocimg("Extensions/extension_ethernet_side_100.jpg",
	             "Extensions/extension_ethernet_side_600.jpg",
	             "Ethernet Extension Seitenansicht")
	}}
	{{
	    tfdocimg("Extensions/extension_ethernet_bottom_100.jpg",
	             "Extensions/extension_ethernet_bottom_600.jpg",
	             "Ethernet Extension von unten")
	}}
	{{
	    tfdocimg("Extensions/extension_ethernet_top_100.jpg",
	             "Extensions/extension_ethernet_top_600.jpg",
	             "Ethernet Extension von oben")
	}}
	{{ tfdocend() }}

Features
--------

* Kommuniziere direkt mit Bricks/Bricklet ohne Brickd
* Unterstützt 10/100 Mbit/s Ethernet (1000 Mbit/s kompatibel)
* Integrierte PoE Stromversorgung (PD Class 0 für IEEE 802.3af)

 * Ermöglicht die Stromversorgung eines Stapels per Ethernetkabel



Beschreibung
------------

Mit dieser Ethernet Extension können :ref:`Bricks <product_overview_bricks>` und
:ref:`Bricklets <product_overview_bricklets>` in ein 
`LAN <https://de.wikipedia.org/wiki/Local_Area_Network>`__ integriert 
werden. Das Modul unterstützt 10BaseT/100BaseTX Ethernet und ist 1000BaseTX 
kompatibel. Die integrierte `PoE <https://de.wikipedia.org/wiki/Power_over_Ethernet>`__
Stromversorgung ermöglicht eine Versorgung der angeschlossenen Module
nach Industriestandard IEEE 802.3af, so dass sowohl über PoE 
Injektoren als auch über PoE fähige Switche versorgt werden kann.

Da die Extension selbst die von der API generierten TCP/IP Pakete behandeln kann, 
ist es möglich direkt vom Smartphone, Tablet oder (Embedded) PC zu steuern. 
Der :ref:`Brick Daemon <brickd>` ist nicht mehr notwendig.

Um die Ethernet Extension zu nutzen ist ein :ref:`Master Brick <master_brick>` 
notwendig. Wenn andere Bricks gesteuert werden sollen, so kann ein Stapel aus 
diesen gebaut werden und auf der Master Brick gesteckt werden. Wenn Bricklets 
verwendet werden sollen, so können diese einfach an den Master Brick oder 
andere Bricks im Stapel angeschlossen werden. Aus Programmierersicht ist 
dies absolut transparent, d.h. alle Bricks und Bricklets können so genutzt 
werden als ob sie direkt per USB mit dem steuernden Gerät verbunden wären.

Der benutzte Master Brick muss eine Firmware Version von 2.1.0 oder neuer 
besitzen um diese Extension nutzen zu können.

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich. 
Die Reihenfolge im Stapel ist dabei nicht relevant:

* Ethernet / RS485 Master
* Ethernet / Chibi Master


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    100mA (Durchschnitt), 175mA (Maximum)
PoE 5V Stapelversorgung           > 1A
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Ethernet Unterstützung            10BaseT/100BaseTX, 1000BaseTX kompatible
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                           22g 
================================  ============================================================


Ressourcen
----------

* W5200 Datenblatt (`Download <https://github.com/Tinkerforge/ethernet-extension/raw/master/datasheets/W5200.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ethernet-extension/raw/master/hardware/ethernet-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ethernet_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ethernet-extension>`__)

.. _ethernet_configuration:

Ethernet Konfiguration
^^^^^^^^^^^^^^^^^^^^^^

Die Ethernet Extension kann in zwei Modi konfiguriert werden: DHCP oder 
statische IP. Nur im statische IP Modus sind **IP**, **Subnet Mask** und 
**Gateway** einzutragen.

Die MAC Adresse der Ethernet Extension ist nicht fest und wird von uns 
vergeben. Sollte diese aus irgendeinem Grund verloren gehen, so ist sie dem 
Aufkleber auf der Ethernet Extension zu entnehmen.

Nach Abschluss der Konfiguration sollte der Button "Save Ethernet Configuration"
geklickt werden und der Master Brick neu gestartet werden.

.. image:: /Images/Extensions/extension_ethernet_brickv.jpg
   :scale: 100 %
   :alt: Ethernet Extension Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_ethernet_brickv.jpg

PoE Stromversorgung
^^^^^^^^^^^^^^^^^^^

Um einen Stapel aus Bricks und Bricklets über PoE zu versorgen
kann zum Beispiel ein PoE Injektor benutzt werden. Die Ethernet 
Extension versorgt dann den kompletten Stapel.
Aktives PoE wird über die grüne LED auf der Extension angezeigt.

Servos und (Schritt-) Motoren angeschlossen an DC-, Servo- oder Stepper Bricks
können nicht über PoE versorgt werden, da die PoE Spannung hierfür zu 
hoch wäre. 

Die Ethernet Extension kann zusammen mit einer Step-Down Power Supply betrieben
werden.

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interfaces>`.

