
.. _api_bindings_uc_hal_arduino:

C/C++ für Mikrocontroller - Arduino HAL
=======================================

.. warning::
 Diese Dokumentation ist möglicherweise veraltet.

Der Arduino Hardware Abstraction Layer (HAL)
wird mit den C/C++ Bindings für Mikrocontroller verwendet
um mit Bricklets über SPI zu kommunizieren.

Unterstützte Hardware
---------------------

Dieser HAL wurde mit den folgenden Boards getestet:

* Arduino Uno (benötigt einen Pegelwandler)
* Arduino MEGA (benötigt einen Pegelwandler)
* Teensy 3.1

Der HAL sollte aber mit allen Arduino-kompatiblen Boards funktionieren
die zum Beispiel `hier <https://en.wikipedia.org/wiki/List_of_Arduino_boards_and_compatible_systems>`__
aufgelistet sind. Eine weniger vollständige deutsche Liste findet sich `hier <https://de.wikipedia.org/wiki/Liste_von_Arduino-Boards>`__.

.. note::
  Ein Pegelwandler ist für Geräte, die einen Logik-Pegel von 5V verwenden notwendig.
  Das betrifft unter anderem alle AVR-basierten Arduinos.

.. note::
  Manche Arduinos haben nur eine kleine Menge Flash und RAM verfügbar. :ref:`Siehe hier <api_bindings_uc_flash_size>`
  für einige Größenoptimierungen.

.. _api_bindings_uc_hal_arduino_examples:

Test eines Beispiels
--------------------

Die Beispiele sind für die Verwendung in der `Arduino IDE <https://www.arduino.cc/>`__ gemacht. Daher muss diese zuerst
entsprechend ihrer Installationsanleitung installiert werden.
Danach in Arduino IDE das passende Board auswählen.

Dieser HAL beinhaltet einen Beispiel-Treiber, mit dem alle Beispiele, die den Bindings beigelegt sind, ausgeführt werden können.

Die Arduino IDE hat spezifische Anforderungen an das Order-Layout des Sketch-Ordners. Ein gültiges Layout
sieht aus wie folgt:

* example_driver/

  * example_driver.ino [aus dem hal_arduino-Ordner]
  * [hier die gewünschte Beispiel .c-Datei ablegen]
  * src/

    * bindings/

      * [hier den Inhalt des bindings-Ordners ablegen]

    * hal_arduino/

      * [hier hal_arduino.cpp und hal_arduino.h ablegen]

Der Hauptordner muss zwingend den selben Namen wie die Sketch-Datei haben.
Wenn also :file:`example_driver.ino` umbenannt werden soll, muss auch der Ordner umbenannt werden.

Als nächstes muss die Port-Zuweisung im Beispiel-Treiber auf den Aufbau angepasst werden.
(:ref:`siehe dieser Abschnitt <api_bindings_uc_hal_arduino_port_spec>`).
Wenn mehrere Bricklets am selben SPI-Bus verbunden werden sollen
(das ist nur mit einem Trenner-Chip möglich),
müssen alle Chip-Select-Pins mit dem Arduino verbunden und in der Port-Zuweisung aufgeführt werden,
selbst wenn noch keine Kommunikation mit den Bricklets gewünscht ist.
Das stellt sicher, dass die Signale korrekt getrennt werden.

Jetzt das Board mit dem PC verbinden und den Sketch bauen und hochladen. Die
Ausgaben des Beispiels sollten in der seriellen Konsole zu sehen sein.

.. _api_bindings_uc_hal_arduino_port_spec:

Port-Spezifikations-Format
--------------------------

Ein Port wird als Instanz der ``TF_Port``-Struktur spezifiziert:

.. code-block:: c

  struct TF_Port {
      int chip_select_pin;
      char port_name;
  }

Der ``chip_select_pin`` ist der Pin, der gesetzt werden muss, um mit dem Port zu kommunizieren.
Der ``port_name`` ist ein Zeichen, das den Port identifiziert. Der Name wird in die
Ergebnisse von ``tf_[device]_get_identity`` aufrufen eingefügt, falls das Gerät direkt mit dem Host
verbunden ist.

Im Beispiel-Treiber :file:`example_driver.c` ist eine Beispiel-Port-Spezifikation enthalten.

.. _api_bindings_uc_hal_arduino_api:

API
---

Die meisten HAL-Funktionen geben einen Fehlercode (``e_code``) zurück.

Mögliche Fehlercodes sind (wie in :file:`errors.h` definiert):

.. include:: API_Bindings_uC_HAL_Errors.inc

.. cpp:namespace-push:: hal_arduino

Dieser HAL definiert keine weiteren Fehlercodes.
Mit :cpp:func:`tf_hal_strerror` kann eine Fehlerbeschreibung zu einem Fehlercode abgefragt werden.

Grundfunktionen
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal, TF_Port *ports, uint8_t port_count)

 Erstellt ein HAL-Objekt, das verwendet werden kann um die verfügbaren Geräte aufzulisten.
 Es wird außerdem für den Konstruktor von Bricks und Bricklets benötigt.

 * ``ports`` ist ein Array von Port-Spezifikationen, wie :ref:`hier <api_bindings_uc_hal_arduino_port_spec>` beschrieben.
 * ``port_count`` ist die Länge des ``ports``-Array.

 .. note:
   Wenn das konfigurierte Log-Level nicht ``TF_LOG_LEVEL_NONE`` ist,
   muss die serielle Konsole initialisiert werden, bevor diese Funktion aufgerufen wird.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Zerstört den übergebenen ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
