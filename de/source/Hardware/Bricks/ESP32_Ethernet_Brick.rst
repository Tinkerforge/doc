
:DISABLED_shoplink: ../../../shop/bricks/esp32-ethernet-brick.html

.. include:: ESP32_Ethernet_Brick.substitutions


.. _esp32_ethernet_brick:

ESP32 Ethernet Brick
====================


.. raw:: html

	{% tfgallery %}

	Bricks/brick_esp32_ethernet_brickv_[100|].jpg     ESP32 Ethernet Brick im Brick Viewer

	{% tfgalleryend %}


Features
--------


.. _esp32_ethernet_brick_description:

Beschreibung
------------



Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Stromverbrauch                    TBDmW (TBDmA bei 5V)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Bricklet-Anschlüsse               6
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           88 x 45 x 12mm (3,46 x 1,77 x 0,47")
Gewicht                           TBDg
================================  ============================================================

Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/esp32-ethernet-brick/raw/master/hardware/esp32-ethernet-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/esp32_ethernet_brick_dimensions.png>`__)
* Quelltexte (`Download <https://github.com/Tinkerforge/esp32-firmware/zipball/master>`__)
* Platinenlayout (`Download <https://github.com/Tinkerforge/esp32-ethernet-brick/zipball/master>`__)
* 3D Modell (`View online <https://autode.sk/TBD>`__ | Download: `STEP <https://download.tinkerforge.com/3d/bricks/esp32_ethernet/esp32-ethernet.step>`__, `FreeCAD <https://download.tinkerforge.com/3d/bricks/esp32_ethernet/esp32-ethernet.FCStd>`__)


.. _esp32_ethernet_brick_setup:

Ersteinrichtung
---------------

Der ESP32 Ethernet Brick muss über den USB Abschluss mit Strom versorgt werden.
Sobald die blaue Status-LED langsam blinkt ist der Brick betriebsbereit.

Die Kommunikation mit dem Brick erfolgt über LAN oder WLAN. LAN und WLAN können
auch gleichzeitig verwendet werden. Der USB Abschluss dient nur zur Stromversorgung
und um den Brick in den Auslieferungszustand zurückversetzen zu können.

Für eine LAN-Verbindung mit automatischer Adresskonfiguration (DHCP) genügt
es im einfachsten Fall ein LAN-Kabel einzustecken. Darauf hin sollte die orange
LED in der LAN-Buchse des Bricks zu blinken beginnen und der Brick unter
``http://[Hostname]`` (z.B. ``http://esp32-ABC``) im Browser erreichbar sein.
Der individuelle Hostname (z.B. ``esp32-ABC``) ist auf dem
WLAN-Zugangsdaten-Aufkleber auf der Rückseite des Bricks vermerkt.

.. image:: /Images/Bricks/brick_esp32_ethernet_label_350.jpg
   :scale: 100 %
   :alt: WLAN-Zugangsdaten-Aufkleber
   :align: center
   :target: ../../_images/Bricks/brick_esp32_ethernet_label_800.jpg

Für eine LAN-Verbindung mit statischer Adresskonfiguration oder die
Verbindung zu einem bestehenden WLAN-Netzwerk muss zunächst eine Verbindung zum
Webinterface des Bricks hergestellt werden. Dies erfolgt über den im
Auslieferungszustand aktivierten WLAN-Access-Point des Bricks.

Die individuellen Zugangsdaten des Access-Points sind auf dem
WLAN-Zugangsdaten-Aufkleber auf der Rückseite des Bricks vermerkt. Der QR-Code des
Aufklebers kann mit dem Smartphone direkt gescannt werden, um automatisch eine
WLAN-Verbindung zum Brick herzustellen. Alternative können SSID und Passphrase auch
von Hand auf dem Smartphone oder Laptop eingegeben werden.

Wenn die WLAN-Verbindung zum Access-Point des Bricks hergestellt ist, dann ist
das Webinterface unter ``http://10.0.0.1`` erreichbar. Eventuell muss auf dem
Smartphone dazu die mobile Datenverbindung deaktiviert werden.

Der auf Samsung Smartphones vorinstallierte Browser *Samsung Internet* scheint
Probleme mit WebSockets aufzuweisen, so dass in diesem Browser das Webinterface
nicht richtig funktioniert. In diesem Fall bitte einen anderen Browser, z.B.
Firefox oder Chrome, verwenden.

LAN-Verbindung konfigurieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Auf der Unterseite **Netzwerk > LAN-Verbindung** kann die LAN-Verbindung de/-aktiviert
und die Adresskonfiguration zwischen *automatisch (DHCP)* und *statisch* umgestellt
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

Falls eine Verbindung zu einem versteckten WLAN-Netzwerk hergestellt werden soll,
dann muss die entsprechend SSID von Hand eingegeben werden, nachdem das versteckte
Netzwerk aus dem Menü ausgewählt wurde.

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
von ``localhost`` auf den Hostname des ESP32 Ethernet Bricks geändert werden.
Der voreingestellte individuelle Hostname (z.B. ``esp32-ABC``) ist auf dem
WLAN-Zugangsdaten-Aufkleber auf der Rückseite des Bricks vermerkt.

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
* **Erweiterung der Standard-Firmware:**:
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
