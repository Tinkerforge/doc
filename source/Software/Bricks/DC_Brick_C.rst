..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _dc_brick_c:

C - DC Brick
============

.. _dc_brick_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Configuration
^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: DC_Brick_C_example_configuration.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: DC_Brick_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

.. _dc_brick_c_api:

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


.. c:function:: void dc_create(DC *dc, const char *uid)

 Creates a DC object with the unique device ID *uid*::

    DC dc;
    dc_create(&dc, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <dc_brick_c_examples>`).


.. c:function:: int dc_set_velocity(DC *dc, int16_t velocity)
 
 Sets the velocity of the Motor. Whereas -32767 is full speed backward, 
 0 is stop and 32767 is full speed forward. Depending on the 
 acceleration (see :c:func:`dc_set_acceleration`), the motor is not immediately 
 brought to the velocity but smoothly accelerated.
 
 The velocity describes the duty cycle of the PWM with which the motor is
 controlled, e.g. a velocity of 3277 sets a PWM with a 10% duty cycle.
 You can not only control the duty cycle of the PWM but also the frequency,
 see :c:func:`dc_set_pwm_frequency`.
 
 The default velocity is 0.
 
.. c:function:: int dc_get_velocity(DC *dc, int16_t *ret_velocity)

 Returns the velocity as set by :c:func:`dc_set_velocity`.
 
.. c:function:: int dc_get_current_velocity(DC *dc, int16_t *ret_velocity)

 Returns the *current* velocity of the motor. This value is different
 from :c:func:`dc_get_velocity` whenever the motor is currently accelerating
 to a goal set by :c:func:`dc_set_velocity`.
 
.. c:function:: int dc_set_acceleration(DC *dc, uint16_t acceleration)

 Sets the acceleration of the Motor. It is given in *velocity/s*. An
 acceleration of 10000 means, that every second the velocity is increased
 by 10000 (or about 30% duty cycle).
 
 For example: If the current velocity is 0 and you want to accelerate to a
 velocity of 16000 (about 50% duty cycle) in 10 seconds, you should set
 an acceleration of 1600.
 
 If acceleration is set to 0, there is no speed ramping, i.e. a new velocity
 is immediately given to the motor.
 
 The default acceleration is 10000.
 
.. c:function:: int dc_get_acceleration(DC *dc, uint16_t *ret_acceleration)

 Returns the acceleration as set by :c:func:`dc_set_acceleration`.
 
.. c:function:: int dc_full_brake(DC *dc)

 Executes an active full brake. 
  
  .. warning::
   This function is for emergency purposes,
   where an immediate brake is necessary. Depending on the current velocity and
   the strength of the motor, a full brake can be quite violent.
 
 Call :c:func:`dc_set_velocity` with 0 if you just want to stop the motor.
 
.. c:function:: int dc_enable(DC *dc)

 Enables the motor. The motor can be configured (velocity, 
 acceleration, etc) before it is enabled.
 
.. c:function:: int dc_disable(DC *dc)

 Disables the motor. The configurations are kept (velocity, 
 acceleration, etc) but the motor is not driven until it is enabled again.
 
.. c:function:: int dc_is_enabled(DC *dc, bool *ret_enabled)

 Returns true if the motor is enabled, false otherwise.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int dc_set_pwm_frequency(DC *dc, uint16_t frequency)

 Sets the frequency (in Hz) of the PWM whith which the motor is driven. 
 The possible range of the frequency is 1-20000Hz. Often a high frequency
 is less noisy and the motor runs smoother. However, with a low frequency
 there are less switches and therefore fewer switching losses. Also with
 most motors lower frequencies enable higher torque.
 
 If you have no idea what all this means, just ignore this function and use
 the default frequency, it will very likely work fine.
 
 The default frequency is 15 kHz.
 
.. c:function:: int dc_get_pwm_frequency(DC *dc, uint16_t *ret_frequency)

 Returns the PWM frequency (in Hz) as set by :c:func:`dc_set_pwm_frequency`.
 
.. c:function:: int dc_get_stack_input_voltage(DC *dc, uint16_t *ret_voltage)

 Returns the stack input voltage in mV. The stack input voltage is the
 voltage that is supplied via the stack, i.e. it is given by a 
 Step-Down or Step-Up power supply Brick.
 
.. c:function:: int dc_get_external_input_voltage(DC *dc, uint16_t *ret_voltage)

 Returns the external input voltage in mV. The external input voltage is
 given via the black power input connector on the DC Brick. 
  
 If there is  an externel input voltage and a stack input voltage, the motor 
 will be driven by the external input voltage. If there is only a stack 
 voltage present, the motor will be driven by this voltage.
 
  .. warning:: 
   This means, if you have a high stack voltage and a low external voltage,
   the motor will be driven with the low external voltage. If you then remove
   the external connection, it will immediately be driven by the high
   stack voltage.
 
.. c:function:: int dc_get_current_consumption(DC *dc, uint16_t *ret_voltage)

 Returns the current consumption of the motor in mA.
 
.. c:function:: int dc_set_drive_mode(DC *dc, uint8_t mode)

 Sets the drive mode. Possible modes are:
  * 0 = Drive/Brake
  * 1 = Drive/Coast
  
 These modes are different kinds of motor controls.
 
 In Drive/Brake mode, the motor is always either driving or braking. There
 is no freewheeling. Advantages are: A more linear correlation between
 PWM and velocity, more exact accelerations and the possibility to drive
 with slower velocities.
 
 In Drive/Coast mode, the motor is always either driving or freewheeling.
 Advantages are: Less current consumption and less demands on the motor/driver.
 
 The defaukt value is 0 = Drive/Brake.
 
.. c:function:: int dc_get_drive_mode(DC *dc, uint8_t *ret_mode)

 Returns the drive mode, as set by :c:func:`dc_set_drive_mode`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void dc_register_callback(DC *dc, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <dc_brick_c_callbacks>`.


.. c:function:: int dc_set_minimum_voltage(DC *dc, uint16_t voltage)

 Sets the minimum voltage in mV, below which the :c:data:`DC_CALLBACK_UNDER_VOLTAGE` callback
 is called. The minimum possible value that works with the DC Brick is 5V.
 You can use this function to detect the discharge of a battery that is used
 to drive the motor. If you have a fixed power supply, you likely do not need 
 this functionality.
 
 The default value is 5V.
 
.. c:function:: int dc_get_minimum_voltage(DC *dc, uint16_t *ret_voltage)

 Returns the minimum voltage as set by :c:func:`dc_set_minimum_voltage`
 
.. c:function:: int dc_set_current_velocity_period(DC *dc, uint16_t period)

 Sets a period in ms with which the :c:data:`DC_CALLBACK_CURRENT_VELOCITY` callback is called.
 A period of 0 turns the callback off.
 
 The default value is 0.
 
.. c:function:: int dc_get_current_velocity_period(DC *dc, uint16_t *ret_period)

 Returns the period as set by :c:func:`dc_set_current_velocity_period`.
 


.. _dc_brick_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    dc_register_callback(&dc, DC_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: DC_CALLBACK_UNDER_VOLTAGE

 .. c:var:: signature: void callback(uint16_t voltage)
    :noindex:


 This callback is called when the input voltage drops below the value set by
 :c:func:`dc_set_minimum_voltage`. The parameter is the current voltage given
 in mV.
 
.. c:var:: DC_CALLBACK_EMERGENCY_SHUTDOWN

 .. c:var:: signature: void callback(void)
    :noindex:


 The EmergencyShutdown callback is called if either the current consumption
 is too high (above 5A) or the temperature of the driver is too high 
 (above 175°C). These two possibilities are essentially the same, since the
 temperature will reach this threshold immediately if the motor draws too
 much current.
 
 If this callback is called, the driver gets disabled at the same time. 
 That means, :c:func:`dc_enable` has to be called to drive the motor again.
 
 .. note::
  This callback only works in Drive/Brake mode (see :func:`SetMode`). In 
  Drive/Coast mode it is unfortunately impossible to reliably read the 
  over current/over temperature signal from the driver chip.
 
.. c:var:: DC_CALLBACK_VELOCITY_REACHED

 .. c:var:: signature: void callback(int16_t voltage)
    :noindex:


 This callback is called whenever a set velocity is reached. For example:
 If a velocity of 0 is present, acceleration is set to 5000 and velocity
 to 10000, func:`VelocityReached` will be called after about 2 seconds, when
 the set velocity is actually reached.
 
 .. note::
  Since we can't get any feedback from the dc motor, this only works if the
  acceleration (see :c:func:`dc_set_acceleration`) is set smaller or equal to the
  maximum acceleration of the motor. Otherwise the motor will lag behind the
  control value and the callback will be called too early.
 
.. c:var:: DC_CALLBACK_CURRENT_VELOCITY

 .. c:var:: signature: void callback(int16_t voltage)
    :noindex:


 This callback is called with the period that is set by 
 :c:func:`dc_set_current_velocity_period`. The parameter is the *current* velocity
 used by the motor.
 
 :c:data:`DC_CALLBACK_CURRENT_VELOCITY` is only called after the set period if there is 
 a change in the velocity.
 


