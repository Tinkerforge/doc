..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - DistanceIR Bricklet
=======================

.. _distance_ir_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: DistanceIR_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: DistanceIR_Bricklet_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: DistanceIR_Bricklet_C_example_threshold.c
 :language: c
 :linenos:
 :tab-width: 4

.. _distance_ir_bricklet_c_api:

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


.. c:function:: void distance_ir_create(DistanceIR *distance_ir, const char *uid)

 Creates a DistanceIR object with the unique device ID *uid*::

    DistanceIR distance_ir;
    distance_ir_create(&distance_ir, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <distance_ir_bricklet_c_examples>`).


.. c:function:: int distance_ir_get_distance(DistanceIR *distance_ir, uint16_t *ret_distance)

 Returns the distance of the sensor. The value is in mm and
 between TODO
 
 If you want to get the distance periodically, it is recommended to use the
 callback :c:data:`DISTANCE_IR_CALLBACK_DISTANCE` and set the period with 
 :c:func:`distance_ir_set_distance_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int distance_ir_get_analog_value(DistanceIR *distance_ir, uint16_t *ret_value)

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :c:func:`distance_ir_get_distance` is averaged over several samples
   to yield less noise, while :c:func:`distance_ir_get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :c:func:`distance_ir_get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
 If you want the analog value periodically, it is recommended to use the 
 callback :c:data:`DISTANCE_IR_CALLBACK_ANALOG_VALUE` and set the period with 
 :c:func:`distance_ir_set_analog_value_callback_period`.
 
.. c:function:: int distance_ir_set_sampling_point(DistanceIR *distance_ir, uint8_t position, uint16_t distance)

 Sets a sampling point value to a specific position of the lookup table.
 The lookup table is comprised of 128 equidistant analog values with
 corresponding distances.
 
 If you measure a distance of 50cm at the analog value 2048, you have
 shoud call this function with (64, 5000). The utilized analog to digital
 converter has a resolution of 12 bit. With 128 sampling points on the
 whole range, this means that every sampling point has a size of 32
 analog values. Thus the analog value 2048 has the corresponding sampling
 point 64 = 2048/32.
 
 Sampling points are saved on the eeprom of the Distance-IR Bricklet and
 loaded again on startup.
 
  .. note::
   An easy way to calibrate the sampling points of the Distace-IR Bricklet is
   implemented in brickv. If you want to calibrate your Bricklet it is
   highly recommended to use this implementation. 
 
 
.. c:function:: int distance_ir_get_sampling_point(DistanceIR *distance_ir, uint8_t position, uint16_t *ret_distance)

 Returns the distance to a sampling point position as set by
 :c:func:`distance_ir_set_sampling_point`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void distance_ir_register_callback(DistanceIR *distance_ir, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <distance_ir_bricklet_c_callbacks>`.


.. c:function:: int distance_ir_set_distance_callback_period(DistanceIR *distance_ir, uint32_t period)

 Sets the period in ms with which the :c:data:`DISTANCE_IR_CALLBACK_DISTANCE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`DISTANCE_IR_CALLBACK_DISTANCE` is only called if the distance has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int distance_ir_get_distance_callback_period(DistanceIR *distance_ir, uint32_t *ret_period)

 Returns the period as set by :c:func:`distance_ir_set_distance_callback_period`.
 
.. c:function:: int distance_ir_set_analog_value_callback_period(DistanceIR *distance_ir, uint32_t period)

 Sets the period in ms with which the :c:data:`DISTANCE_IR_CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`DISTANCE_IR_CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int distance_ir_get_analog_value_callback_period(DistanceIR *distance_ir, uint32_t *ret_period)

 Returns the period as set by :c:func:`distance_ir_set_analog_value_callback_period`.
 
.. c:function:: int distance_ir_set_distance_callback_threshold(DistanceIR *distance_ir, char option, int16_t min, int16_t max)

 Sets the thresholds for the :c:data:`DISTANCE_IR_CALLBACK_DISTANCE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the distance is *outside* the min and max values"
  "'i'", "Callback is called when the distance is *inside* the min and max values"
  "'<'", "Callback is called when the distance is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the distance is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int distance_ir_get_distance_callback_threshold(DistanceIR *distance_ir, char *ret_option, int16_t *ret_min, int16_t *ret_max)

 Returns the threshold as set by :c:func:`distance_ir_set_distance_callback_threshold`.
 
.. c:function:: int distance_ir_set_analog_value_callback_threshold(DistanceIR *distance_ir, char option, uint16_t min, uint16_t max)

 Sets the thresholds for the :c:data:`DISTANCE_IR_CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the distance is *outside* the min and max values"
  "'i'", "Callback is called when the distance is *inside* the min and max values"
  "'<'", "Callback is called when the distance is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the distance is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. c:function:: int distance_ir_get_analog_value_callback_threshold(DistanceIR *distance_ir, char *ret_option, uint16_t *ret_min, uint16_t *ret_max)

 Returns the threshold as set by :c:func:`distance_ir_set_analog_value_callback_threshold`.
 
.. c:function:: int distance_ir_set_debounce_period(DistanceIR *distance_ir, uint32_t debounce)

 Sets the period in ms with which the threshold callbacks
 
  :c:data:`DISTANCE_IR_CALLBACK_DISTANCE_REACHED`, :c:data:`DISTANCE_IR_CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :c:func:`distance_ir_set_distance_callback_threshold`, :c:func:`distance_ir_set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. c:function:: int distance_ir_get_debounce_period(DistanceIR *distance_ir, uint32_t *ret_debounce)

 Returns the debounce period as set by :c:func:`distance_ir_set_debounce_period`.
 


.. _distance_ir_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    distance_ir_register_callback(&distance_ir, DISTANCEIR_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: DISTANCE_IR_CALLBACK_DISTANCE

 .. c:var:: signature: void callback(uint16_t distance)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`distance_ir_set_distance_callback_period`. The parameter is the distance of the
 sensor.
 
 :c:data:`DISTANCE_IR_CALLBACK_DISTANCE` is only called if the distance has changed since the
 last call.
 
.. c:var:: DISTANCE_IR_CALLBACK_ANALOG_VALUE

 .. c:var:: signature: void callback(uint16_t value)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`distance_ir_set_analog_value_callback_period`. The parameter is the analog value of the
 sensor.
 
 :c:data:`DISTANCE_IR_CALLBACK_ANALOG_VALUE` is only called if the distance has changed since the
 last call.
 
.. c:var:: DISTANCE_IR_CALLBACK_DISTANCE_REACHED

 .. c:var:: signature: void callback(uint16_t distance)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`distance_ir_set_distance_callback_threshold` is reached.
 The parameter is the distance of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`distance_ir_set_debounce_period`.
 
.. c:var:: DISTANCE_IR_CALLBACK_ANALOG_VALUE_REACHED

 .. c:var:: signature: void callback(uint16_t value)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`distance_ir_set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`distance_ir_set_debounce_period`.
 


