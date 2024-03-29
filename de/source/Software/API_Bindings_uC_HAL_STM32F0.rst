
.. _api_bindings_uc_hal_stm32f0:

C/C++ für Mikrocontroller - STM32F0 HAL
=======================================

.. warning::
 Diese Dokumentation ist möglicherweise veraltet.

Der STM32F0 Hardware Abstraction Layer (HAL)
wird mit den C/C++ Bindings für Mikrocontroller verwendet
um mit Bricklets über SPI zu kommunizieren.

Unterstützte Hardware
---------------------

Dieser HAL wurde mit den folgenden Geräten getestet:

* TNG-Bricklet4

Der HAL sollte aber mit allen Projekten, die den STM32F0-Mikrocontroller und die stm32cubef0-Bibliothek von STM verwenden, funktionieren.

.. note::
  Manche STM32F0-Mikrocontroller haben nur eine kleine Menge Flash und RAM verfügbar. :ref:`Siehe hier <api_bindings_uc_flash_size>`
  für einige Größenoptimierungen.

.. _api_bindings_uc_hal_stm32f0_examples:

Test eines Beispiels
--------------------

Dieser HAL beinhaltet einen Beispiel-Treiber, mit dem alle Beispiele, die den Bindings beigelegt sind, ausgeführt werden können.

Da der HAL nicht für ein spezifisches Board geschrieben ist, muss `bricklet_main` nach dem Initialsetup
von eigenem Code aufgerufen werden.

Der Beispiel-Treiber definiert vier Bricklet-Ports, die mit zwei verschiedenen SPI-Hardware-Einheiten verbunden sind.
Die Definitionen im Beispiel-Treiber müssen für das verwendete Board angepasst werden.

.. note::
  Der HAL verwendet die `bricklib2 <https://github.com/Tinkerforge/bricklib2>`__ um Timer-, Sleep- und Log-Funktionen zu implementieren.
  Bei Verwendung eines eigenen Boards müssen diese Implementierungen durch entsprechende Funktionen,
  die im Projekt verfügbar sind, ausgetauscht werden.

  Der STM32F0-HAL unterstützt kooperatives Multitasking mit einem Coop-Task. Dieser kann, falls
  verfügbar, durch ähnliche Funktionen ausgetauscht werden, oder durch Setzen eines Defines
  in :file:`hal_stm32f0.c` deaktiviert werden.

  Der HAL verwendet standardmäßig die IRQs 2, 3, 4 und 5 für die SPI-Kommunikation. Falls
  einige dieser IRQs für andere Hardware-Einheiten benötigt werden, muss die DMA-IRQ-Handler-
  Implementierung angepasst werden.

.. _api_bindings_uc_hal_stm32f0_port_spec:

Port-Spezifikations-Format
--------------------------

Ein Port wird als Instanz der ``TF_Port``-Struktur spezifiziert:

.. code-block:: c

  struct TF_Port {
    TF_STMGPIO clk;
    TF_STMGPIO mosi;
    TF_STMGPIO miso;
    TF_STMGPIO *cs;
    uint8_t cs_count;

    SPI_TypeDef *spi_instance;

    IRQn_Type irq_tx;
    IRQn_Type irq_rx;

    DMA_Channel_TypeDef *dma_channel_rx;
    DMA_Channel_TypeDef *dma_channel_tx;
  }

  typedef struct {
    GPIO_InitTypeDef pin;
    GPIO_TypeDef *port;
  } TF_STMGPIO

Die ``TF_Port``-Struktur für den STM32F0-HAL verwendet die typischen stm32cubef0 GPIO, SPI und DMA
Datentypen. Details finden sich in der Beispiel-Port-Spezifikation in :file:`example_driver.c`.

.. _api_bindings_uc_hal_stm32f0_api:

API
---

Die meisten HAL-Funktionen geben einen Fehlercode (``e_code``) zurück.

Mögliche Fehlercodes sind (wie in :file:`errors.h` definiert):

.. include:: API_Bindings_uC_HAL_Errors.inc

Der HAL definiert die folgenden weiteren Fehlercodes:

* TF\_\ **E**\ _CHIP_SELECT_FAILED = -100
* TF\_\ **E**\ _TRANSCEIVE_FAILED = -101
* TF\_\ **E**\ _TRANSCEIVE_TIMEOUT = -102

.. cpp:namespace-push:: hal_stm32f0

Mit :cpp:func:`tf_hal_strerror` kann eine Fehlerbeschreibung zu einem Fehlercode abgefragt werden.

Grundfunktionen
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(struct TF_HAL *hal, TF_Port *ports, uint8_t spi_port_count)

 Erstellt ein HAL-Objekt, das verwendet werden kann um die verfügbaren Geräte aufzulisten.
 Es wird außerdem für den Konstruktor von Bricks und Bricklets benötigt.

 * ``ports`` ist ein Array von Port-Spezifikationen, wie :ref:`hier <api_bindings_uc_hal_stm32f0_port_spec>` beschrieben.
 * ``port_count`` ist die Länge des ``ports``-Array.

 .. note:
   Wenn das konfigurierte Log-Level nicht ``TF_LOG_LEVEL_NONE`` ist,
   muss die serielle Konsole initialisiert werden, bevor diese Funktion aufgerufen wird.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Zerstört den übergebenen ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
