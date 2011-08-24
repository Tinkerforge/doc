..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - DistanceIR Bricklet
============================

.. _distance_ir_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Simple
^^^^^^

TODO: link zum download der datei

.. literalinclude:: DistanceIR_Bricklet_Python_example_simple.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: DistanceIR_Bricklet_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

Threshold
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: DistanceIR_Bricklet_Python_example_threshold.py
 :language: python
 :linenos:
 :tab-width: 4

.. _distance_ir_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: DistanceIR(uid)

 Creates a distance_ir object with the unique device ID *uid*::

    distance_ir = DistanceIR("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <distance_ir_bricklet_python_examples>`).


.. py:function:: DistanceIR.get_distance()

 :rtype: int

 Returns the distance of the sensor. The value is in mm and
 between TODO
 
 If you want to get the distance periodically, it is recommended to use the
 callback :py:attr:`DistanceIR.CALLBACK_DISTANCE` and set the period with 
 :py:func:`DistanceIR.set_distance_callback_period`.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: DistanceIR.get_analog_value()

 :rtype: int

 Returns the value as read by a 12 bit analog to digital converter.
 The value is between 0 and 4095.
 
  .. note::
   The value returned by :py:func:`DistanceIR.get_distance` is averaged over several samples
   to yield less noise, while :py:func:`DistanceIR.get_analog_value` gives back raw
   unfiltered analog values. The only reason to use :py:func:`DistanceIR.get_analog_value` is,
   if you need the full resolution of the analog to digital converter.
 
 If you want the analog value periodically, it is recommended to use the 
 callback :py:attr:`DistanceIR.CALLBACK_ANALOG_VALUE` and set the period with 
 :py:func:`DistanceIR.set_analog_value_callback_period`.
 
.. py:function:: DistanceIR.set_sampling_point(position, distance)

 :param position: int
 :param distance: int
 :rtype: None

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
 
 
.. py:function:: DistanceIR.get_sampling_point(position)

 :param position: int
 :rtype: int

 Returns the distance to a sampling point position as set by
 :py:func:`DistanceIR.set_sampling_point`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: DistanceIR.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <distance_ir_bricklet_python_callbacks>`.


.. py:function:: DistanceIR.set_distance_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`DistanceIR.CALLBACK_DISTANCE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`DistanceIR.CALLBACK_DISTANCE` is only called if the distance has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: DistanceIR.get_distance_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`DistanceIR.set_distance_callback_period`.
 
.. py:function:: DistanceIR.set_analog_value_callback_period(period)

 :param period: int
 :rtype: None

 Sets the period in ms with which the :py:attr:`DistanceIR.CALLBACK_ANALOG_VALUE` callback is called 
 periodically. A value of 0 turns the callback off.
 
 :py:attr:`DistanceIR.CALLBACK_ANALOG_VALUE` is only called if the analog value has changed since the
 last call.
 
 The default value is 0.
 
.. py:function:: DistanceIR.get_analog_value_callback_period()

 :rtype: int

 Returns the period as set by :py:func:`DistanceIR.set_analog_value_callback_period`.
 
.. py:function:: DistanceIR.set_distance_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`DistanceIR.CALLBACK_DISTANCE_REACHED` callback. 
 
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
 
.. py:function:: DistanceIR.get_distance_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`DistanceIR.set_distance_callback_threshold`.
 
.. py:function:: DistanceIR.set_analog_value_callback_threshold(option, min, max)

 :param option: chr
 :param min: int
 :param max: int
 :rtype: None

 Sets the thresholds for the :py:attr:`DistanceIR.CALLBACK_ANALOG_VALUE_REACHED` callback. 
 
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
 
.. py:function:: DistanceIR.get_analog_value_callback_threshold()

 :rtype: (chr, int, int)

 Returns the threshold as set by :py:func:`DistanceIR.set_analog_value_callback_threshold`.
 
.. py:function:: DistanceIR.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the period in ms with which the threshold callbacks
 
  :py:attr:`DistanceIR.CALLBACK_DISTANCE_REACHED`, :py:attr:`DistanceIR.CALLBACK_ANALOG_VALUE_REACHED`
 
 are called, if the thresholds 
 
  :py:func:`DistanceIR.set_distance_callback_threshold`, :py:func:`DistanceIR.set_analog_value_callback_threshold`
 
 keep beeing reached.
 
 The default value is 100.
 
.. py:function:: DistanceIR.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`DistanceIR.set_debounce_period`.
 


.. _distance_ir_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    distance_ir.register_callback(distance_ir.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: DistanceIR.CALLBACK_DISTANCE

 :param distance: int


 This callback is called periodically with the period that is set by 
 :py:func:`DistanceIR.set_distance_callback_period`. The parameter is the distance of the
 sensor.
 
 :py:attr:`DistanceIR.CALLBACK_DISTANCE` is only called if the distance has changed since the
 last call.
 
.. py:attribute:: DistanceIR.CALLBACK_ANALOG_VALUE

 :param value: int


 This callback is called periodically with the period that is set by 
 :py:func:`DistanceIR.set_analog_value_callback_period`. The parameter is the analog value of the
 sensor.
 
 :py:attr:`DistanceIR.CALLBACK_ANALOG_VALUE` is only called if the distance has changed since the
 last call.
 
.. py:attribute:: DistanceIR.CALLBACK_DISTANCE_REACHED

 :param distance: int


 This callback is called when the threshold as set by
 :py:func:`DistanceIR.set_distance_callback_threshold` is reached.
 The parameter is the distance of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`DistanceIR.set_debounce_period`.
 
.. py:attribute:: DistanceIR.CALLBACK_ANALOG_VALUE_REACHED

 :param value: int


 This callback is called when the threshold as set by
 :py:func:`DistanceIR.set_analog_value_callback_threshold` is reached.
 The parameter is the analog value of the sensor.
 
 If the threshold keeps beeing reached, the callback is called periodically 
 with the period as set by :py:func:`DistanceIR.set_debounce_period`.
 


