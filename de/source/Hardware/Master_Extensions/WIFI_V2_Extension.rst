
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / WIFI Master Extension 2.0
:shoplink: ../../../shop/master-extensions/wifi-v2-master-extension.html

.. _wifi_v2_extension:

WIFI Master Extension 2.0
=========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Extensions/extension_wifi2_tilted_350.jpg",
	               "Extensions/extension_wifi2_tilted_800.jpg",
	               "WIFI Extension 2.0")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi2_w_master_100.jpg",
	             "Extensions/extension_wifi2_w_master_800.jpg",
	             "WIFI Extension 2.0 mit Master Brick im stack")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi2_tilted_bottom_100.jpg",
	             "Extensions/extension_wifi2_tilted_bottom_800.jpg",
	             "WIFI Extension 2.0")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi2_hand_100.jpg",
	             "Extensions/extension_wifi2_hand_800.jpg",
	             "WIFI Extension 2.0 in Hand")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi2_top_100.jpg",
	             "Extensions/extension_wifi2_top_800.jpg",
	             "WIFI Extension 2.0 Oberseite")
	}}
	{{
	    tfdocimg("Extensions/extension_wifi2_bottom_100.jpg",
	             "Extensions/extension_wifi2_bottom_800.jpg",
	             "WIFI Extension 2.0 Unterseite")
	}}
	{{
	    tfdocimg("Dimensions/wifi_extension_dimensions_100.png",
	             "Extensions/wifi_extension_dimensions_600.png",
	             "WIFI Extension 2.0 Umriss")
	}}
	{{ tfdocend() }}


Features
--------

* Steuerung von Bricks/Bricklets drahtlos über WLAN Netzwerk
* Arbeitet mit 802.11b/g/n
* Unterstützt WPA2-Verschlüsselung als Client und Access Point
* Unterstützt statische IP sowie DHCP als Client und Access Point
* Unterstützt Client and Access Point Modus gleichzeitig


Beschreibung
------------

Mit der WIFI Extension 2.0 können :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` drahtlos mittels
Smartphone, Tablet oder PC gesteuert werden.
Weitere Informationen zum Master Extension Konzept gibt es in der allgemeinen
:ref:`Beschreibung <primer_master_extensions>`.

..
 Die Extension unterstützt zwei Modi. Im Full Speed Modus ist der WLAN Transceiver permanent eingeschaltet.
 Eingehende Daten werden unverzüglich verarbeitet. Im Low Power Mode ist das Modul nicht permanent an,
 der Transceiver geht nach jeder Nachricht in den Schlafmodus.
 Dies führt zu einer drastisch reduzierten Leistungsaufnahme aber auch zu einem deutlich geringeren Datendurchsatz.

Da die Extension selbst die von der API generierten TCP/IP Pakete behandeln kann, ist es möglich direkt vom
Smartphone, Tablet oder (Embedded) PC zu steuern. Der :ref:`Brick Daemon <brickd>` ist dann nicht mehr notwendig.

Um die WIFI Extension zu nutzen ist ein :ref:`Master Brick <master_brick>` notwendig.
Der :ref:`RED Brick <red_brick>` wird zurzeit nicht unterstützt.
Wenn andere Bricks gesteuert werden sollen, so kann ein :ref:`Stapel <primer_stack>`
aus diesen gebaut werden
und auf den Master Brick gesteckt werden. Wenn Bricklets verwendet werden sollen,
so können diese einfach an der Master Brick oder andere Bricks im Stapel angeschlossen werden.
Aus der Programmierersicht ist dies absolut transparent, d.h. alle Bricks und Bricklets können
so genutzt werden als ob sie direkt per USB mit dem steuernden Gerät verbunden wären.

Der benutzte Master Brick sollte eine Firmware Version von 2.4.0 oder neuer besitzen um diese Extension nutzen zu können.

Die folgenden Kombinationen von Extensions in einem Stapel sind möglich.
Die Reihenfolge im Stapel ist dabei nicht relevant:

* WIFI 2.0 / RS485 Master


Technische Spezifikation
------------------------

===========================================  =============================================================================
Eigenschaft                                  Wert
===========================================  =============================================================================
Stromverbrauch                               80mA (Senden), TBDmA (im Schlafmodus)
-------------------------------------------  -----------------------------------------------------------------------------
-------------------------------------------  -----------------------------------------------------------------------------
Maximale Anzahl gleichzeitiger Verbindungen  10
Modi                                         Client, Access Point und Client/Access Point gleichzeitig
Tinkerforge Protokolle                       Volle Unterstützung (TCP/IP, Authentifizierung und WebSocktes)
-------------------------------------------  -----------------------------------------------------------------------------
-------------------------------------------  -----------------------------------------------------------------------------
RF Ausgangsstärke (typisch)                  bis zu 19.5dBm
Sicherheitsprotokolle                        WPA, WPA2
Unterstützte Standards                       IEEE 802.11 b/g/n, mit CCK, OFDM und MCS7 Modulation
-------------------------------------------  -----------------------------------------------------------------------------
-------------------------------------------  -----------------------------------------------------------------------------
Abmessungen (W x D x H)                      40 x 40 x 16mm  (1.57 x 1.57 x 0.63")
Gewicht                                      12g
===========================================  =============================================================================


Resourcen
---------

* ESP-WROOM-02 (`Homepage <https://espressif.com/en/products/hardware/esp-wroom-02/overview>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/wifi-v2-extension/raw/master/hardware/wifi-extension-schematic.pdf>`__)
* Umriss und Borhplan (`Download <../../_images/Dimensions/wifi_extension_dimensions.png>`__)
* Quelltext und Platinenlayout (`Download <https://github.com/Tinkerforge/wifi-v2-extension/zipball/master>`__)


