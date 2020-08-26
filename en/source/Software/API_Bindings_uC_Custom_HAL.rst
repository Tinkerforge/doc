
.. _api_bindings_uc_custom_hal:

C/C++ for Microcontrollers - Custom HAL
=======================================

Using the C/C++ Bindings for Microcontrollers
requires a hardware specific HAL. If no HAL for
your platform is available, you can write your own
by following this guide.

.. note::
  If you have written a custom HAL for a hardware platform
  and are able to release it under the CC0 license, please
  send a mail to info@tinkerforge.com. We are always interested
  in adding HALs for different platforms to the bindings.

Hardware Requirements
---------------------

Running the bindings requires a microcontroller comparable or better than the ATmega328 used on the Arduino Uno.
The code requires at least 2k RAM and 16k flash for simple use cases.
The host hardware must be able to communicate over SPI with at least 400 kHz.
For maximum performance, a SPI clock rate of 2 MHz is recommended.

Overview
--------

A HAL is responsible for initialization and control of a platform's
SPI hardware. Also it abstracts other hardware specific facilities
such as time keeping and logging.

To implement a HAL, the following steps are necessary:

* Definition of a ``TF_HalContext`` and ``TF_Port`` struct
* Implementation of the ``tf_hal_create`` and ``tf_hal_destroy`` functions for the defined struct
* Implementation of the required HAL functions

To help with implementing a HAL, the following functions defined in :file:`bindings/hal_common.h`
can be used:

.. c:function:: int tf_hal_common_create(TF_HalContext *hal)

 Initializes the ``TF_HalCommon`` instance associated with the given ``TF_HalContext``.
 This function must be called while initializing your HAL as early as possible.

.. c:function:: int tf_hal_common_prepare(TF_HalContext *hal, uint8_t port_count, uint32_t port_discovery_timeout_us)

 Finishes initializing the ``TF_HalCommon`` instance associated with the given ``TF_HalContext``.
 This is normally the last step in the initialization. SPI communication must be possible here.
 The function expects the number of usable ports as well as a timeout in microseconds, for how long
 the bindungs should try to reach a device under one of the ports.
 :c:func:`tf_hal_common_prepare` then builds a list of reachable devices and stores it in the ``TF_HalCommon`` instance.

Defining a ``TF_HalContext`` struct
-----------------------------------

The ``TF_HalContext`` struct holds all data necessary for the SPI
communication. It also stores an instance of ``TF_HalCommon``, an internal type required
once per HAL by the bindings, as well as as well as a Pointer to
an array of port mapping information (``TF_Port``).

The ``TF_Port`` struct can be completely customized to store for example the
chip select pin associated with a port, it's name, the SPI hardware to use if
multiple are available, etc. See the port structs in :file:`hal_arduino_esp32/hal_arduino_esp32.h`
and :file:`hal_linux/hal_linux.h` for examples.

Bricklets are identified by their UID as well as the port over which they are reachable.
A port typically maps to the chip select pin that must be toggled to transfer data over
SPI to the Bricklet. Some HAL functions receive a port ID, this is often an index
into an array of ``TF_Port``.

Implementation of ``tf_hal_create`` and ``tf_hal_destroy``
----------------------------------------------------------

The next step after defining the ``TF_HalContext`` struct is implementing its initialization function
``tf_hal_create``, that handles the following tasks:

* Set the ``TF_HalContext`` struct to a defined state.

* Initialize the ``TF_HalCommon`` instance with :c:func:`tf_hal_common_icreate`

* Prepare the SPI communication
  When your initialization function returns, SPI communication must be possible to all attached devices.
  All chip select pins must be set to HIGH (e.g. disabled) See below for details about the SPI communication.

* Call :c:func:`tf_hal_common_prepare`
  This is typically the last step in the initialization. SPI communication must be possible here.
  The function expects the number of usable ports as well as a timeout in micro seconds, for how long
  the bindings should try to reach a device over one of the ports.
  :c:func:`tf_hal_common_prepare` then builds a list of reachable devices and stores it in the ``TF_HalCommon`` instance.

By convention, ``tf_hal_create`` returns an int that is set to ``TF_E_OK`` on success.
If the initialization fails, you can return any error code defined in :file:`bindings/errors.h`
as well as defining custom error codes for your HAL in its header file.
The error codes from -99 to -1 are reserved for the bindings, so the first valid error code is -100.

