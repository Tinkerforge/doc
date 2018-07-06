
.. _brick_mqtt_proxy:

Brick MQTT Proxy
================

`MQTT <http://mqtt.org/>`__ is a machine-to-machine (M2M) and Internet of Things
(IoT) publish/subscribe message transport protocol. The Brick MQTT Proxy
provides access to Bricks and Bricklets over MQTT. It is written in Python
and translates messages between the :ref:`Tinkerforge TCP/IP Protocol (TFP)
<llproto_tcpip>` and MQTT.

Setup and Usage
---------------

The proxy is provided as Python script and can be downloaded from its 
`Brick MQTT Proxy GitHub Repository <https://github.com/Tinkerforge/brick-mqtt-proxy>`__:

.. code-block:: bash

  wget https://raw.githubusercontent.com/Tinkerforge/brick-mqtt-proxy/master/brick-mqtt-proxy.py

As dependencies the :ref:`Brick Daemon <brickd>`, the :ref:`Python API
Bindings <api_bindings_python>` and the `Eclipse Paho MQTT Python client library
<https://pypi.python.org/pypi/paho-mqtt/1.1>`__ has to be installed.
See the Brick Daemon and Python API Bindings documentation about how to install
them. On Linux the Paho MQTT Python client library can be installed using the
following command:

.. code-block:: bash

  sudo pip install paho-mqtt

Afterwards the proxy can be startet with:

.. code-block:: bash

  python brick-mqtt-proxy.py

Enter the following to get a list of command line arguments for host and port 
configuration for 
:ref:`Brick Daemon <brickd>` and the MQTT broker, data update interval and debug
output:

.. code-block:: bash

  python brick-mqtt-proxy.py --help


Examples
^^^^^^^^

In the following examples we use 
`mosquitto <http://mosquitto.org/documentation/>`__ as broker and client. 
Other broker and clients can be used similarly. To install
the broker and client software under Linux do the following:

.. code-block:: bash

  sudo apt-get install mosquitto mosquitto-clients

Afterwards start the Brick MQTT Proxy and execute the following examples. The
structure is described :ref:`below <brick_mqtt_proxy_topics_and_payload_structure>`.
Keep in mind to change the UID in the path to that of your Bricklet.

.. code-block:: bash

  # enumerate all available devices
  mosquitto_sub -v -t tinkerforge/enumerate/available/#

  # enumerate all available Laser Range Finder Bricklets
  mosquitto_sub -v -t tinkerforge/enumerate/available/bricklet/laser_range_finder

  # enable laser
  mosquitto_pub -t tinkerforge/bricklet/laser_range_finder/vbM/enable_laser/set -m ''

  # get distance
  mosquitto_sub -v -t tinkerforge/bricklet/laser_range_finder/vbM/distance

  # enumerate all available Analog Out 2.0 Bricklets
  mosquitto_sub -v -t tinkerforge/enumerate/available/bricklet/analog_out_v2

  # get input voltage
  mosquitto_sub -v -t tinkerforge/bricklet/analog_out_v2/7xwQ9g/input_voltage

  # get output voltage
  mosquitto_sub -v -t tinkerforge/bricklet/analog_out_v2/7xwQ9g/output_voltage

  # set output voltage to 2.5V
  mosquitto_pub -t tinkerforge/bricklet/analog_out_v2/7xwQ9g/input_voltage -m '{"voltage":2500}'



.. _brick_mqtt_proxy_topics_and_payload_structure:

Topic and Payload Structure
---------------------------

The topics are split into device (currently only ``bricklet/``) and
``enumerate/`` topics.

Devices
^^^^^^^

The proxy publishes retained messages about value and configuration changes
of supported devices on topics with the following pattern:

.. code-block:: none

  tinkerforge/<prefix>/<uid>/<suffix>

For example, for a Temperature Bricklet with UID ``XYZ`` the temperature value
is published on:

.. code-block:: none

  tinkerforge/bricklet/temperature/XYZ/temperature

The value and configuration information is represented in JSON with the
following format:

.. code-block:: json

  {
    "_timestamp": <timestamp>,
    "<key>": <value>
  }

All messages published by the proxy include a UNIX timestamp to indicate the
age of the provided information. The naming and meaning of the key-value pairs
matches the payload definition of our :ref:`TCP/IP protocol <llproto_tcpip>`.
All key-value pairs added by the proxy start with an underscore to avoid name
collisions. For example, for a Temperature Bricklet with UID ``XYZ`` the
temperature value is published as:

.. code-block:: json

  {
    "_timestamp": 1440083842.785104,
    "temperature": 2343
  }

The proxy subscribes to topics ending in ``/set`` allows you to change the
configuration of a device. For example, to change the configuration of an
Ambient Light Bricklet 2.0 with UID ``ABC`` the following JSON payload:

.. code-block:: json

  {
    "illuminance_range": 1,
    "integration_time": 2
  }

Can be published to this topic:

.. code-block:: none

  tinkerforge/bricklet/ambient_light_v2/ABC/configuration/set

The proxy parse the payload and call the configuration setter accordingly.

Again, the naming and meaning of the key-value pairs matches the payload
definition of our TCP/IP protocol. In this case the illuminance range is set to
32000lux and the integration time is set to 150ms.

Enumerate
^^^^^^^^^

There are three major ``enumerate/`` subtopics the proxy will publish enumerate
events on:

* ``tinkerforge/enumerate/available/<device-topic-prefix>``: If the list of
  available devices with a matching topic prefix changes then a retained message
  with the updated list of all now available devices is published.
* ``tinkerforge/enumerate/connected/<device-topic-prefix>``: If a new device
  with a matching topic prefix gets connected then a message with information
  about the connected device is published.
* ``tinkerforge/enumerate/disconnected/<device-topic-prefix>``: If a known
  device with a matching topic prefix gets disconnected then a message with
  information about the disconnected device is published.

For example, if an LCD 20x4 Bricklet gets connected then this is published on:

.. code-block:: none

  tinkerforge/enumerate/connected/bricklet/lcd_20x4

Also, the retained message on ``tinkerforge/enumerate/available/bricklet/lcd_20x4``
is updated. The device information is represented in JSON for all subtopics with
the following format:

.. code-block:: json

  {
    "_timestamp": <timestamp>,
    "uid": "<uid>",
    "connected_uid": "<connected_uid>",
    "position": "<position>",
    "hardware_version": [<major>, <minor>, <release>],
    "firmware_version": [<major>, <minor>, <release>],
    "device_identifier": <device_identifier>
  }

For a Temperature Bricklet it looks like this:

.. code-block:: json

  {
    "_timestamp": 1440143404.176469,
    "uid": "se3",
    "connected_uid": "5VihSm",
    "position": "c",
    "hardware_version": [1, 1, 0],
    "firmware_version": [2, 0, 3],
    "device_identifier": 216
  }


Supported Device Topics
-----------------------

The table below shows all supported devices with their names, suffixes and
links to the corresponding TCP/IP protocol documentation for details about the
payloads.