WLAN Netzwerk
-------------

Die WIFI Extension 2.0 erlaubt es eine drahtlose Verbindung zu
einem Master Brick und allen angeschlossenen Bricks und Bricklets herzustellen.
Es ist kein Brick Deamon notwendig um diese Extension zu nutzen.

Um den Brick Viewer mit einem drahtlosen Aufbau zu verbinden muss
die IP Adresse und der konfigurierte Port im Setup Tab eingegeben werden.
Nach dem Klick auf "Connect" wird dann eine Verbindung zu der WIFI Extension
und nicht zu dem lokal laufenden Brick Daemon hergestellt.

.. image:: /Images/Extensions/extension_wifi_brickv.jpg
   :scale: 100 %
   :alt: Brick Viewer Konfigration für WIFI Extension 2.0
   :align: center
   :target: ../../_images/Extensions/extension_wifi_brickv.jpg

Für die eigene Anwendung muss im Quelltext der übergebene Host und Port
im ``connect`` Aufruf modifiziert werden, z.B.:

.. code-block:: python

 ipcon.connect("localhost", 4223)

muss nach

.. code-block:: python

 ipcon.connect("192.168.0.25", 4223)

geändert werden.


WLAN Konfiguration
------------------

Die WIFI Extension 2.0 kann über den Master Brick Tab des Brick Viewers
konfiguriert werden.

.. image:: /Images/Extensions/extension_wifi2_brickv_complete.jpg
   :scale: 100 %
   :alt: Kompletter Brickv Master Brick Tab
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_complete.jpg

.. _wifi_v2_extension_ports:

Ports
^^^^^

Die ersten Konfigurationsoptionen sind Port, WebSocket Port und Webseiten Port.
Diese Optionen haben die Standardwerte 4223, 4280 und 80. Falls notwendig können
die Ports geändert werden, im Normalfall ist eine Umstellung der Ports nicht
notwendig.

.. image:: /Images/Extensions/extension_wifi2_brickv_ports.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 Port Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_ports.jpg

PHY Modus
^^^^^^^^^

Die PHY Modi

* B,
* G und
* N

stehen zur Verfügung. PHY Modus N kann nicht genutzt werden falls der Access Point
aktiviert ist

.. image:: /Images/Extensions/extension_wifi2_brickv_phy_mode.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 PHY Modus Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_phy_mode.jpg

.. _wifi_v2_extension_authentication:

Authentifizierung
^^^^^^^^^^^^^^^^^

Die WIFI Extension 2.0 unterstützt Authentifizierung. Authentifizierung ist
standardmäßig deaktiviert. Um
Authentifizierung zu aktivieren muss das Häkchen bei "Use Authentication"
gesetzt und ein Authentifizierungsgeheimnis eingetragen werden. Das Geheimnis
kann maximal 64 ASCII Zeichen lang sein. Nachdem die Konfiguration gespeichert
und der Master Brick neugestartet wurde ist Authentifizierung aktiv.

