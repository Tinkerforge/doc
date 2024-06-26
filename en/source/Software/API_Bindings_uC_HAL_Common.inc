.. cpp:function:: void tf_hal_set_timeout(TF_HAL *hal, uint32_t timeout_us)

 Sets the timeout in microseconds for getters and for setters for which the
 response expected flag is activated.

 The default timeout is 2500000 (2.5 seconds).

.. cpp:function:: uint32_t tf_hal_get_timeout(TF_HAL *hal)

 Returns the timeout as set by :cpp:func:`tf_hal_set_timeout`.

.. cpp:function:: int tf_hal_get_device_info(TF_HAL *hal, uint16_t index, char ret_uid[7], char *ret_port_name, uint16_t *ret_device_id)

 Returns the UID, port and :ref:`device identifier <device_identifier>` of the nth (=index) detected device.
 This function returns ``TF_E_DEVICE_NOT_FOUND`` if the index was equal or higher than the number of detected devices.
 To list all devices you can call this function in a loop with growing index until ``TF_E_DEVICE_NOT_FOUND`` is returned once.

.. cpp:function:: int tf_hal_callback_tick(TF_HAL *hal, uint32_t timeout_us)

 Polls for callbacks on all devices with an registered callback handler. Will block for the given
 timeout in microseconds.

 This function can be used in a non-blocking fashion by calling it with a timeout of 0. The bindings
 will then poll a single device for one callback, by clocking out a single byte over SPI,
 returning immediately if no callback is available. If the device starts sending a callback packet,
 it will be received, acked and the callback handler will be called.

 The polling is scheduled round-robin over multiple calls, so even if you only poll with a timeout
 of 0, all devices will be polled as fairly as possble.

.. cpp:function:: bool tf_hal_deadline_elapsed(TF_HAL *hal, uint32_t deadline_us)

 Returns true if the deadline in microseconds is elapsed, false otherwise. Robust against
 overflows up to ``UINT32_MAX / 2``.

.. cpp:function:: int tf_hal_get_error_counters(TF_HAL *hal, char port_name, uint32_t *ret_spitfp_error_count_checksum, uint32_t *ret_spitfp_error_count_frame, uint32_t *ret_tfp_error_count_frame, uint32_t *ret_tfp_error_count_unexpected)

 Returns the error counters for the given port. The following errors are counted:

 * ``spitfp_error_count_checksum``: Received SPITFP packets that where ignored because of a wrong checksum
 * ``spitfp_error_count_frame``: Received SPITFP packets with an invalid length
 * ``tfp_error_count_frame``: Received TFP packets with an invalid length
 * ``tfp_error_count_unexpected``: Received TFP packets that where unexpected because they responded to unknown requests

.. cpp:function:: void tf_hal_log_error(const char *format, ...)

 Logs an error if the log level in :file:`bindings/config.h` is ``TF_LOG_LEVEL_ERROR`` or more.
 Supports a subset of the standard printf syntax. See :cpp:func:`tf_hal_printf` for details.

.. cpp:function:: void tf_hal_log_info(const char *format, ...)

 Logs an information if the log level in :file:`bindings/config.h` is ``TF_LOG_LEVEL_INFO`` or more.
 Supports a subset of the standard printf syntax. See :cpp:func:`tf_hal_printf` for details.

.. cpp:function:: void tf_hal_log_debug(const char *format, ...)

 Logs a debug message if the log level in :file:`bindings/config.h` is ``TF_LOG_LEVEL_DEBUG`` or more.
 Supports a subset of the standard printf syntax. See :cpp:func:`tf_hal_printf` for details.

.. cpp:function:: void tf_hal_printf(const char *format, ...)

 This function is a minimalistic printf implementation.
 The following placeholders are supported:

 * ``%[prefix]u``: An unsigned integer value printed in base 10
 * ``%[prefix]d``: A signed integer value printed in base 10
 * ``%[prefix]b``: An unsigned integer value printed in base 2
 * ``%[prefix]x`` and ``%[prefix]X``: An unsigned integer value printed in base 16, in both cases with lower-case letters
 * ``%c``: A single character
 * ``%s``: A zero terminated string
 * ``%%``: A percent sign

 With the prefix, you can control the width of printed integers.
 Valid prefixes are ``I8``, ``I16``, ``I32`` and ``I64``.
 For example using the placeholder ``%I16x`` will print a 16 bit integer hexadecimal.

 No padding, grouping , l-modifiers or similar, or floats are supported.
 The newline character ``\n`` is translated to the platform specific newline character(s).

.. cpp:function:: const char *tf_hal_strerror(int e_code)

 Returns an error string for the given error code.

.. cpp:function:: const char *tf_get_device_display_name(uint16_t device_id)

 Returns the display name for the given device identifier.
