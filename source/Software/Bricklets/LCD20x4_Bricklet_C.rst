..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _lcd_20x4_bricklet_c:

C - LCD20x4 Bricklet
====================

.. _lcd_20x4_bricklet_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Hello World
^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: LCD20x4_Bricklet_C_example_hello_world.c
 :language: c
 :linenos:
 :tab-width: 4

Button Callbacks
^^^^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: LCD20x4_Bricklet_C_example_button_callbacks.c
 :language: c
 :linenos:
 :tab-width: 4

.. _lcd_20x4_bricklet_c_api:

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


.. c:function:: void lcd_20x4_create(LCD20x4 *lcd_20x4, const char *uid)

 Creates a LCD20x4 object with the unique device ID *uid*::

    LCD20x4 lcd_20x4;
    lcd_20x4_create(&lcd_20x4, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <lcd_20x4_bricklet_c_examples>`).


.. c:function:: int lcd_20x4_write_line(LCD20x4 *lcd_20x4, uint8_t line, uint8_t position, char text[20])

 Writes text to a specific line (0 to 3) with a specific position 
 (0 to 19). The text can have a maximum of 20 characters.
 
 For example: (0, 7, "Hello") will write *Hello* in the middle of the
 first line of the display.
 
.. c:function:: int lcd_20x4_clear_display(LCD20x4 *lcd_20x4)

 Deletes all characters from the display.
 
.. c:function:: int lcd_20x4_backlight_on(LCD20x4 *lcd_20x4)

 Turns the backlight on.
 
.. c:function:: int lcd_20x4_backlight_off(LCD20x4 *lcd_20x4)

 Turns the backlight off.
 
.. c:function:: int lcd_20x4_is_backlight_on(LCD20x4 *lcd_20x4, bool *ret_backlight)

 Returns true if the backlight is on and false otherwise.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int lcd_20x4_set_config(LCD20x4 *lcd_20x4, bool cursor, bool blinking)

 Configures if the cursor (shown as "_") should be visible and if it
 should be blinking (shown as a blinking block). The cursor position
 is one character behind the the last text written with 
 :c:func:`lcd_20x4_write_line`.
 
 The default is (false, false).
 
.. c:function:: int lcd_20x4_get_config(LCD20x4 *lcd_20x4, bool *ret_cursor, bool *ret_blinking)

 Returns the configuration as set by :c:func:`lcd_20x4_set_config`.
 
.. c:function:: int lcd_20x4_is_button_pressed(LCD20x4 *lcd_20x4, uint8_t button, bool *ret_pressed)

 Returns true if the button (0 to 2) is pressed. If you want to react
 on button presses and releases it is recommended to use the
 :c:data:`LCD_20X4_CALLBACK_BUTTON_PRESSED` and :c:data:`LCD_20X4_CALLBACK_BUTTON_RELEASED` callbacks.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void lcd_20x4_register_callback(LCD20x4 *lcd_20x4, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <lcd_20x4_bricklet_c_callbacks>`.




.. _lcd_20x4_bricklet_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    lcd_20x4_register_callback(&lcd_20x4, LCD20X4_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: LCD_20X4_CALLBACK_BUTTON_PRESSED

 .. c:var:: signature: void callback(uint8_t button)
    :noindex:


 This callback is called when a button is pressed. The parameter is
 the number of the button (0 to 2).
 
.. c:var:: LCD_20X4_CALLBACK_BUTTON_RELEASED

 .. c:var:: signature: void callback(uint8_t button)
    :noindex:


 This callback is called when a button is released. The parameter is
 the number of the button (0 to 2).
 


