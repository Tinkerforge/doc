..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - Joystick Bricklet
=====================

.. _joystick_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: Joystick_Bricklet_C_example_simple.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Joystick_Bricklet_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

Find Corners
^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Joystick_Bricklet_C_example_find_corners.c
 :language: c
 :linenos:
 :tab-width: 4

.. _joystick_bricklet_c_api:

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


.. c:function:: void joystick_create(Joystick *joystick, const char *uid)

 Creates a Joystick object with the unique device ID *uid*::

    Joystick joystick;
    joystick_create(&joystick, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <joystick_bricklet_c_examples>`).


.. c:function:: int joystick_get_position(Joystick *joystick, int16_t *ret_x, int16_t *ret_y)

 Returns the position of the Joystick. The value ranges between -100 and
 100 for both axis. The middle position of the joystick is x=0, y=0. The
 returned values are averaged and calibrated (see :c:func:`joystick_calibrate`).
 
 If you want to get the position periodically, it is recommended to use the
 callback :c:data:`JOYSTICK_CALLBACK_POSITION` and set the period with 
 :c:func:`joystick_set_position_callback_period`.
 
.. c:function:: int joystick_is_pressed(Joystick *joystick, bool *ret_pressed)

 Returns true if the button is pressed and false otherwise.
 
 It is recommended to use the :c:data:`JOYSTICK_CALLBACK_PRESSED` and :c:data:`JOYSTICK_CALLBACK_RELEASED` callbacks
 to handle the button.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int joystick_get_analog_value(Joystick *joystick, uint16_t *ret_x, uint16_t *ret_y)

 Returns the values as read by a 12 bit analog to digital converter.
 The values are between 0 and 4095 for both axis.
 
  .. note::
   The values returned by :c:func:`joystick_get_position` are averaged over several samples
   to yield less noise, while :c:func:`joystick_get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :c:func:`joystick_get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
 If you want the analog values periodically, it is recommended to use the 
 callback :c:data:`JOYSTICK_CALLBACK_ANALOG_VALUE` and set the period with 
 :c:func:`joystick_set_analog_value_callback_period`.
 
.. c:function:: int joystick_calibrate(Joystick *joystick)

 Calibrates the middle position of the Joystick. If your Joystick Bricklet
 does not return x=0 and y=0 in the middle position, call this function
 while the Joystick is standing still in the middle position.
 
 The resulting calibration will be saved on the eeprom of the Joystick 
 Bricklet, thus you only have to calibrate it once.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void joystick_register_callback(Joystick *joystick, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <joystick_bricklet_c_callbacks>`.


.. c:function:: int joystick_set_position_callback_period(Joystick *joystick, uint32_t period)

 Sets the period in ms with which the :c:data:`JOYSTICK_CALLBACK_POSITION` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`JOYSTICK_CALLBACK_POSITION` is only called if the position has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int joystick_get_position_callback_period(Joystick *joystick, uint32_t *ret_period)

 Returns the period as set by :c:func:`joystick_set_position_callback_period`.
 
.. c:function:: int joystick_set_analog_value_callback_period(Joystick *joystick, uint32_t period)

 Sets the period in ms with which the :c:data:`JOYSTICK_CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :c:data:`JOYSTICK_CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. c:function:: int joystick_get_analog_value_callback_period(Joystick *joystick, uint32_t *ret_period)

 Returns the period as set by :c:func:`joystick_set_analog_value_callback_period`.
 
.. c:function:: int joystick_set_position_callback_threshold(Joystick *joystick, char option, int16_t min_x, int16_t max_x, int16_t min_y, int16_t max_y)

 Sets the thresholds for the :c:data:`JOYSTICK_CALLBACK_POSITION_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the position is *outside* the min and max values"
  "'i'", "Callback is called when the position is *inside* the min and max values"
  "'<'", "Callback is called when the position is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the position is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0, 0, 0).
 
.. c:function:: int joystick_get_position_callback_threshold(Joystick *joystick, char *ret_option, int16_t *ret_min_x, int16_t *ret_max_x, int16_t *ret_min_y, int16_t *ret_max_y)

 Returns the threshold as set by :c:func:`joystick_set_position_callback_threshold`.
 
.. c:function:: int joystick_set_analog_value_callback_threshold(Joystick *joystick, char option, uint16_t min_x, uint16_t max_x, uint16_t min_y, uint16_t max_y)

 Sets the thresholds for the :c:data:`JOYSTICK_CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the position is *outside* the min and max values"
  "'i'", "Callback is called when the position is *inside* the min and max values"
  "'<'", "Callback is called when the position is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the position is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0, 0, 0).
 
.. c:function:: int joystick_get_analog_value_callback_threshold(Joystick *joystick, char *ret_option, uint16_t *ret_min_x, uint16_t *ret_max_x, uint16_t *ret_min_y, uint16_t *ret_max_y)

 Returns the threshold as set by :c:func:`joystick_set_analog_value_callback_threshold`.
 
.. c:function:: int joystick_set_debounce_period(Joystick *joystick, uint32_t debounce)

 Sets the period in ms with which the threshold callbacks
 
  :c:data:`JOYSTICK_CALLBACK_POSITION_REACHED`, :c:data:`JOYSTICK_CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :c:func:`joystick_set_position_callback_threshold`, :c:func:`joystick_set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. c:function:: int joystick_get_debounce_period(Joystick *joystick, uint32_t *ret_debounce)

 Returns the debounce period as set by :c:func:`joystick_set_debounce_period`.
 


.. _joystick_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    joystick_register_callback(&joystick, JOYSTICK_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: JOYSTICK_CALLBACK_POSITION

 .. c:var:: signature: void callback(int16_t x, int16_t y)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`joystick_set_position_callback_period`. The parameter is the position of the
 Joystick.
 
 :c:data:`JOYSTICK_CALLBACK_POSITION` is only called if the position has changed since the
 last call.
 
.. c:var:: JOYSTICK_CALLBACK_ANALOG_VALUE

 .. c:var:: signature: void callback(uint16_t x, uint16_t y)
    :noindex:


 This callback is called periodically with the period that is set by 
 :c:func:`joystick_set_analog_value_callback_period`. The parameters are the analog values
 of the Joystick.
 
 :c:data:`JOYSTICK_CALLBACK_ANALOG_VALUE` is only called if the value has changed since the
 last call.
 
.. c:var:: JOYSTICK_CALLBACK_POSITION_REACHED

 .. c:var:: signature: void callback(int16_t x, int16_t y)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`joystick_set_position_callback_threshold` is reached.
 The parameter is the position of the Joystick.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`joystick_set_debounce_period`.
 
.. c:var:: JOYSTICK_CALLBACK_ANALOG_VALUE_REACHED

 .. c:var:: signature: void callback(uint16_t x, uint16_t y)
    :noindex:


 This callback is called when the threshold as set by
 :c:func:`joystick_set_analog_value_callback_threshold` is reached.
 The parameters are the analog values of the Joystick.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :c:func:`joystick_set_debounce_period`.
 
.. c:var:: JOYSTICK_CALLBACK_PRESSED

 .. c:var:: signature: void callback(void)
    :noindex:


 This callback is called when the button is pressed.
 
.. c:var:: JOYSTICK_CALLBACK_RELEASED

 .. c:var:: signature: void callback(void)
    :noindex:


 This callback is called when the button is released.
 


