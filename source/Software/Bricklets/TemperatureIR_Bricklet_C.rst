..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - TemperatureIR Bricklet
==========================

.. _temperature_ir_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: TemperatureIR_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

Water Boiling
^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: TemperatureIR_Bricklet_C_example_water_boiling.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: TemperatureIR_Bricklet_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

.. _temperature_ir_bricklet_c_api:

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


.. c:function:: void temperature_ir_create(TemperatureIR *temperature_ir, const char *uid)

 Creates a TemperatureIR object with the unique device ID *uid*::

    TemperatureIR temperature_ir;
    temperature_ir_create(&temperature_ir, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <temperature_ir_bricklet_c_examples>`).


.. c:function:: int temperature_ir_get_ambient_temperature(TemperatureIR *temperature_ir, int16_t *ret_temperature)

 Returns the ambient temperature of the sensor. The value
 has a range of -400 to 1250 and is given in °C/10,
 e.g. a value of 423 means that an ambient temperature of 42.3 °C is 
 measured.
 
 If you want to get the ambient temperature periodically, it is recommended 
 to use the callback :c:data:`TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE` and set the period with 
 :c:func:`temperature_ir_set_ambient_temperature_callback_period`.
 
.. c:function:: int temperature_ir_get_object_temperature(TemperatureIR *temperature_ir, int16_t *ret_temperature)

 Returns the object temperature of the sensor, i.e. the temperature
 of the surface of the object the sensor is aimed at. The value
 has a range of -700 to 3800 and is given in °C/10,
 e.g. a value of 30001 means that a temperature of 300.01 °C is measured
 on the surface of the object.
 
 The temperature of different materials is dependent on their `emissivity 
 <http://en.wikipedia.org/wiki/Emissivity>`_. The emissivity of the material
 can be set with :c:func:`temperature_ir_set_emissivity`.
 
 If you want to get the object temperature periodically, it is recommended 
 to use the callback :c:data:`TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE` and set the period with 
 :c:func:`temperature_ir_set_object_temperature_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int temperature_ir_set_emissivity(TemperatureIR *temperature_ir, uint16_t emissivity)

 Sets the `emissivity <http://en.wikipedia.org/wiki/Emissivity>`_ that is 
 used to calculate the surface temperature as returned by 
 :c:func:`temperature_ir_get_object_temperature`. 
 
 The emissivity is usually given as a value between 0.0 and 1.0. A list of
 emissivities of different materials can be found 
 `here <http://www.infrared-thermography.com/material.htm>`_.
 
 The parameter of :c:func:`temperature_ir_set_emissivity` has to be given with a factor of
 65535 (16 bit). For example: An emissivity of 0.1 can be set with the 
 value 6553, an emissivity of 0.5 with the value 32767 and so on.
 
  .. note::
   If you need a precise measurement for the object temperature, it is
   absolutely crucial that you also provide a precise emissivity.
 
 The default emissivity is 1.0 (value of 65535) and the minimum emissivity the
 sensor can handle is 0.1 (value of 6553).
 
.. c:function:: int temperature_ir_get_emissivity(TemperatureIR *temperature_ir, uint16_t *ret_emissivity)

 Returns the emissivity as set by :c:func:`temperature_ir_set_emissivity`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void temperature_ir_register_callback(TemperatureIR *temperature_ir, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <temperature_ir_bricklet_c_callbacks>`.


.. c:function:: int temperature_ir_set_ambient_temperature_callback_period(TemperatureIR *temperature_ir, uint32_t period)

 Sets the period in ms with which the :c:data:`TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE` is only called if the temperature has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int temperature_ir_get_ambient_temperature_callback_period(TemperatureIR *temperature_ir, uint32_t *ret_period)

 Returns the period as set by :c:func:`temperature_ir_set_ambient_temperature_callback_period`.
 
.. c:function:: int temperature_ir_set_object_temperature_callback_period(TemperatureIR *temperature_ir, uint32_t period)

 Sets the period in ms with which the :c:data:`TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE` is only called if the temperature has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int temperature_ir_get_object_temperature_callback_period(TemperatureIR *temperature_ir, uint32_t *ret_period)

 Returns the period as set by :c:func:`temperature_ir_set_object_temperature_callback_period`.
 
.. c:function:: int temperature_ir_set_ambient_temperature_callback_threshold(TemperatureIR *temperature_ir, char option, int16_t min, int16_t max)

 Sets the thresholds for the :c:data:`TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE_REACHED` callback. 
 
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
 
.. c:function:: int temperature_ir_get_ambient_temperature_callback_threshold(TemperatureIR *temperature_ir, char *ret_option, int16_t *ret_min, int16_t *ret_max)

 Returns the threshold as set by :c:func:`temperature_ir_set_ambient_temperature_callback_threshold`.
 
.. c:function:: int temperature_ir_set_object_temperature_callback_threshold(TemperatureIR *temperature_ir, char option, int16_t min, int16_t max)

 Sets the thresholds for the :c:data:`TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE_REACHED` callback. 
 
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
 
.. c:function:: int temperature_ir_get_object_temperature_callback_threshold(TemperatureIR *temperature_ir, char *ret_option, int16_t *ret_min, int16_t *ret_max)

 Returns the threshold as set by :c:func:`temperature_ir_set_ambient_temperature_callback_threshold`.
 
.. c:function:: int temperature_ir_set_debounce_period(TemperatureIR *temperature_ir, uint32_t debounce)

 Sets the period in ms with which the threshold callbacks
 
  :c:data:`TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE_REACHED`, :c:data:`TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE_REACHED`
 
 are called, if the thresholds 
 
  :c:func:`temperature_ir_set_ambient_temperature_callback_threshold`, :c:func:`temperature_ir_set_object_temperature_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. c:function:: int temperature_ir_get_debounce_period(TemperatureIR *temperature_ir, uint32_t *ret_debounce)

 Returns the debounce period as set by :c:func:`temperature_ir_set_debounce_period`.
 


.. _temperature_ir_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    temperature_ir_register_callback(&temperature_ir, TEMPERATUREIR_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE

 .. c:var:: signature: void callback(int16_t temperature)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`temperature_ir_set_ambient_temperature_callback_period`. The parameter is the ambient 
 temperature of the sensor.
 
 :c:data:`TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE` is only called if the ambient temperature 
 has changed since the last call.
 
.. c:var:: TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE

 .. c:var:: signature: void callback(int16_t temperature)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`temperature_ir_set_object_temperature_callback_period`. The parameter is the object 
 temperature of the sensor.
 
 :c:data:`TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE` is only called if the object temperature 
 has changed since the last call.
 
.. c:var:: TEMPERATURE_IR_CALLBACK_AMBIENT_TEMPERATURE_REACHED

 .. c:var:: signature: void callback(int16_t temperature)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`temperature_ir_set_ambient_temperature_callback_threshold` is reached.
 The parameter is the ambient temperature of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`temperature_ir_set_debounce_period`.
 
.. c:var:: TEMPERATURE_IR_CALLBACK_OBJECT_TEMPERATURE_REACHED

 .. c:var:: signature: void callback(int16_t temperature)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`temperature_ir_set_object_temperature_callback_threshold` is reached.
 The parameter is the object temperature of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`temperature_ir_set_debounce_period`.
 


