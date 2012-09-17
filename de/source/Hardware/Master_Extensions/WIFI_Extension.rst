.. _wifi_extension:

WIFI Extension
==============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Extensions/extension_wifi_tilted_350.jpg",
	               "Extensions/extension_wifi_tilted_600.jpg",
	               "WIFI Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_stack_100.jpg",
	             "Extensions/extension_wifi_stack_600.jpg",
	             "WIFI Extension mit Master Brick im Stapel")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_horizontal_100.jpg",
	             "Extensions/extension_wifi_horizontal_600.jpg",
	             "WIFI Extension Unterseite")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_bottom_100.jpg",
	             "Extensions/extension_wifi_bottom_600.jpg",
	             "WIFI Extension Oberseite")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_caption_100.jpg",
	             "Extensions/extension_wifi_caption_600.jpg",
	             "WIFI Extension mit Beschriftung")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_ufl_100.jpg",
	             "Extensions/extension_wifi_ufl_600.jpg",
	             "U.FL Connector der WIFI Extension")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi_front_100.jpg",
	             "Extensions/extension_wifi_front_600.jpg",
	             "WIFI Extension Vorderseite")
	}}
	{{ tfdocend() }}


Features
--------

* Steuere Bricks/Bricklets drahtlos über dein Smartphone oder Tablet
* Arbeitet mit 802.11b/g/n Access Points, WEP, WPA, WPA2 Personal und Enterprise Verschlüsselung
* Ausgestattet mit einem 18dBm Verstärker für große Reichweite
* Externer RP-SMA und U.FL Antennenanschluss


Beschreibung
------------

Mit dieser WIFI Extension können :ref:`Bricks <product_overview_bricks>` und
:ref:`Bricklets <product_overview_bricklets>` drahtlos mittels
Smartphone, Tablet oder PC gesteuert werden.
Weitere Informationen zum Master Extension Konzept gibt es in der allgemeinen
:ref:`Beschreibung <product_overview_master_extensions>`. Die Extension ist mit einem `GainSpan <http://www.gainspan.com>`__
`GS1011MEES <http://www.gainspan.com/gs1011mees>`__ WIFI Modul mit integriertem Leistungsverstärker ausgestattet
der eine erweiterte Reichweite im Vergleich zu ähnlichen Modulen erlaubt.

Die Extension unterstützt zwei Modi. Im Full Speed Modus ist der WIFI Transceiver permanent eingeschaltet.
Eingehende Daten werden unverzüglich verarbeitet. Im Low Power Mode ist das Modul nicht permanent an,
der Transceiver geht nach jeder Nachricht in den Schlafmodus.
Dies führt zu einer drastisch reduzierten Leistungsaufnahme aber auch zu einem deutlich geringeren Datendurchsatz.

Da die Extension selbst die von der API generierten TCP/IP Pakete behandeln kann, ist es möglich direkt vom
Smartphone, Tablet oder (Embedded) PC zu steuern. Der :ref:`Brick Daemon <brickd>` ist nicht mehr notwendig.

Um die WIFI Extension zu nutzen ist ein :ref:`Master Brick <master_brick>` notwendig.
Wenn andere Bricks gesteuert werden sollen, so kann ein Stapel aus diesen gebaut werden
und auf das Master Brick gesteckt werden. Wenn Bricklets verwendet werden sollen,
so können diese einfach an das Master Brick oder andere Bricks im Stapel angeschlossen werden.
Aus der Programmierersicht ist dies absolut transparent, d.h. alle Bricks und Bricklets können
so genutzt werden als ob sie direkt per USB mit dem steuernden Gerät verbunden wären.

Das benutzte Master Brick sollte eine Firmware Version von 1.3.0 oder neuer besitzen um diese Extension nutzen zu können.


Technische Spezifikation
------------------------

================================  =============================================================================
Eigenschaft                       Wert
================================  =============================================================================
Stromverbrauch                    110mA (Senden), 23mA (im Schlafmodus)
--------------------------------  -----------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------
Maximale Reichweite (Freifeld)    TBD
Maximaler Datendurchsatz          TBD
--------------------------------  -----------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------
RF Ausgangsstärke (Typisch)       18dBm
Externer Antennenanschluss        RP-SMA Female (mit Pin) und U.FL
Sicherheit                        WEP, WPA, WPA2 (Personal und Enterprise), EAP-FAST, EAP-TLS, EAP-TTLS, PEAP
Max. Anzahl Verbindungen          15
--------------------------------  -----------------------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------------------
Abmessungen (B x T x H)           40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Gewicht                           18g
================================  =============================================================================


Resourcen
---------

* GS1011MEES Homepage (`here <http://www.gainspan.com/gs1011mees>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/wifi-extension/raw/master/hardware/wifi-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/wifi_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/wifi-extension/zipball/master>`__)

.. _wifi_network_assembly:

WIFI Netzwerk
-------------

Die Master Extension erlaubt es eine drahtlose Verbindung zu
einem Master Brick uns allen angeschlossenen Bricks und Bricklets herzustellen.
Es ist kein Brick Deamon notwendig um diese Extension zu nutzen.

Um den Brick Viewer mit einem drahtlosen Aufbau zu verbinden muss
die IP Adresse und der konfigurierte Port in dem Setup Tab eingegeben werden.
Nach dem Klick auf "Connect" wird dann eine Verbindung zu der WIFI Extension
und nicht zu dem lokal laufenden Brick Daemon hergestellt.

