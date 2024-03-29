
.. _api_bindings_uc_hal_raspberry_pi:

C/C++ for Microcontrollers - Raspberry Pi HAL
=============================================

The Raspberry Pi Hardware Abstraction Layer (HAL) is used
with the C/C++ bindings for microcontrollers to communicate
with Bricklets over SPI.

Supported Hardware
------------------

This HAL was tested with the Raspberry Pi and Pi Zero with
the :ref:`HAT Brick <hat_brick>` or :ref:`HAT Zero Brick <hat_zero_brick>`.
It will only work with Raspberry Pi compatible devices, that
use the BCM2835 chip.

.. note::
  The Raspberry Pi 3, 4 and Zero scale their clock speed dynamically. Unfortunately this
  also scales the SPI clock speed. You have lock the GPU core frequency to make sure,
  the SPI clock is stable. We recommend setting the core_freq in /boot/config.txt to 250.
  `See here <https://www.raspberrypi.org/documentation/configuration/config-txt/overclocking.md>`__
  for details, especially for the Pi 4B, where the core_freq is influenced by other
  boot options.

  If you select another core_freq than 250, you have to compensate by multiplying
  ``BRICKLET_STACK_SPI_CONFIG_MAX_SPEED_HZ`` by 250 / [your core_freq in MHz].

.. _api_bindings_uc_hal_raspberry_pi_examples:

Testing an Example
------------------

This HAL includes an example driver sketch that can be used to run any example provided with the bindings,
as well as a Makefile to compile any example. To use the Makefile, create the following folder layout:

* [your main folder]/

  * example_driver.c [from the hal_raspberry_pi folder]
  * [copy the example .c file here]
  * Makefile
  * src/

    * bindings/

      * [copy the contents of the bindings folder here]

    * hal_raspberry_pi/

      * [copy the contents of the hal_raspberry_pi folder here]

After creating the folder structure, you have to modify the Makefile for your example:
List the device used in your selected example under ``SOURCES_DEVICES``, for example for the Industrial Digital In 4 2.0 Bricklet

.. code-block:: make

  SOURCES_DEVICES := src/bindings/bricklet_industrial_digital_in_4_v2.c

and add the example source file itself to ``SOURCES_EXAMPLE``, for example

.. code-block:: make

  SOURCES_EXAMPLE := example_edge_count.c

Next you have to modify the port assignment in the example driver
to fit to your set-up (:ref:`see this section <api_bindings_uc_hal_linux_port_spec>`).
If you connect multiple Bricklets to the same SPI bus
(this is only possible with a tri-state buffer chip), you have to connect all their
chip select pins to the Board and list them in the port assignment, even if you don't
want to communicate with the Bricklets yet. This makes sure the signals are correctly separated.

The :ref:`HAT Brick <hat_brick>` or :ref:`HAT Zero Brick <hat_zero_brick>` already
contain the required buffer chip and their port assignment is listed in the example driver.

You can then compile the program with ``make``.
If you want to cross-compile from another machine, use ``make CROSS_COMPILE=[compiler-prefix]``
for example ``make CROSS_COMPILE=arm-linux-gnueabihf-`` for the Raspberry Pi.

To run the compiled program, make sure that no Brick Daemon is running on the device and
start ``./uc_example``.

.. _api_bindings_uc_hal_raspberry_pi_port_spec:

Port Specification Format
-------------------------

A port is specified as an instance of the ``TF_Port`` structure:

.. code-block:: c

  struct TF_Port {
      int chip_select_pin;
      char port_name;
  }


The ``chip_select_pin`` is the pin that has to be pulled to be able to communicate to the port.
The ``port_name`` is a single character that identifies the port. The name is injected into the
result of ``tf_[device]_get_identity`` calls if the device is connected directly to the host.

The :file:`example_driver.c` contains an example port specification.

.. _api_bindings_uc_hal_raspberry_pi_api:

API
---

Most functions of the HAL return an error code (``e_code``).

Possible error codes are (as defined in :file:`errors.h`):

.. include:: API_Bindings_uC_HAL_Errors.inc

The HAL defines the following further error codes:

* TF\_\ **E**\ _BCM2835_INIT_FAILED = -100
* TF\_\ **E**\ _BCM2835_SPI_BEGIN_FAILED = -101

.. cpp:namespace-push:: hal_raspberry_pi

Use :cpp:func:`tf_hal_strerror` to get
an error string for an error code.

Basic Functions
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal, TF_Port *ports, uint8_t port_count)

 Creates a HAL context that can be used to list the available devices.
 It is also required for the constructor of Bricks and Bricklets.

 * ``ports`` is an array of port specifications, as described :ref:`here <api_bindings_uc_hal_raspberry_pi_port_spec>`
 * ``port_count`` is the length of the ``ports`` array.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Destroys the given ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
