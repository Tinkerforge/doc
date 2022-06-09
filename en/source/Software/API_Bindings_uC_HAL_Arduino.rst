
.. _api_bindings_uc_hal_arduino:

C/C++ for Microcontrollers - Arduino HAL
========================================

The Arduino Hardware Abstraction Layer (HAL) is used
with the C/C++ bindings for microcontrollers to communicate
with Bricklets over SPI.

Supported Hardware
------------------

This HAL was tested with the following devices:

* Arduino Uno (requires level shifter)
* Arduino MEGA (requires level shifter)
* Teensy 3.1

But the HAL should work with all Arduino compatible boards,
as listed for example `here <https://en.wikipedia.org/wiki/List_of_Arduino_boards_and_compatible_systems>`__.

.. note::
  A level shifter is necessary for boards that use a logic level
  of 5 Volt (i.e. all AVR based boards).

.. note::
  Some Arduino Boards only have a small amount of flash and RAM available. :ref:`See here <api_bindings_uc_flash_size>`
  for some size optimizations.

.. _api_bindings_uc_hal_arduino_examples:

Testing an Example
------------------

These examples are made to be used in the `Arduino IDE <https://www.arduino.cc/>`__. Start by installing it
according to its manual.
Then select the correct board in Arduino IDE.

This HAL includes an example driver sketch that can be used to run any example provided with the bindings.

The Arduino IDE has specific requirements to the sketch folder layout. A valid folder looks like this:

* example_driver/

  * example_driver.ino [from the hal_arduino folder]
  * [copy the example .c file here]
  * src/

    * bindings/

      * [copy the content of the bindings folder here]

    * hal_arduino/

      * [copy hal_arduino.cpp and hal_arduino.h here]

Note that the top-level folder has to have the same name as the sketch,
i.e. if you rename :file:`example_driver.ino`, you have to rename the folder as well.

After creating the folder structure, you have to modify the port assignment in the sketch
to fit to your set-up (see :ref:`this section <api_bindings_uc_hal_arduino_port_spec>`). If you connect multiple Bricklets to the same SPI bus
(this is only possible with a tri-state buffer chip), you have to connect all their
chip select pins to the Arduino and list them in the port assignment, even if you don't
want to communicate with the Bricklets yet. This makes sure the signals are correctly separated.

Now connect the board to the PC then build and upload the sketch. The prints
of the example should be listed in the serial console.

.. _api_bindings_uc_hal_arduino_port_spec:

Port Specification Format
-------------------------

A port is specified as an instance of the ``TF_Port`` structure:

.. code-block:: c

  struct TF_Port {
      int chip_select_pin;
      char port_name;
  }

The chip select pin is the pin that has to be pulled to be able to communicate to the port.
The port name is a single character that identifies the port. The name is injected into the
result of ``tf_[device]_get_identity`` calls if the device is connected directly to the host.

The :file:`example_driver.c` contains an example port specification.

.. _api_bindings_uc_hal_arduino_api:

API
---

Most functions of the HAL return an error code (``e_code``).

Possible error codes are (as defined in :file:`errors.h`):

.. include:: API_Bindings_uC_HAL_Errors.inc

.. cpp:namespace-push:: hal_arduino

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
