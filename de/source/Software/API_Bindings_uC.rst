
.. _api_bindings_uc:

C/C++ für Mikrocontroller - API Bindings
========================================

Die C/C++ Bindings ermöglichen es :ref:`Bricks <primer_bricks>` und
:ref:`Bricklets <primer_bricklets>` mit selbst erstellen C/C++ Programmen,
die auf einem Mikrocontroller laufen, zu steuern.
Die :ref:`ZIP Datei <downloads_bindings_examples>` für die Bindings beinhaltet:

* in ``source/bindings`` den Quelltext der Bindings
* in ``source/hal_*`` den Quelltext der HALs für einige Plattformen
* in ``examples/`` die Beispiele für alle Bricks und Bricklets

.. _api_bindings_uc_supported_hardware:

Unterstützte Hardware
---------------------

Die C/C++ Bindings für Mikrocontroller unterstützen Co-Prozessor-Bricklets, also diese mit einem
:ref:`7-Pol-Anschluss <tutorial_bricklet_cables>`,
sowie das :ref:`HAT Brick <hat_brick>` und das :ref:`HAT Zero Brick <hat_zero_brick>`.
Die älteren Brickets mit 10-Pol-Anschluss, sowie andere Bricks werden nicht unterstützt.
:ref:`Siehe hier <api_bindings_uc_api_reference>` für eine vollständige Liste unterstützter Geräte.

Das C/C++-Programm, das die Bindings verwendet läuft auf dem Host. Als Host
unterstützt werden aktuelle der :ref:`ESP32 Brick <esp32_brick>` und der
:ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>`. In Zukunft werden weitere
Mikrocontroller als Host unterstützt werden.

..
 Als Host unterstützt werden
 Mikrocontroller, die über SPI kommunizieren können, sowie der Raspberry Pi mit einem
 :ref:`HAT Brick <hat_brick>` oder :ref:`HAT Zero Brick <hat_zero_brick>`.

Die Bindings benötigen einen host-spezifischen Hardware Abstraction Layer (HAL).
:ref:`Siehe hier <api_bindings_uc_hal>` für Details.

..
 Wenn ein Mikrocontroller verwendet wird, muss sichergestellt sein, dass sein Logik-Pegel 3,3V entspricht.
 Andernfalls, zum Beispiel auf AVR-basierten Arduinos wie dem Arduino Uno oder Mega, wird ein Pegelwandler
 benötigt.

 Aufgrund eines Bugs des auf den Bricklets verwendeten XMC-Mikrocontrollers von
 Infineon trennt das Bricklets sich nicht korrekt vom SPI-Bus, wenn das
 Chip-Select-Signal deaktiviert wird. Es treibt dann weiterhin auf MISO einen
 Wert, was dazu führt, dass sich mehrere Bricklets am selben SPI-Bus gegenseitig
 stören. Falls mehrere Bricklets eingesetzt werden sollen, müssen deshalb vom
 Chip-Select-Signal kontrollierte Trenner-Chips eingesetzt werden.

 In naher Zukunft wird es eine neue Version des Breakout Bricklets geben, die sowohl
 einen 5V zu 3,3V Pegelwandler, als auch einen Trenner für das MOSI-Signal mitbringt.

Voraussetzungen
---------------

* C-Compiler (C99-kompatibel) oder C++-Compiler

.. _api_bindings_uc_install:

Installation
------------

.. note:
 C/C++ Bindings für Mikrocontroller sind während der Beta-Phase im
 `TinkerUnity <https://www.tinkerunity.org/topic/5463-betaversion-der-cc-bindings-f%C3%BCr-mikrocontroller/>`__ verfügbar.

Da es keine vorkompilierte Bibliothek für die C/C++ Bindings für Mikrocontroller
gibt, gibt es in diese Sinne auch nichts zu installieren. Die empfohlene Art und
Weise die Bindings zu verwenden, ist ihren Quelltext direkt in das jeweilige C/C++
Projekt mit einzubinden.

Test eines Beispiels
--------------------

Die Beispiele für jeden unterstützten Brick und Bricklet sind nicht vollständig,
da diese von der verwendeten Host-Hardware (und deren HAL) abhängen. Viele
HALs beinhalten einen Beispiel-Treiber der jegliches Beispiel ausführen kann.
Weitere Details sind in den spezifischen HAL Dokumentationen zu finden.

.. _api_bindings_uc_uid_or_port_name:

UID oder Port-Name
------------------

Alle Geräte-``*_create``-Funktionen nehmen ein ``uid_or_port_name`` Parameter,
das es dem Programm ermöglicht festzulegen mit welchem Gerät kommuniziert werden
soll. Dies kann auf drei Weise erfolgen:

* Bei Übergabe von ``NULL`` wird das erste unbenutzte Gerät des entsprechenden Typs
  ausgewählt unabhängig von UID und Port-Name.
* Bei Übergabe einer UID (z.B. "XyZ") wird das erste unbenutzte Gerät des entsprechenden Typs
  mit passender UID ausgewählt.
