
.. _tutorial_esp32_firmware:

Tutorial - ESP32 Firmware
=========================

Dieses Tutorial zeigt wie die ESP32 Firmware um ein eigenes Modul zur
Interaktion mit einem :ref:`RGB LED Button Bricklet <rgb_led_button_bricklet>`
erweitert werden kann.

.. image:: /Images/Tutorial/tutorial_esp32_hardware_600.jpg
   :scale: 100 %
   :alt: ESP32 Ethernet Brick mit angeschlossenem RGB LED Button Bricklet
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_hardware_1200.jpg

Als erster Schritt muss das Bauen der ESP32 Standard-Firmware
:ref:`vorbereitet <esp32_firmware_setup>` werden.

Alle Pfade und Dateinamen in diesem Tutorial beziehen sich auf das ``software/``
Verzeichnis der ESP32 Firmware.

Dieses Tutorial ist in vier Phasen unterteilt. Die jeweiligen Ausbaustufen des
neuen Moduls liegen unbenutzt der ESP32 Firmware bereits bei und werden hier
Schritt für Schritt erklärt.

Es können der :ref:`ESP32 Brick <esp32_brick>` und der
:ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>` für dieses Tutorial verwendet
werden. Der einzige Unterschied zwischen den beiden Bricks ist der Abschnitt
in der ``platformio.ini`` Datei, die im Laufe des Tutorial abgeändert werden
muss:

* ESP32 Brick: ``[env:esp32]``
* ESP32 Ethernet Brick: ``[env:esp32_ethernet]``

Um das jeweilige Tutorial-Modul zu aktivieren muss dessen Name am Ende der
Optionen ``backend_modules`` und ``frontend_modules`` des entsprechenden
Abschnitts hinzufügt werden.

Phase 1: Leeres Modul anlegen
-----------------------------

Modulname für die ``platformio.ini`` Datei: ``Tutorial Phase 1``

.. image:: /Images/Tutorial/tutorial_esp32_phase_1_de_600.png
   :scale: 100 %
   :alt: Webinterface Phase 1
   :align: center
   :target: ../../_images/Tutorial/tutorial_esp32_phase_1_de_1200.png

Module teilen sich in zwei Gruppen auf:

* **Backend**: Diese sind Teil der Firmware und werden in C/C++ programmiert.
  Backend-Module stellen die eigentliche Funktionalität bereit und können mit
  der Hardware kommunizieren. Modulverzeichnis: ``src/modules/``
* **Frontend**: Diese sind Teil des Webinterfaces und werden in
  HTML/Sass/TypeScript programmiert. Frontend-Module stellen die
  Benutzerschnittstelle bereit und können mit den Backend-Modulen kommunizieren.
  Modulverzeichnis: ``web/src/modules/``

Typischerweise treten Module in Backend/Frontend-Paaren auf, dies ist aber nicht
zwingend. Es kann Backend-Module ohne Frontend-Module geben und anders herum.

Aus dem Modulname in der ``platformio.ini`` Datei leitet sich der Verzeichnisname
für das Modul ab. Aus ``Tutorial Phase 1`` wird ``tutorial_phase_1`` (alle
Zeichen zu Kleinbuchstaben umwandeln und Leerzeichen durch Unterstriche ersetzen).

Dateien eines Backend-Moduls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jedes Backend-Modul wird durch eine C++ Klasse repräsentiert. Der Name dieser
Klasse leitet sich auch wieder aus dem Modulnamen ab. Aus ``Tutorial Phase 1``
wird ``TutorialPhase1`` (alle Leerzeichen entfernen).

Die Backend-Modul-Klasse muss in einer Header-Datei deklariert werden, deren
Name dem Verzeichnisnamen des Moduls entspricht und ``.h`` angehängt hat. In
diesem Fall also ``tutorial_phase_1.h``.

Alle Dateien im Modulverzeichnis, die auf ``.cpp``, ``.c`` oder ``.h`` enden,
werden unabhängig von ihrem Namen mit in die Firmware kompiliert.

Dateien eines Frontend-Moduls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jedes Frontend-Modul kann optional folgende Dateien beinhalten:

* **navbar.html**: HTML des Menüeintrags des Moduls. Der Menüeintrags wird
  dynamisch ein- und ausgeblendet, abhängig davon ob das entsprechende
  Backend-Modul erfolgreich initialisiert werden konnte.
* **content.html**: HTML der Unterseite des Moduls. Dies stellt die
  Benutzerschnittstelle des Moduls dar.
* **status.html**: HTML des Eintrags des Moduls auf der Statusseite. Die
  Statusseite stellt einen Übersicht der Module dar.
* **api.ts**: TypeScript-Definition der Backend-API die dieses Frontend-Modul
  nutzt.
* **main.ts**: TypeScript-Code der für dieses Modul ausgeführt wird.
* **translation_en.json**: Englische Übersetzung der Texte des Moduls.
* **translation_de.json**: Deutsche Übersetzung der Texte des Moduls.
