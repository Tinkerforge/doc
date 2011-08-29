..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _io16_bricklet_python:

Python - IO16 Bricklet
======================

.. _io16_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Output
^^^^^^

TODO: link zum download der datei

.. literalinclude:: IO16_Bricklet_Python_example_output.py
 :language: python
 :linenos:
 :tab-width: 4

Interrupt
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: IO16_Bricklet_Python_example_interrupt.py
 :language: python
 :linenos:
 :tab-width: 4

.. _io16_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: IO16(uid)

 Creates a io16 object with the unique device ID *uid*::

    io16 = IO16("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <io16_bricklet_python_examples>`).


.. py:function:: IO16.set_port(port, value_mask)

 :param port: chr
 :param value_mask: int
 :rtype: None

 Sets the output value (high or low) for a port ("a" or "b") with a bit mask. 
 The bit mask is 8 bit long, "true" refers to high and "false" refers to low.
 
 For example: The bitstring "11110000" will turn the pins 0-3 high and the
 pins 4-7 low for the specified port.
 
  .. note::
   This function does nothing for pins that are configured as input.
   Pull up resistors can be switched on with :py:func:`IO16.set_port_configuration`.
 
 
.. py:function:: IO16.get_port(port)

 :param port: chr
 :rtype: int

 Returns a bit mask of the values that are currently measured on the
 specified port. This function works if the pin is configured to input
 as well as if it is configured to output.
 
.. py:function:: IO16.set_port_configuration(port, port_mask, direction, value)

 :param port: chr
 :param port_mask: int
 :param direction: chr
 :param value: bool
 :rtype: None

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
 
 
.. py:function:: IO16.get_port_configuration(port)

 :param port: chr
 :rtype: (int, int)

 Returns a value bit mask and a direction  bit mask for the specified port.
 
 For example: A return value of the bitstrings "11110000" and "11001100" for
 direction and value means that:
 
  * pins 0 and 1 are configured as input pull up, 
  * pins 2 and 3 are configured as intput default, 
  * pins 4 and 5 are configured as output high 
  * and pins 6 and 7 are configured as output low.
 
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: IO16.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <io16_bricklet_python_callbacks>`.


.. py:function:: IO16.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the debounce period of the :py:attr:`IO16.CALLBACK_INTERRUPT` callback in ms.
 
 For example: If you set this value to 100, you will get the interrupt
 maximal every 100ms. This is necessary if something that bounces is
 connected to the IO-16 Bricklet, such as a button.
 
 The default value is 100.
 
.. py:function:: IO16.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`IO16.set_debounce_period`.
 
.. py:function:: IO16.set_port_interrupt(port, interrupt_mask)

 :param port: chr
 :param interrupt_mask: int
 :rtype: None

 Sets the pins on which an interrupt is activated with a bit mask. 
 Interrupts are triggered on changes of the voltage level of the pin,
 i.e. changes from high to low and low to high.
 
 For example: ('a', 129) will enable the interrupt for pins 0 and 7 of
 port a.
 
 The interrupt is delivered with the callback :py:attr:`IO16.CALLBACK_INTERRUPT`.
 
.. py:function:: IO16.get_port_interrupt(port)

 :param port: chr
 :rtype: int

 Returns the interrupt bit mask for the specified port as set by
 :py:func:`IO16.set_port_interrupt`.
 


.. _io16_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    io16.register_callback(io16.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: IO16.CALLBACK_INTERRUPT

 :param port: chr
 :param interrupt_mask: int
 :param value_mask: int


 This callback is called whenever a change of the voltage level is detected
 on pins where the interrupt was activated with :py:func:`IO16.set_port_interrupt`.
 
 The values are the port, a bit mask that specifies which interrupts occurred
 and the current value bit mask of the port.
 
 For example:
 
  * ("a", 1, 1) means that on port a an interrupt on pin 0 occurred and
    currently pin 0 is high and pins 1-7 are low.
  * ("b", 128, 254) means that on port b an interrupt on pins 0 and 7
    occured and currently pin 0 is low and pins 1-7 are high.
 
 


