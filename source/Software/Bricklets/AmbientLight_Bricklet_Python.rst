..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - AmbientLight Bricklet
==============================

.. _ambient_light_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: AmbientLight_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: AmbientLight_Bricklet_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: AmbientLight_Bricklet_Python_example_threshold.py
 :language: python
 :linenos:
 :tab-width: 4

.. _ambient_light_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: AmbientLight(uid)

 Creates a ambient_light object with the unique device ID *uid*::

    ambient_light = AmbientLight("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <ambient_light_bricklet_python_examples>`).


.. py:function:: AmbientLight.get_illuminance()

 :rtype: int

 Returns the illuminance of the ambient light sensor. The value
 has a range of 0 to 9000 and is given in Lux/10, i.e. a value
 of 4500 means that an illuminance of 450 Lux is measured.
 
 If you want to get the illuminance periodically, it is recommended to use the
 callback :py:attr:`AmbientLight.CALLBACK_ILLUMINANCE` and set the period with 
 :py:func:`AmbientLight.set_illuminance_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: AmbientLight.get_analog_value()

 :rtype: int

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :py:func:`AmbientLight.get_illuminance` is averaged over several samples
   to yield less noise, while :py:func:`AmbientLight.get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :py:func:`AmbientLight.get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
   Also, the analog to digital converter covers three different ranges that are
   set dynamically depending on the light intensity. It is impossible to
   distinguish between these ranges with the analog value.
 
 If you want the analog value periodically, it is recommended to use the 
 callback :py:attr:`AmbientLight.CALLBACK_ANALOG_VALUE` and set the period with 
 :py:func:`AmbientLight.set_analog_value_callback_period`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: AmbientLight.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <ambient_light_bricklet_python_callbacks>`.


.. py:function:: AmbientLight.set_illuminance_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`AmbientLight.CALLBACK_ILLUMINANCE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`AmbientLight.CALLBACK_ILLUMINANCE` is only called if the illuminance has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: AmbientLight.get_illuminance_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`AmbientLight.set_illuminance_callback_period`.
 
.. py:function:: AmbientLight.set_analog_value_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`AmbientLight.CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`AmbientLight.CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: AmbientLight.get_analog_value_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`AmbientLight.set_analog_value_callback_period`.
 
.. py:function:: AmbientLight.set_illuminance_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`AmbientLight.CALLBACK_ILLUMINANCE_REACHED` callback. 
 
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
 
.. py:function:: AmbientLight.get_illuminance_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`AmbientLight.set_illuminance_callback_threshold`.
 
.. py:function:: AmbientLight.set_analog_value_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`AmbientLight.CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
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
 
.. py:function:: AmbientLight.get_analog_value_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`AmbientLight.set_analog_value_callback_threshold`.
 
.. py:function:: AmbientLight.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the period in ms with which the threshold callbacks
 
  :py:attr:`AmbientLight.CALLBACK_ILLUMINANCE_REACHED`, :py:attr:`AmbientLight.CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :py:func:`AmbientLight.set_illuminance_callback_threshold`, :py:func:`AmbientLight.set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. py:function:: AmbientLight.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`AmbientLight.set_debounce_period`.
 


.. _ambient_light_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    ambient_light.register_callback(ambient_light.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: AmbientLight.CALLBACK_ILLUMINANCE

 :param illuminance: int


 This callback is called periodically with the period that is set by 
 :py:func:`AmbientLight.set_illuminance_callback_period`. The parameter is the illuminance of the
 ambient light sensor.
 
 :py:attr:`AmbientLight.CALLBACK_ILLUMINANCE` is only called if the illuminance has changed since the
 last call.
 
.. py:attribute:: AmbientLight.CALLBACK_ANALOG_VALUE

 :param value: int


 This callback is called periodically with the period that is set by 
 :py:func:`AmbientLight.set_analog_value_callback_period`. The parameter is the analog value of the
 ambient light sensor.
 
 :py:attr:`AmbientLight.CALLBACK_ANALOG_VALUE` is only called if the illuminance has changed since the
 last call.
 
.. py:attribute:: AmbientLight.CALLBACK_ILLUMINANCE_REACHED

 :param illuminance: int


 This callback is called when the threshold as set by
 :py:func:`AmbientLight.set_illuminance_callback_threshold` is reached.
 The parameter is the illuminance of the ambient light sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`AmbientLight.set_debounce_period`.
 
.. py:attribute:: AmbientLight.CALLBACK_ANALOG_VALUE_REACHED

 :param value: int


 This callback is called when the threshold as set by
 :py:func:`AmbientLight.set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the ambient light sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`AmbientLight.set_debounce_period`.
 


