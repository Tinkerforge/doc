..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _stepper_brick_c:

C - Stepper Brick
=================

.. _stepper_brick_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Configuration
^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Stepper_Brick_C_example_configuration.c
 :language: c
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Stepper_Brick_C_example_callback.c
 :language: c
 :linenos:
 :tab-width: 4

.. _stepper_brick_c_api:

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


.. c:function:: void stepper_create(Stepper *stepper, const char *uid)

 Creates a Stepper object with the unique device ID *uid*::

    Stepper stepper;
    stepper_create(&stepper, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <stepper_brick_c_examples>`).


.. c:function:: int stepper_set_max_velocity(Stepper *stepper, uint16_t velocity)

 Sets the maximum velocity of the stepper motor in steps per second.
 This function does *not* start the motor, it merely sets the maximum
 velocity the stepper motor is accelerated to. To get the motor running use
 either :c:func:`stepper_set_target_position`, :c:func:`stepper_set_steps`, :c:func:`stepper_drive_forward` or
 :c:func:`stepper_drive_backward`.
 
.. c:function:: int stepper_get_max_velocity(Stepper *stepper, uint16_t *ret_velocity)

 Returns the velocity as set by :c:func:`stepper_set_max_velocity`.
 
.. c:function:: int stepper_get_current_velocity(Stepper *stepper, uint16_t *ret_velocity)

 Returns the *current* velocity of the stepper motor in steps per second.
 
.. c:function:: int stepper_set_speed_ramping(Stepper *stepper, uint16_t acceleration, uint16_t deacceleration)

 Sets the acceleration and deacceleration of the stepper motor. The values
 are given in *steps/s²*. An acceleration of 1000 means, that
 every second the velocity is increased by 1000 *steps/s*.
 
 For example: If the current velocity is 0 and you want to accelerate to a
 velocity of 8000 *steps/s* in 10 seconds, you should set an acceleration
 of 800 *steps/s²*.
 
 An dacceleration/deacceleration of 0 means instantaneous 
 acceleration/deacceleration (not recomended)
 
 The default value is 1000 for both
 
.. c:function:: int stepper_get_speed_ramping(Stepper *stepper, uint16_t *ret_acceleration, uint16_t *ret_deacceleration)

 Returns the acceleration and deacceleration as set by 
 :c:func:`stepper_set_speed_ramping`.
 
.. c:function:: int stepper_full_brake(Stepper *stepper)

 Executes an active full brake. 
  
  .. warning::
   This function is for emergency purposes,
   where an immediate brake is necessary. Depending on the current velocity and
   the strength of the motor, a full brake can be quite violent.
 
 Call :c:func:`stepper_stop` if you just want to stop the motor.
 
.. c:function:: int stepper_set_steps(Stepper *stepper, int32_t steps)

 Sets the number of steps the stepper motor should run. Positive values
 will drive the motor forward and negative values backward. 
 The velocity, acceleration and deacceleration as set by
 :c:func:`stepper_set_max_velocity` and :c:func:`stepper_set_speed_ramping` will be used.
 
.. c:function:: int stepper_get_steps(Stepper *stepper, int32_t *ret_steps)

 Returns the last steps as set by :c:func:`stepper_set_steps`.
 
.. c:function:: int stepper_get_remaining_steps(Stepper *stepper, int32_t *ret_steps)

 Returns the remaining steps of the last call of :c:func:`stepper_set_steps`.
 For example, if :c:func:`stepper_set_steps` is called with 2000 and 
 :c:func:`stepper_get_remaining_steps` is called after the motor has run for 500 steps,
 it will return 1500.
 
.. c:function:: int stepper_drive_forward(Stepper *stepper)

 Drives the stepper motor forward until :c:func:`stepper_drive_backward` or
 :c:func:`stepper_stop` is called. The velocity, acceleration and deacceleration as 
 set by :c:func:`stepper_set_max_velocity` and :c:func:`stepper_set_speed_ramping` will be used.
 
.. c:function:: int stepper_drive_backward(Stepper *stepper)

 Drives the stepper motor backward until :c:func:`stepper_drive_forward` or
 :c:func:`stepper_stop` is called. The velocity, acceleration and deacceleration as 
 set by :c:func:`stepper_set_max_velocity` and :c:func:`stepper_set_speed_ramping` will be used.
 
.. c:function:: int stepper_stop(Stepper *stepper)

 Stops the stepper motor with the deacceleration as set by 
 :c:func:`stepper_set_speed_ramping`.
 
.. c:function:: int stepper_set_motor_current(Stepper *stepper, uint16_t current)

 Sets the current in mA with which the motor will be driven.
 The minimum value is 100mA, the maximum value 2291mA and the 
 default value is 800mA.
 
  .. warning::
   Do not set this value above the specifications of your stepper motor.
   Otherwise it may damage your motor.
 
.. c:function:: int stepper_get_motor_current(Stepper *stepper, uint16_t *ret_current)

 Returns the current as set by :c:func:`stepper_set_motor_current`.
 
.. c:function:: int stepper_enable(Stepper *stepper)

 Enables the motor. The motor can be configured (maximum velocity, 
 acceleration, etc) before it is enabled.
 
.. c:function:: int stepper_disable(Stepper *stepper)

 Disables the motor. The configurations are kept (maximum velocity, 
 acceleration, etc) but the motor is not driven until it is enabled again.
 
.. c:function:: int stepper_is_enabled(Stepper *stepper, bool *ret_enabled)

 Returns true if the motor is enabled, false otherwise.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. c:function:: int stepper_set_current_position(Stepper *stepper, int32_t position)

 Sets the current steps of the internal step counter. This can be used to
 set the current position to 0 when some kind of starting position
 is reached (e.g. when a cnc machine reaches a corner).
 
.. c:function:: int stepper_get_current_position(Stepper *stepper, int32_t *ret_position)

 Returns the current position of the stepper motor in steps. On startup
 the position is 0. The steps are counted with all possible driving
 functions (:c:func:`stepper_set_target_position`, :c:func:`stepper_set_steps`, :c:func:`stepper_drive_forward` or
 :c:func:`stepper_drive_backward`). It also is possible to reset the steps to 0 or
 set them to any other desired value with :c:func:`stepper_set_current_position`.
 
.. c:function:: int stepper_set_target_position(Stepper *stepper, int32_t position)

 Sets the target position of the stepper motor in steps. For example,
 if the current position of the motor is 500 and :c:func:`stepper_set_target_position` is
 called with 1000, the stepper motor will drive 500 steps forward. It will
 use the velocity, acceleration and deacceleration as set by
 :c:func:`stepper_set_max_velocity` and :c:func:`stepper_set_speed_ramping`.
 
 A call of :c:func:`stepper_set_target_position` with the parameter *x* is equivalent to
 a call of :c:func:`stepper_set_steps` with the parameter 
 (*x* - :c:func:`stepper_get_current_position`).
 
.. c:function:: int stepper_get_target_position(Stepper *stepper, int32_t *ret_position)

 Returns the last target position as set by :c:func:`stepper_set_target_position`.
 
.. c:function:: int stepper_set_step_mode(Stepper *stepper, uint8_t mode)

 Sets the step mode of the stepper motor. Possible values are:
 
 * Full Step = 1
 * Half Step = 2
 * Quarter Step = 4
 * Eighth Step = 8
 
 A higher value will increase the resolution and
 decrease the torque of the stepper motor.
 
 The default value is 1 (Full Step).
 
.. c:function:: int stepper_get_step_mode(Stepper *stepper, uint8_t *ret_mode)

 Returns the step mode as set by :c:func:`stepper_set_step_mode`.
 
.. c:function:: int stepper_get_stack_input_voltage(Stepper *stepper, uint16_t *ret_voltage)

 Returns the stack input voltage in mV. The stack input voltage is the
 voltage that is supplied via the stack, i.e. it is given by a 
 Step-Down or Step-Up power supply Brick.
 
.. c:function:: int stepper_get_external_input_voltage(Stepper *stepper, uint16_t *ret_voltage)

 Returns the external input voltage in mV. The external input voltage is
 given via the black power input connector on the Stepper Brick. 
  
 If there is  an externel input voltage and a stack input voltage, the motor 
 will be driven by the external input voltage. If there is only a stack 
 voltage present, the motor will be driven by this voltage.
 
  .. warning:: 
   This means, if you have a high stack voltage and a low external voltage,
   the motor will be driven with the low external voltage. If you then remove
   the external connection, it will immediately be driven by the high
   stack voltage
 
.. c:function:: int stepper_get_current_consumption(Stepper *stepper, uint16_t *ret_current)

 Returns the current consumption of the motor in mA.
 
.. c:function:: int stepper_set_decay(Stepper *stepper, uint16_t decay)

 Sets the decay mode of the stepper motor. The possible value range is
 between 0 and 65535. A value of 0 sets the fast decay mode, a value of
 65535 sets the slow decay mode and a value in between sets the mixed
 decay mode.
 
 For a good explanation of the different decay modes see 
 `this <http://robot.avayanex.com/?p=86/>`_ blog post by Avayan.
 
 A good decay mode is unfortunately different for every motor. The best
 way to work out a good decay mode for your stepper motor, if you can't
 measure the current with an oscilloscope, is to listen to the sound of
 the motor. If the value is too low, you often hear a high pitched 
 sound and if it is too high you can often hear a humming sound.
 
 Generally, fast decay mode (small value) will be noisier but also
 allow higher motor speeds.
 
 The default value is 10000.
  .. note::
   There is unfortunately no formula to calculate a perfect decay
   mode for a given stepper motor. If you have problems with loud noises
   or the maximum motor speed is too slow, you should try to tinker with
   the decay value
 
.. c:function:: int stepper_get_decay(Stepper *stepper, uint16_t *ret_decay)

 Returns the decay mode as set by :c:func:`stepper_set_decay`
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void stepper_register_callback(Stepper *stepper, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <stepper_brick_c_callbacks>`.


.. c:function:: int stepper_set_minimum_voltage(Stepper *stepper, uint16_t voltage)

 Sets the minimum voltage in mV, below which the :c:data:`STEPPER_CALLBACK_UNDER_VOLTAGE` signal
 is called. The minimum possible value that works with the Stepper Brick is 8V. 
 You can use this function to detect the discharge of a battery that is used
 to drive the stepper motor. If you have a fixed power supply, you likely do 
 not need this functionality.
 
 The default value is 8V.
 
.. c:function:: int stepper_get_minimum_voltage(Stepper *stepper, uint16_t *ret_voltage)

 Returns the minimum voltage as set by :c:func:`stepper_set_minimum_voltage`.
 


.. _stepper_brick_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    stepper_register_callback(&stepper, STEPPER_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: STEPPER_CALLBACK_UNDER_VOLTAGE

 .. c:var:: signature: void callback(uint16_t voltage)
    :noindex:


 This callback is called when the input voltage drops below the value set by
 :c:func:`stepper_set_minimum_voltage`. The parameter is the current voltage given
 in mV.
 
.. c:var:: STEPPER_CALLBACK_POSITION_REACHED

 .. c:var:: signature: void callback(int32_t position)
    :noindex:


 This callback is called when a position set by :c:func:`stepper_set_steps` or
 :c:func:`stepper_set_target_position` is reached.
 
 .. note::
  Since we can't get any feedback from the stepper motor, this only works if the
  acceleration (see :c:func:`stepper_set_speed_ramping`) is set smaller or equal to the
  maximum acceleration of the motor. Otherwise the motor will lag behind the
  control value and the callback will be called too early.
 


