..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _io16_bricklet_c:

C - IO16 Bricklet
=================

.. _io16_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Output
^^^^^^

TODO: link zum download der datei

.. literalinclude:: IO16_Bricklet_C_example_output.c
 :language: c
 :linenos:
 :tab-width: 4

Interrupt
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: IO16_Bricklet_C_example_interrupt.c
 :language: c
 :linenos:
 :tab-width: 4

.. _io16_bricklet_c_api:

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


.. c:function:: void io16_create(IO16 *io16, const char *uid)

 Creates a IO16 object with the unique device ID *uid*::

    IO16 io16;
    io16_create(&io16, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <io16_bricklet_c_examples>`).


.. c:function:: int io16_set_port(IO16 *io16, char port, uint8_t value_mask)

 Sets the output value (high or low) for a port ("a" or "b") with a bit mask. 
 The bit mask is 8 bit long, "true" refers to high and "false" refers to low.
 
 For example: The bitstring "11110000" will turn the pins 0-3 high and the
 pins 4-7 low for the specified port.
 
  .. note::
   This function does nothing for pins that are configured as input.
   Pull up resistors can be switched on with :c:func:`io16_set_port_configuration`.
 
 
.. c:function:: int io16_get_port(IO16 *io16, char port, uint8_t *ret_value_mask)

 Returns a bit mask of the values that are currently measured on the
 specified port. This function works if the pin is configured to input
 as well as if it is configured to output.
 
.. c:function:: int io16_set_port_configuration(IO16 *io16, char port, uint8_t port_mask, char direction, bool value)

 Configures the value and direction of a specified port. possible directions
 are "i" and "o" for input and output.
 
 If the direction is configured as output, the value is either high or low
 (set as true or false).
 
 If the direction is configured as output, the value is either pull up or
 default (set as true or false).
 
 For example: 
 
  * ("a", 0xFF, 'i', true) will set all pins of port a as input pull up. 
  * ("a", 128, 'i', false) will set pin 7 of port a as input default (floating if nothing is connected). 
  * ("b", 3, 'o', false) will set pins 0 and 1 of port b as output low.
  * ("b", 4, 'o', true) will set pin 2 of port b as output high.
 
 
.. c:function:: int io16_get_port_configuration(IO16 *io16, char port, uint8_t *ret_direction_mask, uint8_t *ret_value_mask)

 Returns a value bit mask and a direction  bit mask for the specified port.
 
 For example: A return value of the bitstrings "11110000" and "11001100" for
 direction and value means that:
 
  * pins 0 and 1 are configured as input pull up, 
  * pins 2 and 3 are configured as intput default, 
  * pins 4 and 5 are configured as output high 
  * and pins 6 and 7 are configured as output low.
 
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void io16_register_callback(IO16 *io16, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <io16_bricklet_c_callbacks>`.


.. c:function:: int io16_set_debounce_period(IO16 *io16, uint32_t debounce)

 Sets the debounce period of the :c:data:`IO16_CALLBACK_INTERRUPT` callback in ms.
 
 For example: If you set this value to 100, you will get the interrupt
 maximal every 100ms. This is necessary if something that bounces is
 connected to the IO-16 Bricklet, such as a button.
 
 The default value is 100.
 
.. c:function:: int io16_get_debounce_period(IO16 *io16, uint32_t *ret_debounce)

 Returns the debounce period as set by :c:func:`io16_set_debounce_period`.
 
.. c:function:: int io16_set_port_interrupt(IO16 *io16, char port, uint8_t interrupt_mask)

 Sets the pins on which an interrupt is activated with a bit mask. 
 Interrupts are triggered on changes of the voltage level of the pin,
 i.e. changes from high to low and low to high.
 
 For example: ('a', 129) will enable the interrupt for pins 0 and 7 of
 port a.
 
 The interrupt is delivered with the callback :c:data:`IO16_CALLBACK_INTERRUPT`.
 
.. c:function:: int io16_get_port_interrupt(IO16 *io16, char port, uint8_t *ret_interrupt_mask)

 Returns the interrupt bit mask for the specified port as set by
 :c:func:`io16_set_port_interrupt`.
 


.. _io16_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    io16_register_callback(&io16, IO16_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: IO16_CALLBACK_INTERRUPT

 .. c:var:: signature: void callback(char port, uint8_t interrupt_mask, uint8_t value_mask)
    :noindex:


 This callback is called whenever a change of the voltage level is detected
 on pins where the interrupt was activated with :c:func:`io16_set_port_interrupt`.
 
 The values are the port, a bit mask that specifies which interrupts occurred
 and the current value bit mask of the port.
 
 For example:
 
  * ("a", 1, 1) means that on port a an interrupt on pin 0 occurred and
    currently pin 0 is high and pins 1-7 are low.
  * ("b", 128, 254) means that on port b an interrupt on pins 0 and 7
    occured and currently pin 0 is low and pins 1-7 are high.
 
 


