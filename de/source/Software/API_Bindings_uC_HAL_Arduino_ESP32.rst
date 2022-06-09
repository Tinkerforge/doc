
.. _api_bindings_uc_hal_arduino_esp32:

C/C++ für Mikrocontroller - Arduino ESP32 HAL
=============================================

Der Arduino ESP32 Hardware Abstraction Layer (HAL)
wird mit den C/C++ Bindings für Mikrocontroller verwendet
um mit Bricklets über SPI zu kommunizieren.

Unterstützte Hardware
---------------------

Dieser HAL wurde mit den folgenden Boards getestet:

* :ref:`ESP32 Brick <esp32_brick>` (es sollte jedoch der angepasste :ref:`Arduino ESP32 Brick HAL <api_bindings_uc_hal_arduino_esp32_brick>` verwendet werden)
* :ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>` (es sollte jedoch der angepasste :ref:`Arduino ESP32 Ethernet Brick HAL <api_bindings_uc_hal_arduino_esp32_ethernet_brick>` verwendet werden)
* NodeMCU ESP32
* ESP32-WROOM-32-Modul
* ESP32-WROVER-32-Modul

Der HAL sollte aber mit allen Modulen und Boards, die einen ESP32 verwenden, funktionieren.
Eine Liste findet sich `hier <https://en.wikipedia.org/wiki/ESP32#Printed_circuit_boards>`__.

Dieser HAL benötigt den Arduino ESP32 Core.

.. _api_bindings_uc_hal_arduino_esp32_examples:

Test eines Beispiels
--------------------

Die Beispiele sind für die Verwendung mit `Arduino ESP32 Core <https://docs.espressif.com/projects/arduino-esp32/>`__
in der `Arduino IDE <https://www.arduino.cc/>`__ gemacht. Daher müssen zuerst beide Projekte
entsprechend ihrer Installationsanleitungen installiert werden.
Danach in Arduino IDE das passende Board auswählen. Für die Verwendung eines
ESP32 Brick oder ESP32 Ethernet Brick muss "ESP32 Dev Module" als Board ausgewählt
werden.

Dieser HAL beinhaltet einen Beispiel-Treiber Arduino Sketch, mit dem alle Beispiele, die den Bindings beigelegt sind, ausgeführt werden können.

Die Arduino IDE hat spezifische Anforderungen an das Order-Layout des Sketch-Ordners. Ein gültiges Layout
sieht aus wie folgt:

* example_driver/

  * example_driver.ino [aus dem hal_arduino_esp32-Ordner]
  * [hier die gewünschte Beispiel .c-Datei ablegen]
  * src/

    * bindings/

      * [hier den Inhalt des bindings-Ordners ablegen]

    * hal_arduino_esp32/

      * [hier hal_arduino_esp32.cpp und hal_arduino_esp32.h ablegen]

Der Hauptordner muss zwingend den selben Namen wie die Sketch-Datei haben.
Wenn also :file:`example_driver.ino` umbenannt werden soll, muss auch der Ordner umbenannt werden.

Als nächstes muss die Port-Zuweisung im Beispiel-Treiber auf den Aufbau angepasst werden
(:ref:`siehe dieser Abschnitt <api_bindings_uc_hal_arduino_esp32_port_spec>`).
Wenn mehrere Bricklets am selben SPI-Bus verbunden werden sollen
(das ist nur mit einem Trenner-Chip möglich),
müssen alle Chip-Select-Pins mit dem Board verbunden und in der Port-Zuweisung aufgeführt werden,
selbst wenn noch keine Kommunikation mit den Bricklets gewünscht ist.
Das stellt sicher, dass die Signale korrekt getrennt werden.

Jetzt das Board mit dem PC verbinden und den Sketch bauen und hochladen. Die
Ausgaben des Beispiels sollten in der seriellen Konsole zu sehen sein.

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

Im Beispiel-Treiber :file:`example_driver.ino` ist eine Beispiel-Port-Spezifikation für den ESP32 Brick enthalten.

.. _api_bindings_uc_hal_arduino_esp32_api:

API
---

Die meisten HAL-Funktionen geben einen Fehlercode (``e_code``) zurück.

Mögliche Fehlercodes sind (wie in :file:`errors.h` definiert):

.. include:: API_Bindings_uC_HAL_Errors.inc

.. cpp:namespace-push:: hal_arduino_esp32

Dieser HAL definiert keine weiteren Fehlercodes.
Mit :cpp:func:`tf_hal_strerror` kann eine Fehlerbeschreibung zu einem Fehlercode abgefragt werden.

Grundfunktionen
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal, TF_Port *ports, uint8_t port_count)

 Erstellt ein HAL-Objekt, das verwendet werden kann um die verfügbaren Geräte aufzulisten.
 Es wird außerdem für den Konstruktor von Bricks und Bricklets benötigt.

 * ``ports`` ist ein Array von Port-Spezifikationen, wie :ref:`hier <api_bindings_uc_hal_arduino_esp32_port_spec>` beschrieben.
 * ``port_count`` ist die Länge des ``ports``-Array.

 .. note:
   Wenn das konfigurierte Log-Level nicht ``TF_LOG_LEVEL_NONE`` ist,
   muss die serielle Konsole initialisiert werden, bevor diese Funktion aufgerufen wird.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Zerstört den übergebenen ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
