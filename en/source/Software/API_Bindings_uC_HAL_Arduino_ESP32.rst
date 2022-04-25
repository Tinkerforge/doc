
.. _api_bindings_uc_hal_arduino_esp32:

C/C++ for Microcontrollers - Arduino ESP32 HAL
==============================================

.. warning::
 This documentation might be outdated.

The Arduino ESP32 Hardware Abstraction Layer (HAL) is used
with the C/C++ bindings for microcontrollers to communicate
with Bricklets over SPI.

Supported Hardware
------------------

This HAL was tested with the following devices:

* ESP32 Brick
* NodeMCU ESP32
* ESP32-WROOM-32 module
* ESP32-WROVER-32 module

But the HAL should work with all modules and boards using the ESP32,
as listed for example `here <https://en.wikipedia.org/wiki/ESP32#Printed_circuit_boards>`__.

The HAL requires usage of the `Arduino ESP32 core <https://github.com/espressif/arduino-esp32>`__.

.. _api_bindings_uc_hal_arduino_esp32_examples:

Testing an Example
------------------

This HAL includes an example driver sketch that can be used to run any example provided with the bindings.

The Arduino IDE has specific requirements to the sketch folder layout. A valid folder looks like this:

* example_driver/

  * example_driver.ino
  * [copy the example C file here]
  * src/

    * bindings/

      * [copy the content of the bindings folder here]

    * hal_arduino_esp32/

      * [copy hal_arduino_esp32.cpp and hal_arduino_esp32.h here]

Note that the top-level folder has to have the same name as the sketch,
i.e. if you rename :file:`example_driver.ino`, you have to rename the folder as well.

After creating the folder structure, you have to modify the port assignment in the sketch
to fit to your set-up (see :ref:`this section <api_bindings_uc_hal_arduino_esp32_port_spec>`). If you connect multiple Bricklets to the same SPI bus
(this is only possible with a tri-state buffer chip, see :ref:`here <api_bindings_uc_supported_hardware>`), you have to connect all their
chip select pins to the Arduino and list them in the port assignment, even if you don't
want to communicate with the Bricklets yet. This makes sure the signals are correctly separated.

As last step, you have to change the UID in the example C file to the UID of your device.
The UID is shown in Brick Viewer if you connect the device to your PC. Also the bindings
will print a list of connected devices to the serial console when calling :c:func:`tf_hal_create`,
if the log level is unchanged.

.. _api_bindings_uc_hal_arduino_esp32_port_spec:

Port Specification Format
-------------------------

A port is specified as an instance of the ``TF_Port`` structure:

.. code-block:: c

  struct TF_Port {
      int chip_select_pin;
      uint8_t spi;
      char port_name;
  }

The chip select pin is the pin that has to be pulled to be able to communicate to the port.
SPI is the SPI hardware unit to use, valid values are ``VSPI`` and ``HSPI``.
The port name is a single character that identifies the port. The name is injected into the
result of ``tf_[device]_get_identity`` calls if the device is connected directly to the host.

The :file:`example_driver.c` contains an example port specification.

.. _api_bindings_uc_hal_arduino_esp32_api:

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
* TF\_\ **E**\ _NULL = -14
* TF\_\ **E**\ _DEVICE_ALREADY_IN_USE = -15
* TF\_\ **E**\ _WRONG_RESPONSE_LENGTH = -16
* TF\_\ **E**\ _NOT_INITIALIZED = -17

.. cpp:namespace-push:: hal_arduino_esp32

(as defined in :file:`errors.h`). This HAL does not define further
error codes. Use :cpp:func:`tf_hal_strerror` to get
an error string for an error code.

Basic Functions
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal, TF_Port *ports, uint8_t port_count)

 Creates a HAL object that can be used to list the available devices.
 It is also requred for the constructor of Bricks and Bricklets.

 * ``ports`` is an array of port specifications, as described :ref:`here <api_bindings_uc_hal_arduino_port_spec>`
 * ``port_count`` is the length of the ``ports`` array.

 .. note:
   If the configured log level is not ``TF_LOG_LEVEL_NONE``,
   please initialize the serial console before calling this function.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Destroys the given ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
