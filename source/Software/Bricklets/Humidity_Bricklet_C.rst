..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _humidity_bricklet_c:

C - Humidity Bricklet
=====================

.. _humidity_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: Humidity_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Humidity_Bricklet_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Humidity_Bricklet_C_example_threshold.c
 :language: c
 :linenos:
 :tab-width: 4

.. _humidity_bricklet_c_api:

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


.. c:function:: void humidity_create(Humidity *humidity, const char *uid)

 Creates a Humidity object with the unique device ID *uid*::

    Humidity humidity;
    humidity_create(&humidity, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <humidity_bricklet_c_examples>`).


.. c:function:: int humidity_get_humidity(Humidity *humidity, uint16_t *ret_humidity)

 Returns the humidity of the sensor. The value
 has a range of 0 to 1000 and is given in %RH/10 (Relative Humidity), 
 i.e. a value of 421 means that a humidity of 42.1 %RH is measured.
 
 If you want to get the humidity periodically, it is recommended to use the
 callback :c:data:`HUMIDITY_CALLBACK_HUMIDITY` and set the period with 
 :c:func:`humidity_set_humidity_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int humidity_get_analog_value(Humidity *humidity, uint16_t *ret_value)

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :c:func:`humidity_get_humidity` is averaged over several samples
   to yield less noise, while :c:func:`humidity_get_analog_value` gives back raw
   unfiltered analog values. The returned humidity value is calibrated for
   room temperatures, if you use the sensor in extreme cold or extreme
   warm enviroments, you might want to calculate the humidity from
   the analog value yourself. See the HIH 5030 datasheet (TODO: link).
 
 If you want the analog value periodically, it is recommended to use the 
 callback :c:data:`HUMIDITY_CALLBACK_ANALOG_VALUE` and set the period with 
 :c:func:`humidity_set_analog_value_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void humidity_register_callback(Humidity *humidity, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <humidity_bricklet_c_callbacks>`.


.. c:function:: int humidity_set_humidity_callback_period(Humidity *humidity, uint32_t period)

 Sets the period in ms with which the :c:data:`HUMIDITY_CALLBACK_HUMIDITY` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`HUMIDITY_CALLBACK_HUMIDITY` is only called if the humidity has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int humidity_get_humidity_callback_period(Humidity *humidity, uint32_t *ret_period)

 Returns the period as set by :c:func:`humidity_set_humidity_callback_period`.
 
.. c:function:: int humidity_set_analog_value_callback_period(Humidity *humidity, uint32_t period)

 Sets the period in ms with which the :c:data:`HUMIDITY_CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`HUMIDITY_CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int humidity_get_analog_value_callback_period(Humidity *humidity, uint32_t *ret_period)

 Returns the period as set by :c:func:`humidity_set_analog_value_callback_period`.
 
.. c:function:: int humidity_set_humidity_callback_threshold(Humidity *humidity, char option, int16_t min, int16_t max)

 Sets the thresholds for the :c:data:`HUMIDITY_CALLBACK_HUMIDITY_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the humidity is *outside* the min and max values"
  "'i'", "Callback is called when the humidity is *inside* the min and max values"
  "'<'", "Callback is called when the humidity is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the humidity is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int humidity_get_humidity_callback_threshold(Humidity *humidity, char *ret_option, int16_t *ret_min, int16_t *ret_max)

 Returns the threshold as set by :c:func:`humidity_set_humidity_callback_threshold`.
 
.. c:function:: int humidity_set_analog_value_callback_threshold(Humidity *humidity, char option, uint16_t min, uint16_t max)

 Sets the thresholds for the :c:data:`HUMIDITY_CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the humidity is *outside* the min and max values"
  "'i'", "Callback is called when the humidity is *inside* the min and max values"
  "'<'", "Callback is called when the humidity is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the humidity is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int humidity_get_analog_value_callback_threshold(Humidity *humidity, char *ret_option, uint16_t *ret_min, uint16_t *ret_max)

 Returns the threshold as set by :c:func:`humidity_set_analog_value_callback_threshold`.
 
.. c:function:: int humidity_set_debounce_period(Humidity *humidity, uint32_t debounce)

 Sets the period in ms with which the threshold callbacks
 
  :c:data:`HUMIDITY_CALLBACK_HUMIDITY_REACHED`, :c:data:`HUMIDITY_CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :c:func:`humidity_set_humidity_callback_threshold`, :c:func:`humidity_set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. c:function:: int humidity_get_debounce_period(Humidity *humidity, uint32_t *ret_debounce)

 Returns the debounce period as set by :c:func:`humidity_set_debounce_period`.
 


.. _humidity_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    humidity_register_callback(&humidity, HUMIDITY_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: HUMIDITY_CALLBACK_HUMIDITY

 .. c:var:: signature: void callback(uint16_t humidity)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`humidity_set_humidity_callback_period`. The parameter is the humidity of the
 sensor.
 
 :c:data:`HUMIDITY_CALLBACK_HUMIDITY` is only called if the humidity has changed since the
 last call.
 
.. c:var:: HUMIDITY_CALLBACK_ANALOG_VALUE

 .. c:var:: signature: void callback(uint16_t value)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`humidity_set_analog_value_callback_period`. The parameter is the analog value of the
 sensor.
 
 :c:data:`HUMIDITY_CALLBACK_ANALOG_VALUE` is only called if the humidity has changed since the
 last call.
 
.. c:var:: HUMIDITY_CALLBACK_HUMIDITY_REACHED

 .. c:var:: signature: void callback(uint16_t humidity)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`humidity_set_humidity_callback_threshold` is reached.
 The parameter is the humidity of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`humidity_set_debounce_period`.
 
.. c:var:: HUMIDITY_CALLBACK_ANALOG_VALUE_REACHED

 .. c:var:: signature: void callback(uint16_t value)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`humidity_set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`humidity_set_debounce_period`.
 


