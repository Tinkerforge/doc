..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _dc_brick_python:

Python - DC Brick
=================

.. _dc_brick_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Configuration
^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: DC_Brick_Python_example_configuration.py
 :language: python
 :linenos:
 :tab-width: 4

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: DC_Brick_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

.. _dc_brick_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: DC(uid)

 Creates a dc object with the unique device ID *uid*::

    dc = DC("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <dc_brick_python_examples>`).


.. py:function:: DC.set_velocity(velocity)

 :param velocity: int
 :rtype: None
 
 Sets the velocity of the Motor. Whereas -32767 is full speed backward, 
 0 is stop and 32767 is full speed forward. Depending on the 
 acceleration (see :py:func:`DC.set_acceleration`), the motor is not immediately 
 brought to the velocity but smoothly accelerated.
 
 The velocity describes the duty cycle of the PWM with which the motor is
 controlled, e.g. a velocity of 3277 sets a PWM with a 10% duty cycle.
 You can not only control the duty cycle of the PWM but also the frequency,
 see :py:func:`DC.set_pwm_frequency`.
 
 The default velocity is 0.
 
.. py:function:: DC.get_velocity()

 :rtype: int

 Returns the velocity as set by :py:func:`DC.set_velocity`.
 
.. py:function:: DC.get_current_velocity()

 :rtype: int

 Returns the *current* velocity of the motor. This value is different
 from :py:func:`DC.get_velocity` whenever the motor is currently accelerating
 to a goal set by :py:func:`DC.set_velocity`.
 
.. py:function:: DC.set_acceleration(acceleration)

 :param acceleration: int
 :rtype: None

 Sets the acceleration of the Motor. It is given in *velocity/s*. An
 acceleration of 10000 means, that every second the velocity is increased
 by 10000 (or about 30% duty cycle).
 
 For example: If the current velocity is 0 and you want to accelerate to a
 velocity of 16000 (about 50% duty cycle) in 10 seconds, you should set
 an acceleration of 1600.
 
 If acceleration is set to 0, there is no speed ramping, i.e. a new velocity
 is immediately given to the motor.
 
 The default acceleration is 10000.
 
.. py:function:: DC.get_acceleration()

 :rtype: int

 Returns the acceleration as set by :py:func:`DC.set_acceleration`.
 
.. py:function:: DC.full_brake()

 :rtype: None

 Executes an active full brake. 
  
  .. warning::
   This function is for emergency purposes,
   where an immediate brake is necessary. Depending on the current velocity and
   the strength of the motor, a full brake can be quite violent.
 
 Call :py:func:`DC.set_velocity` with 0 if you just want to stop the motor.
 
.. py:function:: DC.enable()

 :rtype: None

 Enables the motor. The motor can be configured (velocity, 
 acceleration, etc) before it is enabled.
 
.. py:function:: DC.disable()

 :rtype: None

 Disables the motor. The configurations are kept (velocity, 
 acceleration, etc) but the motor is not driven until it is enabled again.
 
.. py:function:: DC.is_enabled()

 :rtype: bool

 Returns true if the motor is enabled, false otherwise.
 


Advanced Methods
^^^^^^^^^^^^^^^^

.. py:function:: DC.set_pwm_frequency(frequency)

 :param frequency: int
 :rtype: None

 Sets the frequency (in Hz) of the PWM whith which the motor is driven. 
 The possible range of the frequency is 1-20000Hz. Often a high frequency
 is less noisy and the motor runs smoother. However, with a low frequency
 there are less switches and therefore fewer switching losses. Also with
 most motors lower frequencies enable higher torque.
 
 If you have no idea what all this means, just ignore this function and use
 the default frequency, it will very likely work fine.
 
 The default frequency is 15 kHz.
 
.. py:function:: DC.get_pwm_frequency()

 :rtype: int

 Returns the PWM frequency (in Hz) as set by :py:func:`DC.set_pwm_frequency`.
 
.. py:function:: DC.get_stack_input_voltage()

 :rtype: int

 Returns the stack input voltage in mV. The stack input voltage is the
 voltage that is supplied via the stack, i.e. it is given by a 
 Step-Down or Step-Up power supply Brick.
 
.. py:function:: DC.get_external_input_voltage()

 :rtype: int

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
 
.. py:function:: DC.get_current_consumption()

 :rtype: int

 Returns the current consumption of the motor in mA.
 
.. py:function:: DC.set_drive_mode(mode)

 :param mode: int
 :rtype: None

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
 
.. py:function:: DC.get_drive_mode()

 :rtype: int

 Returns the drive mode, as set by :py:func:`DC.set_drive_mode`.
 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: DC.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <dc_brick_python_callbacks>`.


.. py:function:: DC.set_minimum_voltage(voltage)

 :param voltage: int
 :rtype: None

 Sets the minimum voltage in mV, below which the :py:attr:`DC.CALLBACK_UNDER_VOLTAGE` callback
 is called. The minimum possible value that works with the DC Brick is 5V.
 You can use this function to detect the discharge of a battery that is used
 to drive the motor. If you have a fixed power supply, you likely do not need 
 this functionality.
 
 The default value is 5V.
 
.. py:function:: DC.get_minimum_voltage()

 :rtype: int

 Returns the minimum voltage as set by :py:func:`DC.set_minimum_voltage`
 
.. py:function:: DC.set_current_velocity_period(period)

 :param period: int
 :rtype: None

 Sets a period in ms with which the :py:attr:`DC.CALLBACK_CURRENT_VELOCITY` callback is called.
 A period of 0 turns the callback off.
 
 The default value is 0.
 
.. py:function:: DC.get_current_velocity_period()

 :rtype: int

 Returns the period as set by :py:func:`DC.set_current_velocity_period`.
 


.. _dc_brick_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    dc.register_callback(dc.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: DC.CALLBACK_UNDER_VOLTAGE

 :param voltage: int


 This callback is called when the input voltage drops below the value set by
 :py:func:`DC.set_minimum_voltage`. The parameter is the current voltage given
 in mV.
 
.. py:attribute:: DC.CALLBACK_EMERGENCY_SHUTDOWN



 The EmergencyShutdown callback is called if either the current consumption
 is too high (above 5A) or the temperature of the driver is too high 
 (above 175°C). These two possibilities are essentially the same, since the
 temperature will reach this threshold immediately if the motor draws too
 much current.
 
 If this callback is called, the driver gets disabled at the same time. 
 That means, :py:func:`DC.enable` has to be called to drive the motor again.
 
 .. note::
  This callback only works in Drive/Brake mode (see :func:`SetMode`). In 
  Drive/Coast mode it is unfortunately impossible to reliably read the 
  over current/over temperature signal from the driver chip.
 
.. py:attribute:: DC.CALLBACK_VELOCITY_REACHED

 :param voltage: int


 This callback is called whenever a set velocity is reached. For example:
 If a velocity of 0 is present, acceleration is set to 5000 and velocity
 to 10000, func:`VelocityReached` will be called after about 2 seconds, when
 the set velocity is actually reached.
 
 .. note::
  Since we can't get any feedback from the dc motor, this only works if the
  acceleration (see :py:func:`DC.set_acceleration`) is set smaller or equal to the
  maximum acceleration of the motor. Otherwise the motor will lag behind the
  control value and the callback will be called too early.
 
.. py:attribute:: DC.CALLBACK_CURRENT_VELOCITY

 :param voltage: int


 This callback is called with the period that is set by 
 :py:func:`DC.set_current_velocity_period`. The parameter is the *current* velocity
 used by the motor.
 
 :py:attr:`DC.CALLBACK_CURRENT_VELOCITY` is only called after the set period if there is 
 a change in the velocity.
 


