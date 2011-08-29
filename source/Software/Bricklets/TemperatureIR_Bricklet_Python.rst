..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _temperature_ir_bricklet_python:

Python - TemperatureIR Bricklet
===============================

.. _temperature_ir_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: TemperatureIR_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Water Boiling
^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: TemperatureIR_Bricklet_Python_example_water_boiling.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: TemperatureIR_Bricklet_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

.. _temperature_ir_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: TemperatureIR(uid)

 Creates a temperature_ir object with the unique device ID *uid*::

    temperature_ir = TemperatureIR("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <temperature_ir_bricklet_python_examples>`).


.. py:function:: TemperatureIR.get_ambient_temperature()

 :rtype: int

 Returns the ambient temperature of the sensor. The value
 has a range of -400 to 1250 and is given in °C/10,
 e.g. a value of 423 means that an ambient temperature of 42.3 °C is 
 measured.
 
 If you want to get the ambient temperature periodically, it is recommended 
 to use the callback :py:attr:`TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE` and set the period with 
 :py:func:`TemperatureIR.set_ambient_temperature_callback_period`.
 
.. py:function:: TemperatureIR.get_object_temperature()

 :rtype: int

 Returns the object temperature of the sensor, i.e. the temperature
 of the surface of the object the sensor is aimed at. The value
 has a range of -700 to 3800 and is given in °C/10,
 e.g. a value of 30001 means that a temperature of 300.01 °C is measured
 on the surface of the object.
 
 The temperature of different materials is dependent on their `emissivity 
 <http://en.wikipedia.org/wiki/Emissivity>`_. The emissivity of the material
 can be set with :py:func:`TemperatureIR.set_emissivity`.
 
 If you want to get the object temperature periodically, it is recommended 
 to use the callback :py:attr:`TemperatureIR.CALLBACK_OBJECT_TEMPERATURE` and set the period with 
 :py:func:`TemperatureIR.set_object_temperature_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: TemperatureIR.set_emissivity(emissivity)

 :param emissivity: int
 :rtype: None

 Sets the `emissivity <http://en.wikipedia.org/wiki/Emissivity>`_ that is 
 used to calculate the surface temperature as returned by 
 :py:func:`TemperatureIR.get_object_temperature`. 
 
 The emissivity is usually given as a value between 0.0 and 1.0. A list of
 emissivities of different materials can be found 
 `here <http://www.infrared-thermography.com/material.htm>`_.
 
 The parameter of :py:func:`TemperatureIR.set_emissivity` has to be given with a factor of
 65535 (16 bit). For example: An emissivity of 0.1 can be set with the 
 value 6553, an emissivity of 0.5 with the value 32767 and so on.
 
  .. note::
   If you need a precise measurement for the object temperature, it is
   absolutely crucial that you also provide a precise emissivity.
 
 The default emissivity is 1.0 (value of 65535) and the minimum emissivity the
 sensor can handle is 0.1 (value of 6553).
 
.. py:function:: TemperatureIR.get_emissivity()

 :rtype: int

 Returns the emissivity as set by :py:func:`TemperatureIR.set_emissivity`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: TemperatureIR.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <temperature_ir_bricklet_python_callbacks>`.


.. py:function:: TemperatureIR.set_ambient_temperature_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE` is only called if the temperature has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: TemperatureIR.get_ambient_temperature_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`TemperatureIR.set_ambient_temperature_callback_period`.
 
.. py:function:: TemperatureIR.set_object_temperature_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`TemperatureIR.CALLBACK_OBJECT_TEMPERATURE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`TemperatureIR.CALLBACK_OBJECT_TEMPERATURE` is only called if the temperature has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: TemperatureIR.get_object_temperature_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`TemperatureIR.set_object_temperature_callback_period`.
 
.. py:function:: TemperatureIR.set_ambient_temperature_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE_REACHED` callback. 
 
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
 
.. py:function:: TemperatureIR.get_ambient_temperature_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`TemperatureIR.set_ambient_temperature_callback_threshold`.
 
.. py:function:: TemperatureIR.set_object_temperature_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`TemperatureIR.CALLBACK_OBJECT_TEMPERATURE_REACHED` callback. 
 
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
 
.. py:function:: TemperatureIR.get_object_temperature_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`TemperatureIR.set_ambient_temperature_callback_threshold`.
 
.. py:function:: TemperatureIR.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the period in ms with which the threshold callbacks
 
  :py:attr:`TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE_REACHED`, :py:attr:`TemperatureIR.CALLBACK_OBJECT_TEMPERATURE_REACHED`
 
 are called, if the thresholds 
 
  :py:func:`TemperatureIR.set_ambient_temperature_callback_threshold`, :py:func:`TemperatureIR.set_object_temperature_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. py:function:: TemperatureIR.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`TemperatureIR.set_debounce_period`.
 


.. _temperature_ir_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    temperature_ir.register_callback(temperature_ir.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE

 :param temperature: int


 This callback is called periodically with the period that is set by 
 :py:func:`TemperatureIR.set_ambient_temperature_callback_period`. The parameter is the ambient 
 temperature of the sensor.
 
 :py:attr:`TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE` is only called if the ambient temperature 
 has changed since the last call.
 
.. py:attribute:: TemperatureIR.CALLBACK_OBJECT_TEMPERATURE

 :param temperature: int


 This callback is called periodically with the period that is set by 
 :py:func:`TemperatureIR.set_object_temperature_callback_period`. The parameter is the object 
 temperature of the sensor.
 
 :py:attr:`TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE` is only called if the object temperature 
 has changed since the last call.
 
.. py:attribute:: TemperatureIR.CALLBACK_AMBIENT_TEMPERATURE_REACHED

 :param temperature: int


 This callback is called when the threshold as set by
 :py:func:`TemperatureIR.set_ambient_temperature_callback_threshold` is reached.
 The parameter is the ambient temperature of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`TemperatureIR.set_debounce_period`.
 
.. py:attribute:: TemperatureIR.CALLBACK_OBJECT_TEMPERATURE_REACHED

 :param temperature: int


 This callback is called when the threshold as set by
 :py:func:`TemperatureIR.set_object_temperature_callback_threshold` is reached.
 The parameter is the object temperature of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`TemperatureIR.set_debounce_period`.
 


