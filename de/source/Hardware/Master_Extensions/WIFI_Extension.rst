
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#master-extensions">Master Extensions</a> / WIFI Extension
:shoplink: ../../../shop/master-extensions/wifi-master-extension.html

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

* Steuere Bricks/Bricklets drahtlos über Smartphone oder Tablet
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
und auf der Master Brick gesteckt werden. Wenn Bricklets verwendet werden sollen,
so können diese einfach an der Master Brick oder andere Bricks im Stapel angeschlossen werden.
Aus der Programmierersicht ist dies absolut transparent, d.h. alle Bricks und Bricklets können
so genutzt werden als ob sie direkt per USB mit dem steuernden Gerät verbunden wären.

Der benutzte Master Brick sollte eine Firmware Version von 1.3.0 oder neuer besitzen um diese Extension nutzen zu können.

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich:

* WIFI oben / RS485 Master unten
* WIFI unten / RS485 Master oben

Technische Spezifikation
------------------------

============================================  =============================================================================
Eigenschaft                                   Wert
============================================  =============================================================================
Stromverbrauch                                110mA (Senden), 23mA (im Schlafmodus)
--------------------------------------------  -----------------------------------------------------------------------------
--------------------------------------------  -----------------------------------------------------------------------------
Maximale Reichweite (Freifeld)                TBD
Maximaler Datendurchsatz                      TBD
Maximale Anzahl gleichzeitiger Verbindungen   15
--------------------------------------------  -----------------------------------------------------------------------------
--------------------------------------------  -----------------------------------------------------------------------------
RF Ausgangsstärke (Typisch)                   18dBm
Externer Antennenanschluss                    RP-SMA Female (mit Pin) und U.FL
Sicherheitsprotokolle                         WEP, WPA, WPA2 (Personal und Enterprise), EAP-FAST, EAP-TLS, EAP-TTLS, PEAP
--------------------------------------------  -----------------------------------------------------------------------------
--------------------------------------------  -----------------------------------------------------------------------------
Abmessungen (B x T x H)                       40 x 40 x 16mm (1,57 x 1,57 x 0,63")
Gewicht                                       18g
============================================  =============================================================================


Ressourcen
----------

* GS1011MEES Homepage (`here <http://www.gainspan.com/gs1011mees>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/wifi-extension/raw/master/hardware/wifi-extension-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/wifi_extension_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/wifi-extension/zipball/master>`__)

.. _wifi_network_assembly:

WIFI Netzwerk
-------------

Die Master Extension erlaubt es eine drahtlose Verbindung zu
einem Master Brick und allen angeschlossenen Bricks und Bricklets herzustellen.
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

 ipcon.connect("localhost", 4223)

muss nach

.. code-block:: python

 ipcon.connect("192.168.0.25", 4223)

geändert werden.


.. _wifi_configuration:

WIFI Konfiguration
------------------

Die WIFI Extension wird über das Tab des Master Bricks im Brick Viewer konfiguriert.
Als erstes muss die SSID (eingeschränkt auf ASCII Zeichen, ohne das
Anführungszeichen) des drahtlosen Netzes
eingegeben werden und ob DHCP oder eine statische IP genutzt werden soll.

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

Um WPA zu nutzen muss nur der Schlüssel (eingeschränkt auf ASCII Zeichen, ohne
das Anführungszeichen) eingegeben werden.

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
Der Schlüssel ist hierbei in Hex-Notation einzutragen mit voller Schlüssellänge (abhängig von 64bit und 128bit Schlüssel).

.. image:: /Images/Extensions/extension_wifi_encryption_wep.jpg
   :scale: 100 %
   :alt: Konfiguriere WEP Verschlüsselung
   :align: center
   :target: ../../_images/Extensions/extension_wifi_encryption_wep.jpg

Soll keine Verschlüsselung genutzt werden muss "No Encryption" gewählt werden. 

Nun kann noch der Power Mode konfiguriert werden. Es gibt zwei Modi:
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

.. note::
 Der Power Mode wird nicht permanent gespeichert, er wird beim Neustart des Master Bricks automatisch
 auf Full Speed zurückgestellt. Dies ist notwendig, da der Low Power Mode nicht
 schnell genug ist für die initiale Enumerierung nach einem Neustart. Daher muss
 der Low Power Mode nach jedem Neustart neu eingestellt werden.

Zum Schluss muss auf "Save WIFI Configuration" geklickt werden um die Konfiguration
dauerhaft auf der WIFI Extension zu speichern.
Falls andere Einstellungen als der Power Mode geändert wurden muss der Master Brick
neu gestartet werden um die neue Konfiguration zu übernehmen. Nach dem Neustart
sollte der Master Brick bei Eingabe der konfigurierten IP Adresse und Port im Brick Viewer erreichbar sein.


.. _extension_wifi_adhoc_ap:

Access Point Modus und Ad Hoc Modus
-----------------------------------

.. note::
 Access Point und Ad Hoc Modus stehen ab Master Brick Firmware
 Version 1.3.3 und Brick Viewer Version 1.1.8 zur Verfügung.

Es ist möglich direkt mit der WIFI Extension zu kommunizieren, ohne einen
zusätzlichen externen Access Point. Um dies zu ermöglichen wurde ein
Access Point und ein Ad Hoc Modus implementiert. Da der Ad Hoc Modus
vom sich verbindenden Gerät spezifisch unterstützt werden muss,
empfehlen wir die Verwendung des Access Point Modus. Im AP Modus
simuliert die WIFI Extension einen Access Point und sie sollte
als ganz normaler Access Point auf dem PC angezeigt werden.

.. image:: /Images/Extensions/extension_wifi_connection_adhoc_ap.jpg
   :scale: 100 %
   :alt: Konfiguration von Ad Hoc und Access Point Modus
   :align: center
   :target: ../../_images/Extensions/extension_wifi_connection_adhoc_ap.jpg

Es ist möglich bei beiden Modi zwischen DHCP und statischer IP auszuwählen.
Falls DHCP ausgewählt wird, muss der DHCP Server von außen bereitgestellt werden!
Es gibt keine DHCP Server Implementierung auf dem WIFI Modul. Da das aufsetzen
eines DHCP Servers mühselig sein kann, empfehlen wir die Benutzung einer
statischen IP.

Als Verschlüsselung steht WEP zur Verfügung. WPA wird 
im Ad Hoc und Access Point Modus leider nicht unterstützt. Der WEP Schlüssel
sollte 64 oder 128 Bit groß sein und in Hexadezimaler Schreibweise angegeben
sein. Gültige WEP Schlüssel können 
`hier <http://www.andrewscompanies.com/tools/wep.asp>`__ generiert werden.

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

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interfaces>`.

