..
 #############################################################
 # This file was automatically generated on 2011-08-23.      #
 #                                                           #
 # If you have a bugfix for this file and want to commit it, #
 # please fix the bug in the generator. You can find a link  #
 # to the generator git on tinkerforge.com                   #
 #############################################################

C - IMU Brick
=============

.. _imu_brick_c_examples:


TODO: links zur api übersicht, zur hardware seite vom device, zur
installation

Examples
--------

.. _imu_brick_c_api:

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


.. c:function:: void imu_create(IMU *imu, const char *uid)

 Creates a IMU object with the unique device ID *uid*::

    IMU imu;
    imu_create(&imu, "YOUR_DEVICE_UID");

 This object can then be added to the IP connection (see examples 
 :ref:`above <imu_brick_c_examples>`).


.. c:function:: int imu_get_acceleration(IMU *imu, int16_t *ret_x, int16_t *ret_y, int16_t *ret_z)
 
 
.. c:function:: int imu_get_magnetic_field(IMU *imu, int16_t *ret_x, int16_t *ret_y, int16_t *ret_z)

 
.. c:function:: int imu_get_angular_velocity(IMU *imu, int16_t *ret_x, int16_t *ret_y, int16_t *ret_z)

 
.. c:function:: int imu_get_all_data(IMU *imu, int16_t *ret_acc_x, int16_t *ret_acc_y, int16_t *ret_acc_z, int16_t *ret_mag_x, int16_t *ret_mag_y, int16_t *ret_mag_z, int16_t *ret_ang_x, int16_t *ret_ang_y, int16_t *ret_ang_z, int16_t *ret_temperature)

 
.. c:function:: int imu_get_orientation(IMU *imu, int16_t *ret_roll, int16_t *ret_pitch, int16_t *ret_yaw)

 
.. c:function:: int imu_get_quaternion(IMU *imu, float *ret_w, float *ret_x, float *ret_y, float *ret_z)

 
.. c:function:: int imu_get_imu_temperature(IMU *imu, int16_t *ret_temperature)

 
.. c:function:: int imu_leds_on(IMU *imu)

 
.. c:function:: int imu_leds_off(IMU *imu)

 
.. c:function:: int imu_are_leds_on(IMU *imu, bool *ret_leds)

 
.. c:function:: int imu_set_acceleration_range(IMU *imu, uint8_t range)

 
.. c:function:: int imu_get_acceleration_range(IMU *imu, uint8_t *ret_range)

 
.. c:function:: int imu_set_magnetometer_range(IMU *imu, uint8_t range)

 
.. c:function:: int imu_get_magnetometer_range(IMU *imu, uint8_t *ret_range)

 
.. c:function:: int imu_set_zero(IMU *imu)

 
.. c:function:: int imu_set_debounce_period(IMU *imu, uint32_t debounce_period)

 
.. c:function:: int imu_get_debounce_period(IMU *imu, uint32_t *ret_debounce_period)

 
.. c:function:: int imu_set_acceleration_threshold(IMU *imu, uint8_t num, int16_t threshold[3], char option[3])

 
.. c:function:: int imu_get_acceleration_threshold(IMU *imu, uint8_t num, int16_t ret_threshold[3], char ret_option[3])

 
.. c:function:: int imu_set_magnetic_field_threshold(IMU *imu, uint8_t num, int16_t threshold[3], char option[3])

 
.. c:function:: int imu_get_magnetic_field_threshold(IMU *imu, uint8_t num, int16_t ret_threshold[3], char ret_option[3])

 
.. c:function:: int imu_set_angular_velocity_threshold(IMU *imu, uint8_t num, int16_t threshold[3], char option[3])

 
.. c:function:: int imu_get_angular_velocity_threshold(IMU *imu, uint8_t num, int16_t ret_threshold[3], char ret_option[3])

 
.. c:function:: int imu_set_all_data_threshold(IMU *imu, uint8_t num, int16_t threshold[9], char option[9])

 
.. c:function:: int imu_get_all_data_threshold(IMU *imu, uint8_t num, int16_t ret_threshold[9], char ret_option[9])

 
.. c:function:: int imu_set_orientation_threshold(IMU *imu, uint8_t num, int16_t threshold[3], char option[3])

 
.. c:function:: int imu_get_orientation_threshold(IMU *imu, uint8_t num, int16_t ret_threshold[3], char ret_option[3])

 
.. c:function:: int imu_set_acceleration_period(IMU *imu, uint32_t period)

 
.. c:function:: int imu_get_acceleration_period(IMU *imu, uint32_t *ret_period)

 
.. c:function:: int imu_set_magnetic_field_period(IMU *imu, uint32_t period)

 
.. c:function:: int imu_get_magnetic_field_period(IMU *imu, uint32_t *ret_period)

 
.. c:function:: int imu_set_angular_velocity_period(IMU *imu, uint32_t period)

 
.. c:function:: int imu_get_angular_velocity_period(IMU *imu, uint32_t *ret_period)

 
.. c:function:: int imu_set_all_data_period(IMU *imu, uint32_t period)

 
.. c:function:: int imu_get_all_data_period(IMU *imu, uint32_t *ret_period)

 
.. c:function:: int imu_set_orientation_period(IMU *imu, uint32_t period)

 
.. c:function:: int imu_get_orientation_period(IMU *imu, uint32_t *ret_period)

 
.. c:function:: int imu_set_quaternion_period(IMU *imu, uint32_t period)

 
.. c:function:: int imu_get_quaternion_period(IMU *imu, uint32_t *ret_period)

 


Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. c:function:: void imu_register_callback(IMU *imu, uint8_t cb_id, void *func)

 Registers a callback with ID *cb_id* to the function *func*. The available
 IDs with corresponding function signatures are listed 
 :ref:`below <imu_brick_c_callbacks>`.




