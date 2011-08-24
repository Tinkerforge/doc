..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

Python - Stepper Brick
======================

.. _stepper_brick_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Configuration
^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Stepper_Brick_Python_example_configuration.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Stepper_Brick_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

.. _stepper_brick_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: Stepper(uid)

 Creates a stepper object with the unique device ID *uid*::

    stepper = Stepper("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <stepper_brick_python_examples>`).


.. py:function:: Stepper.set_max_velocity(velocity)

 :param velocity: int
 :rtype: None

 Sets the maximum velocity of the stepper motor in steps per second.
 This function does *not* start the motor, it merely sets the maximum
 velocity the stepper motor is accelerated to. To get the motor running use
 either :py:func:`Stepper.set_target_position`, :py:func:`Stepper.set_steps`, :py:func:`Stepper.drive_forward` or
 :py:func:`Stepper.drive_backward`.
 
.. py:function:: Stepper.get_max_velocity()

 :rtype: int

 Returns the velocity as set by :py:func:`Stepper.set_max_velocity`.
 
.. py:function:: Stepper.get_current_velocity()

 :rtype: int

 Returns the *current* velocity of the stepper motor in steps per second.
 
.. py:function:: Stepper.set_speed_ramping(acceleration, deacceleration)

 :param acceleration: int
 :param deacceleration: int
 :rtype: None

 Sets the acceleration and deacceleration of the stepper motor. The values
 are given in *steps/s²*. An acceleration of 1000 means, that
 every second the velocity is increased by 1000 *steps/s*.
 
 For example: If the current velocity is 0 and you want to accelerate to a
 velocity of 8000 *steps/s* in 10 seconds, you should set an acceleration
 of 800 *steps/s²*.
 
 An dacceleration/deacceleration of 0 means instantaneous 
 acceleration/deacceleration (not recomended)
 
 The default value is 1000 for both
 
.. py:function:: Stepper.get_speed_ramping()

 :rtype: (int, int)

 Returns the acceleration and deacceleration as set by 
 :py:func:`Stepper.set_speed_ramping`.
 
.. py:function:: Stepper.full_brake()

 :rtype: None

 Executes an active full brake. 
  
  .. warning::
   This function is for emergency purposes,
   where an immediate brake is necessary. Depending on the current velocity and
   the strength of the motor, a full brake can be quite violent.
 
 Call :py:func:`Stepper.stop` if you just want to stop the motor.
 
.. py:function:: Stepper.set_steps(steps)

 :param steps: int
 :rtype: None

 Sets the number of steps the stepper motor should run. Positive values
 will drive the motor forward and negative values backward. 
 The velocity, acceleration and deacceleration as set by
 :py:func:`Stepper.set_max_velocity` and :py:func:`Stepper.set_speed_ramping` will be used.
 
.. py:function:: Stepper.get_steps()

 :rtype: int

 Returns the last steps as set by :py:func:`Stepper.set_steps`.
 
.. py:function:: Stepper.get_remaining_steps()

 :rtype: int

 Returns the remaining steps of the last call of :py:func:`Stepper.set_steps`.
 For example, if :py:func:`Stepper.set_steps` is called with 2000 and 
 :py:func:`Stepper.get_remaining_steps` is called after the motor has run for 500 steps,
 it will return 1500.
 
.. py:function:: Stepper.drive_forward()

 :rtype: None

 Drives the stepper motor forward until :py:func:`Stepper.drive_backward` or
 :py:func:`Stepper.stop` is called. The velocity, acceleration and deacceleration as 
 set by :py:func:`Stepper.set_max_velocity` and :py:func:`Stepper.set_speed_ramping` will be used.
 
.. py:function:: Stepper.drive_backward()

 :rtype: None

 Drives the stepper motor backward until :py:func:`Stepper.drive_forward` or
 :py:func:`Stepper.stop` is called. The velocity, acceleration and deacceleration as 
 set by :py:func:`Stepper.set_max_velocity` and :py:func:`Stepper.set_speed_ramping` will be used.
 
.. py:function:: Stepper.stop()

 :rtype: None

 Stops the stepper motor with the deacceleration as set by 
 :py:func:`Stepper.set_speed_ramping`.
 
.. py:function:: Stepper.set_motor_current(current)

 :param current: int
 :rtype: None

 Sets the current in mA with which the motor will be driven.
 The minimum value is 100mA, the maximum value 2291mA and the 
 default value is 800mA.
 
  .. warning::
   Do not set this value above the specifications of your stepper motor.
   Otherwise it may damage your motor.
 
.. py:function:: Stepper.get_motor_current()

 :rtype: int

 Returns the current as set by :py:func:`Stepper.set_motor_current`.
 
.. py:function:: Stepper.enable()

 :rtype: None

 Enables the motor. The motor can be configured (maximum velocity, 
 acceleration, etc) before it is enabled.
 
.. py:function:: Stepper.disable()

 :rtype: None

 Disables the motor. The configurations are kept (maximum velocity, 
 acceleration, etc) but the motor is not driven until it is enabled again.
 
.. py:function:: Stepper.is_enabled()

 :rtype: bool

 Returns true if the motor is enabled, false otherwise.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: Stepper.set_current_position(position)

 :param position: int
 :rtype: None

 Sets the current steps of the internal step counter. This can be used to
 set the current position to 0 when some kind of starting position
 is reached (e.g. when a cnc machine reaches a corner).
 
.. py:function:: Stepper.get_current_position()

 :rtype: int

 Returns the current position of the stepper motor in steps. On startup
 the position is 0. The steps are counted with all possible driving
 functions (:py:func:`Stepper.set_target_position`, :py:func:`Stepper.set_steps`, :py:func:`Stepper.drive_forward` or
 :py:func:`Stepper.drive_backward`). It also is possible to reset the steps to 0 or
 set them to any other desired value with :py:func:`Stepper.set_current_position`.
 
.. py:function:: Stepper.set_target_position(position)

 :param position: int
 :rtype: None

 Sets the target position of the stepper motor in steps. For example,
 if the current position of the motor is 500 and :py:func:`Stepper.set_target_position` is
 called with 1000, the stepper motor will drive 500 steps forward. It will
 use the velocity, acceleration and deacceleration as set by
 :py:func:`Stepper.set_max_velocity` and :py:func:`Stepper.set_speed_ramping`.
 
 A call of :py:func:`Stepper.set_target_position` with the parameter *x* is equivalent to
 a call of :py:func:`Stepper.set_steps` with the parameter 
 (*x* - :py:func:`Stepper.get_current_position`).
 
.. py:function:: Stepper.get_target_position()

 :rtype: int

 Returns the last target position as set by :py:func:`Stepper.set_target_position`.
 
.. py:function:: Stepper.set_step_mode(mode)

 :param mode: int
 :rtype: None

 Sets the step mode of the stepper motor. Possible values are:
 
 * Full Step = 1
 * Half Step = 2
 * Quarter Step = 4
 * Eighth Step = 8
 
 A higher value will increase the resolution and
 decrease the torque of the stepper motor.
 
 The default value is 1 (Full Step).
 
.. py:function:: Stepper.get_step_mode()

 :rtype: int

 Returns the step mode as set by :py:func:`Stepper.set_step_mode`.
 
.. py:function:: Stepper.get_stack_input_voltage()

 :rtype: int

 Returns the stack input voltage in mV. The stack input voltage is the
 voltage that is supplied via the stack, i.e. it is given by a 
 Step-Down or Step-Up power supply Brick.
 
.. py:function:: Stepper.get_external_input_voltage()

 :rtype: int

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
 
.. py:function:: Stepper.get_current_consumption()

 :rtype: int

 Returns the current consumption of the motor in mA.
 
.. py:function:: Stepper.set_decay(decay)

 :param decay: int
 :rtype: None

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
 
.. py:function:: Stepper.get_decay()

 :rtype: int

 Returns the decay mode as set by :py:func:`Stepper.set_decay`
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: Stepper.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <stepper_brick_python_callbacks>`.


.. py:function:: Stepper.set_minimum_voltage(voltage)

 :param voltage: int
 :rtype: None

 Sets the minimum voltage in mV, below which the :py:attr:`Stepper.CALLBACK_UNDER_VOLTAGE` signal
 is called. The minimum possible value that works with the Stepper Brick is 8V. 
 You can use this function to detect the discharge of a battery that is used
 to drive the stepper motor. If you have a fixed power supply, you likely do 
 not need this functionality.
 
 The default value is 8V.
 
.. py:function:: Stepper.get_minimum_voltage()

 :rtype: int

 Returns the minimum voltage as set by :py:func:`Stepper.set_minimum_voltage`.
 


.. _stepper_brick_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    stepper.register_callback(stepper.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: Stepper.CALLBACK_UNDER_VOLTAGE

 :param voltage: int


 This callback is called when the input voltage drops below the value set by
 :py:func:`Stepper.set_minimum_voltage`. The parameter is the current voltage given
 in mV.
 
.. py:attribute:: Stepper.CALLBACK_POSITION_REACHED

 :param position: int


 This callback is called when a position set by :py:func:`Stepper.set_steps` or
 :py:func:`Stepper.set_target_position` is reached.
 
 .. note::
  Since we can't get any feedback from the stepper motor, this only works if the
  acceleration (see :py:func:`Stepper.set_speed_ramping`) is set smaller or equal to the
  maximum acceleration of the motor. Otherwise the motor will lag behind the
  control value and the callback will be called too early.
 