* Bei Übergabe eines Port-Names (z.B. "A") wird das erste unbenutzte Gerät des entsprechenden Typs
  mit passendem Port-Namen ausgewählt.

In diesem Fall bedeutet unbenutzt, dass das Gerät keinem Device-Objekt zugeordnet
ist. Zum Beispiel sind zwei Temperature Bricklet 2.0 angeschlossen, eins an Port A
und eins an Port B. Bei Übergabe von ``NULL`` wählt der erste ``tf_temperature_v2_create``
Aufruf das Bricklet an Port A aus. Der zweite Aufruf wählt das Bricklet an Port B,
da das Bricklet an Port A bereits benutzt wird.

.. _api_bindings_uc_hal:

Hardware Abstraction Layer
--------------------------

Die C/C++ Bindings für Mikrocontroller funktionieren anders als die anderen verfügbaren Bindings.
Während andere Bindings, die über TCP/IP mit einem Brick Daemon kommunizieren, eine IP Connection verwenden,
benötigen die C/C++ Bindings für Mikrocontroller einen Hardware Abstraction Layer (HAL).
Der HAL abstrahiert den plattformspezifischen Weg der SPI-Kommunikation.

Die Bindings beinhalten HALs für die folgenden Plattformen.
Für andere Plattformen muss ein eigener HAL implementiert werden (siehe unten).

..
 * :ref:`HAL Arduino <api_bindings_uc_hal_arduino>` für Arduino-kompatible Boards mit AVR- oder ARM-Prozessor

