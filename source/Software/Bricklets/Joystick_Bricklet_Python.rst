..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - Joystick Bricklet
==========================

.. _joystick_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: Joystick_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Joystick_Bricklet_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

Find Corners
^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Joystick_Bricklet_Python_example_find_corners.py
 :language: python
 :linenos:
 :tab-width: 4

.. _joystick_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: Joystick(uid)

 Creates a joystick object with the unique device ID *uid*::

    joystick = Joystick("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <joystick_bricklet_python_examples>`).


.. py:function:: Joystick.get_position()

 :rtype: (int, int)

 Returns the position of the Joystick. The value ranges between -100 and
 100 for both axis. The middle position of the joystick is x=0, y=0. The
 returned values are averaged and calibrated (see :py:func:`Joystick.calibrate`).
 
 If you want to get the position periodically, it is recommended to use the
 callback :py:attr:`Joystick.CALLBACK_POSITION` and set the period with 
 :py:func:`Joystick.set_position_callback_period`.
 
.. py:function:: Joystick.is_pressed()

 :rtype: bool

 Returns true if the button is pressed and false otherwise.
 
 It is recommended to use the :py:attr:`Joystick.CALLBACK_PRESSED` and :py:attr:`Joystick.CALLBACK_RELEASED` callbacks
 to handle the button.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: Joystick.get_analog_value()

 :rtype: (int, int)

 Returns the values as read by a 12 bit analog to digital converter.
 The values are between 0 and 4095 for both axis.
 
  .. note::
   The values returned by :py:func:`Joystick.get_position` are averaged over several samples
   to yield less noise, while :py:func:`Joystick.get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :py:func:`Joystick.get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
 If you want the analog values periodically, it is recommended to use the 
 callback :py:attr:`Joystick.CALLBACK_ANALOG_VALUE` and set the period with 
 :py:func:`Joystick.set_analog_value_callback_period`.
 
.. py:function:: Joystick.calibrate()

 :rtype: None

 Calibrates the middle position of the Joystick. If your Joystick Bricklet
 does not return x=0 and y=0 in the middle position, call this function
 while the Joystick is standing still in the middle position.
 
 The resulting calibration will be saved on the eeprom of the Joystick 
 Bricklet, thus you only have to calibrate it once.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: Joystick.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <joystick_bricklet_python_callbacks>`.


.. py:function:: Joystick.set_position_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`Joystick.CALLBACK_POSITION` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`Joystick.CALLBACK_POSITION` is only called if the position has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: Joystick.get_position_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`Joystick.set_position_callback_period`.
 
.. py:function:: Joystick.set_analog_value_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`Joystick.CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`Joystick.CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: Joystick.get_analog_value_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`Joystick.set_analog_value_callback_period`.
 
.. py:function:: Joystick.set_position_callback_threshold(option, min_x, max_x, min_y, max_y)

 :param option: chr
 :param min_x: int
 :param max_x: int
 :param min_y: int
 :param max_y: int
 :rtype: None

 Sets the thresholds for the :py:attr:`Joystick.CALLBACK_POSITION_REACHED` callback. 
 
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
 
.. py:function:: Joystick.get_position_callback_threshold()

 :rtype: (chr, int, int, int, int)

 Returns the threshold as set by :py:func:`Joystick.set_position_callback_threshold`.
 
.. py:function:: Joystick.set_analog_value_callback_threshold(option, min_x, max_x, min_y, max_y)

 :param option: chr
 :param min_x: int
 :param max_x: int
 :param min_y: int
 :param max_y: int
 :rtype: None

 Sets the thresholds for the :py:attr:`Joystick.CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
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
 
.. py:function:: Joystick.get_analog_value_callback_threshold()

 :rtype: (chr, int, int, int, int)

 Returns the threshold as set by :py:func:`Joystick.set_analog_value_callback_threshold`.
 
.. py:function:: Joystick.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the period in ms with which the threshold callbacks
 
  :py:attr:`Joystick.CALLBACK_POSITION_REACHED`, :py:attr:`Joystick.CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :py:func:`Joystick.set_position_callback_threshold`, :py:func:`Joystick.set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. py:function:: Joystick.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`Joystick.set_debounce_period`.
 


.. _joystick_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    joystick.register_callback(joystick.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: Joystick.CALLBACK_POSITION

 :param x: int
 :param y: int


 This callback is called periodically with the period that is set by 
 :py:func:`Joystick.set_position_callback_period`. The parameter is the position of the
 Joystick.
 
 :py:attr:`Joystick.CALLBACK_POSITION` is only called if the position has changed since the
 last call.
 
.. py:attribute:: Joystick.CALLBACK_ANALOG_VALUE

 :param x: int
 :param y: int


 This callback is called periodically with the period that is set by 
 :py:func:`Joystick.set_analog_value_callback_period`. The parameters are the analog values
 of the Joystick.
 
 :py:attr:`Joystick.CALLBACK_ANALOG_VALUE` is only called if the value has changed since the
 last call.
 
.. py:attribute:: Joystick.CALLBACK_POSITION_REACHED

 :param x: int
 :param y: int


 This callback is called when the threshold as set by
 :py:func:`Joystick.set_position_callback_threshold` is reached.
 The parameter is the position of the Joystick.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`Joystick.set_debounce_period`.
 
.. py:attribute:: Joystick.CALLBACK_ANALOG_VALUE_REACHED

 :param x: int
 :param y: int


 This callback is called when the threshold as set by
 :py:func:`Joystick.set_analog_value_callback_threshold` is reached.
 The parameters are the analog values of the Joystick.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`Joystick.set_debounce_period`.
 
.. py:attribute:: Joystick.CALLBACK_PRESSED



 This callback is called when the button is pressed.
 
.. py:attribute:: Joystick.CALLBACK_RELEASED



 This callback is called when the button is released.
 


