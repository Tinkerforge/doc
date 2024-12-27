
.. _esp32_firmware:

ESP32 Firmware
==============

Die ESP32 Firmware kann in mehreren Varianten für verschiedenen Geräte gebaut werden:

* :ref:`ESP32 Brick <esp32_brick>`
* :ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>`
* `WARP Charger <https://www.warp-charger.com/warp1.html>`__ Smart und Pro
* `WARP2 Charger <https://www.warp-charger.com/warp2.html>`__ Smart und Pro
* `WARP Energy Manager <https://www.warp-charger.com/energy-manager.html>`__

Die Firmware ist in C/C++ programmiert und der Quelltext ist frei auf
`GitHub <https://github.com/Tinkerforge/esp32-firmware>`__ verfügbar.
Als Basis dienen das `Arduino ESP32 Projekt <https://docs.espressif.com/projects/arduino-esp32/>`__
und PlatformIO.

.. _esp32_firmware_setup:

Vorbereitung
------------

Zuerst müssen `PlatformIO <https://platformio.org/>`__ (mindestens Version 6),
`Node.js <https://nodejs.org/>`__ (mindestens Version 14) und `Git <https://git-scm.com/>`__ anhand der
Anleitung des jeweiligen Projekts installiert werden.
Für PlatformIO empfehlen wir die PlatformIO IDE Erweiterung für
`Visual Studio Code <https://code.visualstudio.com/>`__ zu verwenden. Es kann
aber auch PlatformIO Core verwendet werden. Node.js und Git müssen aber immer
außerhalb von Visual Studio Code installiert werden und nicht als Visual Studio
Code Erweiterung.

Allgemein sollte immer die neueste Version von PlatformIO und Node.js verwendet
werden. Der Node.js Package Manager ``npm`` muss mindestens in Version 8
vorliegen.

Für Windows muss der `Silicon Labs CP210x Universal Windows Driver <https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers>`__
installiert werden. Linux und macOS bringen diesen Treiber schon von sich aus mit.

Die ESP32 Firmware beinhaltet einige Datein mit sehr langen Dateinamen. Diese können
die veraltet Windows Beschänkung von maximal 260 Zeichen überschreiten. Es wird empfohlen
die `Unterstützung für lange Dateinamen in Windows zu aktivieren <https://learn.microsoft.com/de-de/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#registry-setting-to-enable-long-paths>`__.

Dann das `esp32-firmware <https://github.com/Tinkerforge/esp32-firmware>`__
Repository von GitHub mittels `git <https://www.git-scm.com/>`__ clonen.

Die ``platformio.ini`` Datei befindet sich im ``software/`` Verzeichnis.
Achte darauf das ``software/`` Verzeichnis in Visual Studio Code als
Projekt-Verzeichnis zu öffnen um eine der Umgebungen zu bauen (``build``).

.. _esp32_firmware_build:

Firmware bauen
--------------

Die Standard-PlatformIO-Umgebung ist auf ``empty`` gesetzt und erzeugt keine nützliche Firmware.
Abhängig von der zu bauenden Variante der Firmware muss die entsprechenden
PlatformIO-Umgebung gewählt werden:

* ESP32 Brick: ``esp32`` definiert in ``esp32.ini``
* ESP32 Ethernet Brick: ``esp32_ethernet`` definiert in ``esp32_ethernet.ini``
* WARP Charger Smart und Pro: ``warp`` definiert in ``warp.ini``
* WARP2 Charger Smart und Pro: ``warp2`` definiert in ``warp2.ini``
* WARP Energy Manager: ``energy_manager`` definiert in ``energy_manager.ini``

Um die entsprechende Firmware zu bauen muss dann die PlatformIO "Build" Aufgabe ausgeführt
werden. Es kann aber auch die Standard-PlatformIO-Umgebung in der ``platformio.ini`` Datei
von ``empty`` auf die gewünschte Umgebung geändert werden. Zum Beispiel ``empty`` durch
``esp32_ethernet`` in dieser Zeile ersetzen, um standardmäßig die ESP32 Ethernet Brick Firmware
zu bauen::

 default_envs = empty

Um die Firmware in einem Schritt zu bauen, auf den Brick hochzuladen
und eine Verbindung zur seriellen Konsole herzustellen kann die PlatformIO "Upload and Monitor"
Aufgabe ausgeführt werden. Dazu muss der Brick vorher per USB angeschlossen werden.
Alternativ kann die gebaute Firmware über das Webinterface hochgeladen werden.

Die Firmware-Datei befindet sich im Verzeichnis ``software/build`` und endet auf ``_merged.bin``.
Der Aufbau des Dateinamens ist wie folgt: ``[Umgebung]_firmware_[Versionsnummer]_[Bauzeitpunkt][Endung]``,
zum Beispiel ist ``warp2_firmware_2_0_7_62d7d0b1_merged.bin`` eine Firmware für den WARP2 Charger mit
der Version 2.0.7, die am Unix Timestamp 0x62d7d0b1 = 1658310833, also am 20.07.2022 13:27:02 gebaut wurde.

Struktur der Firmware
---------------------

Die Funktionalität und das Webinterface der Firmware sind aus Modulen zusammengesetzt.
Die verschiedenen Varianten der Firmware unterscheiden sich hauptsächlich durch
die aktiven Module. Die Liste der aktiven Module wird in der jeweligen ``.ini``
Datei für jede Umgebung durch die Optionen ``custom_backend_modules`` und ``custom_frontend_modules``
festgelegt.

Das Tutorial zur :ref:`ESP32 Firmware <tutorial_esp32_firmware>` zeigt Schritt
für Schritt wie die Standard-Firmware um ein eigenes Modul erweitert werden kann.

..
 TODO: WebSocket/HTTP/MQTT API der ESP32 Firmware dokumentieren, dazu den
       WARP Charger API Doc Generator refaktorisieren
