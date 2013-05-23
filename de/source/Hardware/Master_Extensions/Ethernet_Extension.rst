
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#master-extensions">Master Extensions</a> / Ethernet Extension
:shoplink: ../../../shop/master-extensions/ethernet-master-extension.html

.. _etherner_extension:

Ethernet Extension
==================

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
Stromversorgung ermöglicht eine Stromversorgung der angeschlossenen Module
nach Industriestandard IEEE 802.3af, so dass sowohl über kostengünstige PoE 
Injektoren als auch über high End PoE fähige Switche versorgt werden kann.

Da die Extension selbst die von der API generierten TCP/IP Pakete behandeln kann, 
ist es möglich direkt vom Smartphone, Tablet oder (Embedded) PC zu steuern. 
Der :ref:`Brick Daemon <brickd>` ist nicht mehr notwendig.

Um die Ethernet Extension zu nutzen ist ein :ref:`Master Brick <master_brick>` 
notwendig. Wenn andere Bricks gesteuert werden sollen, so kann ein Stapel aus 
diesen gebaut werden und auf der Master Brick gesteckt werden. Wenn Bricklets 
verwendet werden sollen, so können diese einfach an der Master Brick oder 
andere Bricks im Stapel angeschlossen werden. Aus der Programmierersicht ist 
dies absolut transparent, d.h. alle Bricks und Bricklets können so genutzt 
werden als ob sie direkt per USB mit dem steuernden Gerät verbunden wären.

Der benutzte Master Brick sollte eine Firmware Version von 2.1.0 oder neuer 
besitzen um diese Extension nutzen zu können.

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich. 
Die Reihenfolge im Stack ist dabei nicht relevant:

* Ethernet / RS485 Master
* Ethernet / Chibi


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    TBD
PoE 5V Stackversorgung            > 1A
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximale Baudrate                 2Mbit/s
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 16mm (1.57 x 1.57 x 0.63")
Gewicht                           TBD
================================  ============================================================


Ressourcen
----------

* W5200 Datenblatt (`Download <https://github.com/Tinkerforge/ethernet-extension/raw/master/datasheets/W5200.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ethernet-extension/raw/master/hardware/ethernet-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ethernet_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ethernet-extension>`__)


.. _ethernet_connectivity:

Anschlussmöglichkeit
--------------------

Das folgende Bild zeigt die verschiedenen Anschlussmöglichkeit der Ethernet Extension.


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

Um einen Stapel aus Bricks und Bricklets über die PoE zu versorgen
kann zum Beispiel ein kostengünstiger PoE Injektor benutzt werden. Die Ethernet 
Extension versorgt dann den Stapel, so dass alle Bricks und Bricklets benutzt 
werden können. Aktives PoE wird über die grüne LED auf der Extension angezeigt.

Servos und (Schritt-) Motoren angeschlossen an DC-, Servo- oder Stepper Bricks
können nicht über PoE versorgt werden, da die PoE Spannung hierfür zu 
hoch wäre. 

Die Ethernet Extension kann ohne weiteres zusammen mit einer Step-Down 
Powersupply betrieben werden.

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interfaces>`.

