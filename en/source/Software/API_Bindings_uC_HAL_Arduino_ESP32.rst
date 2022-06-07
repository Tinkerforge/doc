
.. _api_bindings_uc_hal_arduino_esp32:

C/C++ for Microcontrollers - Arduino ESP32 HAL
==============================================

The Arduino ESP32 Hardware Abstraction Layer (HAL) is used
with the C/C++ bindings for microcontrollers to communicate
with Bricklets over SPI.

Supported Hardware
------------------

This HAL was tested with the following devices:

* ESP32 Brick (the customized :ref:`Arduino ESP32 Brick HAL <api_bindings_uc_hal_arduino_esp32_brick>` should be used instead)
* ESP32 Ethernet Brick (the customized :ref:`Arduino ESP32 Ethernet Brick HAL <api_bindings_uc_hal_arduino_esp32_ethernet_brick>` should be used instead)
* NodeMCU ESP32
* ESP32-WROOM-32 module
* ESP32-WROVER-32 module

But the HAL should work with all modules and boards using the ESP32,
as listed for example `here <https://en.wikipedia.org/wiki/ESP32#Printed_circuit_boards>`__.

The HAL requires usage of the Arduino ESP32 core.

.. _api_bindings_uc_hal_arduino_esp32_examples:

Testing an Example
------------------

These examples are made to be used with `Arduino ESP32 core <https://docs.espressif.com/projects/arduino-esp32/>`__
in the `Arduino IDE <https://www.arduino.cc/>`__. Start by installing both projects
according to their manuals.
Then select the correct board in Arduino IDE. If you are using an ESP32 Brick or
ESP32 Ethernet Brick then select "ESP32 Dev Module".

This HAL includes an example driver Arduino sketch that can be used to run any example provided with the bindings.

The Arduino IDE has specific requirements to the sketch folder layout. A valid folder looks like this:

* example_driver/

  * example_driver.ino [from the hal_arduino_esp32 folder]
  * [copy the example .c file here]
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

Now connect the board to the PC then build and upload the sketch. The prints
of the example should be listed in the serial console.

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

The :file:`example_driver.ino` contains an example port specification for the ESP32 Brick.

.. _api_bindings_uc_hal_arduino_esp32_api:

API
---

Most functions of the HAL return an error code (``e_code``).

Possible error codes are (as defined in :file:`errors.h`):

.. include:: API_Bindings_uC_HAL_Errors.inc

.. cpp:namespace-push:: hal_arduino_esp32

This HAL does not define further
error codes. Use :cpp:func:`tf_hal_strerror` to get
an error string for an error code.

Basic Functions
^^^^^^^^^^^^^^^

.. cpp:function:: int tf_hal_create(TF_HAL *hal, TF_Port *ports, uint8_t port_count)

 Creates a HAL object that can be used to list the available devices.
 It is also required for the constructor of Bricks and Bricklets.

 * ``ports`` is an array of port specifications, as described :ref:`here <api_bindings_uc_hal_arduino_port_spec>`
 * ``port_count`` is the length of the ``ports`` array.

 .. note:
   If the configured log level is not ``TF_LOG_LEVEL_NONE``,
   please initialize the serial console before calling this function.

.. cpp:function:: int tf_hal_destroy(TF_HAL *hal)

 Destroys the given ``TF_HAL``.

.. include:: API_Bindings_uC_HAL_Common.inc

.. cpp:namespace-pop::
