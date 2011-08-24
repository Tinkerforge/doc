..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - LCD16x2 Bricklet
=========================

.. _lcd_16x2_bricklet_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Hello World
^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: LCD16x2_Bricklet_Python_example_hello_world.py
 :language: python
 :linenos:
 :tab-width: 4

Button Callbacks
^^^^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: LCD16x2_Bricklet_Python_example_button_callbacks.py
 :language: python
 :linenos:
 :tab-width: 4

.. _lcd_16x2_bricklet_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: LCD16x2(uid)

 Creates a lcd_16x2 object with the unique device ID *uid*::

    lcd_16x2 = LCD16x2("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <lcd_16x2_bricklet_python_examples>`).


.. py:function:: LCD16x2.write_line(line, position, text)

 :param line: int
 :param position: int
 :param text: str
 :rtype: None

 Writes text to a specific line (0 to 1) with a specific position 
 (0 to 15). The text can have a maximum of 16 characters.
 
 For example: (0, 5, "Hello") will write *Hello* in the middle of the
 first line of the display.
 
.. py:function:: LCD16x2.clear_display()

 :rtype: None

 Deletes all characters from the display.
 
.. py:function:: LCD16x2.backlight_on()

 :rtype: None

 Turns the backlight on.
 
.. py:function:: LCD16x2.backlight_off()

 :rtype: None

 Turns the backlight off.
 
.. py:function:: LCD16x2.is_backlight_on()

 :rtype: bool

 Returns true if the backlight is on and false otherwise.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: LCD16x2.set_config(cursor, blinking)

 :param cursor: bool
 :param blinking: bool
 :rtype: None

 Configures if the cursor (shown as "_") should be visible and if it
 should be blinking (shown as a blinking block). The cursor position
 is one character behind the the last text written with 
 :py:func:`LCD16x2.write_line`.
 
 The default is (false, false).
 
.. py:function:: LCD16x2.get_config()

 :rtype: (bool, bool)

 Returns the configuration as set by :py:func:`LCD16x2.set_config`.
 
.. py:function:: LCD16x2.is_button_pressed(button)

 :param button: int
 :rtype: bool

 Returns true if the button (0 to 2) is pressed. If you want to react
 on button presses and releases it is recommended to use the
 :py:attr:`LCD16x2.CALLBACK_BUTTON_PRESSED` and :py:attr:`LCD16x2.CALLBACK_BUTTON_RELEASED` callbacks.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: LCD16x2.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <lcd_16x2_bricklet_python_callbacks>`.




.. _lcd_16x2_bricklet_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    lcd_16x2.register_callback(lcd_16x2.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: LCD16x2.CALLBACK_BUTTON_PRESSED

 :param button: int


 This callback is called when a button is pressed. The parameter is
 the number of the button (0 to 2).
 
.. py:attribute:: LCD16x2.CALLBACK_BUTTON_RELEASED

 :param button: int


 This callback is called when a button is released. The parameter is
 the number of the button (0 to 2).
 


