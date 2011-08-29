..
 #############################################################
 # This file was automatically generated on 2011-08-29.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

.. _imu_brick_python:

Python - IMU Brick
==================

.. _imu_brick_python_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

.. _imu_brick_python_api:

API
---


Basic Methods
^^^^^^^^^^^^^


.. py:function:: IMU(uid)

 Creates a imu object with the unique device ID *uid*::

    imu = IMU("YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <imu_brick_python_examples>`).


.. py:function:: IMU.get_acceleration()

 :rtype: (int, int, int)
 
 
.. py:function:: IMU.get_magnetic_field()

 :rtype: (int, int, int)

 
.. py:function:: IMU.get_angular_velocity()

 :rtype: (int, int, int)

 
.. py:function:: IMU.get_all_data()

 :rtype: (int, int, int, int, int, int, int, int, int, int)

 
.. py:function:: IMU.get_orientation()

 :rtype: (int, int, int)

 
.. py:function:: IMU.get_quaternion()

 :rtype: (float, float, float, float)

 
.. py:function:: IMU.get_imu_temperature()

 :rtype: int

 
.. py:function:: IMU.leds_on()

 :rtype: None

 
.. py:function:: IMU.leds_off()

 :rtype: None

 
.. py:function:: IMU.are_leds_on()

 :rtype: bool

 
.. py:function:: IMU.set_acceleration_range(range)

 :param range: int
 :rtype: None

 
.. py:function:: IMU.get_acceleration_range()

 :rtype: int

 
.. py:function:: IMU.set_magnetometer_range(range)

 :param range: int
 :rtype: None

 
.. py:function:: IMU.get_magnetometer_range()

 :rtype: int

 
.. py:function:: IMU.set_zero()

 :rtype: None

 
.. py:function:: IMU.set_debounce_period(debounce_period)

 :param debounce_period: int
 :rtype: None

 
.. py:function:: IMU.get_debounce_period()

 :rtype: int

 
.. py:function:: IMU.set_acceleration_threshold(num, threshold, option)

 :param num: int
 :param threshold: [int, int, int]
 :param option: [chr, chr, chr]
 :rtype: None

 
.. py:function:: IMU.get_acceleration_threshold(num)

 :param num: int
 :rtype: ([int, int, int], [chr, chr, chr])

 
.. py:function:: IMU.set_magnetic_field_threshold(num, threshold, option)

 :param num: int
 :param threshold: [int, int, int]
 :param option: [chr, chr, chr]
 :rtype: None

 
.. py:function:: IMU.get_magnetic_field_threshold(num)

 :param num: int
 :rtype: ([int, int, int], [chr, chr, chr])

 
.. py:function:: IMU.set_angular_velocity_threshold(num, threshold, option)

 :param num: int
 :param threshold: [int, int, int]
 :param option: [chr, chr, chr]
 :rtype: None

 
.. py:function:: IMU.get_angular_velocity_threshold(num)

 :param num: int
 :rtype: ([int, int, int], [chr, chr, chr])

 
.. py:function:: IMU.set_all_data_threshold(num, threshold, option)

 :param num: int
 :param threshold: [int, int, int, int, int, int, int, int, int]
 :param option: [chr, chr, chr, chr, chr, chr, chr, chr, chr]
 :rtype: None

 
.. py:function:: IMU.get_all_data_threshold(num)

 :param num: int
 :rtype: ([int, int, int, int, int, int, int, int, int], [chr, chr, chr, chr, chr, chr, chr, chr, chr])

 
.. py:function:: IMU.set_orientation_threshold(num, threshold, option)

 :param num: int
 :param threshold: [int, int, int]
 :param option: [chr, chr, chr]
 :rtype: None

 
.. py:function:: IMU.get_orientation_threshold(num)

 :param num: int
 :rtype: ([int, int, int], [chr, chr, chr])

 
.. py:function:: IMU.set_acceleration_period(period)

 :param period: int
 :rtype: None

 
.. py:function:: IMU.get_acceleration_period()

 :rtype: int

 
.. py:function:: IMU.set_magnetic_field_period(period)

 :param period: int
 :rtype: None

 
.. py:function:: IMU.get_magnetic_field_period()

 :rtype: int

 
.. py:function:: IMU.set_angular_velocity_period(period)

 :param period: int
 :rtype: None

 
.. py:function:: IMU.get_angular_velocity_period()

 :rtype: int

 
.. py:function:: IMU.set_all_data_period(period)

 :param period: int
 :rtype: None

 
.. py:function:: IMU.get_all_data_period()

 :rtype: int

 
.. py:function:: IMU.set_orientation_period(period)

 :param period: int
 :rtype: None

 
.. py:function:: IMU.get_orientation_period()

 :rtype: int

 
.. py:function:: IMU.set_quaternion_period(period)

 :param period: int
 :rtype: None

 
.. py:function:: IMU.get_quaternion_period()

 :rtype: int

 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. py:function:: IMU.register_callback(cb_id, func)

 :param cb_id: int
 :param func: function
 :rtype: None

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <imu_brick_python_callbacks>`.




.. _imu_brick_python_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function of the device object. The first
parameter is the callback id and the second parameter the callback
function::

    def my_callback(param):
        print(param)

    imu.register_callback(imu.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are 
described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. py:attribute:: IMU.CALLBACK_ACCELERATION

 :param x: int
 :param y: int
 :param z: int


 
.. py:attribute:: IMU.CALLBACK_MAGNETIC_FIELD

 :param x: int
 :param y: int
 :param z: int


 
.. py:attribute:: IMU.CALLBACK_ANGULAR_VELOCITY

 :param x: int
 :param y: int
 :param z: int


 
.. py:attribute:: IMU.CALLBACK_ALL_DATA

 :param acc_x: int
 :param acc_y: int
 :param acc_z: int
 :param mag_x: int
 :param mag_y: int
 :param mag_z: int
 :param ang_x: int
 :param ang_y: int
 :param ang_z: int
 :param temperature: int


 
.. py:attribute:: IMU.CALLBACK_ORIENTATION

 :param roll: int
 :param pitch: int
 :param yaw: int


 
.. py:attribute:: IMU.CALLBACK_QUATERNION

 :param w: float
 :param x: float
 :param y: float
 :param z: float


 
.. py:attribute:: IMU.CALLBACK_ACCELERATION_REACHED

 :param x: int
 :param y: int
 :param z: int


 
.. py:attribute:: IMU.CALLBACK_MAGNETIC_FIELD_REACHED

 :param x: int
 :param y: int
 :param z: int


 
.. py:attribute:: IMU.CALLBACK_ANGULAR_VELOCITY_REACHED

 :param x: int
 :param y: int
 :param z: int


 
.. py:attribute:: IMU.CALLBACK_ALL_DATA_REACHED

 :param acc_x: int
 :param acc_y: int
 :param acc_z: int
 :param mag_x: int
 :param mag_y: int
 :param mag_z: int
 :param ang_x: int
 :param ang_y: int
 :param ang_z: int
 :param temperature: int


 
.. py:attribute:: IMU.CALLBACK_ORIENTATION_REACHED

 :param roll: int
 :param pitch: int
 :param yaw: int


 


