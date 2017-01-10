
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Ethernet Master Extension
:shoplink: ../../../shop/master-extensions/ethernet-master-extension.html

.. _ethernet_extension:

Ethernet Master Extension
=========================

.. raw:: html

	{% tfgallery %}

	Extensions/extension_ethernet11_w_and_wo_poe_[100|800].jpg  Ethernet Extension mit und ohne PoE
	Extensions/extension_ethernet11_w_poe_tilted_[?|?].jpg      Ethernet Extension mit PoE
	Extensions/extension_ethernet11_wo_poe_tilted_[?|?].jpg     Ethernet Extension ohne PoE
	Extensions/extension_ethernet11_w_poe_stack_[?|?].jpg       Ethernet Extension mit PoE auf Master Brick
	Extensions/extension_ethernet11_wo_poe_stack_[?|?].jpg      Ethernet Extension ohne PoE auf Master Brick
	Extensions/extension_ethernet11_w_poe_top_[?|?].jpg         Ethernet Extension mit PoE Oberseite
	Extensions/extension_ethernet11_wo_poe_top_[?|?].jpg        Ethernet Extension ohne PoE Oberseite
	Extensions/extension_ethernet11_w_poe_bottom_[?|?].jpg      Ethernet Extension mit PoE Unterseite
	Extensions/extension_ethernet11_wo_poe_bottom_[?|?].jpg     Ethernet Extension ohne PoE Unterseite

	{% tfgalleryend %}


Features
--------

* Kommuniziere direkt mit Bricks/Bricklet ohne Brickd
* Unterstützt 10/100 Mbit/s Ethernet (1000 Mbit/s kompatibel)
* Integrierte PoE Stromversorgung (PD Class 0 für IEEE 802.3af)

  * Ermöglicht die Stromversorgung eines Stapels per Ethernetkabel



Beschreibung
------------

Mit dieser Ethernet Extension können :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` in ein 
`LAN <https://de.wikipedia.org/wiki/Local_Area_Network>`__ integriert 
werden. 10BaseT/100BaseTX Ethernet wird unterstützt und das Modul ist 
1000BaseTX kompatibel. Die Extension wird in zwei Varianten angeboten:
In der PoE Variante verfügt diese über eine integrierte 
`PoE <https://de.wikipedia.org/wiki/Power_over_Ethernet>`__
Stromversorgung, die eine Versorgung der angeschlossenen Module
nach Industriestandard IEEE 802.3af ermöglicht, so dass sowohl über PoE 
Injektoren als auch über PoE fähige Switche versorgt werden kann.
Zusätzlich ist eine zweite Variante ohne PoE erhältlich.

Da die Extension selbst die von der API generierten TCP/IP Pakete behandeln kann, 
ist es möglich direkt vom Smartphone, Tablet oder (Embedded) PC zu steuern. 
Der :ref:`Brick Daemon <brickd>` ist nicht mehr notwendig.

Die Ethernet Extension kann zusammen mit einem :ref:`Master Brick <master_brick>` 
oder einem :ref:`RED Brick <red_brick>` genutzt werden. 
Wenn andere Bricks gesteuert werden sollen, so kann ein 
:ref:`Stapel <primer_stack>` aus diesen gebaut werden und auf den Master Brick 
bzw. RED Brick gesteckt werden. Wenn Bricklets verwendet werden sollen, 
so können diese einfach an einen beliebigen Brick im Stapel angeschlossen werden 
(Mit Ausnahme des RED Bricks).

Aus Programmierersicht ist die Nutzung einer Ethernet Extension absolut transparent, 
d.h. alle Bricks und Bricklets können so genutzt werden als ob sie direkt per USB 
mit dem steuernden Gerät verbunden wären.

Der benutzte Master Brick muss eine Firmware Version von 2.1.0 oder neuer 
besitzen um diese Extension nutzen zu können.

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich. 
Die Reihenfolge im Stapel ist dabei nicht relevant:

* Ethernet / RS485 Master


Technische Spezifikation
------------------------

============================================  ============================================================
Eigenschaft                                   Wert
============================================  ============================================================
Stromverbrauch                                100mA (Durchschnitt), 175mA (Maximum)
PoE 5V Stapelversorgung                       > 1A
--------------------------------------------  ------------------------------------------------------------
--------------------------------------------  ------------------------------------------------------------
Ethernet Unterstützung                        10BaseT/100BaseTX, 1000BaseTX kompatible
Maximale Anzahl gleichzeitiger Verbindungen   7
--------------------------------------------  ------------------------------------------------------------
--------------------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)                       40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                                       22g
============================================  ============================================================


Ressourcen
----------

* W5200 Datenblatt (`Download <https://github.com/Tinkerforge/ethernet-extension/raw/master/datasheets/W5200.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ethernet-extension/raw/master/hardware/ethernet-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ethernet_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ethernet-extension>`__)


.. _ethernet_extension_configuration:

Ethernet Konfiguration
----------------------

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

.. _ethernet_extension_websockets:

WebSockets
^^^^^^^^^^

Die Ethernet Extension unterstützt seit Master Brick Firmware Version 2.2.0
`WebSockets <https://de.wikipedia.org/wiki/WebSocket>`__. Die "Max Connections"
Einstellung erlaubt die sieben Sockets der Ethernet Extension nach belieben
zwischen normalen und WebSocket-Verbindungen aufzuteilen.

WebSockets werden von der Browser-Version der :ref:`JavaScript Bindings
<api_bindings_javascript>` verwendet um Bricks und Bricklets zu steuern.


.. _ethernet_extension_authentication:

Authentifizierung
^^^^^^^^^^^^^^^^^

Die Ethernet Extension unterstützt seit Master Brick Firmware Version 2.2.0
Authentifizierung. Diese ist standardmäßig deaktiviert. Um
Authentifizierung zu aktivieren muss das Häkchen bei "Use Authentication"
gesetzt und ein Authentifizierungsgeheimnis eingetragen werden. Das Geheimnis
kann maximal 64 ASCII Zeichen lang sein. Nachdem die Konfiguration gespeichert
und der Master Brick neugestartet wurde ist Authentifizierung aktiv.

Ab jetzt muss jede TCP/IP Verbindung zur Ethernet Extension zuerst nachweisen,
dass sie das Authentifizierungsgeheimnis kennt, bevor normale Kommunikation
stattfinden kann. Für mehr Informationen zur Authentifizierung siehe das
dazugehörige :ref:`Tutorial <tutorial_authentication>`.


PoE Stromversorgung
-------------------

Um einen Stapel aus Bricks und Bricklets über PoE zu versorgen
kann zum Beispiel ein PoE Injektor benutzt werden. Die Ethernet 
Extension versorgt dann den kompletten Stapel.
Aktives PoE wird über die grüne LED auf der Extension angezeigt.

Servos und (Schritt-) Motoren angeschlossen an DC-, Servo- oder Stepper Bricks
können nicht über PoE versorgt werden, da die PoE Spannung hierfür zu 
hoch wäre. 

Die Ethernet Extension kann zusammen mit einer Step-Down Power Supply betrieben
werden.


Programmierschnittstelle
------------------------

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interface>`.