* :ref:`HAL Arduino ESP32 <api_bindings_uc_hal_arduino_esp32>` für Arduino-kompatible Boards mit ESP32-Prozessor
* :ref:`HAL Arduino ESP32 Brick <api_bindings_uc_hal_arduino_esp32_brick>` für :ref:`ESP32 Brick <esp32_brick>` auf Arduino-Basis
* :ref:`HAL Arduino ESP32 Ethernet Brick <api_bindings_uc_hal_arduino_esp32_ethernet_brick>` für :ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>` auf Arduino-Basis
* :ref:`HAL Linux <api_bindings_uc_hal_linux>` für Linux-Systeme mit spidev-Unterstützung

..
 * :ref:`HAL Raspberry Pi <api_bindings_uc_hal_raspberry_pi>` für Raspberry Pi 2, 3, 4 und Zero mit dem BCM2835 Chip
 * :ref:`HAL STM32F0 <api_bindings_uc_hal_stm32f0>` für den STM32F0 Mikrocontroller

Implementieren eines eigenen HALs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Falls die Bindings auf einer anderen Plattform verwendet werden sollen,
muss ein eigener HAL implementiert werden. :ref:`Diese Anleitung <api_bindings_uc_custom_hal>` zeigt wie.

.. _api_bindings_uc_callbacks:

Callbacks
---------

Callbacks funktionieren in den C/C++ Bindings für Mikrocontroller anders als
in anderen Bindings. Da es auf vielen der Zielplattformen kein Multi-Threading
gibt, wird nicht automatisch nach Callbacks gepollt. Stattdessen muss, wenn
Callbacks empfangen werden sollen, mit der in jedem HAL verfügbaren
``tf_hal_callback_tick``-Funktion nach Callbacks gepollt werden.
Diese Funktion pollt nur angeschlossene Geräte, für die mindestens
ein Callback-Handler registriert ist.

Callback werden nicht von einem anderen Thread ausgeliefert, sondern
nur, während ein Getter, Setter oder die ``tf_hal_callback_tick``-Funktion
ausgeführt wird. Die Bindings sind deshalb während der Ausführung eines
Callback-Handlers in einem Zustand, der es nicht erlaubt weitere Pakete zu schicken.
**Es ist nicht erlaubt, Getter, Setter oder Tick-Funktionen aus einem Callback-Handler aufzurufen**

.. _api_bindings_uc_thread_safety:

Threadsicherheit
----------------

Die primäre Zielplatform für die Bindings sind Mikrocontroller,
deshalb sind sie **nicht** thread-sicher. Einige HALs unterstützen
kooperatives Multitasking, es sind aber keine Aufrufe der Bindings-API
erlaubt, während sie pausiert sind. Alle Funktionen geben während
die Bindings pausiert sind, oder gerade ein Callback ausgeliefert wird,
``TF_E_LOCKED`` zurück.

.. _api_bindings_uc_performance:

Performanceoptimierungen
------------------------

Um die beste Performance aus den Bindings zu holen, kann der folgenden
Liste von Optimierungen gefolgt werden:

* Erhöhen der SPI-Taktfrequenz von 1,4 MHz auf so nah wie möglich an 2 MHz.
  Eine zu hohe Taktfrequenz wird die Performance aber wieder verschlechtern,
  da die angeschlossenen Geräte die Daten nicht mehr empfangen können. In unseren
  Tests wurde die optimale Performance bei 1,95 bis 1,96 MHz erreicht, aber das ist
  stark abhängig vom Aufbau, dem HAL und der Stabilität der SPI Clock des Host-Systems.

  Die SPI-Taktfrequenz kann in den HAL-Implementierungen eingestellt werden.

  .. note:
   EMV Tests werden mit der Standardbaudrate durchgeführt. Falls eine
   CE-Kompatibilität o.ä. in der Anwendung notwendig ist, empfehlen wir die
   SPI-Taktfrequenz nicht zu ändern.

* Bevorzugung von Callbacks. Die Bindings können ein angeschlossenes Gerät nach
  verfügbaren Callbacks fragen, indem ein einzelnes Byte über SPI geschickt wird.
  Wenn Getter verwendet werden um schnell veränderlichen Zustand abzufragen, muss jedes
  Mal eine komplette TFP-Anfrage, deren Antwort und ein Acknowledgment über SPI verschickt werden,
  was mindestens 23 Byte Datenverkehr bedeutet.

* Wenn exakt bekannt ist, welche Callbacks in welchen Intervallen eintreffen werden,
  sollte nicht ``tf_hal_callback_tick`` verwendet werden, sondern ein eigenes Scheduling
  für das Pollen mit den gerätespezifischen ``tf_[device]_callback_tick``-Funktionen verwendet werden.
  Das erlaubt es, mehr Zeit für andere Aufgaben aufzuwenden. ``tf_hal_callback_tick`` verwendet
  einen Round-Robin-Scheduler um alle Geräte mit einem registrierten Callback Handler zu pollen.

* Falls mehrere SPI-Einheiten verfügbar sind, können, soweit unterstützt,
  mehrere HAL-Instanzen verwendet werden. Das erlaubt es, mit mehreren Geräten
  parallel zu kommunizieren. Jede HAL-Instanz darf trotzdem nur von einem Thread verwendet werden.

.. _api_bindings_uc_flash_size:

RAM und Flashgröße optimieren
-----------------------------

Damit eine Firmware mit den Bindings auf kleinere Plattformen
wie den Arduino Uno passt, können die folgenden Konfigurationsoptionen
in :file:`bindings/config.h` angepasst werden:

* ``TF_INVENTORY_SIZE``:
  Die Größe des Inventory, also des Mappings von
  UIDs auf die Ports unter denen die Geräte erreichbar sind.
  Wenn pekannt ist, mit wie vielen Geräten kommuniziert werden soll,
  kann die Größe auf diesen Wert gesetzt werden. Die HAL-Initialisierung
  gibt ``TF_E_TOO_MANY_DEVICES`` zurück, falls das Inventory zu klein war.
* ``TF_IMPLEMENT_CALLBACKS``:
  Falls keine Callbacks benutzt werden sollen, kann dieses define entfernt werden, damit
  der entsprechende Code nicht verwendet wird
* ``TF_LOG_LEVEL``:
  Durch reduzieren des Log-Levels werden viele String-Konstanten nicht einkompiliert.
  Valide Werte sind:

  * ``TF_LOG_LEVEL_NONE``: Deaktiviert das Logging komplett
  * ``TF_LOG_LEVEL_ERROR``: Loggt nur HAL-spezifische Fehler wenn sie auftreten
  * ``TF_LOG_LEVEL_INFO``: Loggt zusätzlich die Liste der gefundenen Geräte bei der HAL-Initialisierung
  * ``TF_LOG_LEVEL_DEBUG``: Loggt zusätzlich alle internen Zustandsänderungen der SPITFP-Zustandsmaschine

* ``TF_IMPLEMENT_STRERROR``:
  Wenn dieses define entfernt wird, wird die ``tf_hal_strerror``-Funktion nicht implementiert.
  Damit können ungefähr 500 Bytes Speicherplatz freigemacht werden.

.. _api_bindings_uc_api_reference:

API Referenz und Beispiele
--------------------------

Links zur API Referenz der HALs, Bricks und Bricklets sowie die
Beispiele aus der ZIP Datei der Bindings sind in der folgenden Tabelle
aufgelistet. Anleitungen für weiterführende Projekte finden sich im Abschnitt
über :ref:`Kits <index_kits>`.

.. include:: API_Bindings_uC_links.table

.. toctree::
   :hidden:

   ~HAL Arduino <API_Bindings_uC_HAL_Arduino>
   HAL Arduino ESP32 <API_Bindings_uC_HAL_Arduino_ESP32>
   HAL Arduino ESP32 Brick <API_Bindings_uC_HAL_Arduino_ESP32_Brick>
   HAL Arduino ESP32 Ethernet Brick <API_Bindings_uC_HAL_Arduino_ESP32_Ethernet_Brick>
   HAL Linux <API_Bindings_uC_HAL_Linux>
   ~HAL Raspberry Pi <API_Bindings_uC_HAL_Raspberry_Pi>
   ~HAL STM32F0 <API_Bindings_uC_HAL_STM32F0>
   ~Eigener HAL <API_Bindings_uC_Custom_HAL>
   Bricks <Bricks_uC>
   Bricks (Abgekündigt) <Bricks_uC_Discontinued>
   Bricklets <Bricklets_uC>
   Bricklets (Abgekündigt) <Bricklets_uC_Discontinued>