.. _imu_brick_c_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered with *callback IDs* to receive
time critical or recurring data from the device. The registration is done
with the ``register_callback`` function. The parameters consist of
the device object, the callback id and the callback function::

    void my_callback(int p) {
        printf("parameter: %d\n", p);
    }

    imu_register_callback(&imu, IMU_CALLBACK_EXAMPLE, (void*)my_callback);

The available constants with corresponding callback function signatures 
are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered 
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

.. c:var:: IMU_CALLBACK_ACCELERATION

 .. c:var:: signature: void callback(int16_t x, int16_t y, int16_t z)
    :noindex:


 
.. c:var:: IMU_CALLBACK_MAGNETIC_FIELD

 .. c:var:: signature: void callback(int16_t x, int16_t y, int16_t z)
    :noindex:


 
.. c:var:: IMU_CALLBACK_ANGULAR_VELOCITY

 .. c:var:: signature: void callback(int16_t x, int16_t y, int16_t z)
    :noindex:


 
.. c:var:: IMU_CALLBACK_ALL_DATA

 .. c:var:: signature: void callback(int16_t acc_x, int16_t acc_y, int16_t acc_z, int16_t mag_x, int16_t mag_y, int16_t mag_z, int16_t ang_x, int16_t ang_y, int16_t ang_z, int16_t temperature)
    :noindex:


 
.. c:var:: IMU_CALLBACK_ORIENTATION

 .. c:var:: signature: void callback(int16_t roll, int16_t pitch, int16_t yaw)
    :noindex:


 
.. c:var:: IMU_CALLBACK_QUATERNION

 .. c:var:: signature: void callback(float w, float x, float y, float z)
    :noindex:


 
.. c:var:: IMU_CALLBACK_ACCELERATION_REACHED

 .. c:var:: signature: void callback(int16_t x, int16_t y, int16_t z)
    :noindex:


 
.. c:var:: IMU_CALLBACK_MAGNETIC_FIELD_REACHED

 .. c:var:: signature: void callback(int16_t x, int16_t y, int16_t z)
    :noindex:


 
.. c:var:: IMU_CALLBACK_ANGULAR_VELOCITY_REACHED

 .. c:var:: signature: void callback(int16_t x, int16_t y, int16_t z)
    :noindex:


 
.. c:var:: IMU_CALLBACK_ALL_DATA_REACHED

 .. c:var:: signature: void callback(int16_t acc_x, int16_t acc_y, int16_t acc_z, int16_t mag_x, int16_t mag_y, int16_t mag_z, int16_t ang_x, int16_t ang_y, int16_t ang_z, int16_t temperature)
    :noindex:


 
.. c:var:: IMU_CALLBACK_ORIENTATION_REACHED

 .. c:var:: signature: void callback(int16_t roll, int16_t pitch, int16_t yaw)
    :noindex:


 


