
.. _api_bindings_uc_hal_arduino_esp32_ethernet_brick:

C/C++ for Microcontrollers - Arduino ESP32 Ethernet Brick HAL
=============================================================

The Arduino ESP32 Brick Ethernet Hardware Abstraction Layer (HAL) is used
with the C/C++ bindings for microcontrollers to communicate
with Bricklets over SPI.

Supported Hardware
------------------

This HAL is designed to be used with the :ref:`ESP32 Ethernet Brick <esp32_ethernet_brick>` only and
requires usage of the Arduino ESP32 core.

.. _api_bindings_uc_hal_arduino_esp32_ethernet_brick_examples:

Testing an Example
------------------

These examples are made to be used with `Arduino ESP32 core <https://docs.espressif.com/projects/arduino-esp32/>`__
in the `Arduino IDE <https://www.arduino.cc/>`__. Start by installing both projects
according to their manuals.
Then select "ESP32 Dev Module" as board in Arduino IDE.

This HAL includes an example driver Arduino sketch that can be used to run any example provided with the bindings.

The Arduino IDE has specific requirements to the sketch folder layout. A valid folder looks like this:

* example_driver/

  * example_driver.ino [from the hal_arduino_esp32_ethernet_brick folder]
  * [copy the example .c file here]
  * src/

    * bindings/

      * [copy the content of the bindings folder here]

    * hal_arduino_esp32_ethernet_brick/

      * [copy hal_arduino_esp32_ethernet_brick.cpp and hal_arduino_esp32_ethernet_brick.h here]

Note that the top-level folder has to have the same name as the sketch,
i.e. if you rename :file:`example_driver.ino`, you have to rename the folder as well.

Now connect the ESP32 Ethernet Brick to USB then build and upload the sketch. The prints
of the example should be listed in the serial console.

.. _api_bindings_uc_hal_arduino_esp32_ethernet_brick_api:

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

.. cpp:namespace-push:: hal_arduino_esp32_ethernet_brick

(as defined in :file:`errors.h`). This HAL does not define further
error codes. Use :cpp:func:`tf_hal_strerror` to get
an error string for an error code.

Basic Functions
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal)

 Creates a HAL object that can be used to list the available devices.
 It is also required for the constructor of Bricks and Bricklets.

 .. note:
   If the configured log level is not ``TF_LOG_LEVEL_NONE``,
   please initialize the serial console before calling this function.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Destroys the given ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
