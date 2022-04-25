
.. _api_bindings_uc_hal_arduino_esp32_brick:

C/C++ für Mikrocontroller - Arduino ESP32 Brick HAL
===================================================

Der Arduino ESP32 Brick Hardware Abstraction Layer (HAL)
wird mit den C/C++ Bindings für Mikrocontroller verwendet
um mit Bricklets über SPI zu kommunizieren.

Unterstützte Hardware
---------------------

Dieser HAL ist speziell für die Verwendung mit dem :ref:`ESP32 Brick <esp32_brick>`
gemacht und benötigt den Arduino ESP32 Core.

.. _api_bindings_uc_hal_arduino_esp32_brick_examples:

Test eines Beispiels
--------------------

Die Beispiele sind für die Verwendung mit `Arduino ESP32 Core <https://docs.espressif.com/projects/arduino-esp32/>`__
in der `Arduino IDE <https://www.arduino.cc/>`__ gemacht. Daher müssen zuerst beide Projekte
entsprechend ihrer Installationsanleitungen installiert werden.
Danach in Arduino IDE das "ESP32 Dev Module" als Board auswählen.

Dieser HAL beinhaltet einen Beispiel-Treiber Arduino Sketch, mit dem alle Beispiele, die den Bindings beigelegt sind, ausgeführt werden können.

Die Arduino IDE hat spezifische Anforderungen an das Order-Layout des Sketch-Ordners. Ein gültiges Layout
sieht aus wie folgt:

* example_driver/

  * example_driver.ino [aus dem hal_arduino_esp32_brick-Ordner]
  * [hier die gewünschte Beispiel .c-Datei ablegen]
  * src/

    * bindings/

      * [hier den Inhalt des bindings-Ordners ablegen]

    * hal_arduino_esp32_brick/

      * [hier hal_arduino_esp32_brick.cpp und hal_arduino_esp32_brick.h ablegen]

Der Hauptordner muss zwingend den selben Namen wie die Sketch-Datei haben.
Wenn also :file:`example_driver.ino` umbenannt werden soll, muss auch der Ordner umbenannt werden.

Jetzt den ESP Brick mit USB verbinden und den Sketch bauen und hochladen. Die
Ausgaben des Beispiels sollten in der seriellen Konsole zu sehen sein.

.. _api_bindings_uc_hal_arduino_esp32_brick_api:

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
* TF\_\ **E**\ _NULL = -14
* TF\_\ **E**\ _DEVICE_ALREADY_IN_USE = -15
* TF\_\ **E**\ _WRONG_RESPONSE_LENGTH = -16
* TF\_\ **E**\ _NOT_INITIALIZED = -17

.. cpp:namespace-push:: hal_arduino_esp32_brick

(as defined in :file:`errors.h`). Dieser HAL definiert keine weiteren Fehlercodes.
Mit :cpp:func:`tf_hal_strerror` kann eine Fehlerbeschreibung zu einem Fehlercode abgefragt werden.

Grundfunktionen
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal)

 Erstellt ein HAL-Objekt, das verwendet werden kann um die verfügbaren Geräte aufzulisten.
 Es wird außerdem für den Konstruktor von Bricks und Bricklets benötigt.

 .. note:
   Wenn das konfigurierte Log-Level nicht ``TF_LOG_LEVEL_NONE`` ist,
   muss die serielle Konsole initialisiert werden, bevor diese Funktion aufgerufen wird.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Zerstört den übergebenen ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
