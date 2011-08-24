..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - Current25 Bricklet
===========================

.. _current25_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: Current25_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Current25_Bricklet_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Current25_Bricklet_Python_example_threshold.py
 :language: python
 :linenos:
 :tab-width: 4

.. _current25_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: Current25(uid)

 Creates a current25 object with the unique device ID *uid*::

    current25 = Current25("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <current25_bricklet_python_examples>`).


.. py:function:: Current25.get_current()

 :rtype: int

 Returns the current of the sensor. The value is in mA
 and between -25000mA and 25000.
 
 If you want to get the current periodically, it is recommended to use the
 callback :py:attr:`Current25.CALLBACK_CURRENT` and set the period with 
 :py:func:`Current25.set_current_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: Current25.calibrate()

 :rtype: None

 Calibrates the 0 value of the sensor. You have to call this function
 when there is no current present. 
 
 The zero point of the current sensor
 is depending on the exact properties of the analog to digital converter,
 the length of the Bricklet cable and the temperature. Thus, if you change
 the Brick or the environment in which the Bricklet is used, you might
 have to recalibrate.
 
 The resulting calibration will be saved on the eeprom of the Current
 Bricklet.
 
.. py:function:: Current25.is_over_current()

 :rtype: bool

 Returns true if more than 25A were measured.
 
  .. note::
   To reset this value you have to power cycle the Bricklet.
 
 
.. py:function:: Current25.get_analog_value()

 :rtype: int

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :py:func:`Current25.get_current` is averaged over several samples
   to yield less noise, while :py:func:`Current25.get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :py:func:`Current25.get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
 If you want the analog value periodically, it is recommended to use the 
 callback :py:attr:`Current25.CALLBACK_ANALOG_VALUE` and set the period with 
 :py:func:`Current25.set_analog_value_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: Current25.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <current25_bricklet_python_callbacks>`.


.. py:function:: Current25.set_current_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`Current25.CALLBACK_CURRENT` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`Current25.CALLBACK_CURRENT` is only called if the current has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: Current25.get_current_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`Current25.set_current_callback_period`.
 
.. py:function:: Current25.set_analog_value_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`Current25.CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`Current25.CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: Current25.get_analog_value_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`Current25.set_analog_value_callback_period`.
 
.. py:function:: Current25.set_current_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`Current25.CALLBACK_CURRENT_REACHED` callback. 
 
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
 
.. py:function:: Current25.get_current_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`Current25.set_current_callback_threshold`.
 
.. py:function:: Current25.set_analog_value_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`Current25.CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
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
 
.. py:function:: Current25.get_analog_value_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`Current25.set_analog_value_callback_threshold`.
 
.. py:function:: Current25.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the period in ms with which the threshold callbacks
 
  :py:attr:`Current25.CALLBACK_CURRENT_REACHED`, :py:attr:`Current25.CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :py:func:`Current25.set_current_callback_threshold`, :py:func:`Current25.set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. py:function:: Current25.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`Current25.set_debounce_period`.
 


.. _current25_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    current25.register_callback(current25.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: Current25.CALLBACK_CURRENT

 :param current: int


 This callback is called periodically with the period that is set by 
 :py:func:`Current25.set_current_callback_period`. The parameter is the current of the
 sensor.
 
 :py:attr:`Current25.CALLBACK_CURRENT` is only called if the current has changed since the
 last call.
 
.. py:attribute:: Current25.CALLBACK_ANALOG_VALUE

 :param value: int


 This callback is called periodically with the period that is set by 
 :py:func:`Current25.set_analog_value_callback_period`. The parameter is the analog value of the
 sensor.
 
 :py:attr:`Current25.CALLBACK_ANALOG_VALUE` is only called if the current has changed since the
 last call.
 
.. py:attribute:: Current25.CALLBACK_CURRENT_REACHED

 :param current: int


 This callback is called when the threshold as set by
 :py:func:`Current25.set_current_callback_threshold` is reached.
 The parameter is the current of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`Current25.set_debounce_period`.
 
.. py:attribute:: Current25.CALLBACK_ANALOG_VALUE_REACHED

 :param value: int


 This callback is called when the threshold as set by
 :py:func:`Current25.set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`Current25.set_debounce_period`.
 
.. py:attribute:: Current25.CALLBACK_OVER_CURRENT



 This callback is called when an over current is measured
 (see :py:func:`Current25.is_over_current`).
 


