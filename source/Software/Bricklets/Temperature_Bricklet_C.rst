..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - Temperature Bricklet
========================

.. _temperature_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: Temperature_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Temperature_Bricklet_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Temperature_Bricklet_C_example_threshold.c
 :language: c
 :linenos:
 :tab-width: 4

.. _temperature_bricklet_c_api:

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


.. c:function:: void temperature_create(Temperature *temperature, const char *uid)

 Creates a Temperature object with the unique device ID *uid*::

    Temperature temperature;
    temperature_create(&temperature, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <temperature_bricklet_c_examples>`).


.. c:function:: int temperature_get_temperature(Temperature *temperature, int16_t *ret_temperature)

 Returns the temperature of the sensor. The value
 has a range of -2500 to 8500 and is given in °C/100,
 e.g. a value of 4223 means that a temperature of 42.23 °C is measured.
 
 If you want to get the temperature periodically, it is recommended 
 to use the callback :c:data:`TEMPERATURE_CALLBACK_TEMPERATURE` and set the period with 
 :c:func:`temperature_set_temperature_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void temperature_register_callback(Temperature *temperature, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <temperature_bricklet_c_callbacks>`.


.. c:function:: int temperature_set_temperature_callback_period(Temperature *temperature, uint32_t period)

 Sets the period in ms with which the :c:data:`TEMPERATURE_CALLBACK_TEMPERATURE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`TEMPERATURE_CALLBACK_TEMPERATURE` is only called if the temperature has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int temperature_get_temperature_callback_period(Temperature *temperature, uint32_t *ret_period)

 Returns the period as set by :c:func:`temperature_set_temperature_callback_period`.
 
.. c:function:: int temperature_set_temperature_callback_threshold(Temperature *temperature, char option, int16_t min, int16_t max)

 Sets the thresholds for the :c:data:`TEMPERATURE_CALLBACK_TEMPERATURE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the temperature is *outside* the min and max values"
  "'i'", "Callback is called when the temperature is *inside* the min and max values"
  "'<'", "Callback is called when the temperature is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the temperature is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int temperature_get_temperature_callback_threshold(Temperature *temperature, char *ret_option, int16_t *ret_min, int16_t *ret_max)

 Returns the threshold as set by :c:func:`temperature_set_temperature_callback_threshold`.
 
.. c:function:: int temperature_set_debounce_period(Temperature *temperature, uint32_t debounce)

 Sets the period in ms with which the threshold callback
 
  :c:data:`TEMPERATURE_CALLBACK_TEMPERATURE_REACHED`
 
 is called, if the threshold
 
  :c:func:`temperature_set_temperature_callback_threshold`
 
 keeps beeing reached.
 
 The default value is 100.
 
.. c:function:: int temperature_get_debounce_period(Temperature *temperature, uint32_t *ret_debounce)

 Returns the debounce period as set by :c:func:`temperature_set_debounce_period`.
 


.. _temperature_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    temperature_register_callback(&temperature, TEMPERATURE_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: TEMPERATURE_CALLBACK_TEMPERATURE

 .. c:var:: signature: void callback(int16_t temperature)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`temperature_set_temperature_callback_period`. The parameter is the temperature of the
 sensor.
 
 :c:data:`TEMPERATURE_CALLBACK_TEMPERATURE` is only called if the temperature has changed since the
 last call.
 
.. c:var:: TEMPERATURE_CALLBACK_TEMPERATURE_REACHED

 .. c:var:: signature: void callback(int16_t temperature)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`temperature_set_temperature_callback_threshold` is reached.
 The parameter is the temperature of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`temperature_set_debounce_period`.
 


