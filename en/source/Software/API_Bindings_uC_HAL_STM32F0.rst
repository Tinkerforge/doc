
.. _api_bindings_uc_hal_stm32f0:

C/C++ for Microcontrollers - STM32F0 HAL
========================================

.. warning::
 This documentation might be outdated.

The STM32F0 Hardware Abstraction Layer (HAL) is used
with the C/C++ bindings for microcontrollers to communicate
with Bricklets over SPI.

Supported Hardware
------------------

This HAL was tested with the following devices:

* TNG-Bricklet4

But the HAL should work with all projects that use a STM32F0 microcontroller and the stm32cubef0 library from STM.

.. note::
  Some STM32F0 microcontroller only have a small amout of flash and RAM available. :ref:`See here <api_bindings_uc_flash_size>`
  for some size optimizations.

.. _api_bindings_uc_hal_stm32f0_examples:

Testing an Example
------------------

This HAL includes an example driver that can be used to run any example provided with the bindings.

Since the HAL is not written for any specific board, you need tho call the :c:func:`bricklet_main`
function from your code after you did the initial setup for your board.

The example driver defines four Bricklet ports that are connected to two different SPI hardware units.
You need to change the defines at the top of the example driver to fit to your board layout.

.. note::
  The HAL uses the `bricklib2 <https://github.com/Tinkerforge/bricklib2>`__ to implement the timer, sleep and log functions.
  If you make your own board you will likely have to replace these implementations with
  timer, sleep and log functions that are available in your project.

  Additionally the STM32F0 HAL uses a coop task (non-preemptive scheduling). You can either replace
  it with similar functions if available or disable the scheduling support with a define at
  the top of the file :file:`hal_stm32f0.c`.

  By default the HAL uses IRQs 2, 3, 4 and 5 for SPI communication. If you need any of these
  IRQs for other hardware units in your project, you will also have to change/remove the
  DMA-IRQ-Handler implementation.

.. _api_bindings_uc_hal_stm32f0_port_spec:

Port Specification Format
-------------------------

A port is specified as an instance of the ``TF_Port`` structure:

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

The TF_Port struct for the STM32F0 HAL uses the typical stm32cubef0 GPIO, SPI and DMA
data types. For details take a look at the :file:`example_driver.c`. 

It contains an example port specification.

.. _api_bindings_uc_hal_stm32f0_api:

API
---

Most functions of the HAL return an error code (``e_code``).

Possible error codes are (as defined in :file:`errors.h`):

.. include:: API_Bindings_uC_HAL_Errors.inc

The HAL defines the following further error codes:

* TF\_\ **E**\ _CHIP_SELECT_FAILED = -100
* TF\_\ **E**\ _TRANSCEIVE_FAILED = -101
* TF\_\ **E**\ _TRANSCEIVE_TIMEOUT = -102

.. cpp:namespace-push:: hal_stm32f0

Use :cpp:func:`tf_hal_strerror` to get
an error string for an error code.

Basic Functions
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal, TF_Port *ports, uint8_t spi_port_count)

 Creates a HAL object that can be used to list the available devices.
 It is also required for the constructor of Bricks and Bricklets.

 * ``ports`` is an array of port specifications, as described :ref:`here <api_bindings_uc_hal_stm32f0_port_spec>`
 * ``port_count`` is the length of the ``ports`` array.

 .. note:
   If the configured log level is not ``TF_LOG_LEVEL_NONE``,
   please initialize the serial console before calling this function.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Destroys the given ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
