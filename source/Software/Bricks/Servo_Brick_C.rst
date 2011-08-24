..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - Servo Brick
===============

.. _servo_brick_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Configuration
^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Servo_Brick_C_example_configuration.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Servo_Brick_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

.. _servo_brick_c_api:

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


.. c:function:: void servo_create(Servo *servo, const char *uid)

 Creates a Servo object with the unique device ID *uid*::

    Servo servo;
    servo_create(&servo, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <servo_brick_c_examples>`).


.. c:function:: int servo_enable(Servo *servo, uint8_t servo_num)

 Enables a servo (0 to 6). If a servo is enabled, the configured position,
 velocity, acceleration, etc. are applied immediately.
 
.. c:function:: int servo_disable(Servo *servo, uint8_t servo_num)

 Disables a servo (0 to 6). Disabled servos are not driven at all, i.e. a
 disabled servo will not hold its position if a load is applied.
 
.. c:function:: int servo_is_enabled(Servo *servo, uint8_t servo_num, bool *ret_enabled)

 Returns true if the specified servo is enabled, false otherwise.
 
.. c:function:: int servo_set_position(Servo *servo, uint8_t servo_num, int16_t position)

 Sets the position in °/100 for the specified servo. 
 
 The default range of the position is -9000 to 9000, but it can be specified
 according to your servo with :c:func:`servo_set_degree`.
 
 If you want to control a linear servo or RC brushless motor controller or
 similar with the Servo Brick, you can also define lengths or speeds with
 :c:func:`servo_set_degree`.
 
.. c:function:: int servo_get_position(Servo *servo, uint8_t servo_num, int16_t *ret_position)

 Returns the position of the specified servo as set by :c:func:`servo_set_position`.
 
.. c:function:: int servo_get_current_position(Servo *servo, uint8_t servo_num, int16_t *ret_position)

 Returns the *current* position of the specified servo. This may not be the
 value of :c:func:`servo_set_position` if the servo is currently approaching a
 position goal.
 
.. c:function:: int servo_set_velocity(Servo *servo, uint8_t servo_num, uint16_t velocity)

 Sets the maximum velocity of the specified servo in °/100s. The velocity
 is accelerated according to the value set by :c:func:`servo_set_acceleration`.
 
 The minimum velocity is 0 (no movement) and the maximum velocity is 65535.
 With a value of 65535 the position will be set immediately (no velocity).
 
 The default value is 65535.
 
.. c:function:: int servo_get_velocity(Servo *servo, uint8_t servo_num, uint16_t *ret_velocity)

 Returns the velocity of the specified servo as set by :c:func:`servo_set_velocity`.
 
.. c:function:: int servo_get_current_velocity(Servo *servo, uint8_t servo_num, uint16_t *ret_velocity)

 Returns the *current* velocity of the specified servo. This may not be the
 value of :c:func:`servo_set_velocity` if the servo is currently approaching a
 velocity goal.
 
.. c:function:: int servo_set_acceleration(Servo *servo, uint8_t servo_num, uint16_t acceleration)

 Sets the acceleration of the specified servo in °/100s².
 
 The minimum acceleration is 1 and the maximum acceleration is 65535.
 With a value of 65535 the velocity will be set immediately (no acceleration).
 
 The default value is 65535.
 
.. c:function:: int servo_get_acceleration(Servo *servo, uint8_t servo_num, uint16_t *ret_acceleration)

 Returns the acceleration for the specified servo as set by 
 :c:func:`servo_set_acceleration`.
 
.. c:function:: int servo_set_output_voltage(Servo *servo, uint16_t voltage)

 Sets the output voltages with which the servos are driven in mV.
 The minimum output voltage is 5000mV and the maximum output voltage is 
 9000mV.
 
  .. note::
   We recommend that you set this value to the maximum voltage that is
   specified for your servo, most servos achieve their maximum force only
   with high voltages.
 
 The default value is 5000.
 
.. c:function:: int servo_get_output_voltage(Servo *servo, uint16_t *ret_voltage)

 Returns the output voltage as specified by :c:func:`servo_set_output_voltage`.
 
.. c:function:: int servo_set_pulse_width(Servo *servo, uint8_t servo_num, uint16_t min, uint16_t max)

 Sets the minimum and maximum pulse width of the specified servo in µs.
 
 Usually, servos are controlled with a 
 `PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`_, whereby the 
 length of the pulse controls the position of the servo. Every servo has
 different minimum and maximum pulse widths, these can be specified with
 this function.
 
 If you have a datasheet for your servo that specifies the minimum and
 maximum pulse width, you should set the values accordingly. If your servo
 comes without any datasheet you have to find the values via trial and error.
 
 Both values have a range from 1 to 65535 (unsigned 16 bit integer). The
 minimum must be smaller than the maximum.
 
 The default values are 1000µs (1ms) and 2000µs (2ms) for minimum and 
 maximum pulse width.
 
.. c:function:: int servo_get_pulse_width(Servo *servo, uint8_t servo_num, uint16_t *ret_min, uint16_t *ret_max)

 Returns the minimum and maximum pulse width for the specified servo as set by
 :c:func:`servo_set_pulse_width`.
 
.. c:function:: int servo_set_degree(Servo *servo, uint8_t servo_num, int16_t min, int16_t max)

 Sets the minimum and maximum degree for the specified servo (by default
 given as °/100).
 
 This only specifies the abstract values between which the minimum and maximum
 pulse width is scaled. For example: If you specifiy a pulse width of 1000µs
 to 2000µs and a degree range of -90° to 90°, a call of :c:func:`servo_set_position`
 with 0 will result in a pulse width of 1500µs 
 (-90° = 1000µs, 90° = 2000µs, etc.).
 
 Possible usage:
 
  * The datasheet of your servo specifies a range of 200° with the middle position at 110°. In this case you can set the minimum to -9000 and the maximum to 11000.
  * You measure a range of 220° on your servo and you don't have or need a middle position. In this case you can set the minimum to 0 and the maximum to 22000.
  * You have a linear servo with a drive length of 20cm, In this case you could set the minimum to 0 and the maximum to 20000. Now you can set the Position with :c:func:`servo_set_position` with a resolution of cm/100. Also the velocity will have a resoltion of cm/100s and the acceleration will have a resolution of cm/100s².
  * You don't care about units and just want the highest possible resolution. In this case you should set the minimum to -32767 and the maximum to 32767.
  * You have a brushless motor with a maximum speed of 10000 rpm and want to conrol it with a RC brushless motor controller. In this case you can set the minimum to 0 and the maximum to 10000. :c:func:`servo_set_position` now controls the rpm.
 
 Both values have a possible range from -32767 to 32767 
 (signed 16 bit integer). The minimum must be smaller than the maximum.
 
 The default values are -9000 and 9000 for the minimum and maximum degree.
 
.. c:function:: int servo_get_degree(Servo *servo, uint8_t servo_num, int16_t *ret_min, int16_t *ret_max)

 Returns the minimum and maximum degree for the specified servo as set by
 :c:func:`servo_set_degree`.
 
.. c:function:: int servo_set_period(Servo *servo, uint8_t servo_num, uint16_t period)

 Sets the period of the specified servo in µs.
 
 Usually, servos are controlled with a 
 `PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`_. Different
 servos expect PWMs with different periods. Most servos run well with a 
 period of about 20ms.
 
 If your servo comes with a datasheet that specifies a period, you should
 set it accordingly. If you don't have a datasheet and you have no idea
 what the correct period is, the default value (19.5ms) will most likely
 work fine. 
 
 The minimum possible period is 2000µs and the maximum is 65535µs.
 
 The default value is 19.5ms (19500µs).
 
.. c:function:: int servo_get_period(Servo *servo, uint8_t servo_num, uint16_t *ret_period)

 Returns the period for the specified servo as set by :c:func:`servo_set_period`.
 
.. c:function:: int servo_get_servo_current(Servo *servo, uint8_t servo_num, uint16_t *ret_current)

 Returns the current consumption of the specified servo in mA.
 
.. c:function:: int servo_get_overall_current(Servo *servo, uint16_t *ret_current)

 Returns the current consumption of all servos together in mA.
 
.. c:function:: int servo_get_stack_input_voltage(Servo *servo, uint16_t *ret_voltage)

 Returns the stack input voltage in mV. The stack input voltage is the
 voltage that is supplied via the stack, i.e. it is given by a 
 Step-Down or Step-Up power supply Brick.
 
.. c:function:: int servo_get_external_input_voltage(Servo *servo, uint16_t *ret_voltage)

 Returns the external input voltage in mV. The external input voltage is
 given via the black power input connector on the Servo Brick. 
  
 If there is  an externel input voltage and a stack input voltage, the motor 
 will be driven by the external input voltage. If there is only a stack 
 voltage present, the motor will be driven by this voltage.
 
  .. warning:: 
   This means, if you have a high stack voltage and a low external voltage,
   the motor will be driven with the low external voltage. If you then remove
   the external connection, it will immediately be driven by the high
   stack voltage
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void servo_register_callback(Servo *servo, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <servo_brick_c_callbacks>`.


.. c:function:: int servo_set_minimum_voltage(Servo *servo, uint16_t voltage)

 Sets the minimum voltage in mV, below which the :c:data:`SERVO_CALLBACK_UNDER_VOLTAGE` signal
 is called. The minimum possible value that works with the Servo Brick is 5V. 
 You can use this function to detect the discharge of a battery that is used
 to drive the stepper motor. If you have a fixed power supply, you likely do 
 not need this functionality.
 
 The default value is 5V (5000mV).
 
.. c:function:: int servo_get_minimum_voltage(Servo *servo, uint16_t *ret_voltage)

 Returns the minimum voltage as set by :c:func:`servo_set_minimum_voltage`
 


.. _servo_brick_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    servo_register_callback(&servo, SERVO_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: SERVO_CALLBACK_UNDER_VOLTAGE

 .. c:var:: signature: void callback(uint16_t voltage)
    :noindex:


 This callback is called when the input voltage drops below the value set by
 :c:func:`servo_set_minimum_voltage`. The parameter is the current voltage given
 in mV.
 
.. c:var:: SERVO_CALLBACK_POSITION_REACHED

 .. c:var:: signature: void callback(uint8_t servo_num, int16_t position)
    :noindex:


 This callback is called when a position set by :c:func:`servo_set_position` 
 is reached. The parameters are the servo and the position that is reached.
 
 .. note::
  Since we can't get any feedback from the servo, this only works if the
  velocity (see :c:func:`servo_set_velocity`) is set smaller or equal to the
  maximum velocity of the servo. Otherwise the servo will lag behind the
  control value and the callback will be called too early.
 
.. c:var:: SERVO_CALLBACK_VELOCITY_REACHED

 .. c:var:: signature: void callback(uint8_t servo_num, int16_t velocity)
    :noindex:


 This callback is called when a velocity set by :c:func:`servo_set_velocity` 
 is reached. The parameters are the servo and the velocity that is reached.
 
 .. note::
  Since we can't get any feedback from the servo, this only works if the
  acceleration (see :c:func:`servo_set_acceleration`) is set smaller or equal to the
  maximum acceleration of the servo. Otherwise the servo will lag behind the
  control value and the callback will be called too early.
 