.. image:: /Images/Extensions/extension_wifi_brickv.jpg
   :scale: 100 %
   :alt: Brick Viewer Konfigration für WIFI Extension
   :align: center
   :target: ../../_images/Extensions/extension_wifi_brickv.jpg

Für die eigene Anwendung muss im Quelltext der übergebene Host und Port
im IPConnection Aufruf modifiziert werden, z.B.:

.. code-block:: python

 ipcon = IPConnection("localhost", 4223)

muss nach

.. code-block:: python

 ipcon = IPConnection("192.168.0.25", 4223)

geändert werden.


.. _wifi_configuration:

WIFI Konfiguration
------------------

.. note::

 Adhoc Modus wird noch nicht unterstützt.


Die WIFI Extension wird über das Tab des Master Bricks im Brick Viewer konfiguriert.
Als erstes muss die SSID des drahtlosen Netzes eingegeben werden und ob
DHCP oder eine statische IP genutzt werden soll.

Für den Fall, dass DHCP genutzt werden soll muss einfach DHCP ausgewählt werden
und der Port definiert werden.

.. image:: /Images/Extensions/extension_wifi_connection_dhcp.jpg
   :scale: 100 %
   :alt: Konfiguriere die Verbindung mit DHCP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_dhcp.jpg

Wenn eine statische IP Adresse genutzt werden soll muss diese zusammen mit
der Subnet Mask und Gateway Adresse konfiguriert werden.
Zusätzlich ist auch der Port über den Kommuniziert werden soll zu konfigurieren.

.. image:: /Images/Extensions/extension_wifi_connection_static.jpg
   :scale: 100 %
   :alt: Konfiguriere die Verbindung mit statischer IP
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_static.jpg

Wir empfehlen ein verschlüsseltes Netzwerk zu nutzen.
WPA/WPA2, WPA Enterprise (EAP-FAST, EAP-TLS, EAP-TTLS, PEAP) und WEP
sind verfügbar.

Um WPA zu nutzen muss nur der Schlüssel in Hex-Notation eingegeben werden.

.. image:: /Images/Extensions/extension_wifi_encryption_wpa.jpg
   :scale: 100 %
   :alt: Konfiguriere WPA Verschlüsselung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wpa.jpg

Für WPA Enterprise muss die äußere Authentifizierung 
(FAST, TLS, TTLS, PEAP), die innere (MSCHAP, GTC), Benutzer und Passwort
konfiguriert werden sowie die notwendigen Zertifikate (ca cert, client cert, private key)
hinzugefügt werden.

.. image:: /Images/Extensions/extension_wifi_encryption_wpa_enterprise.jpg
   :scale: 100 %
   :alt: Konfiguriere WPA Enterprise Verschlüsselung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wpa_enterprise.jpg

Um WEP zu benutzen muss ein Schlüssel und ein Schlüssel Index eingegeben werden.
Ist kein Index bekannt so ist dieser vermutlich 1.
Der Schlüssel ist in Hex-Notation einzutragen mit voller Schlüssellänge (abhängig von 64bit und 128bit Schlüssel).

.. image:: /Images/Extensions/extension_wifi_encryption_wep.jpg
   :scale: 100 %
   :alt: Konfiguriere WEP Verschlüsselung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wep.jpg

Soll keine Verschlüsselung genutzt werden muss "No Encryption" gewählt werden. 

Zum Schluss muss der Power Mode konfiguriert werden. Es gibt zwei Modis:
Full Speed und Low Power. Im Full Speed Modus verbraucht die Extension mehr Leistung
besitzt aber einen deutlich höheren Datendurchsatz. Dies ist für die meisten Anwendungen
die typische Konfiguration. Müssen nur ein paar Nachrichten pro Sekunden transferiert werden,
z.B. bei der drahtlosen Temperaturmessung, so kann auch der Low Power Mode gewählt 
und Energie gespart werden.

.. image:: /Images/Extensions/extension_wifi_power_mode.jpg
   :scale: 100 %
   :alt: Konfiguriere Power Mode
   :align: center
   :target: ../../_images/Extensions/extension_wifi_power_mode.jpg

Zum Schluss muss auf "Save WIFI Configuration" geklickt werden um die Konfiguration zu speichern
und das Master Brick neu gestartet werden um die Konfiguration zu laden. Nach dem Neustart
sollte das Master Brick bei Eingabe der konfigurierten IP Adresse und Port im Brick Viewer erreichbar sein.


.. _extension_wifi_leds:

LEDs und Anschlussmöglichkeiten
-------------------------------

.. image:: /Images/Extensions/extension_wifi_caption_600.jpg
   :scale: 100 %
   :alt: WIFI Extension mit Beschriftung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_caption_800.jpg

Die blaue LED leuchtet permanent wenn die Extension mit Strom versorgt wird.
Als Status LED ist eine grüne LED vorhanden (permanent aus = Fehler, blinkend = Verbindungsaufbau, permanent an = Verbunden).

Das WIFI Modul ist mit einem U.FL Anschluss und einem 75 Ohm U.FL nach RP-SMA Kabel ausgestattet.
Abhängig von der Anwendung kann dieses Kabel auch vom WIFI Modul getrennt und ein eigenes
angeschlossen werden.