.. image:: /Images/Extensions/extension_wifi2_brickv_authentication.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 Authentifizierung Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_brickv_wifi2_authentication.jpg

Bei aktivierter Authentifizierung muss jede TCP/IP Verbindung zur WIFI Extension zuerst nachweisen,
dass sie das Authentifizierungsgeheimnis kennt, bevor normale Kommunikation
stattfinden kann. Für mehr Informationen zur Authentifizierung siehe das
dazugehörige :ref:`Tutorial <tutorial_authentication>`.

Betriebsarten
^^^^^^^^^^^^^

Die WIFI Extension 2.0 kann als

* Client,
* Access Point oder
* beides gleichzeitig

agieren.

.. image:: /Images/Extensions/extension_wifi2_brickv_mode.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 phy mode configuration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_mode.jpg

Falls Client und Access Point Modus gleichzeitig verwendet werden, sind beide
Netzwerke komplett unabhängig voneinander. Der Client hat eine andere
MAC Adresse als der Access Point und es gibt keinerlei Routing zwischen
den beiden Netzwerken.

Die komplette Konfiguration (inklusive Client und Access Point Konfiguration)
wird durch einen Klick auf den "Save WIFI Configuration"-Knopf gespeichert.

Der aktuelle Status der WIFI Extension 2.0 kann über den "Show Status"-Knopf
abgerufen werden.

Client Mode Konfiguration
-------------------------

Im Client Mode kann ein Hostname mit bis zu 32 ASCII-Zeichen verwendet werden.

.. image:: /Images/Extensions/extension_wifi2_brickv_client_hostname.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 Client Hostname Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_client_hostname.jpg

Die IP kann per DHCP vergeben werden. Alternativ ist es auch möglich
eine statisch IP einzutragen. In letzterem Fall muss eine IP, eine Subnetzmaske
sowie ein Gateway angegeben werden.

.. image:: /Images/Extensions/extension_wifi2_brickv_client_ip.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 Client IP Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_client_ip.jpg

Die SSID des Access Points (zu dem der Client sich verbinden soll) kann
bis zu 32 ASCII-Zeichen lang sein.

.. image:: /Images/Extensions/extension_wifi2_brickv_client_ssid.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 Client SSID Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_client_ssid.jpg

Es ist möglich eine Verbindung zu einem offenen Netzwerk oder einem per
WPA/WPA2 verschlüsseltem Netzwerk herzustellen.

.. image:: /Images/Extensions/extension_wifi2_brickv_client_encryption.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 Client Verschlüsselung Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_client_encryption.jpg

Für verschlüsselte Netzwerke kann ein Passwort mit bis zu 64 ASCII-Zeichen
angegeben werden.

Falls die Verbindung auf einen bestimmten Access Point stattfinden soll,
kann die entsprechende BSSID eingetragen werde. Eine Angabe eine
selbst erstellten MAC Adresse ist auch möglich.

.. image:: /Images/Extensions/extension_wifi2_brickv_client_bssid_mac.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 Client BSSID und MAC Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_client_bssid_mac.jpg

Access Point Mode Konfiguration
-------------------------------

Im Access Point Modus kann entweder DHCP aktiviert werden (in diesem Fall
führt die WIFI Extension 2.0 einen DHCP Server aus) oder eine statische
IP genutzt werden.

Falls eine statische IP gewählt wird, muss sichergestellt werden dass der
Client passende IP, Subnetzmaske und Gateway wählt welche mit dem eingestellten
Netzwerk der WIFI Extension 2.0 kompatibel sind.

.. image:: /Images/Extensions/extension_wifi2_brickv_ap_ip.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 AP IP Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_ap_ip.jpg

Die SSID kann bis zu 32 ASCII-Zeichen lang sein.

.. image:: /Images/Extensions/extension_wifi2_brickv_ap_ssid.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 AP SSID Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_ap_ssid.jpg

Im Access Point Modus unterstützt die WIFI Extension 2.0 die
Verschlüsselungsprotokolle

* WPA PSK,
* WPA2 PSK und
* WPA/WPA2 PSK.

Es ist auch möglich ein Netzwerk ohne Verschlüsselung zu erstellen. Falls
Verschlüsselung aktiviert ist, kann ein Passwort mit bis zu 64
ASCII-Zeichen eingetragen werden.

