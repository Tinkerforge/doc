..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _servo_brick_python:

Python - Servo Brick
====================

.. _servo_brick_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

Callback
^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Servo_Brick_Python_example_callback.py
 :language: python
 :linenos:
 :tab-width: 4

Configuration
^^^^^^^^^^^^^

TODO: link zum download der datei

.. literalinclude:: Servo_Brick_Python_example_configuration.py
 :language: python
 :linenos:
 :tab-width: 4

.. _servo_brick_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: Servo(uid)

 Creates a servo object with the unique device ID *uid*::

    servo = Servo("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <servo_brick_python_examples>`).


.. py:function:: Servo.enable(servo_num)

 :param servo_num: int
 :rtype: None

 Enables a servo (0 to 6). If a servo is enabled, the configured position,
 velocity, acceleration, etc. are applied immediately.
 
.. py:function:: Servo.disable(servo_num)

 :param servo_num: int
 :rtype: None

 Disables a servo (0 to 6). Disabled servos are not driven at all, i.e. a
 disabled servo will not hold its position if a load is applied.
 
.. py:function:: Servo.is_enabled(servo_num)

 :param servo_num: int
 :rtype: bool

 Returns true if the specified servo is enabled, false otherwise.
 
.. py:function:: Servo.set_position(servo_num, position)

 :param servo_num: int
 :param position: int
 :rtype: None

 Sets the position in °/100 for the specified servo. 
 
 The default range of the position is -9000 to 9000, but it can be specified
 according to your servo with :py:func:`Servo.set_degree`.
 
 If you want to control a linear servo or RC brushless motor controller or
 similar with the Servo Brick, you can also define lengths or speeds with
 :py:func:`Servo.set_degree`.
 
.. py:function:: Servo.get_position(servo_num)

 :param servo_num: int
 :rtype: int

 Returns the position of the specified servo as set by :py:func:`Servo.set_position`.
 
.. py:function:: Servo.get_current_position(servo_num)

 :param servo_num: int
 :rtype: int

 Returns the *current* position of the specified servo. This may not be the
 value of :py:func:`Servo.set_position` if the servo is currently approaching a
 position goal.
 
.. py:function:: Servo.set_velocity(servo_num, velocity)

 :param servo_num: int
 :param velocity: int
 :rtype: None

 Sets the maximum velocity of the specified servo in °/100s. The velocity
 is accelerated according to the value set by :py:func:`Servo.set_acceleration`.
 
 The minimum velocity is 0 (no movement) and the maximum velocity is 65535.
 With a value of 65535 the position will be set immediately (no velocity).
 
 The default value is 65535.
 
.. py:function:: Servo.get_velocity(servo_num)

 :param servo_num: int
 :rtype: int

 Returns the velocity of the specified servo as set by :py:func:`Servo.set_velocity`.
 
.. py:function:: Servo.get_current_velocity(servo_num)

 :param servo_num: int
 :rtype: int

 Returns the *current* velocity of the specified servo. This may not be the
 value of :py:func:`Servo.set_velocity` if the servo is currently approaching a
 velocity goal.
 
.. py:function:: Servo.set_acceleration(servo_num, acceleration)

 :param servo_num: int
 :param acceleration: int
 :rtype: None

 Sets the acceleration of the specified servo in °/100s².
 
 The minimum acceleration is 1 and the maximum acceleration is 65535.
 With a value of 65535 the velocity will be set immediately (no acceleration).
 
 The default value is 65535.
 
.. py:function:: Servo.get_acceleration(servo_num)

 :param servo_num: int
 :rtype: int

 Returns the acceleration for the specified servo as set by 
 :py:func:`Servo.set_acceleration`.
 
.. py:function:: Servo.set_output_voltage(voltage)

 :param voltage: int
 :rtype: None

 Sets the output voltages with which the servos are driven in mV.
 The minimum output voltage is 5000mV and the maximum output voltage is 
 9000mV.
 
  .. note::
   We recommend that you set this value to the maximum voltage that is
   specified for your servo, most servos achieve their maximum force only
   with high voltages.
 
 The default value is 5000.
 
.. py:function:: Servo.get_output_voltage()

 :rtype: int

 Returns the output voltage as specified by :py:func:`Servo.set_output_voltage`.
 
.. py:function:: Servo.set_pulse_width(servo_num, min, max)

 :param servo_num: int
 :param min: int
 :param max: int
 :rtype: None

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
 
.. py:function:: Servo.get_pulse_width(servo_num)

 :param servo_num: int
 :rtype: (int, int)

 Returns the minimum and maximum pulse width for the specified servo as set by
 :py:func:`Servo.set_pulse_width`.
 
.. py:function:: Servo.set_degree(servo_num, min, max)

 :param servo_num: int
 :param min: int
 :param max: int
 :rtype: None

 Sets the minimum and maximum degree for the specified servo (by default
 given as °/100).
 
 This only specifies the abstract values between which the minimum and maximum
 pulse width is scaled. For example: If you specifiy a pulse width of 1000µs
 to 2000µs and a degree range of -90° to 90°, a call of :py:func:`Servo.set_position`
 with 0 will result in a pulse width of 1500µs 
 (-90° = 1000µs, 90° = 2000µs, etc.).
 
 Possible usage:
 
  * The datasheet of your servo specifies a range of 200° with the middle position at 110°. In this case you can set the minimum to -9000 and the maximum to 11000.
  * You measure a range of 220° on your servo and you don't have or need a middle position. In this case you can set the minimum to 0 and the maximum to 22000.
  * You have a linear servo with a drive length of 20cm, In this case you could set the minimum to 0 and the maximum to 20000. Now you can set the Position with :py:func:`Servo.set_position` with a resolution of cm/100. Also the velocity will have a resoltion of cm/100s and the acceleration will have a resolution of cm/100s².
  * You don't care about units and just want the highest possible resolution. In this case you should set the minimum to -32767 and the maximum to 32767.
  * You have a brushless motor with a maximum speed of 10000 rpm and want to conrol it with a RC brushless motor controller. In this case you can set the minimum to 0 and the maximum to 10000. :py:func:`Servo.set_position` now controls the rpm.
 
 Both values have a possible range from -32767 to 32767 
 (signed 16 bit integer). The minimum must be smaller than the maximum.
 
 The default values are -9000 and 9000 for the minimum and maximum degree.
 
.. py:function:: Servo.get_degree(servo_num)

 :param servo_num: int
 :rtype: (int, int)

 Returns the minimum and maximum degree for the specified servo as set by
 :py:func:`Servo.set_degree`.
 
.. py:function:: Servo.set_period(servo_num, period)

 :param servo_num: int
 :param period: int
 :rtype: None

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
 
.. py:function:: Servo.get_period(servo_num)

 :param servo_num: int
 :rtype: int

 Returns the period for the specified servo as set by :py:func:`Servo.set_period`.
 
.. py:function:: Servo.get_servo_current(servo_num)

 :param servo_num: int
 :rtype: int

 Returns the current consumption of the specified servo in mA.
 
.. py:function:: Servo.get_overall_current()

 :rtype: int

 Returns the current consumption of all servos together in mA.
 
.. py:function:: Servo.get_stack_input_voltage()

 :rtype: int

 Returns the stack input voltage in mV. The stack input voltage is the
 voltage that is supplied via the stack, i.e. it is given by a 
 Step-Down or Step-Up power supply Brick.
 
.. py:function:: Servo.get_external_input_voltage()

 :rtype: int

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


.. py:function:: Servo.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <servo_brick_python_callbacks>`.


.. py:function:: Servo.set_minimum_voltage(voltage)

 :param voltage: int
 :rtype: None

 Sets the minimum voltage in mV, below which the :py:attr:`Servo.CALLBACK_UNDER_VOLTAGE` signal
 is called. The minimum possible value that works with the Servo Brick is 5V. 
 You can use this function to detect the discharge of a battery that is used
 to drive the stepper motor. If you have a fixed power supply, you likely do 
 not need this functionality.
 
 The default value is 5V (5000mV).
 
.. py:function:: Servo.get_minimum_voltage()

 :rtype: int

 Returns the minimum voltage as set by :py:func:`Servo.set_minimum_voltage`
 


.. _servo_brick_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    servo.register_callback(servo.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: Servo.CALLBACK_UNDER_VOLTAGE

 :param voltage: int


 This callback is called when the input voltage drops below the value set by
 :py:func:`Servo.set_minimum_voltage`. The parameter is the current voltage given
 in mV.
 
.. py:attribute:: Servo.CALLBACK_POSITION_REACHED

 :param servo_num: int
 :param position: int


 This callback is called when a position set by :py:func:`Servo.set_position` 
 is reached. The parameters are the servo and the position that is reached.
 
 .. note::
  Since we can't get any feedback from the servo, this only works if the
  velocity (see :py:func:`Servo.set_velocity`) is set smaller or equal to the
  maximum velocity of the servo. Otherwise the servo will lag behind the
  control value and the callback will be called too early.
 
.. py:attribute:: Servo.CALLBACK_VELOCITY_REACHED

 :param servo_num: int
 :param velocity: int


 This callback is called when a velocity set by :py:func:`Servo.set_velocity` 
 is reached. The parameters are the servo and the velocity that is reached.
 
 .. note::
  Since we can't get any feedback from the servo, this only works if the
  acceleration (see :py:func:`Servo.set_acceleration`) is set smaller or equal to the
  maximum acceleration of the servo. Otherwise the servo will lag behind the
  control value and the callback will be called too early.
 


