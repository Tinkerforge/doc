..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - AmbientLight Bricklet
=========================

.. _ambient_light_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: AmbientLight_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: AmbientLight_Bricklet_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: AmbientLight_Bricklet_C_example_threshold.c
 :language: c
 :linenos:
 :tab-width: 4

.. _ambient_light_bricklet_c_api:

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


.. c:function:: void ambient_light_create(AmbientLight *ambient_light, const char *uid)

 Creates a AmbientLight object with the unique device ID *uid*::

    AmbientLight ambient_light;
    ambient_light_create(&ambient_light, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <ambient_light_bricklet_c_examples>`).


.. c:function:: int ambient_light_get_illuminance(AmbientLight *ambient_light, uint16_t *ret_illuminance)

 Returns the illuminance of the ambient light sensor. The value
 has a range of 0 to 9000 and is given in Lux/10, i.e. a value
 of 4500 means that an illuminance of 450 Lux is measured.
 
 If you want to get the illuminance periodically, it is recommended to use the
 callback :c:data:`AMBIENT_LIGHT_CALLBACK_ILLUMINANCE` and set the period with 
 :c:func:`ambient_light_set_illuminance_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int ambient_light_get_analog_value(AmbientLight *ambient_light, uint16_t *ret_value)

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :c:func:`ambient_light_get_illuminance` is averaged over several samples
   to yield less noise, while :c:func:`ambient_light_get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :c:func:`ambient_light_get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
   Also, the analog to digital converter covers three different ranges that are
   set dynamically depending on the light intensity. It is impossible to
   distinguish between these ranges with the analog value.
 
 If you want the analog value periodically, it is recommended to use the 
 callback :c:data:`AMBIENT_LIGHT_CALLBACK_ANALOG_VALUE` and set the period with 
 :c:func:`ambient_light_set_analog_value_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void ambient_light_register_callback(AmbientLight *ambient_light, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <ambient_light_bricklet_c_callbacks>`.


.. c:function:: int ambient_light_set_illuminance_callback_period(AmbientLight *ambient_light, uint32_t period)

 Sets the period in ms with which the :c:data:`AMBIENT_LIGHT_CALLBACK_ILLUMINANCE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`AMBIENT_LIGHT_CALLBACK_ILLUMINANCE` is only called if the illuminance has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int ambient_light_get_illuminance_callback_period(AmbientLight *ambient_light, uint32_t *ret_period)

 Returns the period as set by :c:func:`ambient_light_set_illuminance_callback_period`.
 
.. c:function:: int ambient_light_set_analog_value_callback_period(AmbientLight *ambient_light, uint32_t period)

 Sets the period in ms with which the :c:data:`AMBIENT_LIGHT_CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`AMBIENT_LIGHT_CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int ambient_light_get_analog_value_callback_period(AmbientLight *ambient_light, uint32_t *ret_period)

 Returns the period as set by :c:func:`ambient_light_set_analog_value_callback_period`.
 
.. c:function:: int ambient_light_set_illuminance_callback_threshold(AmbientLight *ambient_light, char option, int16_t min, int16_t max)

 Sets the thresholds for the :c:data:`AMBIENT_LIGHT_CALLBACK_ILLUMINANCE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the illuminance is *outside* the min and max values"
  "'i'", "Callback is called when the illuminance is *inside* the min and max values"
  "'<'", "Callback is called when the illuminance is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the illuminance is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int ambient_light_get_illuminance_callback_threshold(AmbientLight *ambient_light, char *ret_option, int16_t *ret_min, int16_t *ret_max)

 Returns the threshold as set by :c:func:`ambient_light_set_illuminance_callback_threshold`.
 
.. c:function:: int ambient_light_set_analog_value_callback_threshold(AmbientLight *ambient_light, char option, uint16_t min, uint16_t max)

 Sets the thresholds for the :c:data:`AMBIENT_LIGHT_CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the illuminance is *outside* the min and max values"
  "'i'", "Callback is called when the illuminance is *inside* the min and max values"
  "'<'", "Callback is called when the illuminance is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the illuminance is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int ambient_light_get_analog_value_callback_threshold(AmbientLight *ambient_light, char *ret_option, uint16_t *ret_min, uint16_t *ret_max)

 Returns the threshold as set by :c:func:`ambient_light_set_analog_value_callback_threshold`.
 
.. c:function:: int ambient_light_set_debounce_period(AmbientLight *ambient_light, uint32_t debounce)

 Sets the period in ms with which the threshold callbacks
 
  :c:data:`AMBIENT_LIGHT_CALLBACK_ILLUMINANCE_REACHED`, :c:data:`AMBIENT_LIGHT_CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :c:func:`ambient_light_set_illuminance_callback_threshold`, :c:func:`ambient_light_set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. c:function:: int ambient_light_get_debounce_period(AmbientLight *ambient_light, uint32_t *ret_debounce)

 Returns the debounce period as set by :c:func:`ambient_light_set_debounce_period`.
 


.. _ambient_light_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    ambient_light_register_callback(&ambient_light, AMBIENTLIGHT_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: AMBIENT_LIGHT_CALLBACK_ILLUMINANCE

 .. c:var:: signature: void callback(uint16_t illuminance)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`ambient_light_set_illuminance_callback_period`. The parameter is the illuminance of the
 ambient light sensor.
 
 :c:data:`AMBIENT_LIGHT_CALLBACK_ILLUMINANCE` is only called if the illuminance has changed since the
 last call.
 
.. c:var:: AMBIENT_LIGHT_CALLBACK_ANALOG_VALUE

 .. c:var:: signature: void callback(uint16_t value)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`ambient_light_set_analog_value_callback_period`. The parameter is the analog value of the
 ambient light sensor.
 
 :c:data:`AMBIENT_LIGHT_CALLBACK_ANALOG_VALUE` is only called if the illuminance has changed since the
 last call.
 
.. c:var:: AMBIENT_LIGHT_CALLBACK_ILLUMINANCE_REACHED

 .. c:var:: signature: void callback(uint16_t illuminance)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`ambient_light_set_illuminance_callback_threshold` is reached.
 The parameter is the illuminance of the ambient light sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`ambient_light_set_debounce_period`.
 
.. c:var:: AMBIENT_LIGHT_CALLBACK_ANALOG_VALUE_REACHED

 .. c:var:: signature: void callback(uint16_t value)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`ambient_light_set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the ambient light sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`ambient_light_set_debounce_period`.
 


