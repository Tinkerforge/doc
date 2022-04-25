
.. _api_bindings_uc_hal_linux:

C/C++ for Microcontrollers - Linux HAL
======================================

The Linux Hardware Abstraction Layer (HAL) is used
with the C/C++ bindings for microcontrollers to communicate
with Bricklets over SPI.

Supported Hardware
------------------

This HAL was tested with the Raspberry Pi and Pi Zero with
the :ref:`HAT Brick <hat_brick>` or :ref:`HAT Zero Brick <hat_zero_brick>`,
but should work with all Linux based systems with spidev support. A more performant HAL
specifically for the Raspberry Pi is also available :ref:`here <api_bindings_uc_hal_raspberry_pi>`.

.. note::
  The Raspberry Pi 3, 4 and Zero scale their clock speed dynamically. Unfortunately this
  also scales the SPI clock speed. You have lock the GPU core frequency to make sure,
  the SPI clock is stable. We recommend setting the core_freq in config.txt to 250.
  See `here <https://www.raspberrypi.org/documentation/configuration/config-txt/overclocking.md>`__
  for details, especially for the Pi 4B, where the core_freq is influenced by other
  boot options.

  If you select another core_freq than 250, you have to compensate by multiplying
  ``BRICKLET_STACK_SPI_CONFIG_MAX_SPEED_HZ`` by 250 / [your core_freq in mhz].

.. note::
  A level shifter is necessary for boards that use a logic level
  of 5 Volt.

.. _api_bindings_uc_hal_linux_examples:

Testing an Example
------------------

This HAL includes an example driver sketch that can be used to run any example provided with the bindings,
as well as a Makefile to compile any example. To use the Makefile, create the following folder layout:

* [your main folder]/

  * example_driver.c
  * [copy the example C file here]
  * Makefile
  * src/

    * bindings/

      * [copy the contents of the bindings folder here]

    * hal_linux/

      * [copy the contents of the hal_linux folder here]

After creating the folder structure, you have to modify the Makefile for your example:
List the device used in your selected example under ``SOURCES_DEVICES``, for example for the Industrial Digital In 4 2.0 Bricklet

.. code-block:: make

  SOURCES_DEVICES :=  bricklet_industrial_digital_in_4_v2.c

and add the example source file itself to ``SOURCES``, for example

.. code-block:: make

  SOURCES :=  example_edge_count.c

Next you have to modify the port assignment in the sketch
to fit to your set-up (see :ref:`this section <api_bindings_uc_hal_linux_port_spec>`).
If you connect multiple Bricklets to the same SPI bus
(this is only possible with a tri-state buffer chip), you have to connect all their
chip select pins to the Board and list them in the port assignment, even if you don't
want to communicate with the Bricklets yet. This makes sure the signals are correctly separated.

The :ref:`HAT Brick <hat_brick>` or :ref:`HAT Zero Brick <hat_zero_brick>` already
contain the required buffer chip and their port assignment is listed in the example driver.

Then you maybe have to change the path to the spidev in the example driver.
The default ``"/dev/spidev0.0"`` is correct for the ::ref:`HAT Brick <hat_brick>` and the
:ref:`HAT Zero Brick <hat_zero_brick>`.

As last step, you have to change the UID in the example C file to the UID of your device.
The UID is shown in Brick Viewer if you connect the device to your PC. Also the bindings
will print a list of connected devices to the standard output when calling :c:func:`tf_hal_create`,
if the log level is unchanged.

You can then compile the program with ``make``.
If you want to cross-compile from another machine, use ``make CROSS_COMPILE=[compiler prefix]``
for example ``make CROSS_COMPILE=arm-linux-gnueabihf-`` for the Raspberry Pi.

To run the compiled program, make sure that no Brick Daemon is running on the device and
start ``./uc_example``.

.. _api_bindings_uc_hal_linux_port_spec:

Port Specification Format
-------------------------

A port is specified as an instance of the ``TF_Port`` structure:

.. code-block:: c

  struct TF_Port {
      //external
      int chip_select_pin;
      char port_name;

      //internal
      int _cs_pin_fd;
  }


Revelant members are ``int chip_select_pin`` and ``char port_name``.
The chip select pin is the pin that has to be pulled to be able to communicate to the port.
The port name is a single character that identifies the port. The name is injected into the
result of ``tf_[device]_get_identity`` calls if the device is connected directly to the host.
You don't have to initialize ``_cs_pin_fd``.

The :file:`example_driver.c` contains an example port specification.

.. _api_bindings_uc_hal_linux_api:

API
---

Most functions of the HAL return an error code (``e_code``).

Possible error codes are:

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

(as defined in :file:`errors.h`).
The HAL defines the following further error codes:

* TF\_\ **E**\ _EXPORT_GPIO_FAILED = -100
* TF\_\ **E**\ _SET_GPIO_DIRECTION_FAILED = -101
* TF\_\ **E**\ _OPEN_GPIO_FAILED = -102

* TF\_\ **E**\ _OPEN_SPI_DEV_FAILED = -103
* TF\_\ **E**\ _SPI_DEV_CONFIG_FAILED = -104
* TF\_\ **E**\ _CHIP_SELECT_FAILED = -105
* TF\_\ **E**\ _TRANSCEIVE_FAILED = -106

.. cpp:namespace-push:: hal_linux

Use :cpp:func:`tf_hal_strerror` to get
an error string for an error code.

Basic Functions
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal, const char *spidev_path, TF_Port *ports, uint8_t port_count)

 Creates a HAL object that can be used to list the available devices.
 It is also requred for the constructor of Bricks and Bricklets.

 * ``spidev_path`` is the path to the spidev to use, for example "/dev/spidev0.0".
 * ``ports`` is an array of port specifications, as described :ref:`here <api_bindings_uc_hal_linux_port_spec>`
 * ``port_count`` is the length of the ``ports`` array.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Destroys the given ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