.. image:: /Images/Extensions/extension_wifi2_brickv_ap_encryption.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 AP Verschlüsselung Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_ap_encryption.jpg

Zusätzlich kann der WLAN Kanal zwischen 1 und 13 eingestellt werden. Es ist auch
möglich die SSID zu verstecken sowie eine selbst erstellte MAC Adresse zu
nutzen.

.. image:: /Images/Extensions/extension_wifi2_brickv_ap_channel_hide_ssid_mac.jpg
   :scale: 100 %
   :alt: WIFI Extension 2.0 AP Channel, Hide SSID, und MAC Konfiguration
   :align: center
   :target: ../../_images/Extensions/extension_wifi2_brickv_ap_channel_hide_ssid_mac.jpg


Web Interface
-------------

Ab Firmware Version 2.0.1 bietet die Extension ein Web Interface zur Konfiguration
und Abfrage von Statusinformationen.

.. image:: /Images/Extensions/extension_wifi2_web_interface_status.jpg
  :scale: 100 %
  :alt: Statusansicht des Web Interface der WIFI Extension 2.0
  :align: center
  :target: ../../_images/Extensions/extension_wifi2_web_interface_status.jpg

Über die "Disable Web Interface" Checkbox Konfigurationsansicht kann das Web
Interface aktiviert und deaktiviert werden. Wenn das Web Interface deaktiviert
ist kann es über Brick Viewer wieder aktiviert werden. Bis einschließlich
Brick Viewer 2.3.6 muss zum Deaktivieren in das "Website Port" Feld eine 1
eingetragen werden. Zum Aktivieren des Web Interface muss ein Wert größer 1
eingetragen werden. ab Brick Viewer 2.3.7 steht hierzu eine eigene Checkbox
bereit, wie auch im Web Interface.

.. image:: /Images/Extensions/extension_wifi2_web_interface_settings.jpg
  :scale: 100 %
  :alt: Konfigurationsansicht des Web Interface der WIFI Extension 2.0
  :align: center
  :target: ../../_images/Extensions/extension_wifi2_web_interface_settings.jpg

Falls die Authentifizierung aktiviert ist, dann fragt das Web Interface das
Secret mit folgender Seite ab:

.. image:: /Images/Extensions/extension_wifi2_web_interface_authentication.jpg
  :scale: 100 %
  :alt: Authentication view of the web interface of WIFI Extension 2.0
  :align: center
  :target: ../../_images/Extensions/extension_wifi2_web_interface_authentication.jpg


.. TODO: German mesh documentation.

Mesh
----

.. image:: /Images/Extensions/extension_wifi2_mesh_example.jpg
  :scale: 100 %
  :alt: Example topology of mesh usage
  :align: center
  :target: ../../_images/Extensions/extension_wifi2_mesh_example.jpg

.. image:: /Images/Extensions/extension_wifi2_mesh_mode.jpg
  :scale: 100 %
  :alt: Example topology of mesh usage
  :align: center
  :target: ../../_images/Extensions/extension_wifi2_mesh_mode.jpg

.. image:: /Images/Extensions/extension_wifi2_mesh_router.jpg
  :scale: 100 %
  :alt: Example topology of mesh usage
  :align: center
  :target: ../../_images/Extensions/extension_wifi2_mesh_router.jpg

.. image:: /Images/Extensions/extension_wifi2_mesh_group.jpg
  :scale: 100 %
  :alt: Example topology of mesh usage
  :align: center
  :target: ../../_images/Extensions/extension_wifi2_mesh_group.jpg


LEDs
----

Die blaue LED ist permanent an, solange die WIFI Extension mit Strom versorgt wird.

Die grüne LED ist eine Status LED.

Im Client Mode blinkt sie schnell während die Verbindung zum Access Point aufgebaut wird.
Sie bleibt an sobald die Verbindung aufgebaut ist.

Im Access Point Mode blinkt die LED langsam so lange sich kein Client verbunden hat.

Falls beide Modi aktiviert sind, blinkt die LED zuerst schnell bis eine Verbindung zum
externen Access Point hergestellt wurde. Danach blinkt die LED langsam bis ein
externe Client sich zum Access Point der WIFI Extension 2.0 verbindet.

.. TODO: German mesh documentation related to LED status.


Programmierschnittstelle
------------------------

Siehe :ref:`Master Brick Dokumentation <master_brick_programming_interface>`.
