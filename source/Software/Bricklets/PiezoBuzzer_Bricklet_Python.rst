..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - PiezoBuzzer Bricklet
=============================

.. _piezo_buzzer_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Beep
^^^^

TODO: link zum download der datei

.. literalinclude:: PiezoBuzzer_Bricklet_Python_example_beep.py
 :language: python
 :linenos:
 :tab-width: 4

Morse Code
^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: PiezoBuzzer_Bricklet_Python_example_morse_code.py
 :language: python
 :linenos:
 :tab-width: 4

.. _piezo_buzzer_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: PiezoBuzzer(uid)

 Creates a piezo_buzzer object with the unique device ID *uid*::

    piezo_buzzer = PiezoBuzzer("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <piezo_buzzer_bricklet_python_examples>`).


.. py:function:: PiezoBuzzer.beep(duration)

 :param duration: int
 :rtype: None

 Beeps with the duration in ms. For example: If you set a value of 1000,
 the piezo buzzer will beep for one second.
 
.. py:function:: PiezoBuzzer.morse_code(morse)

 :param morse: str
 :rtype: None

 Sets morse code that will be played by the piezo buzzer. The morse code
 is given as a string consisting of "." (dot), "-" (minus) and " " (space)
 for *dits*, *dahs* and *pauses*. Every other character is ignored.
 
 For example: If you set the string "...---...", the piezo buzzer will beep
 nine times with the durations "short short short long long long short 
 short short".
 
 The maximum string size is 60.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: PiezoBuzzer.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <piezo_buzzer_bricklet_python_callbacks>`.




.. _piezo_buzzer_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    piezo_buzzer.register_callback(piezo_buzzer.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: PiezoBuzzer.CALLBACK_BEEP_FINISHED



 This callback is called if a beep set by :py:func:`PiezoBuzzer.beep` is finished
 
.. py:attribute:: PiezoBuzzer.CALLBACK_MORSE_CODE_FINISHED



 This callback is called if the playback of the morse code set by 
 :py:func:`PiezoBuzzer.morse_code` is finished.
 


