
:shoplink: ../../../shop/bricks/esp32-ethernet-brick.html

.. include:: ESP32_Ethernet_Brick.substitutions

.. _esp32_ethernet_brick:

ESP32 Ethernet Brick
====================

.. raw:: html

	{% tfgallery %}

	Bricks/brick_esp32_ethernet_tilted_[?|?].jpg              ESP32 Ethernet Brick
	Bricks/brick_esp32_ethernet_top_[?|?].jpg                 ESP32 Ethernet Brick
	Bricks/brick_esp32_ethernet_tilted2_[?|?].jpg             ESP32 Ethernet Brick
	Bricks/brick_esp32_ethernet_bottom_[?|?].jpg              ESP32 Ethernet Brick
	Bricks/brick_esp32_ethernet_tilted_back_[?|?].jpg         ESP32 Ethernet Brick
	Bricks/brick_esp32_ethernet_caption_[?|?].jpg             ESP32 Ethernet Brick
	Bricks/brick_esp32_ethernet_brickv_[100|].jpg             ESP32 Ethernet Brick in Brick Viewer

	{% tfgalleryend %}

Features
--------

* Anschlüsse für **sechs** 7-Pol Bricklets
* Ausführung von eigener Software direkt auf diesem Brick (**Standalone-Betrieb**)
* Nutzung des vorprogrammierten Bricks um Bricklets per **LAN/WLAN** zu steuern

.. _esp32_ethernet_brick_description:

Beschreibung
------------

Der ESP32 Ethernet Brick bietet **sechs** :ref:`Bricklet <primer_bricklets>`
Anschlüsse und ist mit einem leistungsstarken ESP32 Mikrocontroller
ausgestattet. Der ESP32 verfügt über zwei CPU Kerne (bis zu 240MHz), 16MB SPI
Flash, WLAN (802.11b/g/n) und Bluetooth (V4.2 BR/EDR, BLE).

Der Brick kann für zwei Anwendungsfälle eingesetzt werden:

Bei **Standalone**-Anwendungen kann auf dem Brick die eigene Software
geflasht und ausgeführt werden. Eine Steuerung von außen ist nicht notwendig.
Um auf die angeschlossenen Bricklets im eigenen Code zuzugreifen, wird
einfach die
:ref:`C/C++ API Bindings für Mikrocontroller <api_bindings_uc>` Bibliothek
eingebunden. Unterstützung für LAN/WLAN, Bluetooth und andere ESP32 Features
ist über die offiziellen Espressif ESP32 Plattform Bibliotheken gegeben.
Die eigene Software kann auf den Brick über den integrierten USB nach UART
Wandler geflasht werden oder per LAN/WLAN wenn eine entsprechende Firmware
eingesetzt wird.

Für Anwendungen bei denen das System von außen gesteuert werden soll, kann
der Brick ohne eigene Software eingesetzt werden. Der Brick wird mit einer
Standard-Firmware ausgeliefert. Über diese Firmware kann auf die
angeschlossenen Bricklets per LAN/WLAN zugegriffen werden. Die Firmware bietet
ein Webinterface um die Konfiguration von LAN und WLAN Schnittstelle vornehmen
zu können. Für das initiale Setup kann der **WLAN-Access-Point** des Bricks
genutzt werden. Nach der Konfiguration kann der Access-Point deaktiviert werden.

Eine zeitgleiche Nutzung von Standalone-Anwendungen und die zusätzliche externe
Steuerung über die High-Level-APIs von Tinkerforge ist möglich.
Dadurch sind Anwendungen möglich in denen auf einzelne Events sofort
reagiert wird (closed loop) während gleichzeitig eine Steuerung von
außen stattfindet (open loop).

Die Stromversorgung des Bricks erfolgt über seinen USB-C Stecker oder über eine
optionale :ref:`ESP32 Power Supply <esp32_power_supply>` über den GPIO Stecker des Bricks.

Technische Spezifikation
------------------------