.. csv-table::
 :header: Device, Prefix, Suffix
 :delim: |
 :widths: 30, 30, 40

 :ref:`DC Brick <dc_brick>`                                                     | brick/dc                             | :tcpip:func:`velocity <BrickDC.get_velocity>`
                                                                                |                                      | :tcpip:func:`current_velocity <BrickDC.get_current_velocity>`
                                                                                |                                      | :tcpip:func:`acceleration <BrickDC.get_acceleration>`
                                                                                |                                      | :tcpip:func:`enabled <BrickDC.is_enabled>`
                                                                                |                                      | :tcpip:func:`pwm_frequency <BrickDC.get_pwm_frequency>`
                                                                                |                                      | :tcpip:func:`stack_input_voltage <BrickDC.get_stack_input_voltage>`
                                                                                |                                      | :tcpip:func:`external_input_voltage <BrickDC.get_external_input_voltage>`
                                                                                |                                      | :tcpip:func:`current_consumption <BrickDC.get_current_consumption>`
                                                                                |                                      | :tcpip:func:`drive_mode <BrickDC.get_drive_mode>`
                                                                                |                                      | :tcpip:func:`status_led_enabled <BrickDC.is_status_led_enabled>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickDC.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`velocity/set <BrickDC.set_velocity>`
                                                                                |                                      | :tcpip:func:`acceleration/set <BrickDC.set_acceleration>`
                                                                                |                                      | :tcpip:func:`full_brake/set <BrickDC.full_brake>`
                                                                                |                                      | :tcpip:func:`enable/set <BrickDC.enable>`
                                                                                |                                      | :tcpip:func:`disable/set <BrickDC.disable>`
                                                                                |                                      | :tcpip:func:`pwm_frequency/set <BrickDC.set_pwm_frequency>`
                                                                                |                                      | :tcpip:func:`drive_mode/set <BrickDC.set_drive_mode>`
                                                                                |                                      | :tcpip:func:`enable_status_led/set <BrickDC.enable_status_led>`
                                                                                |                                      | :tcpip:func:`disable_status_led/set <BrickDC.disable_status_led>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickDC.reset>`

 :ref:`IMU Brick <imu_brick>`                                                   | brick/imu                            | :tcpip:func:`orientation <BrickIMU.get_orientation>`
                                                                                |                                      | :tcpip:func:`quaternion <BrickIMU.get_quaternion>`
                                                                                |                                      | :tcpip:func:`leds_on <BrickIMU.are_leds_on>`
                                                                                |                                      | :tcpip:func:`convergence_speed <BrickIMU.get_convergence_speed>`
                                                                                |                                      | :tcpip:func:`acceleration <BrickIMU.get_acceleration>`
                                                                                |                                      | :tcpip:func:`magnetic_field <BrickIMU.get_magnetic_field>`
                                                                                |                                      | :tcpip:func:`angular_velocity <BrickIMU.get_angular_velocity>`
                                                                                |                                      | :tcpip:func:`all_data <BrickIMU.get_all_data>`
                                                                                |                                      | :tcpip:func:`imu_temperature <BrickIMU.get_imu_temperature>`
                                                                                |                                      | :tcpip:func:`acceleration_range <BrickIMU.get_acceleration_range>`
                                                                                |                                      | :tcpip:func:`magnetometer_range <BrickIMU.get_magnetometer_range>`
                                                                                |                                      | :tcpip:func:`get_calibration/set <BrickIMU.get_calibration>`
                                                                                |                                      | :tcpip:func:`orientation_calculation_on <BrickIMU.is_orientation_calculation_on>`
                                                                                |                                      | :tcpip:func:`status_led_enabled <BrickIMU.is_status_led_enabled>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickIMU.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`leds_on/set <BrickIMU.leds_on>`
                                                                                |                                      | :tcpip:func:`leds_off/set <BrickIMU.leds_off>`
                                                                                |                                      | :tcpip:func:`convergence_speed/set <BrickIMU.set_convergence_speed>`
                                                                                |                                      | :tcpip:func:`acceleration_range/set <BrickIMU.set_acceleration_range>`
                                                                                |                                      | :tcpip:func:`magnetometer_range/set <BrickIMU.set_magnetometer_range>`
                                                                                |                                      | :tcpip:func:`calibration/set <BrickIMU.set_calibration>`
                                                                                |                                      | :tcpip:func:`orientation_calculation_on/set <BrickIMU.orientation_calculation_on>`
                                                                                |                                      | :tcpip:func:`orientation_calculation_off/set <BrickIMU.orientation_calculation_off>`
                                                                                |                                      | :tcpip:func:`enable_status_led/set <BrickIMU.enable_status_led>`
                                                                                |                                      | :tcpip:func:`disable_status_led/set <BrickIMU.disable_status_led>`

 :ref:`IMUV2 Brick <imu_v2_brick>`                                              | brick/imu_v2                         | :tcpip:func:`orientation <BrickIMUV2.get_orientation>`
                                                                                |                                      | :tcpip:func:`linear_acceleration <BrickIMUV2.get_linear_acceleration>`
                                                                                |                                      | :tcpip:func:`gravity_vector <BrickIMUV2.get_gravity_vector>`
                                                                                |                                      | :tcpip:func:`quaternion <BrickIMUV2.get_quaternion>`
                                                                                |                                      | :tcpip:func:`all_data <BrickIMUV2.get_all_data>`
                                                                                |                                      | :tcpip:func:`leds_on <BrickIMUV2.are_leds_on>`
                                                                                |                                      | :tcpip:func:`acceleration <BrickIMUV2.get_acceleration>`
                                                                                |                                      | :tcpip:func:`magnetic_field <BrickIMUV2.get_magnetic_field>`
                                                                                |                                      | :tcpip:func:`angular_velocity <BrickIMUV2.get_angular_velocity>`
                                                                                |                                      | :tcpip:func:`temperature <BrickIMUV2.get_temperature>`
                                                                                |                                      | :tcpip:func:`sensor_configuration <BrickIMUV2.get_sensor_configuration>`
                                                                                |                                      | :tcpip:func:`sensor_fusion_mode <BrickIMUV2.get_sensor_fusion_mode>`
                                                                                |                                      | :tcpip:func:`status_led_enabled <BrickIMUV2.is_status_led_enabled>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickIMUV2.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`leds_on/set <BrickIMUV2.leds_on>`
                                                                                |                                      | :tcpip:func:`leds_off/set <BrickIMUV2.leds_off>`
                                                                                |                                      | :tcpip:func:`sensor_configuration/set <BrickIMUV2.set_sensor_configuration>`
                                                                                |                                      | :tcpip:func:`sensor_fusion_mode/set <BrickIMUV2.set_sensor_fusion_mode>`
                                                                                |                                      | :tcpip:func:`enable_status_led/set <BrickIMUV2.enable_status_led>`
                                                                                |                                      | :tcpip:func:`disable_status_led/set <BrickIMUV2.disable_status_led>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickIMUV2.reset>`

 :ref:`Master Brick <master_brick>`                                             | brick/master                         | :tcpip:func:`stack_voltage <BrickMaster.get_stack_voltage>`
                                                                                |                                      | :tcpip:func:`stack_current <BrickMaster.get_stack_current>`
                                                                                |                                      | :tcpip:func:`usb_voltage <BrickMaster.get_usb_voltage>`
                                                                                |                                      | :tcpip:func:`connection_type <BrickMaster.get_connection_type>`
                                                                                |                                      | :tcpip:func:`status_led_enabled <BrickMaster.is_status_led_enabled>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickMaster.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`enable_status_led/set <BrickMaster.enable_status_led>`
                                                                                |                                      | :tcpip:func:`disable_status_led/set <BrickMaster.disable_status_led>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickMaster.reset>`

 :ref:`Servo Brick <servo_brick>`                                               | brick/servo                          | :tcpip:func:`enabled <BrickServo.is_enabled>`
                                                                                |                                      | :tcpip:func:`position <BrickServo.get_position>`
                                                                                |                                      | :tcpip:func:`current_position <BrickServo.get_current_position>`
                                                                                |                                      | :tcpip:func:`velocity <BrickServo.get_velocity>`
                                                                                |                                      | :tcpip:func:`current_velocity <BrickServo.get_current_velocity>`
                                                                                |                                      | :tcpip:func:`acceleration <BrickServo.get_acceleration>`
                                                                                |                                      | :tcpip:func:`output_voltage <BrickServo.get_output_voltage>`
                                                                                |                                      | :tcpip:func:`pulse_width <BrickServo.get_pulse_width>`
                                                                                |                                      | :tcpip:func:`degree <BrickServo.get_degree>`
                                                                                |                                      | :tcpip:func:`period <BrickServo.get_period>`
                                                                                |                                      | :tcpip:func:`servo_current <BrickServo.get_servo_current>`
                                                                                |                                      | :tcpip:func:`overall_current <BrickServo.get_overall_current>`
                                                                                |                                      | :tcpip:func:`stack_input_voltage <BrickServo.get_stack_input_voltage>`
                                                                                |                                      | :tcpip:func:`external_input_voltage <BrickServo.get_external_input_voltage>`
                                                                                |                                      | :tcpip:func:`status_led_enabled <BrickServo.is_status_led_enabled>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickServo.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`enable/set <BrickServo.enable>`
                                                                                |                                      | :tcpip:func:`disable/set <BrickServo.disable>`
                                                                                |                                      | :tcpip:func:`position/set <BrickServo.set_position>`
                                                                                |                                      | :tcpip:func:`velocity/set <BrickServo.set_velocity>`
                                                                                |                                      | :tcpip:func:`acceleration/set <BrickServo.set_acceleration>`
                                                                                |                                      | :tcpip:func:`output_voltage/set <BrickServo.set_output_voltage>`
                                                                                |                                      | :tcpip:func:`pulse_width/set <BrickServo.set_pulse_width>`
                                                                                |                                      | :tcpip:func:`degree/set <BrickServo.set_degree>`
                                                                                |                                      | :tcpip:func:`period/set <BrickServo.set_period>`
                                                                                |                                      | :tcpip:func:`enable_status_led/set <BrickServo.enable_status_led>`
                                                                                |                                      | :tcpip:func:`disable_status_led/set <BrickServo.disable_status_led>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickServo.reset>`

 :ref:`Silent Stepper Brick <silent_stepper_brick>`                             | brick/silent_stepper                 | :tcpip:func:`max_velocity <BrickSilentStepper.get_max_velocity>`
                                                                                |                                      | :tcpip:func:`current_velocity <BrickSilentStepper.get_current_velocity>`
                                                                                |                                      | :tcpip:func:`speed_ramping <BrickSilentStepper.get_speed_ramping>`
                                                                                |                                      | :tcpip:func:`steps <BrickSilentStepper.get_steps>`
                                                                                |                                      | :tcpip:func:`remaining_steps <BrickSilentStepper.get_remaining_steps>`
                                                                                |                                      | :tcpip:func:`motor_current <BrickSilentStepper.get_motor_current>`
                                                                                |                                      | :tcpip:func:`enabled <BrickSilentStepper.is_enabled>`
                                                                                |                                      | :tcpip:func:`basic_configuration <BrickSilentStepper.get_basic_configuration>`
                                                                                |                                      | :tcpip:func:`current_position <BrickSilentStepper.get_current_position>`
                                                                                |                                      | :tcpip:func:`target_position <BrickSilentStepper.get_target_position>`
                                                                                |                                      | :tcpip:func:`step_configuration <BrickSilentStepper.get_step_configuration>`
                                                                                |                                      | :tcpip:func:`stack_input_voltage <BrickSilentStepper.get_stack_input_voltage>`
                                                                                |                                      | :tcpip:func:`external_input_voltage <BrickSilentStepper.get_external_input_voltage>`
                                                                                |                                      | :tcpip:func:`spreadcycle_configuration <BrickSilentStepper.get_spreadcycle_configuration>`
                                                                                |                                      | :tcpip:func:`stealth_configuration <BrickSilentStepper.get_stealth_configuration>`
                                                                                |                                      | :tcpip:func:`coolstep_configuration <BrickSilentStepper.get_coolstep_configuration>`
                                                                                |                                      | :tcpip:func:`misc_configuration <BrickSilentStepper.get_misc_configuration>`
                                                                                |                                      | :tcpip:func:`driver_status <BrickSilentStepper.get_driver_status>`
                                                                                |                                      | :tcpip:func:`time_base <BrickSilentStepper.get_time_base>`
                                                                                |                                      | :tcpip:func:`all_data <BrickSilentStepper.get_all_data>`
                                                                                |                                      | :tcpip:func:`status_led_enabled <BrickSilentStepper.is_status_led_enabled>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickSilentStepper.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`max_velocity/set <BrickSilentStepper.set_max_velocity>`
                                                                                |                                      | :tcpip:func:`speed_ramping/set <BrickSilentStepper.set_speed_ramping>`
                                                                                |                                      | :tcpip:func:`full_brake/set <BrickSilentStepper.full_brake>`
                                                                                |                                      | :tcpip:func:`steps/set <BrickSilentStepper.set_steps>`
                                                                                |                                      | :tcpip:func:`drive_forward/set <BrickSilentStepper.drive_forward>`
                                                                                |                                      | :tcpip:func:`drive_backward/set <BrickSilentStepper.drive_backward>`
                                                                                |                                      | :tcpip:func:`stop/set <BrickSilentStepper.stop>`
                                                                                |                                      | :tcpip:func:`motor_current/set <BrickSilentStepper.set_motor_current>`
                                                                                |                                      | :tcpip:func:`enable/set <BrickSilentStepper.enable>`
                                                                                |                                      | :tcpip:func:`disable/set <BrickSilentStepper.disable>`
                                                                                |                                      | :tcpip:func:`basic_configuration/set <BrickSilentStepper.set_basic_configuration>`
                                                                                |                                      | :tcpip:func:`current_position/set <BrickSilentStepper.set_current_position>`
                                                                                |                                      | :tcpip:func:`target_position/set <BrickSilentStepper.set_target_position>`
                                                                                |                                      | :tcpip:func:`step_configuration/set <BrickSilentStepper.set_step_configuration>`
                                                                                |                                      | :tcpip:func:`spreadcycle_configuration/set <BrickSilentStepper.set_spreadcycle_configuration>`
                                                                                |                                      | :tcpip:func:`stealth_configuration/set <BrickSilentStepper.set_stealth_configuration>`
                                                                                |                                      | :tcpip:func:`coolstep_configuration/set <BrickSilentStepper.set_coolstep_configuration>`
                                                                                |                                      | :tcpip:func:`misc_configuration/set <BrickSilentStepper.set_misc_configuration>`
                                                                                |                                      | :tcpip:func:`time_base/set <BrickSilentStepper.set_time_base>`
                                                                                |                                      | :tcpip:func:`enable_status_led/set <BrickSilentStepper.enable_status_led>`
                                                                                |                                      | :tcpip:func:`disable_status_led/set <BrickSilentStepper.disable_status_led>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickSilentStepper.reset>`

 :ref:`Stepper Brick <stepper_brick>`                                           | brick/stepper                        | :tcpip:func:`max_velocity <BrickStepper.get_max_velocity>`
                                                                                |                                      | :tcpip:func:`current_velocity <BrickStepper.get_current_velocity>`
                                                                                |                                      | :tcpip:func:`speed_ramping <BrickStepper.get_speed_ramping>`
                                                                                |                                      | :tcpip:func:`steps <BrickStepper.get_steps>`
                                                                                |                                      | :tcpip:func:`remaining_steps <BrickStepper.get_remaining_steps>`
                                                                                |                                      | :tcpip:func:`motor_current <BrickStepper.get_motor_current>`
                                                                                |                                      | :tcpip:func:`enabled <BrickStepper.is_enabled>`
                                                                                |                                      | :tcpip:func:`current_position <BrickStepper.get_current_position>`
                                                                                |                                      | :tcpip:func:`target_position <BrickStepper.get_target_position>`
                                                                                |                                      | :tcpip:func:`step_mode <BrickStepper.get_step_mode>`
                                                                                |                                      | :tcpip:func:`stack_input_voltage <BrickStepper.get_stack_input_voltage>`
                                                                                |                                      | :tcpip:func:`external_input_voltage <BrickStepper.get_external_input_voltage>`
                                                                                |                                      | :tcpip:func:`current_consumption <BrickStepper.get_current_consumption>`
                                                                                |                                      | :tcpip:func:`decay <BrickStepper.get_decay>`
                                                                                |                                      | :tcpip:func:`sync_rect <BrickStepper.is_sync_rect>`
                                                                                |                                      | :tcpip:func:`time_base <BrickStepper.get_time_base>`
                                                                                |                                      | :tcpip:func:`all_data <BrickStepper.get_all_data>`
                                                                                |                                      | :tcpip:func:`status_led_enabled <BrickStepper.is_status_led_enabled>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickStepper.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`max_velocity/set <BrickStepper.set_max_velocity>`
                                                                                |                                      | :tcpip:func:`speed_ramping/set <BrickStepper.set_speed_ramping>`
                                                                                |                                      | :tcpip:func:`full_brake/set <BrickStepper.full_brake>`
                                                                                |                                      | :tcpip:func:`steps/set <BrickStepper.set_steps>`
                                                                                |                                      | :tcpip:func:`drive_forward/set <BrickStepper.drive_forward>`
                                                                                |                                      | :tcpip:func:`drive_backward/set <BrickStepper.drive_backward>`
                                                                                |                                      | :tcpip:func:`stop/set <BrickStepper.stop>`
                                                                                |                                      | :tcpip:func:`motor_current/set <BrickStepper.set_motor_current>`
                                                                                |                                      | :tcpip:func:`enable/set <BrickStepper.enable>`
                                                                                |                                      | :tcpip:func:`disable/set <BrickStepper.disable>`
                                                                                |                                      | :tcpip:func:`current_position/set <BrickStepper.set_current_position>`
                                                                                |                                      | :tcpip:func:`target_position/set <BrickStepper.set_target_position>`
                                                                                |                                      | :tcpip:func:`step_mode/set <BrickStepper.set_step_mode>`
                                                                                |                                      | :tcpip:func:`decay/set <BrickStepper.set_decay>`
                                                                                |                                      | :tcpip:func:`sync_rect/set <BrickStepper.set_sync_rect>`
                                                                                |                                      | :tcpip:func:`time_base/set <BrickStepper.set_time_base>`
                                                                                |                                      | :tcpip:func:`enable_status_led/set <BrickStepper.enable_status_led>`
                                                                                |                                      | :tcpip:func:`disable_status_led/set <BrickStepper.disable_status_led>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickStepper.reset>`

 :ref:`Accelerometer Bricklet <accelerometer_bricklet>`                         | bricklet/accelerometer               | :tcpip:func:`acceleration <BrickletAccelerometer.get_acceleration>`
                                                                                |                                      | :tcpip:func:`temperature <BrickletAccelerometer.get_temperature>`
                                                                                |                                      | :tcpip:func:`led_on <BrickletAccelerometer.is_led_on>`
                                                                                |                                      | :tcpip:func:`led_on/set <BrickletAccelerometer.led_on>`
                                                                                |                                      | :tcpip:func:`led_off/set <BrickletAccelerometer.led_off>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletAccelerometer.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletAccelerometer.set_configuration>`

 :ref:`Ambient Light Bricklet <ambient_light_bricklet>`                         | bricklet/ambient_light               | :tcpip:func:`illuminance <BrickletAmbientLight.get_illuminance>`

 :ref:`Ambient Light Bricklet 2.0 <ambient_light_v2_bricklet>`                  | bricklet/ambient_light_v2            | :tcpip:func:`illuminance <BrickletAmbientLightV2.get_illuminance>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletAmbientLightV2.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletAmbientLightV2.set_configuration>`

 :ref:`Analog In Bricklet <analog_in_bricklet>`                                 | bricklet/analog_in                   | :tcpip:func:`voltage <BrickletAnalogIn.get_voltage>`
                                                                                |                                      | :tcpip:func:`averaging <BrickletAnalogIn.get_averaging>`
                                                                                |                                      | :tcpip:func:`averaging/set <BrickletAnalogIn.set_averaging>`
                                                                                |                                      | :tcpip:func:`range <BrickletAnalogIn.get_range>`
                                                                                |                                      | :tcpip:func:`range/set <BrickletAnalogIn.set_range>`

 :ref:`Analog In Bricklet 2.0 <analog_in_v2_bricklet>`                          | bricklet/analog_in_v2                | :tcpip:func:`voltage <BrickletAnalogInV2.get_voltage>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletAnalogInV2.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletAnalogInV2.set_moving_average>`

 :ref:`Analog In Bricklet 3.0 <analog_in_v3_bricklet>`                          | bricklet/analog_in_v3                | :tcpip:func:`voltage <BrickletAnalogInV3.get_voltage>`

 :ref:`Analog Out Bricklet <analog_out_bricklet>`                               | bricklet/analog_out                  | :tcpip:func:`voltage <BrickletAnalogOut.get_voltage>`
                                                                                |                                      | :tcpip:func:`voltage/set <BrickletAnalogOut.set_voltage>`
                                                                                |                                      | :tcpip:func:`mode <BrickletAnalogOut.get_mode>`
                                                                                |                                      | :tcpip:func:`mode/set <BrickletAnalogOut.set_mode>`

 :ref:`Analog Out Bricklet 2.0 <analog_out_v2_bricklet>`                        | bricklet/analog_out_v2               | :tcpip:func:`output_voltage <BrickletAnalogOutV2.get_output_voltage>`
                                                                                |                                      | :tcpip:func:`output_voltage/set <BrickletAnalogOutV2.set_output_voltage>`
                                                                                |                                      | :tcpip:func:`input_voltage <BrickletAnalogOutV2.get_input_voltage>`

 :ref:`Barometer Bricklet <barometer_bricklet>`                                 | bricklet/barometer                   | :tcpip:func:`air_pressure <BrickletBarometer.get_air_pressure>`
                                                                                |                                      | :tcpip:func:`altitude <BrickletBarometer.get_altitude>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletBarometer.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`reference_air_pressure <BrickletBarometer.get_reference_air_pressure>`
                                                                                |                                      | :tcpip:func:`reference_air_pressure/set <BrickletBarometer.set_reference_air_pressure>`
                                                                                |                                      | :tcpip:func:`averaging <BrickletBarometer.get_averaging>`
                                                                                |                                      | :tcpip:func:`averaging/set <BrickletBarometer.set_averaging>`

 :ref:`CAN Bricklet <can_bricklet>`                                             | bricklet/can                         | :tcpip:func:`read_frame <BrickletCAN.read_frame>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletCAN.get_configuration>`
                                                                                |                                      | :tcpip:func:`read_filter <BrickletCAN.get_read_filter>`
                                                                                |                                      | :tcpip:func:`error_log <BrickletCAN.get_error_log>`
                                                                                |                                      | :tcpip:func:`write_frame/set <BrickletCAN.write_frame>` (calls :tcpip:func:`write_frame <BrickletCAN.write_frame>` with the parameters provided by the *write_frame/set* topic and the output of the getter being published to the *write_frame* topic)
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletCAN.set_configuration>`
                                                                                |                                      | :tcpip:func:`read_filter/set <BrickletCAN.set_read_filter>`

 :ref:`CO2 Bricklet <co2_bricklet>`                                             | bricklet/co2                         | :tcpip:func:`co2_concentration <BrickletCO2.get_co2_concentration>`

 :ref:`Current12 Bricklet <current12_bricklet>`                                 | bricklet/current12                   | :tcpip:func:`current <BrickletCurrent12.get_current>`
                                                                                |                                      | :tcpip:func:`over_current <BrickletCurrent12.is_over_current>`
                                                                                |                                      | :tcpip:func:`calibrate/set <BrickletCurrent12.calibrate>`

 :ref:`Current25 Bricklet <current25_bricklet>`                                 | bricklet/current25                   | :tcpip:func:`current <BrickletCurrent25.get_current>`
                                                                                |                                      | :tcpip:func:`over_current <BrickletCurrent25.is_over_current>`
                                                                                |                                      | :tcpip:func:`calibrate/set <BrickletCurrent25.calibrate>`

 :ref:`Distance IR Bricklet <distance_ir_bricklet>`                             | bricklet/distance_ir                 | :tcpip:func:`distance <BrickletDistanceIR.get_distance>`

 :ref:`Distance US Bricklet <distance_us_bricklet>`                             | bricklet/distance_us                 | :tcpip:func:`distance_value <BrickletDistanceUS.get_distance_value>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletDistanceUS.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletDistanceUS.set_moving_average>`

 :ref:`DMX Bricklet <dmx_bricklet>`                                             | bricklet/dmx                         | :tcpip:func:`dmx_mode <BrickletDMX.get_dmx_mode>`
                                                                                |                                      | :tcpip:func:`read_frame <BrickletDMX.read_frame>`
                                                                                |                                      | :tcpip:func:`frame_duration <BrickletDMX.get_frame_duration>`
                                                                                |                                      | :tcpip:func:`frame_error_count <BrickletDMX.get_frame_error_count>`
                                                                                |                                      | :tcpip:func:`communication_led_config <BrickletDMX.get_communication_led_config>`
                                                                                |                                      | :tcpip:func:`error_led_config <BrickletDMX.get_error_led_config>`
                                                                                |                                      | :tcpip:func:`status_led_config <BrickletDMX.get_status_led_config>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletDMX.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`dmx_mode/set <BrickletDMX.set_dmx_mode>`
                                                                                |                                      | :tcpip:func:`write_frame/set <BrickletDMX.write_frame>`
                                                                                |                                      | :tcpip:func:`frame_duration/set <BrickletDMX.set_frame_duration>`
                                                                                |                                      | :tcpip:func:`communication_led_config/set <BrickletDMX.set_communication_led_config>`
                                                                                |                                      | :tcpip:func:`error_led_config/set <BrickletDMX.set_error_led_config>`
                                                                                |                                      | :tcpip:func:`status_led_config/set <BrickletDMX.set_status_led_config>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickletDMX.reset>`

 :ref:`Dual Button Bricklet <dual_button_bricklet>`                             | bricklet/dual_button                 | :tcpip:func:`button_state <BrickletDualButton.get_button_state>`
                                                                                |                                      | :tcpip:func:`led_state <BrickletDualButton.get_led_state>`
                                                                                |                                      | :tcpip:func:`led_state/set <BrickletDualButton.set_led_state>`
                                                                                |                                      | :tcpip:func:`selected_led_state/set <BrickletDualButton.set_selected_led_state>`

 :ref:`Dual Relay Bricklet <dual_relay_bricklet>`                               | bricklet/dual_relay                  | :tcpip:func:`state <BrickletDualRelay.get_state>`
                                                                                |                                      | :tcpip:func:`state/set <BrickletDualRelay.set_state>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletDualRelay.set_monoflop>`
                                                                                |                                      | :tcpip:func:`selected_state/set <BrickletDualRelay.set_selected_state>`

 :ref:`Dust Detector Bricklet <dust_detector_bricklet>`                         | bricklet/dust_detector               | :tcpip:func:`dust_density <BrickletDustDetector.get_dust_density>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletDustDetector.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletDustDetector.set_moving_average>`

 :ref:`GPS Bricklet <gps_bricklet>`                                             | bricklet/gps                         | :tcpip:func:`status <BrickletGPS.get_status>`
                                                                                |                                      | :tcpip:func:`coordinates <BrickletGPS.get_coordinates>`
                                                                                |                                      | :tcpip:func:`altitude <BrickletGPS.get_altitude>`
                                                                                |                                      | :tcpip:func:`motion <BrickletGPS.get_motion>`
                                                                                |                                      | :tcpip:func:`date_time <BrickletGPS.get_date_time>`
                                                                                |                                      | :tcpip:func:`restart/set <BrickletGPS.restart>`

 :ref:`GPS Bricklet 2.0 <gps_v2_bricklet>`                                      | bricklet/gps_v2                      | :tcpip:func:`coordinates <BrickletGPSV2.get_coordinates>`
                                                                                |                                      | :tcpip:func:`status <BrickletGPSV2.get_status>`
                                                                                |                                      | :tcpip:func:`altitude <BrickletGPSV2.get_altitude>`
                                                                                |                                      | :tcpip:func:`motion <BrickletGPSV2.get_motion>`
                                                                                |                                      | :tcpip:func:`date_time <BrickletGPSV2.get_date_time>`
                                                                                |                                      | :tcpip:func:`satellite_system_status <BrickletGPSV2.get_satellite_system_status>`
                                                                                |                                      | :tcpip:func:`satellite_status <BrickletGPSV2.get_satellite_status>`
                                                                                |                                      | :tcpip:func:`fix_led_config <BrickletGPSV2.get_fix_led_config>`
                                                                                |                                      | :tcpip:func:`sbas_config <BrickletGPSV2.get_sbas_config>`
                                                                                |                                      | :tcpip:func:`status_led_config <BrickletGPSV2.get_status_led_config>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletGPSV2.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`restart/set <BrickletGPSV2.restart>`
                                                                                |                                      | :tcpip:func:`fix_led_config/set <BrickletGPSV2.set_fix_led_config>`
                                                                                |                                      | :tcpip:func:`sbas_config/set <BrickletGPSV2.set_sbas_config>`
                                                                                |                                      | :tcpip:func:`status_led_config/set <BrickletGPSV2.set_status_led_config>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickletGPSV2.reset>`

 :ref:`Hall Effect Bricklet <hall_effect_bricklet>`                             | bricklet/hall_effect                 | :tcpip:func:`value <BrickletHallEffect.get_value>`
                                                                                |                                      | :tcpip:func:`edge_count_config <BrickletHallEffect.get_edge_count_config>`
                                                                                |                                      | :tcpip:func:`edge_count_config/set <BrickletHallEffect.set_edge_count_config>`

 :ref:`Humidity Bricklet <humidity_bricklet>`                                   | bricklet/humidity                    | :tcpip:func:`humidity <BrickletHumidity.get_humidity>`

 :ref:`Humidity Bricklet 2.0 <humidity_v2_bricklet>`                            | bricklet/humidity_v2                 | :tcpip:func:`humidity <BrickletHumidityV2.get_humidity>`
                                                                                |                                      | :tcpip:func:`temperature <BrickletHumidityV2.get_temperature>`
                                                                                |                                      | :tcpip:func:`heater_config <BrickletHumidityV2.get_heater_configuration>`
                                                                                |                                      | :tcpip:func:`moving_average_configuration <BrickletHumidityV2.get_moving_average_configuration>`
                                                                                |                                      | :tcpip:func:`status_led_config <BrickletHumidityV2.get_status_led_config>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletHumidityV2.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`heater_configuration/set <BrickletHumidityV2.set_heater_configuration>`
                                                                                |                                      | :tcpip:func:`moving_average_configuration/set <BrickletHumidityV2.set_moving_average_configuration>`
                                                                                |                                      | :tcpip:func:`status_led_config/set <BrickletHumidityV2.set_status_led_config>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickletHumidityV2.reset>`

 :ref:`Industrial Analog Out Bricklet <industrial_analog_out_bricklet>`         | bricklet/industrial_analog_out       | :tcpip:func:`voltage <BrickletIndustrialAnalogOut.get_voltage>`
                                                                                |                                      | :tcpip:func:`voltage/set <BrickletIndustrialAnalogOut.set_voltage>`
                                                                                |                                      | :tcpip:func:`current <BrickletIndustrialAnalogOut.get_current>`
                                                                                |                                      | :tcpip:func:`current/set <BrickletIndustrialAnalogOut.set_current>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletIndustrialAnalogOut.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletIndustrialAnalogOut.set_configuration>`
                                                                                |                                      | :tcpip:func:`enabled <BrickletIndustrialAnalogOut.is_enabled>`
                                                                                |                                      | :tcpip:func:`enable/set <BrickletIndustrialAnalogOut.enable>`
                                                                                |                                      | :tcpip:func:`disable/set <BrickletIndustrialAnalogOut.disable>`

 :ref:`Industrial Digital In 4 Bricklet <industrial_digital_in_4_bricklet>`     | bricklet/industrial_digital_in_4     | :tcpip:func:`value <BrickletIndustrialDigitalIn4.get_value>`
                                                                                |                                      | :tcpip:func:`edge_count_config/set <BrickletIndustrialDigitalIn4.set_edge_count_config>`
                                                                                |                                      | :tcpip:func:`available_for_group <BrickletIndustrialDigitalIn4.get_available_for_group>`
                                                                                |                                      | :tcpip:func:`group <BrickletIndustrialDigitalIn4.get_group>`
                                                                                |                                      | :tcpip:func:`group/set <BrickletIndustrialDigitalIn4.set_group>`

 :ref:`Industrial Digital Out 4 Bricklet <industrial_digital_in_4_bricklet>`    | bricklet/industrial_digital_out_4    | :tcpip:func:`value <BrickletIndustrialDigitalOut4.get_value>`
                                                                                |                                      | :tcpip:func:`value/set <BrickletIndustrialDigitalOut4.set_value>`
                                                                                |                                      | :tcpip:func:`selected_values/set <BrickletIndustrialDigitalOut4.set_selected_values>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletIndustrialDigitalOut4.set_monoflop>`
                                                                                |                                      | :tcpip:func:`available_for_group <BrickletIndustrialDigitalOut4.get_available_for_group>`
                                                                                |                                      | :tcpip:func:`group <BrickletIndustrialDigitalOut4.get_group>`
                                                                                |                                      | :tcpip:func:`group/set <BrickletIndustrialDigitalOut4.set_group>`

 :ref:`Industrial Dual 0-20mA Bricklet <industrial_dual_0_20ma_bricklet>`       | bricklet/industrial_dual_0_20ma      | :tcpip:func:`sample_rate <BrickletIndustrialDual020mA.get_sample_rate>`
                                                                                |                                      | :tcpip:func:`sample_rate/set <BrickletIndustrialDual020mA.set_sample_rate>`

 :ref:`Industrial Dual Analog In Bricklet <industrial_dual_analog_in_bricklet>` | bricklet/industrial_dual_analog_in   | :tcpip:func:`sample_rate <BrickletIndustrialDualAnalogIn.get_sample_rate>`
                                                                                |                                      | :tcpip:func:`sample_rate/set <BrickletIndustrialDualAnalogIn.set_sample_rate>`
                                                                                |                                      | :tcpip:func:`calibration <BrickletIndustrialDualAnalogIn.get_calibration>`
                                                                                |                                      | :tcpip:func:`calibration/set <BrickletIndustrialDualAnalogIn.set_calibration>`
                                                                                |                                      | :tcpip:func:`adc_values <BrickletIndustrialDualAnalogIn.get_adc_values>`

 :ref:`Industrial Quad Relay Bricklet <industrial_quad_relay_bricklet>`         | bricklet/industrial_quad_relay       | :tcpip:func:`value <BrickletIndustrialQuadRelay.get_value>`
                                                                                |                                      | :tcpip:func:`value/set <BrickletIndustrialQuadRelay.set_value>`
                                                                                |                                      | :tcpip:func:`selected_values/set <BrickletIndustrialQuadRelay.set_selected_values>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletIndustrialQuadRelay.set_monoflop>`
                                                                                |                                      | :tcpip:func:`available_for_group <BrickletIndustrialQuadRelay.get_available_for_group>`
                                                                                |                                      | :tcpip:func:`group <BrickletIndustrialQuadRelay.get_group>`
                                                                                |                                      | :tcpip:func:`group/set <BrickletIndustrialQuadRelay.set_group>`

 :ref:`IO-16 Bricklet <io16_bricklet>`                                          | bricklet/io16                        | :tcpip:func:`port <BrickletIO16.get_port>`
                                                                                |                                      | :tcpip:func:`port/set <BrickletIO16.set_port>`
                                                                                |                                      | :tcpip:func:`port_configuration <BrickletIO16.get_port_configuration>`
                                                                                |                                      | :tcpip:func:`port_configuration/set <BrickletIO16.set_port_configuration>`
                                                                                |                                      | :tcpip:func:`port_monoflop/set <BrickletIO16.set_port_monoflop>`
                                                                                |                                      | :tcpip:func:`selected_values/set <BrickletIO16.set_selected_values>`
                                                                                |                                      | :tcpip:func:`edge_count_config/set <BrickletIO16.set_edge_count_config>`

 :ref:`IO-4 Bricklet <io4_bricklet>`                                            | bricklet/io4                         | :tcpip:func:`value <BrickletIO4.get_value>`
                                                                                |                                      | :tcpip:func:`value/set <BrickletIO4.set_value>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletIO4.set_configuration>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletIO4.set_monoflop>`
                                                                                |                                      | :tcpip:func:`selected_values/set <BrickletIO4.set_selected_values>`
                                                                                |                                      | :tcpip:func:`edge_count_config/set <BrickletIO4.set_edge_count_config>`

 :ref:`Joystick Bricklet <joystick_bricklet>`                                   | bricklet/joystick                    | :tcpip:func:`position <BrickletJoystick.get_position>`
                                                                                |                                      | :tcpip:func:`pressed <BrickletJoystick.is_pressed>`
                                                                                |                                      | :tcpip:func:`calibrate/set <BrickletJoystick.calibrate>`

 :ref:`Laser Range Finder Bricklet <laser_range_finder_bricklet>`               | bricklet/laser_range_finder          | :tcpip:func:`distance <BrickletLaserRangeFinder.get_distance>`
                                                                                |                                      | :tcpip:func:`velocity <BrickletLaserRangeFinder.get_velocity>`
                                                                                |                                      | :tcpip:func:`mode <BrickletLaserRangeFinder.get_mode>`
                                                                                |                                      | :tcpip:func:`mode/set <BrickletLaserRangeFinder.set_mode>`
                                                                                |                                      | :tcpip:func:`laser_enabled <BrickletLaserRangeFinder.is_laser_enabled>`
                                                                                |                                      | :tcpip:func:`enable_laser/set <BrickletLaserRangeFinder.enable_laser>`
                                                                                |                                      | :tcpip:func:`disable_laser/set <BrickletLaserRangeFinder.disable_laser>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletLaserRangeFinder.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletLaserRangeFinder.set_moving_average>`

 :ref:`LCD 16x2 Bricklet <lcd_16x2_bricklet>`                                   | bricklet/lcd_16x2                    | :tcpip:func:`write_line/set <BrickletLCD16x2.write_line>`
                                                                                |                                      | :tcpip:func:`clear_display/set <BrickletLCD16x2.clear_display>`
                                                                                |                                      | :tcpip:func:`backlight_on <BrickletLCD16x2.is_backlight_on>`
                                                                                |                                      | :tcpip:func:`backlight_on/set <BrickletLCD16x2.backlight_on>`
                                                                                |                                      | :tcpip:func:`backlight_off/set <BrickletLCD16x2.backlight_off>`
                                                                                |                                      | :tcpip:func:`config <BrickletLCD16x2.get_config>`
                                                                                |                                      | :tcpip:func:`config/set <BrickletLCD16x2.set_config>`
                                                                                |                                      | :tcpip:func:`custom_character <BrickletLCD16x2.get_custom_character>`
                                                                                |                                      | :tcpip:func:`custom_character/set <BrickletLCD16x2.set_custom_character>`
                                                                                |                                      | :tcpip:func:`button_pressed <BrickletLCD16x2.is_button_pressed>`

 :ref:`LCD 20x4 Bricklet <lcd_20x4_bricklet>`                                   | bricklet/lcd_20x4                    | :tcpip:func:`write_line/set <BrickletLCD20x4.write_line>`
                                                                                |                                      | :tcpip:func:`clear_display/set <BrickletLCD20x4.clear_display>`
                                                                                |                                      | :tcpip:func:`backlight_on <BrickletLCD20x4.is_backlight_on>`
                                                                                |                                      | :tcpip:func:`backlight_on/set <BrickletLCD20x4.backlight_on>`
                                                                                |                                      | :tcpip:func:`backlight_off/set <BrickletLCD20x4.backlight_off>`
                                                                                |                                      | :tcpip:func:`config <BrickletLCD20x4.get_config>`
                                                                                |                                      | :tcpip:func:`config/set <BrickletLCD20x4.set_config>`
                                                                                |                                      | :tcpip:func:`custom_character <BrickletLCD20x4.get_custom_character>`
                                                                                |                                      | :tcpip:func:`custom_character/set <BrickletLCD20x4.set_custom_character>`
                                                                                |                                      | :tcpip:func:`button_pressed <BrickletLCD20x4.is_button_pressed>`
                                                                                |                                      | :tcpip:func:`default_text <BrickletLCD20x4.get_default_text>`
                                                                                |                                      | :tcpip:func:`default_text/set <BrickletLCD20x4.set_default_text>`
                                                                                |                                      | :tcpip:func:`default_text_counter <BrickletLCD20x4.get_default_text_counter>`
                                                                                |                                      | :tcpip:func:`default_text_counter/set <BrickletLCD20x4.set_default_text_counter>`

 :ref:`LED Strip Bricklet <led_strip_bricklet>`                                 | bricklet/led_strip                   | :tcpip:func:`rgb_values <BrickletLEDStrip.get_rgb_values>`
                                                                                |                                      | :tcpip:func:`rgb_values/set <BrickletLEDStrip.set_rgb_values>`
                                                                                |                                      | :tcpip:func:`frame_duration <BrickletLEDStrip.get_frame_duration>`
                                                                                |                                      | :tcpip:func:`frame_duration/set <BrickletLEDStrip.set_frame_duration>`
                                                                                |                                      | :tcpip:func:`supply_voltage <BrickletLEDStrip.get_supply_voltage>`
                                                                                |                                      | :tcpip:func:`clock_frequency <BrickletLEDStrip.get_clock_frequency>`
                                                                                |                                      | :tcpip:func:`clock_frequency/set <BrickletLEDStrip.set_clock_frequency>`
                                                                                |                                      | :tcpip:func:`chip_type <BrickletLEDStrip.get_chip_type>`
                                                                                |                                      | :tcpip:func:`chip_type/set <BrickletLEDStrip.set_chip_type>`

 :ref:`Line Bricklet <line_bricklet>`                                           | bricklet/line                        | :tcpip:func:`reflectivity <BrickletLine.get_reflectivity>`

 :ref:`Linear Poti Bricklet <line_bricklet>`                                    | bricklet/linear_poti                 | :tcpip:func:`position <BrickletLinearPoti.get_position>`

 :ref:`Load Cell Bricklet <load_cell_bricklet>`                                 | bricklet/load_cell                   | :tcpip:func:`weight <BrickletLoadCell.get_weight>`
                                                                                |                                      | :tcpip:func:`led_on <BrickletLoadCell.is_led_on>`
                                                                                |                                      | :tcpip:func:`led_on/set <BrickletLoadCell.led_on>`
                                                                                |                                      | :tcpip:func:`led_off/set <BrickletLoadCell.led_off>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletLoadCell.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletLoadCell.set_moving_average>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletLoadCell.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletLoadCell.set_configuration>`
                                                                                |                                      | :tcpip:func:`tare/set <BrickletLoadCell.tare>`

 :ref:`Moisture Bricklet <moisture_bricklet>`                                   | bricklet/moisture                    | :tcpip:func:`moisture_value <BrickletMoisture.get_moisture_value>`
                                                                                |                                      | :tcpip:func:`moving_average <BrickletMoisture.get_moving_average>`
                                                                                |                                      | :tcpip:func:`moving_average/set <BrickletMoisture.set_moving_average>`

 :ref:`Motion Detector Bricklet <motion_detector_bricklet>`                     | bricklet/motion_detector             | :tcpip:func:`motion_detected <BrickletMotionDetector.get_motion_detected>`

 :ref:`Motion Detector Bricklet 2.0 <motion_detector_v2_bricklet>`              | bricklet/motion_detector_v2          | :tcpip:func:`motion_detected <BrickletMotionDetectorV2.get_motion_detected>`

 :ref:`Motorized Linear Poti Bricklet <motorized_linear_poti_bricklet>`         | bricklet/motorized_linear_poti       | :tcpip:func:`position <BrickletMotorizedLinearPoti.get_position>`
                                                                                |                                      | :tcpip:func:`motor_position <BrickletMotorizedLinearPoti.get_motor_position>`
                                                                                |                                      | :tcpip:func:`status_led_config <BrickletMotorizedLinearPoti.get_status_led_config>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletMotorizedLinearPoti.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`motor_position/set <BrickletMotorizedLinearPoti.set_motor_position>`
                                                                                |                                      | :tcpip:func:`calibrate/set <BrickletMotorizedLinearPoti.calibrate>`
                                                                                |                                      | :tcpip:func:`status_led_config/set <BrickletMotorizedLinearPoti.set_status_led_config>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickletMotorizedLinearPoti.reset>`

 :ref:`Multi Touch Bricklet <multi_touch_bricklet>`                             | bricklet/multi_touch                 | :tcpip:func:`touch_state <BrickletMultiTouch.get_touch_state>`
                                                                                |                                      | :tcpip:func:`electrode_config <BrickletMultiTouch.get_electrode_config>`
                                                                                |                                      | :tcpip:func:`electrode_config/set <BrickletMultiTouch.set_electrode_config>`
                                                                                |                                      | :tcpip:func:`electrode_sensitivity <BrickletMultiTouch.get_electrode_sensitivity>`
                                                                                |                                      | :tcpip:func:`electrode_sensitivity/set <BrickletMultiTouch.set_electrode_sensitivity>`
                                                                                |                                      | :tcpip:func:`recalibrate/set <BrickletMultiTouch.recalibrate>`

 :ref:`NFC RFID Bricklet <nfc_rfid_bricklet>`                                   | bricklet/nfc_rfid                    | :tcpip:func:`tag_id <BrickletNFCRFID.get_tag_id>`
                                                                                |                                      | :tcpip:func:`state <BrickletNFCRFID.get_state>`
                                                                                |                                      | :tcpip:func:`page <BrickletNFCRFID.get_page>`
                                                                                |                                      | :tcpip:func:`request_tag_id/set <BrickletNFCRFID.request_tag_id>`
                                                                                |                                      | :tcpip:func:`authenticate_mifare_classic_page/set <BrickletNFCRFID.authenticate_mifare_classic_page>`
                                                                                |                                      | :tcpip:func:`write_page/set <BrickletNFCRFID.write_page>`
                                                                                |                                      | :tcpip:func:`request_page/set <BrickletNFCRFID.request_page>`

 :ref:`OLED 128x64 Bricklet <oled_128x64_bricklet>`                             | bricklet/oled_128x64                 | :tcpip:func:`write/set <BrickletOLED128x64.write>`
                                                                                |                                      | :tcpip:func:`new_window/set <BrickletOLED128x64.new_window>`
                                                                                |                                      | :tcpip:func:`clear_display/set <BrickletOLED128x64.clear_display>`
                                                                                |                                      | :tcpip:func:`write_line/set <BrickletOLED128x64.write_line>`
                                                                                |                                      | :tcpip:func:`display_configuration <BrickletOLED128x64.get_display_configuration>`
                                                                                |                                      | :tcpip:func:`display_configuration/set <BrickletOLED128x64.set_display_configuration>`

 :ref:`OLED 64x48 Bricklet <oled_64x48_bricklet>`                               | bricklet/oled_64x48                  | :tcpip:func:`write/set <BrickletOLED64x48.write>`
                                                                                |                                      | :tcpip:func:`new_window/set <BrickletOLED64x48.new_window>`
                                                                                |                                      | :tcpip:func:`clear_display/set <BrickletOLED64x48.clear_display>`
                                                                                |                                      | :tcpip:func:`write_line/set <BrickletOLED64x48.write_line>`
                                                                                |                                      | :tcpip:func:`display_configuration <BrickletOLED64x48.get_display_configuration>`
                                                                                |                                      | :tcpip:func:`display_configuration/set <BrickletOLED64x48.set_display_configuration>`

 :ref:`Piezo Buzzer Bricklet <piezo_buzzer_bricklet>`                           | bricklet/piezo_buzzer                | :tcpip:func:`beep/set <BrickletPiezoBuzzer.beep>`
                                                                                |                                      | :tcpip:func:`morse_code/set <BrickletPiezoBuzzer.morse_code>`

 :ref:`Piezo Speaker Bricklet <piezo_speaker_bricklet>`                         | bricklet/piezo_speaker               | :tcpip:func:`beep/set <BrickletPiezoSpeaker.beep>`
                                                                                |                                      | :tcpip:func:`morse_code/set <BrickletPiezoSpeaker.morse_code>`

 :ref:`Outdoor Weather Bricklet <outdoor_weather_bricklet>`                     | bricklet/outdoor_weather             | :tcpip:func:`station_data <BrickletOutdoorWeather.get_station_data>`
                                                                                |                                      | :tcpip:func:`sensor_data <BrickletOutdoorWeather.get_sensor_data>`

 :ref:`PTC Bricklet <ptc_bricklet>`                                             | bricklet/ptc                         | :tcpip:func:`temperature <BrickletPTC.get_temperature>`
                                                                                |                                      | :tcpip:func:`resistance <BrickletPTC.get_resistance>`
                                                                                |                                      | :tcpip:func:`sensor_connected <BrickletPTC.is_sensor_connected>`
                                                                                |                                      | :tcpip:func:`wire_mode <BrickletPTC.get_wire_mode>`
                                                                                |                                      | :tcpip:func:`wire_mode/set <BrickletPTC.set_wire_mode>`
                                                                                |                                      | :tcpip:func:`noise_rejection_filter <BrickletPTC.get_noise_rejection_filter>`
                                                                                |                                      | :tcpip:func:`noise_rejection_filter/set <BrickletPTC.set_noise_rejection_filter>`

 :ref:`Real-Time Clock Bricklet <real_time_clock_bricklet>`                     | bricklet/real_time_clock             | :tcpip:func:`date_time <BrickletRealTimeClock.get_date_time>`
                                                                                |                                      | :tcpip:func:`date_time/set <BrickletRealTimeClock.set_date_time>`
                                                                                |                                      | :tcpip:func:`timestamp <BrickletRealTimeClock.get_timestamp>`
                                                                                |                                      | :tcpip:func:`offset <BrickletRealTimeClock.get_offset>`
                                                                                |                                      | :tcpip:func:`offset/set <BrickletRealTimeClock.set_offset>`

 :ref:`Remote Switch Bricklet <remote_switch_bricklet>`                         | bricklet/remote_switch               | :tcpip:func:`switching_state <BrickletRemoteSwitch.get_switching_state>`
                                                                                |                                      | :tcpip:func:`repeats <BrickletRemoteSwitch.get_repeats>`
                                                                                |                                      | :tcpip:func:`repeats/set <BrickletRemoteSwitch.set_repeats>`
                                                                                |                                      | :tcpip:func:`switch_socket_a/set <BrickletRemoteSwitch.switch_socket_a>`
                                                                                |                                      | :tcpip:func:`switch_socket_b/set <BrickletRemoteSwitch.switch_socket_b>`
                                                                                |                                      | :tcpip:func:`dim_socket_b/set <BrickletRemoteSwitch.dim_socket_b>`
                                                                                |                                      | :tcpip:func:`switch_socket_c/set <BrickletRemoteSwitch.switch_socket_c>`

:ref:`Remote Switch Bricklet 2.0 <remote_switch_v2_bricklet>`                   | bricklet/remote_switch_v2            | :tcpip:func:`switching_state <BrickletRemoteSwitchV2.get_switching_state>`
                                                                                |                                      | :tcpip:func:`repeats <BrickletRemoteSwitchV2.get_repeats>`
                                                                                |                                      | :tcpip:func:`repeats/set <BrickletRemoteSwitchV2.set_repeats>`
                                                                                |                                      | :tcpip:func:`switch_socket_a/set <BrickletRemoteSwitchV2.switch_socket_a>`
                                                                                |                                      | :tcpip:func:`switch_socket_b/set <BrickletRemoteSwitchV2.switch_socket_b>`
                                                                                |                                      | :tcpip:func:`dim_socket_b/set <BrickletRemoteSwitchV2.dim_socket_b>`
                                                                                |                                      | :tcpip:func:`switch_socket_c/set <BrickletRemoteSwitchV2.switch_socket_c>`

 :ref:`RGB LED Bricklet <rgb_led_bricklet>`                                     | bricklet/rgb_led                     | :tcpip:func:`rgb_value <BrickletRGBLED.get_rgb_value>`
                                                                                |                                      | :tcpip:func:`rgb_value/set <BrickletRGBLED.set_rgb_value>`

 :ref:`RGB LED Button Bricklet <rgb_led_button_bricklet>`                       | bricklet/rgb_led_button              | :tcpip:func:`color <BrickletRGBLEDButton.get_color>`
                                                                                |                                      | :tcpip:func:`button_state <BrickletRGBLEDButton.get_button_state>`
                                                                                |                                      | :tcpip:func:`color_calibration <BrickletRGBLEDButton.get_color_calibration>`
                                                                                |                                      | :tcpip:func:`status_led_config <BrickletRGBLEDButton.get_status_led_config>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletRGBLEDButton.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`color/set <BrickletRGBLEDButton.set_color>`
                                                                                |                                      | :tcpip:func:`color_calibration/set <BrickletRGBLEDButton.set_color_calibration>`
                                                                                |                                      | :tcpip:func:`status_led_config/set <BrickletRGBLEDButton.set_status_led_config>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickletRGBLEDButton.reset>`

 :ref:`RGB LED Matrix Bricklet <rgb_led_matrix_bricklet>`                       | bricklet/rgb_led_matrix              | :tcpip:func:`red <BrickletRGBLEDMatrix.get_red>`
                                                                                |                                      | :tcpip:func:`green <BrickletRGBLEDMatrix.get_green>`
                                                                                |                                      | :tcpip:func:`blue <BrickletRGBLEDMatrix.get_blue>`
                                                                                |                                      | :tcpip:func:`frame_duration <BrickletRGBLEDMatrix.get_frame_duration>`
                                                                                |                                      | :tcpip:func:`supply_voltage <BrickletRGBLEDMatrix.get_supply_voltage>`
                                                                                |                                      | :tcpip:func:`status_led_config <BrickletRGBLEDMatrix.get_status_led_config>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletRGBLEDMatrix.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`red/set <BrickletRGBLEDMatrix.set_blue>`
                                                                                |                                      | :tcpip:func:`green/set <BrickletRGBLEDMatrix.set_blue>`
                                                                                |                                      | :tcpip:func:`blue/set <BrickletRGBLEDMatrix.set_blue>`
                                                                                |                                      | :tcpip:func:`frame_duration/set <BrickletRGBLEDMatrix.set_frame_duration>`
                                                                                |                                      | :tcpip:func:`draw_frame/set <BrickletRGBLEDMatrix.draw_frame>`
                                                                                |                                      | :tcpip:func:`status_led_config/set <BrickletRGBLEDMatrix.set_status_led_config>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickletRGBLEDMatrix.reset>`

 :ref:`Rotary Encoder Bricklet <rotary_encoder_bricklet>`                       | bricklet/rotary_encoder              | :tcpip:func:`count <BrickletRotaryEncoder.get_count>` (calls :tcpip:func:`get_count <BrickletRotaryEncoder.get_count>` with *false*)
                                                                                |                                      | :tcpip:func:`get_count/set <BrickletRotaryEncoder.get_count>` (calls :tcpip:func:`get_count <BrickletRotaryEncoder.get_count>` with the parameters provided by the *get_count/set* topic and the output of the getter being published to the *count* topic)
                                                                                |                                      | :tcpip:func:`pressed <BrickletRotaryEncoder.is_pressed>`

 :ref:`Rotary Encoder Bricklet 2.0 <rotary_encoder_v2_bricklet>`                | bricklet/rotary_encoder_v2           | :tcpip:func:`count <BrickletRotaryEncoderV2.get_count>` (calls :tcpip:func:`get_count <BrickletRotaryEncoderV2.get_count>` with *false*)
                                                                                |                                      | :tcpip:func:`get_count/set <BrickletRotaryEncoderV2.get_count>` (calls :tcpip:func:`get_count <BrickletRotaryEncoderV2.get_count>` with the parameters provided by the *get_count/set* topic and the output of the getter being published to the *count* topic)
                                                                                |                                      | :tcpip:func:`pressed <BrickletRotaryEncoderV2.is_pressed>`

 :ref:`Rotary Poti Bricklet <rotary_poti_bricklet>`                             | bricklet/rotary_poti                 | :tcpip:func:`position <BrickletRotaryPoti.get_position>`

 :ref:`RS232 Bricklet <rs232_bricklet>`                                         | bricklet/rs232                       | :tcpip:func:`read <BrickletRS232.read>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletRS232.get_configuration>`
                                                                                |                                      | :tcpip:func:`write/set <BrickletRS232.write>` (calls :tcpip:func:`write <BrickletRS232.write>` with the parameters provided by the *write/set* topic and the output of the getter being published to the *write* topic)
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletRS232.set_configuration>`
                                                                                |                                      | :tcpip:func:`break_condition/set <BrickletRS232.set_break_condition>`

 :ref:`RS485 Bricklet <rs485_bricklet>`                                         | bricklet/rs485                       | :tcpip:func:`rs485_configuration <BrickletRS485.get_rs485_configuration>`
                                                                                |                                      | :tcpip:func:`modbus_configuration <BrickletRS485.get_modbus_configuration>`
                                                                                |                                      | :tcpip:func:`mode <BrickletRS485.get_mode>`
                                                                                |                                      | :tcpip:func:`communication_led_config <BrickletRS485.get_communication_led_config>`
                                                                                |                                      | :tcpip:func:`error_led_config <BrickletRS485.get_error_led_config>`
                                                                                |                                      | :tcpip:func:`buffer_config <BrickletRS485.get_buffer_config>`
                                                                                |                                      | :tcpip:func:`buffer_status <BrickletRS485.get_buffer_status>`
                                                                                |                                      | :tcpip:func:`error_count <BrickletRS485.get_error_count>`
                                                                                |                                      | :tcpip:func:`modbus_common_error_count <BrickletRS485.get_modbus_common_error_count>`
                                                                                |                                      | :tcpip:func:`status_led_config <BrickletRS485.get_status_led_config>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletRS485.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`write/set <BrickletRS485.write>` (calls :tcpip:func:`write <BrickletRS485.write>` with the parameters provided by the *write/set* topic and the output of the getter being published to the *write* topic)
                                                                                |                                      | :tcpip:func:`read/set <BrickletRS485.read>` (calls :tcpip:func:`read <BrickletRS485.read>` with the parameters provided by the *read/set* topic and the output of the getter being published to the *read* topic)
                                                                                |                                      | :tcpip:func:`rs485_configuration/set <BrickletRS485.set_rs485_configuration>`
                                                                                |                                      | :tcpip:func:`modbus_configuration/set <BrickletRS485.set_modbus_configuration>`
                                                                                |                                      | :tcpip:func:`mode/set <BrickletRS485.set_mode>`
                                                                                |                                      | :tcpip:func:`communication_led_config/set <BrickletRS485.set_communication_led_config>`
                                                                                |                                      | :tcpip:func:`error_led_config/set <BrickletRS485.set_error_led_config>`
                                                                                |                                      | :tcpip:func:`buffer_config/set <BrickletRS485.set_buffer_config>`
                                                                                |                                      | :tcpip:func:`status_led_config/set <BrickletRS485.set_status_led_config>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickletRS485.reset>`

 :ref:`Solid State Relay Bricklet <solid_state_relay_bricklet>`                 | bricklet/solid_state_relay           | :tcpip:func:`state <BrickletSolidStateRelay.get_state>`
                                                                                |                                      | :tcpip:func:`state/set <BrickletSolidStateRelay.set_state>`
                                                                                |                                      | :tcpip:func:`monoflop <BrickletSolidStateRelay.get_monoflop>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletSolidStateRelay.set_monoflop>`

 :ref:`Solid State Relay Bricklet 2.0 <solid_state_relay_v2_bricklet>`          | bricklet/solid_state_relay_v2        | :tcpip:func:`state <BrickletSolidStateRelayV2.get_state>`
                                                                                |                                      | :tcpip:func:`state/set <BrickletSolidStateRelayV2.set_state>`
                                                                                |                                      | :tcpip:func:`monoflop <BrickletSolidStateRelayV2.get_monoflop>`
                                                                                |                                      | :tcpip:func:`monoflop/set <BrickletSolidStateRelayV2.set_monoflop>`

 :ref:`Sound Intensity Bricklet <sound_intensity_bricklet>`                     | bricklet/sound_intensity             | :tcpip:func:`intensity <BrickletSoundIntensity.get_intensity>`

 :ref:`Temperature Bricklet <temperature_bricklet>`                             | bricklet/temperature                 | :tcpip:func:`temperature <BrickletTemperature.get_temperature>`
                                                                                |                                      | :tcpip:func:`i2c_mode <BrickletTemperature.get_i2c_mode>`
                                                                                |                                      | :tcpip:func:`i2c_mode/set <BrickletTemperature.set_i2c_mode>`

 :ref:`Temperature IR Bricklet <temperature_ir_bricklet>`                       | bricklet/temperature_ir              | :tcpip:func:`ambient_temperature <BrickletTemperatureIR.get_ambient_temperature>`
                                                                                |                                      | :tcpip:func:`object_temperature <BrickletTemperatureIR.get_object_temperature>`
                                                                                |                                      | :tcpip:func:`emissivity <BrickletTemperatureIR.get_emissivity>`
                                                                                |                                      | :tcpip:func:`emissivity/set <BrickletTemperatureIR.set_emissivity>`

 :ref:`Temperature IR Bricklet 2.0 <temperature_ir_v2_bricklet>`                | bricklet/temperature_ir_v2           | :tcpip:func:`ambient_temperature <BrickletTemperatureIRV2.get_ambient_temperature>`
                                                                                |                                      | :tcpip:func:`object_temperature <BrickletTemperatureIRV2.get_object_temperature>`
                                                                                |                                      | :tcpip:func:`emissivity <BrickletTemperatureIRV2.get_emissivity>`
                                                                                |                                      | :tcpip:func:`emissivity/set <BrickletTemperatureIRV2.set_emissivity>`

 :ref:`Thermal Imaging Bricklet <thermal_imaging_bricklet>`                     | bricklet/thermal_imaging             | :tcpip:func:`high_contrast_image <BrickletThermalImaging.get_high_contrast_image>`
                                                                                |                                      | :tcpip:func:`temperature_image <BrickletThermalImaging.get_>`
                                                                                |                                      | :tcpip:func:`statistics <BrickletThermalImaging.get_statistics>`
                                                                                |                                      | :tcpip:func:`resolution <BrickletThermalImaging.get_resolution>`
                                                                                |                                      | :tcpip:func:`spotmeter_config <BrickletThermalImaging.get_spotmeter_config>`
                                                                                |                                      | :tcpip:func:`high_contrast_config <BrickletThermalImaging.get_high_contrast_config>`
                                                                                |                                      | :tcpip:func:`status_led_config <BrickletThermalImaging.get_status_led_config>`
                                                                                |                                      | :tcpip:func:`chip_temperature <BrickletThermalImaging.get_chip_temperature>`
                                                                                |                                      | :tcpip:func:`image_transfer_config <BrickletThermalImaging.get_image_transfer_config>`
                                                                                |                                      | :tcpip:func:`resolution/set <BrickletThermalImaging.set_resolution>`
                                                                                |                                      | :tcpip:func:`spotmeter_config/set <BrickletThermalImaging.set_spotmeter_config>`
                                                                                |                                      | :tcpip:func:`high_contrast_config/set <BrickletThermalImaging.set_high_contrast_config>`
                                                                                |                                      | :tcpip:func:`status_led_config/set <BrickletThermalImaging.set_status_led_config>`
                                                                                |                                      | :tcpip:func:`reset/set <BrickletThermalImaging.reset>`
                                                                                |                                      | :tcpip:func:`image_transfer_config/set <BrickletThermalImaging.set_image_transfer_config>`

 :ref:`Thermocouple Bricklet <thermocouple_bricklet>`                           | bricklet/thermocouple                | :tcpip:func:`temperature <BrickletThermocouple.get_temperature>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletThermocouple.get_configuration>`
                                                                                |                                      | :tcpip:func:`error_state <BrickletThermocouple.get_error_state>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletThermocouple.set_configuration>`

 :ref:`Tilt Bricklet <tilt_bricklet>`                                           | bricklet/tilt                        | :tcpip:func:`tilt_state <BrickletTilt.get_tilt_state>`

 :ref:`UV Light Bricklet <uv_light_bricklet>`                                   | bricklet/uv_light                    | :tcpip:func:`uv_light <BrickletUVLight.get_uv_light>`

 :ref:`Voltage Bricklet <voltage_bricklet>`                                     | bricklet/voltage                     | :tcpip:func:`voltage <BrickletVoltage.get_voltage>`

 :ref:`Voltage/Current Bricklet <voltage_current_bricklet>`                     | bricklet/voltage_current             | :tcpip:func:`voltage <BrickletVoltageCurrent.get_voltage>`
                                                                                |                                      | :tcpip:func:`current <BrickletVoltageCurrent.get_current>`
                                                                                |                                      | :tcpip:func:`power <BrickletVoltageCurrent.get_power>`
                                                                                |                                      | :tcpip:func:`configuration <BrickletVoltageCurrent.get_configuration>`
                                                                                |                                      | :tcpip:func:`configuration/set <BrickletVoltageCurrent.set_configuration>`
                                                                                |                                      | :tcpip:func:`calibration <BrickletVoltageCurrent.get_calibration>`
                                                                                |                                      | :tcpip:func:`calibration/set <BrickletVoltageCurrent.set_calibration>`


Adding Support for other Bricks and Bricklets
---------------------------------------------

The Brick MQTT Proxy is designed to be easily extendable for other Bricks and 
Bricklets. Take a look in the 
`source of the script <https://github.com/Tinkerforge/brick-mqtt-proxy/blob/master/brick-mqtt-proxy.py>`__.
To add other products you will have to implement your own proxy class derived 
from ``DeviceProxy`` class. Comments in the code describe the necessary
structure.
