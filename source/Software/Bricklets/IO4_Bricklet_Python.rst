..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - IO4 Bricklet
=====================

.. _io4_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Output
^^^^^^

TODO: link zum download der datei

.. literalinclude:: IO4_Bricklet_Python_example_output.py
 :language: python
 :linenos:
 :tab-width: 4

Interrupt
^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: IO4_Bricklet_Python_example_interrupt.py
 :language: python
 :linenos:
 :tab-width: 4

.. _io4_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: IO4(uid)

 Creates a io4 object with the unique device ID *uid*::

    io4 = IO4("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <io4_bricklet_python_examples>`).


.. py:function:: IO4.set_value(value_mask)

 :param value_mask: int
 :rtype: None

 Sets the output value (high or low) with a bit mask. The bit mask
 is 4 bit long, "true" refers to high and "false" refers to low.
 
 For example: The bitstring "1100" will turn the pins 0-1 high and the
 pins 2-3 low.
 
  .. note::
   This function does nothing for pins that are configured as input.
   Pull up resistors can be switched on with :func:`SetPortConfiguration`.
 
 
.. py:function:: IO4.get_value()

 :rtype: int

 Returns a bit mask of the values that are currently measured.
 This function works if the pin is configured to input
 as well as if it is configured to output.
 
.. py:function:: IO4.set_configuration(pin_mask, direction, value)

 :param pin_mask: int
 :param direction: chr
 :param value: bool
 :rtype: None

 Configures the value and direction of the specified pins. Possible directions
 are "i" and "o" for input and output.
 
 If the direction is configured as output, the value is either high or low
 (set as true or false).
 
 If the direction is configured as output, the value is either pull up or
 default (set as true or false).
 
 For example: 
 
  * (15, 'i', true) will set all pins of as input pull up. 
  * (8, 'i', false) will set pin 3 of as input default (floating if nothing is connected). 
  * (3, 'o', false) will set pins 0 and 1 as output low.
  * (4, 'o', true) will set pin 2 of as output high.
 
 
.. py:function:: IO4.get_configuration()

 :rtype: (int, int)

 Returns a value bit mask and a direction bit mask.
 
 For example: A return value of the bitstrings "1100" and "1010" for
 direction and value means that:
 
  * pin 0 is configured as input pull up, 
  * pin 1 is configured as intput default, 
  * pin 2 is  configured as output high 
  * and pin 3 is are configured as output low.
 
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: IO4.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <io4_bricklet_python_callbacks>`.


.. py:function:: IO4.set_debounce_period(debounce)

 :param debounce: int
 :rtype: None

 Sets the debounce period of the :py:attr:`IO4.CALLBACK_INTERRUPT` callback in ms.
 
 For example: If you set this value to 100, you will get the interrupt
 maximal every 100ms. This is necessary if something that bounces is
 connected to the IO-4 Bricklet, such as a button.
 
 The default value is 100.
 
.. py:function:: IO4.get_debounce_period()

 :rtype: int

 Returns the debounce period as set by :py:func:`IO4.set_debounce_period`.
 
.. py:function:: IO4.set_interrupt(interrupt_mask)

 :param interrupt_mask: int
 :rtype: None

 Sets the pins on which an interrupt is activated with a bit mask. 
 Interrupts are triggered on changes of the voltage level of the pin,
 i.e. changes from high to low and low to high.
 
 For example: An interrupt bit mask of 9 will enable the interrupt for 
 pins 0 and 3.
 
 The interrupt is delivered with the callback :py:attr:`IO4.CALLBACK_INTERRUPT`.
 
.. py:function:: IO4.get_interrupt()

 :rtype: int

 Returns the interrupt bit mask as set by :func:`SetPortInterrupt`.
 


.. _io4_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    io4.register_callback(io4.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: IO4.CALLBACK_INTERRUPT

 :param interrupt_mask: int
 :param value_mask: int


 This callback is called whenever a change of the voltage level is detected
 on pins where the interrupt was activated with :func:`SetPortInterrupt`.
 
 The values are a bit mask that specifies which interrupts occurred
 and the current value bit mask of the port.
 
 For example:
 
  * (1, 1) means that an interrupt on pin 0 occurred and
    currently pin 0 is high and pins 1-3 are low.
  * (9, 14) means that an interrupt on pins 0 and 3
    occured and currently pin 0 is low and pins 1-3 are high.
 
 


