..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _piezo_buzzer_bricklet_c:

C - PiezoBuzzer Bricklet
========================

.. _piezo_buzzer_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Beep
^^^^

TODO: link zum download der datei

.. literalinclude:: PiezoBuzzer_Bricklet_C_example_beep.c
 :language: c
 :linenos:
 :tab-width: 4

Morse Code
^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: PiezoBuzzer_Bricklet_C_example_morse_code.c
 :language: c
 :linenos:
 :tab-width: 4

.. _piezo_buzzer_bricklet_c_api:

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


.. c:function:: void piezo_buzzer_create(PiezoBuzzer *piezo_buzzer, const char *uid)

 Creates a PiezoBuzzer object with the unique device ID *uid*::

    PiezoBuzzer piezo_buzzer;
    piezo_buzzer_create(&piezo_buzzer, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <piezo_buzzer_bricklet_c_examples>`).


.. c:function:: int piezo_buzzer_beep(PiezoBuzzer *piezo_buzzer, uint32_t duration)

 Beeps with the duration in ms. For example: If you set a value of 1000,
 the piezo buzzer will beep for one second.
 
.. c:function:: int piezo_buzzer_morse_code(PiezoBuzzer *piezo_buzzer, char morse[60])

 Sets morse code that will be played by the piezo buzzer. The morse code
 is given as a string consisting of "." (dot), "-" (minus) and " " (space)
 for *dits*, *dahs* and *pauses*. Every other character is ignored.
 
 For example: If you set the string "...---...", the piezo buzzer will beep
 nine times with the durations "short short short long long long short 
 short short".
 
 The maximum string size is 60.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void piezo_buzzer_register_callback(PiezoBuzzer *piezo_buzzer, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <piezo_buzzer_bricklet_c_callbacks>`.




.. _piezo_buzzer_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    piezo_buzzer_register_callback(&piezo_buzzer, PIEZOBUZZER_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: PIEZO_BUZZER_CALLBACK_BEEP_FINISHED

 .. c:var:: signature: void callback(void)
    :noindex:


 This callback is called if a beep set by :c:func:`piezo_buzzer_beep` is finished
 
.. c:var:: PIEZO_BUZZER_CALLBACK_MORSE_CODE_FINISHED

 .. c:var:: signature: void callback(void)
    :noindex:


 This callback is called if the playback of the morse code set by 
 :c:func:`piezo_buzzer_morse_code` is finished.
 


