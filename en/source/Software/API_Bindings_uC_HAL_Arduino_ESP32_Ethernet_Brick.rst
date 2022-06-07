
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

Possible error codes are (as defined in :file:`errors.h`):

.. include:: API_Bindings_uC_HAL_Errors.inc

.. cpp:namespace-push:: hal_arduino_esp32_ethernet_brick

This HAL does not define further
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
