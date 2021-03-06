
.. _api_bindings_uc_hal_arduino_esp32:

C/C++ für Mikrocontroller - Arduino ESP32 HAL
=============================================

Der Arduino ESP32 Hardware Abstraction Layer (HAL)
wird mit den C/C++ Bindings für Mikrocontroller verwendet
um mit Bricklets über SPI zu kommunizieren.

Unterstützte Hardware
---------------------

Dieser HAL wurde mit den folgenden Boards getestet:

* ESP32 Brick
* NodeMCU ESP32
* dem ESP32-WROOM-32-Modul selbst

sollte aber mit allen Modulen und Boards, die einen ESP32 verwenden, funktionieren.
Eine Liste findet sich `hier <https://en.wikipedia.org/wiki/ESP32#Printed_circuit_boards>`__.

Dieser HAL benötigt den `Arduino ESP32 Core <https://github.com/espressif/arduino-esp32>`__.

.. _api_bindings_uc_hal_arduino_esp32_examples:

Test eines Beispiels
--------------------

Dieser HAL beinhaltet einen Beispiel-Treiber, mit dem alle Beispiele, die den Bindings beigelegt sind, ausgeführt werden können.

Die Arduino IDE hat spezifische Anforderungen an das Order-Layout des Sketch-Ordners. Ein gültiges Layout
sieht aus wie folgt:

* example_driver/

  * example_driver.ino
  * src/

    * [hier die gewünschte Beispiel .c-Datei ablegen]
    * bindings/

      * [hier den Inhalt des bindings-Ordners ablegen]

    * hal_arduino_esp32/

      * [hier hal_arduino_esp32.cpp und hal_arduino_esp32.h ablegen]

Der Hauptordner muss zwingend den selben Namen wie die Sketch-Datei haben.
Wenn also :file:`example_driver.ino` umbenannt werden soll, muss auch der Ordner umbenannt werden.

Als nächstes muss die Port-Zuweisung im Beispiel-Treiber auf den Aufbau angepasst werden.
(:ref:`siehe dieser Abschnitt <api_bindings_uc_hal_arduino_esp32_port_spec>`).
Wenn mehrere Bricklets am selben SPI-Bus verbunden werden sollen
(das ist nur mit einem Trenner-Chip möglich),
müssen alle Chip-Select-Pins mit dem Board verbunden und in der Port-Zuweisung aufgeführt werden,
selbst wenn noch keine Kommunikation mit den Bricklets gewünscht ist.
Das stellt sicher, dass die Signale korrekt getrennt werden.

Als letzer Schritt muss die UID im verwendeten Beispiel angepasst werden. Die UID
wird im Brick Viewer angezeigt, wenn das Gerät mit einem PC verbunden wird. Außerdem
geben die Bindings eine Liste verbundener Geräte aus, wenn mit unverändertem Log-Level
:c:func:`tf_hal_create` aufgerufen wird.

.. _api_bindings_uc_hal_arduino_esp32_port_spec:

Port-Spezifikations-Format
--------------------------

Ein Port wird als Instanz der ``TF_Port``-Struktur spezifiziert:

.. code-block:: c

  struct TF_Port {
      int chip_select_pin;
      uint8_t spi;
      char port_name;
  }


Der ``chip_select_pin`` ist der Pin, der gesetzt werden muss, um mit dem Port zu kommunizieren.
``SPI`` ist die SPI-Hardware-Einheit die verwendet werden soll. Gültige Werte sind ``VSPI`` und ``HSPI``.
Der ``port_name`` ist ein Zeichen, das den Port identifiziert. Der Name wird in die
Ergebnisse von ``tf_[device]_get_identity`` aufrufen eingefügt, falls das Gerät direkt mit dem Host
verbunden ist.

Im Beispiel-Treiber :file:`example_driver.c` ist eine Beispiel-Port-Spezifikation enthalten.

.. _api_bindings_uc_hal_arduino_esp32_api:

API
---

Die meisten HAL-Funktionen geben einen Fehlercode (``e_code``) zurück.

Mögliche Fehlercodes sind:

* TF\_\ **E**\ _OK = 0
* TF\_\ **E**\ _TIMEOUT = -1
* TF\_\ **E**\ _INVALID_PARAMETER = -2
* TF\_\ **E**\ _NOT_SUPPORTED = -3
* TF\_\ **E**\ _UNKNOWN_ERROR_CODE = -4
* TF\_\ **E**\ _STREAM_OUT_OF_SYNC = -5
* TF\_\ **E**\ _INVALID_CHAR_IN_UID = -6
* TF\_\ **E**\ _UID_TOO_LONG = -7
* TF\_\ **E**\ _UID_OVERFLOW = -8
* TF\_\ **E**\ _TOO_MANY_DEVICES = -9
* TF\_\ **E**\ _DEVICE_NOT_FOUND = -10
* TF\_\ **E**\ _WRONG_DEVICE_TYPE = -11
* TF\_\ **E**\ _LOCKED = -12
* TF\_\ **E**\ _PORT_NOT_FOUND = -13

.. cpp:namespace-push:: hal_arduino_esp32

(as defined in :file:`errors.h`). Dieser HAL definiert keine weiteren Fehlercodes.
Mit :cpp:func:`tf_hal_strerror` kann eine Fehlerbeschreibung zu einem Fehlercode abgefragt werden.

Grundfunktionen
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HalContext *hal, TF_Port *ports, uint8_t port_count)

 Erstellt ein HAL-Objekt, das verwendet werden kann um die verfügbaren Geräte aufzulisten.
 Es wird außerdem für den Konstruktor von Bricks und Bricklets benötigt.

 * ``ports`` ist ein Array von Port-Spezifikationen, wie :ref:`hier <api_bindings_uc_hal_arduino_esp32_port_spec>` beschrieben.
 * ``port_count`` ist die Länge des ``ports``-Array.

 .. note:
   Wenn das konfigurierte Log-Level nicht ``TF_LOG_LEVEL_NONE`` ist,
   muss die serielle Konsole initialisiert werden, bevor diese Funktion aufgerufen wird.

.. cpp:function:: int tf_hal_destroy(TF_HalContext *hal)

 Zerstört den übergebenen ``TF_HalContext``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
