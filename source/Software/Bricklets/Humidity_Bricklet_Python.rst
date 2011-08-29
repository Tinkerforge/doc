..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _humidity_bricklet_python:

Python - Humidity Bricklet
==========================

.. _humidity_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: Humidity_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Humidity_Bricklet_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Humidity_Bricklet_Python_example_threshold.py
 :language: python
 :linenos:
 :tab-width: 4

.. _humidity_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: Humidity(uid)

 Creates a humidity object with the unique device ID *uid*::

    humidity = Humidity("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <humidity_bricklet_python_examples>`).


.. py:function:: Humidity.get_humidity()

 :rtype: int

 Returns the humidity of the sensor. The value
 has a range of 0 to 1000 and is given in %RH/10 (Relative Humidity), 
 i.e. a value of 421 means that a humidity of 42.1 %RH is measured.
 
 If you want to get the humidity periodically, it is recommended to use the
 callback :py:attr:`Humidity.CALLBACK_HUMIDITY` and set the period with 
 :py:func:`Humidity.set_humidity_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: Humidity.get_analog_value()

 :rtype: int

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :py:func:`Humidity.get_humidity` is averaged over several samples
   to yield less noise, while :py:func:`Humidity.get_analog_value` gives back raw
   unfiltered analog values. The returned humidity value is calibrated for
   room temperatures, if you use the sensor in extreme cold or extreme
   warm enviroments, you might want to calculate the humidity from
   the analog value yourself. See the HIH 5030 datasheet (TODO: link).
 
 If you want the analog value periodically, it is recommended to use the 
 callback :py:attr:`Humidity.CALLBACK_ANALOG_VALUE` and set the period with 
 :py:func:`Humidity.set_analog_value_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: Humidity.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <humidity_bricklet_python_callbacks>`.


.. py:function:: Humidity.set_humidity_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`Humidity.CALLBACK_HUMIDITY` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`Humidity.CALLBACK_HUMIDITY` is only called if the humidity has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: Humidity.get_humidity_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`Humidity.set_humidity_callback_period`.
 
.. py:function:: Humidity.set_analog_value_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`Humidity.CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`Humidity.CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: Humidity.get_analog_value_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`Humidity.set_analog_value_callback_period`.
 
.. py:function:: Humidity.set_humidity_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`Humidity.CALLBACK_HUMIDITY_REACHED` callback. 
 
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
 
.. py:function:: Humidity.get_humidity_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`Humidity.set_humidity_callback_threshold`.
 
.. py:function:: Humidity.set_analog_value_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`Humidity.CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
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
 
.. py:function:: Humidity.get_analog_value_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`Humidity.set_analog_value_callback_threshold`.
 
.. py:function:: Humidity.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the period in ms with which the threshold callbacks
 
  :py:attr:`Humidity.CALLBACK_HUMIDITY_REACHED`, :py:attr:`Humidity.CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :py:func:`Humidity.set_humidity_callback_threshold`, :py:func:`Humidity.set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. py:function:: Humidity.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`Humidity.set_debounce_period`.
 


.. _humidity_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    humidity.register_callback(humidity.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: Humidity.CALLBACK_HUMIDITY

 :param humidity: int


 This callback is called periodically with the period that is set by 
 :py:func:`Humidity.set_humidity_callback_period`. The parameter is the humidity of the
 sensor.
 
 :py:attr:`Humidity.CALLBACK_HUMIDITY` is only called if the humidity has changed since the
 last call.
 
.. py:attribute:: Humidity.CALLBACK_ANALOG_VALUE

 :param value: int


 This callback is called periodically with the period that is set by 
 :py:func:`Humidity.set_analog_value_callback_period`. The parameter is the analog value of the
 sensor.
 
 :py:attr:`Humidity.CALLBACK_ANALOG_VALUE` is only called if the humidity has changed since the
 last call.
 
.. py:attribute:: Humidity.CALLBACK_HUMIDITY_REACHED

 :param humidity: int


 This callback is called when the threshold as set by
 :py:func:`Humidity.set_humidity_callback_threshold` is reached.
 The parameter is the humidity of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`Humidity.set_debounce_period`.
 
.. py:attribute:: Humidity.CALLBACK_ANALOG_VALUE_REACHED

 :param value: int


 This callback is called when the threshold as set by
 :py:func:`Humidity.set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`Humidity.set_debounce_period`.
 


