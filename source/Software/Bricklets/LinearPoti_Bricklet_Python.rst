..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _linear_poti_bricklet_python:

Python - LinearPoti Bricklet
============================

.. _linear_poti_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: LinearPoti_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: LinearPoti_Bricklet_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

.. _linear_poti_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: LinearPoti(uid)

 Creates a linear_poti object with the unique device ID *uid*::

    linear_poti = LinearPoti("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <linear_poti_bricklet_python_examples>`).


.. py:function:: LinearPoti.get_position()

 :rtype: int

 Returns the position of the Linear Potentiometer. The value is  
 between 0 (slider down) and 100 (slider up).
 
 If you want to get the position periodically, it is recommended to use the
 callback :py:attr:`LinearPoti.CALLBACK_POSITION` and set the period with 
 :py:func:`LinearPoti.set_position_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: LinearPoti.get_analog_value()

 :rtype: int

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :py:func:`LinearPoti.get_position` is averaged over several samples
   to yield less noise, while :py:func:`LinearPoti.get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :py:func:`LinearPoti.get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
 If you want the analog value periodically, it is recommended to use the 
 callback :py:attr:`LinearPoti.CALLBACK_ANALOG_VALUE` and set the period with 
 :py:func:`LinearPoti.set_analog_value_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: LinearPoti.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <linear_poti_bricklet_python_callbacks>`.


.. py:function:: LinearPoti.set_position_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`LinearPoti.CALLBACK_POSITION` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`LinearPoti.CALLBACK_POSITION` is only called if the position has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: LinearPoti.get_position_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`LinearPoti.set_position_callback_period`.
 
.. py:function:: LinearPoti.set_analog_value_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`LinearPoti.CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`LinearPoti.CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: LinearPoti.get_analog_value_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`LinearPoti.set_analog_value_callback_period`.
 
.. py:function:: LinearPoti.set_position_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`LinearPoti.CALLBACK_POSITION_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the position is *outside* the min and max values"
  "'i'", "Callback is called when the position is *inside* the min and max values"
  "'<'", "Callback is called when the position is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the position is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. py:function:: LinearPoti.get_position_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`LinearPoti.set_position_callback_threshold`.
 
.. py:function:: LinearPoti.set_analog_value_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`LinearPoti.CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
 The following options are possible:
 
 .. csv-table::
  :header: "Option", "Description"
  :widths: 10, 100
 
  "'x'", "Callback is turned off."
  "'o'", "Callback is called when the position is *outside* the min and max values"
  "'i'", "Callback is called when the position is *inside* the min and max values"
  "'<'", "Callback is called when the position is smaller than the min value (max is ignored)"
  "'>'", "Callback is called when the position is greater than the min value (max is ignored)"
 
 The default value is ('x', 0, 0).
 
.. py:function:: LinearPoti.get_analog_value_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`LinearPoti.set_analog_value_callback_threshold`.
 
.. py:function:: LinearPoti.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the period in ms with which the threshold callbacks
 
  :py:attr:`LinearPoti.CALLBACK_POSITION_REACHED`, :py:attr:`LinearPoti.CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :py:func:`LinearPoti.set_position_callback_threshold`, :py:func:`LinearPoti.set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. py:function:: LinearPoti.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`LinearPoti.set_debounce_period`.
 


.. _linear_poti_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    linear_poti.register_callback(linear_poti.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: LinearPoti.CALLBACK_POSITION

 :param position: int


 This callback is called periodically with the period that is set by 
 :py:func:`LinearPoti.set_position_callback_period`. The parameter is the position of the
 Linear Potentiometer.
 
 :py:attr:`LinearPoti.CALLBACK_POSITION` is only called if the position has changed since the
 last call.
 
.. py:attribute:: LinearPoti.CALLBACK_ANALOG_VALUE

 :param value: int


 This callback is called periodically with the period that is set by 
 :py:func:`LinearPoti.set_analog_value_callback_period`. The parameter is the analog value of the
 Linear Potentiometer.
 
 :py:attr:`LinearPoti.CALLBACK_ANALOG_VALUE` is only called if the position has changed since the
 last call.
 
.. py:attribute:: LinearPoti.CALLBACK_POSITION_REACHED

 :param position: int


 This callback is called when the threshold as set by
 :py:func:`LinearPoti.set_position_callback_threshold` is reached.
 The parameter is the position of the Linear Potentiometer.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`LinearPoti.set_debounce_period`.
 
.. py:attribute:: LinearPoti.CALLBACK_ANALOG_VALUE_REACHED

 :param value: int


 This callback is called when the threshold as set by
 :py:func:`LinearPoti.set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the Linear Potentiometer.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`LinearPoti.set_debounce_period`.
 