After this, implement ``tf_hal_destroy`` that ends the communication. Note that
it should be possible to create the HAL with ``tf_hal_create``, use it, destroy
it with ``tf_hal_destroy`` and then recreate it with ``tf_hal_create``. The
recreated HAL must usable again.

Implementation of the required HAL functions
--------------------------------------------

Finally all of the following functions must be implemented.
They are defined in :file:`bindings/hal_common.h` between
``// BEGIN - To be implemented by the specific HAL``
and
``// END - To be implemented by the specific HAL``
All functions returning an int should return ``TF_E_OK`` on success.

.. c:function:: int tf_hal_chip_select(TF_HalContext *hal, uint8_t port_id, bool enable)

 If enable is true, this function selects the port with the given ID for the following SPI communication.
 If enable is false, this function deselects the port with the given ID.

 Depending on the platform, more work has to be done here. For example on
 an Arduino, ``begin/endTransaction`` must be called to make sure, that the SPI
 configuration is applied. The bindings make sure, that only one chip select
 pin is enabled at the same time.

 .. note:
  ``enable`` is true when the chip select pin is to be set to LOW. See below for details.

.. c:function:: int tf_hal_transceive(TF_HalContext *hal, uint8_t port_id, const uint8_t *write_buffer, uint8_t *read_buffer, uint32_t length)

 Transmits length bytes of data from the ``write_buffer`` to the bricklet while receiving the same
 amount of bytes (as SPI is bi-directional) into the ``read_buffer``. The buffers are always big enough
 to read/write ``length`` bytes.

 This function will only be called with a port ID after :c:func:`tf_hal_chip_select` has been called with
 the same port ID and ``enable=true``.

 If your platform supports DMA, you can initiate a transfer here, but have to block until it's done.

 If your platform supports cooperative multitasking as well, yield after initiating a transfer.
 To make sure, no one else uses the bindings, while the transfer is in progress, you can
 lock the bindings with

 .. code-block:: c

  TF_HalCommon *common = tf_hal_get_common(hal);
  common->locked = true

 Don't forget to unlock the bindings again when the transfer is done.

.. c:function:: uint32_t tf_hal_current_time_us(TF_HalContext *hal)

 Returns the current time in microseconds. This time has no relation to any "real" time,
 but is monotonic except for overflows.

.. c:function:: void tf_hal_sleep_us(TF_HalContext *hal, uint32_t us)

 Blocks for the given time in microseconds. If your platform supports cooperative
 multitasking, lock the bindings and yield if the time to sleep for is large enough.
 See :c:func:`tf_hal_transceive` for details.

.. c:function:: TF_HalCommon *tf_hal_get_common(TF_HalContext *hal)

 Returns the ``TF_HalCommon`` instance associated with the given ``TF_HalContext``.

.. c:function:: char tf_hal_get_port_name(TF_HalContext *hal, uint8_t port_id)

 Returns the port name (typically a letter between 'A' and 'Z') for the given port ID.
 This name will be patched into ``get_identity`` results for devices directly connected
 to the host.

.. c:function:: void tf_hal_log_message(const char *msg, uint32_t len)

 Logs the given message. The message has a length of ``len`` and is not null-terminated.
 Depending on the platform you can use a serial console (Arduino) or
 the standard output (Linux). Writing the log to a file is also possible.

 .. note:
  This function may not assume that the HAL was initialized successfully, to be able
  to log errors that occurred while initializing the HAL.

.. c:function:: void tf_hal_log_newline()

 Logs the platform specific newline character(s).

.. c:function:: const char *tf_hal_strerror(int rc)

 Returns an error description for the given error code. To be as space efficient
 as possible, this function can be customized as follows:

 * Removing ``TF_IMPLEMENT_STRERROR`` removes the function completely
 * All string literals are wrapped in ``TF_CONST_STRING`` to allow moving them into static memory

 Error codes used by the bindings are handled by including :file:`bindings/errors.inc`.

 Use the following skeleton when implementing this function:

 .. code-block:: c

  #ifdef TF_IMPLEMENT_STRERROR
  const char *tf_hal_strerror(int rc) {
      #define TF_CONST_STRING(x) x
      switch(rc) {
          #include "../bindings/errors.inc"
          /* Add HAL specific error codes here, for example:
          case TF_E_OPEN_GPIO_FAILED:
              return TF_CONST_STRING("failed to open GPIO");
          */
          default:
              return TF_CONST_STRING("unknown error");
      }
      #undef TF_CONST_STRING
  }
  #endif
