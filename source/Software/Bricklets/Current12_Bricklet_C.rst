..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - Current12 Bricklet
======================

.. _current12_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: Current12_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Current12_Bricklet_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Current12_Bricklet_C_example_threshold.c
 :language: c
 :linenos:
 :tab-width: 4

.. _current12_bricklet_c_api:

API
---

Every function of the c bindings returns an integer which describes an
error code. Data returned from the device, when a getter is called,
is handled via call by reference. These parameters are labelled with the
``ret_`` prefix.

Possible error codes are

 * E_OK = 0
 * E_TIMEOUT = -1
 * E_NO_STREAM_SOCKET = -2
 * E_HOSTNAME_INVALID = -3
 * E_NO_CONNECT = -4
 * E_NO_THREAD = -5
 * E_NOT_ADDED = -6

as defined in :file:`ip_connection.h`.


Basic Methods
^^^^^^^^^^^^^


.. c:function:: void current12_create(Current12 *current12, const char *uid)

 Creates a Current12 object with the unique device ID *uid*::

    Current12 current12;
    current12_create(&current12, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <current12_bricklet_c_examples>`).


.. c:function:: int current12_get_current(Current12 *current12, int16_t *ret_current)

 Returns the current of the sensor. The value is in mA
 and between -12500mA and 12500.
 
 If you want to get the current periodically, it is recommended to use the
 callback :c:data:`CURRENT12_CALLBACK_CURRENT` and set the period with 
 :c:func:`current12_set_current_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int current12_calibrate(Current12 *current12)

 Calibrates the 0 value of the sensor. You have to call this function
 when there is no current present. 
 
 The zero point of the current sensor
 is depending on the exact properties of the analog to digital converter,
 the length of the Bricklet cable and the temperature. Thus, if you change
 the Brick or the environment in which the Bricklet is used, you might
 have to recalibrate.
 
 The resulting calibration will be saved on the eeprom of the Current
 Bricklet.
 
.. c:function:: int current12_is_over_current(Current12 *current12, bool *ret_over)

 Returns true if more than 12.5A were measured.
 
  .. note::
   To reset this value you have to power cycle the Bricklet.
 
 
.. c:function:: int current12_get_analog_value(Current12 *current12, uint16_t *ret_value)

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :c:func:`current12_get_current` is averaged over several samples
   to yield less noise, while :c:func:`current12_get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :c:func:`current12_get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
 If you want the analog value periodically, it is recommended to use the 
 callback :c:data:`CURRENT12_CALLBACK_ANALOG_VALUE` and set the period with 
 :c:func:`current12_set_analog_value_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void current12_register_callback(Current12 *current12, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <current12_bricklet_c_callbacks>`.


.. c:function:: int current12_set_current_callback_period(Current12 *current12, uint32_t period)

 Sets the period in ms with which the :c:data:`CURRENT12_CALLBACK_CURRENT` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`CURRENT12_CALLBACK_CURRENT` is only called if the current has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int current12_get_current_callback_period(Current12 *current12, uint32_t *ret_period)

 Returns the period as set by :c:func:`current12_set_current_callback_period`.
 
.. c:function:: int current12_set_analog_value_callback_period(Current12 *current12, uint32_t period)

 Sets the period in ms with which the :c:data:`CURRENT12_CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`CURRENT12_CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int current12_get_analog_value_callback_period(Current12 *current12, uint32_t *ret_period)

 Returns the period as set by :c:func:`current12_set_analog_value_callback_period`.
 
.. c:function:: int current12_set_current_callback_threshold(Current12 *current12, char option, int16_t min, int16_t max)

 Sets the thresholds for the :c:data:`CURRENT12_CALLBACK_CURRENT_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the current is *outside* the min and max values"
  "'i'", "Callback is called when the current is *inside* the min and max values"
  "'<'", "Callback is called when the current is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the current is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int current12_get_current_callback_threshold(Current12 *current12, char *ret_option, int16_t *ret_min, int16_t *ret_max)

 Returns the threshold as set by :c:func:`current12_set_current_callback_threshold`.
 
.. c:function:: int current12_set_analog_value_callback_threshold(Current12 *current12, char option, uint16_t min, uint16_t max)

 Sets the thresholds for the :c:data:`CURRENT12_CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the current is *outside* the min and max values"
  "'i'", "Callback is called when the current is *inside* the min and max values"
  "'<'", "Callback is called when the current is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the current is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int current12_get_analog_value_callback_threshold(Current12 *current12, char *ret_option, uint16_t *ret_min, uint16_t *ret_max)

 Returns the threshold as set by :c:func:`current12_set_analog_value_callback_threshold`.
 
.. c:function:: int current12_set_debounce_period(Current12 *current12, uint32_t debounce)

 Sets the period in ms with which the threshold callbacks
 
  :c:data:`CURRENT12_CALLBACK_CURRENT_REACHED`, :c:data:`CURRENT12_CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :c:func:`current12_set_current_callback_threshold`, :c:func:`current12_set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. c:function:: int current12_get_debounce_period(Current12 *current12, uint32_t *ret_debounce)

 Returns the debounce period as set by :c:func:`current12_set_debounce_period`.
 


.. _current12_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    current12_register_callback(&current12, CURRENT12_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: CURRENT12_CALLBACK_CURRENT

 .. c:var:: signature: void callback(int16_t current)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`current12_set_current_callback_period`. The parameter is the current of the
 sensor.
 
 :c:data:`CURRENT12_CALLBACK_CURRENT` is only called if the current has changed since the
 last call.
 
.. c:var:: CURRENT12_CALLBACK_ANALOG_VALUE

 .. c:var:: signature: void callback(uint16_t value)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`current12_set_analog_value_callback_period`. The parameter is the analog value of the
 sensor.
 
 :c:data:`CURRENT12_CALLBACK_ANALOG_VALUE` is only called if the current has changed since the
 last call.
 
.. c:var:: CURRENT12_CALLBACK_CURRENT_REACHED

 .. c:var:: signature: void callback(int16_t current)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`current12_set_current_callback_threshold` is reached.
 The parameter is the current of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`current12_set_debounce_period`.
 
.. c:var:: CURRENT12_CALLBACK_ANALOG_VALUE_REACHED

 .. c:var:: signature: void callback(uint16_t value)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`current12_set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`current12_set_debounce_period`.
 
.. c:var:: CURRENT12_CALLBACK_OVER_CURRENT

 .. c:var:: signature: void callback(void)
    :noindex:


 This callback is called when an over current is measured
 (see :c:func:`current12_is_over_current`).
 


