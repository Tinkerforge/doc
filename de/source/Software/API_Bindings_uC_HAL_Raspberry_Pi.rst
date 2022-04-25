
.. _api_bindings_uc_hal_raspberry_pi:

C/C++ für Mikrocontroller - Raspberry Pi HAL
============================================

Der Raspberry Pi Hardware Abstraction Layer (HAL)
wird mit den C/C++ Bindings für Mikrocontroller verwendet
um mit Bricklets über SPI zu kommunizieren.

Unterstützte Hardware
---------------------

Dieser HAL wurde mit dem Raspberry Pi bzw. Pi Zero mit dem
:ref:`HAT Brick <hat_brick>` bzw. :ref:`HAT Zero Brick <hat_zero_brick>` getestet.
Er funktioniert nur mit Raspberry Pi kompatiblen Geräten, die den
BCM2835-Chip verwenden.

.. note::
  Der Raspberry Pi 3, 4 und Zero skalieren den Takt des BCM2835 dynamisch. Leider
  skaliert dies auch die SPI-Taktfrequenz. Die GPU-Kern-Frequenz muss auf einen
  festen Wert gesetzt werden, damit die SPI-Taktfrequenz stabil ist. Wir empfehlen,
  die core_freq in /boot/config.txt auf 250 zu setzen.
  `Siehe hier <https://www.raspberrypi.org/documentation/configuration/config-txt/overclocking.md>`__
  für Details, inbesondere für den Pi 4B, bei dem die core_freq durch andere Boot-Optionen beeinflusst wird.

  Wenn eine core_freq ungleich 250 gewählt wird, muss in :file:`hal_raspberry_pi.c`
  die ``BRICKLET_STACK_SPI_CONFIG_MAX_SPEED_HZ``-Konstante durch Multiplizieren von
  250 / [gewählte core_freq in MHz] kompensiert werden.

.. _api_bindings_uc_hal_raspberry_pi_examples:

Test eines Beispiels
--------------------

Dieser HAL beinhaltet einen Beispiel-Treiber, mit dem alle Beispiele, die den Bindings beigelegt sind, ausgeführt werden können,
sowie ein Makefile mit dem diese kompiliert werden können. Damit da Makefile verwendet werden kann
muss folgende Orderstruktur erstellt werden:

* [Hauptordner]/

  * example_driver.c
  * [hier die gewünschte Beispiel .c-Datei ablegen]
  * Makefile
  * src/

    * bindings/

      * [hier den Inhalt des bindings-Ordners ablegen]

    * hal_raspberry_pi/

      * [hier den Inhalt des hal_raspberry_pi-Ordners ablegen]

Nachdem die Orderstruktur abgelegt wurde, muss das Makefile für das Beispiel abgeändert werden:
Unter ``SOURCES_DEVICES`` muss das Gerät, das verwendet werden soll aufgeführt werden,
zum Beispiel für das Industrial Digital In 4 2.0 Bricklet:

.. code-block:: make

  SOURCES_DEVICES :=  bricklet_industrial_digital_in_4_v2.c

Der Quellcode des Beispiels selbst muss zu den ``SOURCES`` hinzugefügt werden,
zum Beispiel:

.. code-block:: make

  SOURCES :=  example_edge_count.c

Als nächstes muss die Port-Zuweisung im Beispiel-Treiber auf den Aufbau angepasst werden.
(:ref:`siehe dieser Abschnitt <api_bindings_uc_hal_linux_port_spec>`).
Wenn mehrere Bricklets am selben SPI-Bus verbunden werden sollen
(das ist nur mit einem Trenner-Chip möglich),
müssen alle Chip-Select-Pins mit dem Pi verbunden und in der Port-Zuweisung aufgeführt werden,
selbst wenn noch keine Kommunikation mit den Bricklets gewünscht ist.
Das stellt sicher, dass die Signale korrekt getrennt werden.

Der :ref:`HAT Brick <hat_brick>` und :ref:`HAT Zero Brick <hat_zero_brick>` beinhalten
bereits den benötigten Trenner-Chip und die korrekte Port-Zuweisung ist im Beispiel-Treiber
aufgeführt.

Als letzter Schritt muss die UID im verwendeten Beispiel angepasst werden. Die UID
wird im Brick Viewer angezeigt, wenn das Gerät mit einem PC verbunden wird. Außerdem
geben die Bindings eine Liste verbundener Geräte aus, wenn mit unverändertem Log-Level
:c:func:`tf_hal_create` aufgerufen wird.

Das Programm kann jetzt mit ``make`` kompiliert werden. Wenn von einem anderen
Rechner aus cross-kompiliert werden soll, kann ``make CROSS_COMPILE=[compiler-prefix]``
verwendet werden, zum Beispiel ``make CROSS_COMPILE=arm-linux-gnueabihf-`` für den Raspberry Pi.

Das Programm kann mit ``./uc_example`` gestartet werden. Es darf dabei kein Brick Daemon
auf dem Gerät laufen.

.. _api_bindings_uc_hal_raspberry_pi_port_spec:

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

Im Beispiel-Treiber :file:`example_driver.c` sind Port-Spezifikationen für den
:ref:`HAT Brick <hat_brick>` und :ref:`HAT Zero Brick <hat_zero_brick>` enthalten.

.. _api_bindings_uc_hal_raspberry_pi_api:

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

(wie in :file:`errors.h` definiert).
Der HAL definiert die folgenden weiteren Fehlercodes:

* TF\_\ **E**\ _BCM2835_INIT_FAILED = -100
* TF\_\ **E**\ _BCM2835_SPI_BEGIN_FAILED = -101

.. cpp:namespace-push:: hal_raspberry_pi

Mit :cpp:func:`tf_hal_strerror` kann eine Fehlerbeschreibung zu einem Fehlercode abgefragt werden.

Grundfunktionen
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal, TF_Port *ports, uint8_t port_count)

 Erstellt ein HAL-Objekt, das verwendet werden kann um die verfügbaren Geräte aufzulisten.
 Es wird außerdem für den Konstruktor von Bricks und Bricklets benötigt.

 * ``ports`` ist ein Array von Port-Spezifikationen, wie :ref:`hier <api_bindings_uc_hal_raspberry_pi_port_spec>` beschrieben.
 * ``port_count`` ist die Länge des ``ports``-Array.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Zerstört den übergebenen ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