=================================  ============================================================
Eigenschaft                        Wert
=================================  ============================================================
Stromversorgung                    Mittels USB-C Stecker, optional per ESP32 Power Supply Modul
Stromverbrauch (WLAN aktiviert)    925mW (185mA bei 5V)
Stromverbrauch (WLAN deaktiviert)  520mW (104mA bei 5V)
---------------------------------  ------------------------------------------------------------
---------------------------------  ------------------------------------------------------------
Bricklet-Anschlüsse                6 (7-pol)
ESP32 Variante                     ESP32WROOM32E mit 16MB Flash (ESP32WRM32E128PH)
LAN                                10BASE-T, 100BASE-TX (KSZ8091 Ethernet PHY)
WLAN                               802.11b/g/n (mit bis zu 150 Mbps)
Bluetooth                          V4.2 BR/EDR und Bluetooth LE
---------------------------------  ------------------------------------------------------------
---------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)            88 x 45 x 12mm (3,46 x 1,77 x 0,47")
Gewicht                            20g
=================================  ============================================================

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/esp32-ethernet-brick/raw/master/hardware/esp32-ethernet-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/esp32_ethernet_brick_dimensions.png>`__)
* Quelltexte (`Download <https://github.com/Tinkerforge/esp32-firmware/zipball/master>`__)
* Platinenlayout (`Download <https://github.com/Tinkerforge/esp32-ethernet-brick/zipball/master>`__)
* 3D Modell (`View online <https://a360.co/3iVsZUI>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/esp32_ethernet/esp32-ethernet.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/esp32_ethernet/esp32-ethernet.FCStd>`__)

.. _esp32_ethernet_brick_hardware:

Hardwarebeschreibung
--------------------

.. image:: /Images/Bricks/brick_esp32_ethernet_caption_600.jpg
   :scale: 100 %
   :alt: ESP32 Ethernet Brick Beschreibung
   :align: center
   :target: ../../_images/Bricks/brick_esp32_ethernet_caption_1000.jpg




.. _esp32_ethernet_brick_setup:

Ersteinrichtung
---------------

Zur Ersteinrichtung muss der ESP32 Ethernet Brick über den USB-C Anschluss
mit Strom versorgt werden. Sobald die blaue Status-LED langsam blinkt ist der
Brick betriebsbereit.

Die Kommunikation mit dem Brick erfolgt über LAN oder WLAN. LAN und WLAN können
auch gleichzeitig verwendet werden. Der USB Abschluss dient nur zur Stromversorgung
und um den Brick in den Auslieferungszustand zurückversetzen zu können.
Im Gegensatz zu anderen Bricks taucht ein ESP32 Ethernet Brick verbunden mit USB
nicht in einem zu localhost verbundenen Brick Viewer auf.

Für eine LAN-Verbindung mit automatischer IP-Adresskonfiguration (DHCP) genügt
es im einfachsten Fall ein LAN-Kabel einzustecken. Darauf hin sollte die orange
LED in der LAN-Buchse des Bricks zu blinken beginnen und der Brick unter
``http://[Hostname]`` (z.B. ``http://esp32-ABC``) im Browser erreichbar sein.
Der individuelle Hostname (z.B. ``esp32-ABC``) ist auf dem
WLAN-Zugangsdaten-Aufkleber auf der Rückseite des Bricks vermerkt.

.. image:: /Images/Bricks/brick_esp32_ethernet_label_200.jpg
   :scale: 100 %
   :alt: WLAN-Zugangsdaten-Aufkleber
   :align: center
   :target: ../../_images/Bricks/brick_esp32_ethernet_label_800.jpg

Für eine LAN-Verbindung mit statischer IP-Adresskonfiguration oder die
Verbindung zu einem bestehenden WLAN-Netzwerk muss zunächst eine Verbindung zum
Webinterface des Bricks hergestellt werden. Dies erfolgt über den im
Auslieferungszustand aktivierten WLAN-Access-Point des Bricks.

Die individuellen Zugangsdaten des Access-Points sind auf dem
WLAN-Zugangsdaten-Aufkleber auf der Rückseite des Bricks vermerkt. Der QR-Code des
Aufklebers kann mit dem Smartphone direkt gescannt werden, um automatisch eine
WLAN-Verbindung zum Brick herzustellen. Alternativ können SSID und Passphrase auch
von Hand auf dem Smartphone oder Laptop eingegeben werden.

Wenn die WLAN-Verbindung zum Access-Point des Bricks hergestellt ist, dann ist
das Webinterface unter ``http://10.0.0.1`` erreichbar. Eventuell muss auf dem
Smartphone dazu die mobile Datenverbindung deaktiviert werden.

Der auf Samsung Smartphones vorinstallierte Browser "Samsung Internet" scheint
Probleme mit WebSockets aufzuweisen, so dass in diesem Browser das Webinterface
nicht richtig funktioniert. In diesem Fall bitte einen anderen Browser, z.B.
Firefox oder Chrome, verwenden.

LAN-Verbindung konfigurieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Auf der Unterseite **Netzwerk > LAN-Verbindung** kann die LAN-Verbindung de/-aktiviert
und die Adresskonfiguration zwischen "automatisch (DHCP)" und "statisch" umgestellt
werden. Im Auslieferungszustand ist die LAN-Verbindung mit automatischer
Adresskonfiguration aktiviert.

Änderungen werden erst nach einem Druck auf den Speichern-Knopf und einem
Neustart des Bricks übernommen.

.. image:: /Images/Bricks/brick_esp32_ethernet_lan_config_de_450.png
   :scale: 100 %
   :alt: ESP32 Ethernet Brick LAN-Verbindung konfigurieren
   :align: center
   :target: ../../_images/Bricks/brick_esp32_ethernet_lan_config_de.png

WLAN-Verbindung konfigurieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Auf der Unterseite **Netzwerk > WLAN-Verbindung** kann die WLAN-Verbindung
konfiguriert werden. Im Auslieferungszustand ist die Verbindung zu einem bestehenden
WLAN-Netzwerk deaktiviert.

Um den Brick mit einem bestehenden Netzwerk zu verbinden muss die WLAN-Verbindung
aktiviert und die SSID und Passphrase des bestehenden Netzwerks angegeben werden.
Ein Druck auf den Netzwerksuche-Knopf öffnet nach einem kurzen Moment ein Menü
mit den gefundenen bestehenden Netzwerken, aus dem das gewünschte Netzwerk
ausgewählt werden kann.

Änderungen werden erst nach einem Druck auf den Speichern-Knopf und einem
Neustart des Bricks übernommen.

.. image:: /Images/Bricks/brick_esp32_ethernet_wifi_config_de_450.png
   :scale: 100 %
   :alt: ESP32 Ethernet Brick WLAN-Verbindung konfigurieren
   :align: center
   :target: ../../_images/Bricks/brick_esp32_ethernet_wifi_config_de.png

WLAN-Access-Point konfigurieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Auf der Unterseite **Netzwerk > WLAN-Access-Point** kann der WLAN-Access-Point
konfiguriert werden. Im Auslieferungszustand ist der Access-Point dauerhaft
aktiviert und verwendet die individuelle SSID und Passphrase, die auf dem
WLAN-Zugangsdaten-Aufkleber auf der Rückseite des Bricks vermerkt sind.

Der Access-Point kann als Fallback konfiguriert werden und ist dann nur aktiv,
falls weder LAN- noch WLAN-Verbindung bestehen.

Der Access-Point kann vollständig deaktiviert werden. Davon wird aber im
Normalfall abgeraten, da sonst bei einer fehlgeschlagenen Verbindung zu einem
anderen Netzwerk das Webinterface nicht mehr erreichbar ist. Die einzige
Möglichkeit das Webinterface dann wieder zu erreichen ist ein Zurücksetzen
auf den Auslieferungszustand.

Änderungen werden erst nach einem Druck auf den Speichern-Knopf und einem
Neustart des Bricks übernommen.

.. image:: /Images/Bricks/brick_esp32_ethernet_ap_config_de_450.png
   :scale: 100 %
   :alt: ESP32 Ethernet Brick WLAN-Access-Point konfigurieren
   :align: center
   :target: ../../_images/Bricks/brick_esp32_ethernet_ap_config_de.png

.. _esp32_ethernet_brick_test:

Erster Test
-----------

Um einen ESP32 Ethernet Brick testen zu können, muss :ref:`Brick Viewer <brickv>`
installiert werden. Brick Viewer kann sich mit dem ESP32 Ethernet Brick verbinden,
gibt Informationen über die angeschlossenen Bricklets aus und ermöglicht es
diese zu testen.

Im Brick Viewer muss vor dem Klick auf den Connect-Knopf die Host-Einstellung
von ``localhost`` auf den Hostname oder IP Adresse des ESP32 Ethernet Bricks
geändert werden. Der voreingestellte individuelle Hostname
(z.B. ``esp32-ABC``) ist auf dem WLAN-Zugangsdaten-Aufkleber auf der Rückseite
des Bricks vermerkt.

Nach dem Klick auf den Connect-Knopf sollte im Brick Viewer ein neuer Tab namens
"ESP32 Ethernet Brick" auftauchen. Wähle diesen Tab aus.

.. image:: /Images/Bricks/brick_esp32_ethernet_brickv.jpg
   :scale: 100 %
   :alt: ESP32 Ethernet Brick im Brick Viewer
   :align: center
   :target: ../../_images/Bricks/brick_esp32_ethernet_brickv.jpg

Im Brick Viewer stellt der ESP32 Ethernet Brick keine weitere Funktionalität
bereit, sondern dient nur dazu Zugriff auf die angeschlossenen Bricklets zu bieten.
Jegliche Einstellungen des Bricks werden über dessen Webinterface vorgenommen.

.. _esp32_ethernet_brick_firmware:

Firmware
--------

Für den ESP32 Ethernet Brick stehen verschiedenen Firmware-Optionen zur Verfügung:

* **Standard-Firmware**:
  Der ESP32 Ethernet Brick ist im Auslieferungszustand mit der
  `Standard-Firmware <https://github.com/Tinkerforge/esp32-firmware>`__
  geflasht. Diese ermöglicht es die Netzwerkkonfiguration über das Webinterface
  vorzunehmen und über die Netzwerkverbindung des Bricks ist der Zugriff auf
  angeschlossene Bricklets über :ref:`Brick Viewer <brickv>` und die
  :ref:`API Bindings <api_bindings>` möglich, ähnlich zu einem
  :ref:`Master Brick <master_brick>` mit :ref:`Ethernet <ethernet_extension>`
  oder :ref:`WIFI Master Extension 2.0 <wifi_v2_extension>`.
* **Erweiterung der Standard-Firmware**:
  Die Funktionalität und das Webinterface der Standard-Firmware sind aus Modulen
  zusammengesetzt. Dieses :ref:`Tutorial zur ESP32 Firmware <tutorial_esp32_firmware>`
  erklärt Schritt für Schritt wie die Standard-Firmware um ein eigenes Modul
  erweitert werden kann.
* **Eigene Firmware auf Basis der C/C++ Bindings für Mikrocontroller**:
  Die :ref:`C/C++ Bindings für Mikrocontroller <api_bindings_uc>` erlauben es von unterstützten
  Mikrocontrollern aus direkt mit Bricklets zu kommunizieren. Diese API Bindings
  können z.B. zusammen mit dem `Arduino ESP32 Projekt <https://docs.espressif.com/projects/arduino-esp32/>`__
  verwendet werden, um eine eigene Firmware für den ESP32 Ethernet Brick zu
  erstellen.
