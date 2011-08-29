..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _temperature_bricklet_python:

Python - Temperature Bricklet
=============================

.. _temperature_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: Temperature_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Temperature_Bricklet_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Temperature_Bricklet_Python_example_threshold.py
 :language: python
 :linenos:
 :tab-width: 4

.. _temperature_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: Temperature(uid)

 Creates a temperature object with the unique device ID *uid*::

    temperature = Temperature("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <temperature_bricklet_python_examples>`).


.. py:function:: Temperature.get_temperature()

 :rtype: int

 Returns the temperature of the sensor. The value
 has a range of -2500 to 8500 and is given in °C/100,
 e.g. a value of 4223 means that a temperature of 42.23 °C is measured.
 
 If you want to get the temperature periodically, it is recommended 
 to use the callback :py:attr:`Temperature.CALLBACK_TEMPERATURE` and set the period with 
 :py:func:`Temperature.set_temperature_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: Temperature.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <temperature_bricklet_python_callbacks>`.


.. py:function:: Temperature.set_temperature_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`Temperature.CALLBACK_TEMPERATURE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`Temperature.CALLBACK_TEMPERATURE` is only called if the temperature has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: Temperature.get_temperature_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`Temperature.set_temperature_callback_period`.
 
.. py:function:: Temperature.set_temperature_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`Temperature.CALLBACK_TEMPERATURE_REACHED` callback. 
 
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
 
.. py:function:: Temperature.get_temperature_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`Temperature.set_temperature_callback_threshold`.
 
.. py:function:: Temperature.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the period in ms with which the threshold callback
 
  :py:attr:`Temperature.CALLBACK_TEMPERATURE_REACHED`
 
 is called, if the threshold
 
  :py:func:`Temperature.set_temperature_callback_threshold`
 
 keeps beeing reached.
 
 The default value is 100.
 
.. py:function:: Temperature.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`Temperature.set_debounce_period`.
 


.. _temperature_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    temperature.register_callback(temperature.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: Temperature.CALLBACK_TEMPERATURE

 :param temperature: int


 This callback is called periodically with the period that is set by 
 :py:func:`Temperature.set_temperature_callback_period`. The parameter is the temperature of the
 sensor.
 
 :py:attr:`Temperature.CALLBACK_TEMPERATURE` is only called if the temperature has changed since the
 last call.
 
.. py:attribute:: Temperature.CALLBACK_TEMPERATURE_REACHED

 :param temperature: int


 This callback is called when the threshold as set by
 :py:func:`Temperature.set_temperature_callback_threshold` is reached.
 The parameter is the temperature of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`Temperature.set_debounce_period`.
 


