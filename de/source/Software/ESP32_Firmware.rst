
.. _esp32_firmware:

ESP32 Firmware
==============

Die ESP32 Firmware kann in mehreren Varianten für verschiedenen Geräte gebaut werden:

* :ref:`ESP32 Brick <esp32_brick>`
* :ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>`
* `WARP Charger <https://www.warp-charger.com/index_warp1.html>`__ Smart und Pro
* `WARP2 Charger <https://www.warp-charger.com/>`__ Smart und Pro

..
 * WARP Energy Manager, TODO: Link zur Dokumentation hinzufügen

Die Firmware ist in C/C++ programmiert und der Quelltext ist frei auf
`GitHub <https://github.com/Tinkerforge/esp32-firmware>`__ verfügbar.
Als Basis dienen das `Arduino ESP32 Projekt <https://docs.espressif.com/projects/arduino-esp32/>`__
und PlatformIO.

.. _esp32_firmware_setup:

Vorbereitung
------------

Zuerst müssen `PlatformIO <https://platformio.org/>`__ und
`Node.js <https://nodejs.org/>`__ anhand der Anleitung des jeweiligen
Projekts installiert werden.
Für PlatformIO empfehlen wir die PlatformIO IDE Erweiterung für
`Visual Studio Code <https://code.visualstudio.com/>`__ zu verwenden.

Dann das `esp32-firmware <https://github.com/Tinkerforge/esp32-firmware>`__
Repository von GitHub als
`ZIP Datei <https://github.com/Tinkerforge/esp32-firmware/archive/refs/heads/master.zip>`__
herunterladen und entpacken oder mittels `git <https://www.git-scm.com/>`__ clonen.

Die ``platformio.ini`` Datei befindet sich im ``software/`` Unterverzeichnis.
Dieses Verzeichnis in Visual Studio Code öffnen und die ``prepare`` Umgebung
bauen, um das Bauen der anderen Umgebungen vorzubereiten.

.. _esp32_firmware_build:

Firmware bauen
--------------

Abhängig von der zu bauenden Variante der Firmware muss die entsprechenden
PlatformIO Umgebung gewählt werden:

* ESP32 Brick: ``esp32``
* ESP32 Ethernet Brick: ``esp32_ethernet``
* WARP Charger Smart und Pro: ``warp``
* WARP2 Charger Smart und Pro: ``warp2``

..
 * WARP Energy Manager: ``energy_manager``

Um die entsprechende Firmware zu bauen muss dann die PlatformIO "Build" Aufgabe ausgeführt
werden. Um die Firmware in einem Schritt zu bauen, auf den Brick hochzuladen
und eine Verbindung zur seriellen Konsole herzustellen kann die PlatformIO "Upload and Monitor"
Aufgabe ausgeführt werden. Dazu muss der Brick vorher per USB angeschlossen werden.

Struktur der Firmware
---------------------

Die Funktionalität und das Webinterface der Firmware sind aus Modulen zusammengesetzt.
Die verschiedenen Varianten der Firmware unterscheiden sich hauptsächlich durch
die aktiven Module. Die Liste der aktiven Module wird in der ``platformio.ini``
Datei für jede Umgebung durch die Optionen ``backend_modules`` und ``frontend_modules``
festgelegt.

Das Tutorial zur :ref:`ESP32 Firmware <tutorial_esp32_firmware>` zeigt Schritt
für Schritt wie die Standard-Firmware um ein eigenes Modul erweitert werden kann.

..
 TODO: WebSocket/HTTP/MQTT API der ESP32 Firmware dokumentieren, dazu den
       WARP Charger API Doc Generator refaktorisieren
