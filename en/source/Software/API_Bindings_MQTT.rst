
.. _api_bindings_mqtt:

MQTT - API Bindings
===================

The MQTT bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` using the MQTT protocol. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``tinkerforge_mqtt`` a Python script that acts as a translation proxy between a MQTT broker and a Brick Daemon
* in ``examples/`` the examples for every Brick and Bricklet

The MQTT bindings are based on the :ref:`Python bindings <api_bindings_python>`.

Requirements
------------

* Python 2.7.9 or newer with ``argparse`` module, Python 3.4 or newer is also supported.
* Paho's python library 1.3.1 or newer.


.. _api_bindings_mqtt_install:

Installation
------------

The MQTT bindings can be installed, but can also be used without installation.

To install the bindings copy the ``tinkerforge_mqtt`` file to a folder that is in
the ``PATH``. For example, this folder on Linux and macOS::

 /usr/local/bin/

On Windows the ``Scripts/`` folder of the Python installation is a good choice::

 C:\Python27\Scripts\

To be able to call the bindings directly on Windows you have to create a
``tinkerforge_mqtt.bat`` file in the ``Scripts/`` folder with the following content::

 @"C:\Python27\python.exe" "C:\Python27\Scripts\tinkerforge_mqtt"

If your Python is not installed in ``C:\Python27\`` then you have to adapt the
content of the ``tinkerforge_mqtt.bat`` file accordingly.


Testing an Example
------------------

To test a MQTT example :ref:`Brick Daemon <brickd>` and :ref:`Brick Viewer
<brickv>` have to be installed first. Brick Daemon acts as a proxy between the
USB interface of the Bricks and the API bindings. Brick Viewer connects to
Brick Daemon and helps to figure out basic information about the connected
Bricks and Bricklets.

Then run the ``tinkerforge_mqtt`` script, configured to connect to your Brick Daemon
and MQTT broker, using the command line switches. See the output of ``tinkerforge_mqtt --help``.

All examples are written in pseudo code, you have to translate them to your favorite
programming language before running them. Alternatively you can use the mosquitto_pub
and mosquitto_sub commands, which are part of the mosquitto MQTT broker.

The examples consist of a setup and a cleanup block. The setup block configures devices
and callbacks, the cleanup block stops them. Not all examples have a cleanup block.

The pseudo code denotes MQTT publish operations as ``publish [PAYLOAD] to [TOPIC]``
and subscribe operations as ``subscribe to [TOPIC]``. Subscriptions optionally
contain logic which should be run if a message arrives. These blocks end with ``endsubscribe``.

MQTT Topics
^^^^^^^^^^^

MQTT topics are structured as follows: ``[<GLOBAL_PREFIX>/]<OPERATION>/<DEVICE>[/<UID>]/<FUNCTION>[/<SUFFIX>]``

``[<GLOBAL_PREFIX>/]`` is the global prefix for all topics (default: ``tinkerforge/``).
It can be changed using the ``--global-topic-prefix`` command line flag.
The  prefix can be used to disambiguate multiple instances of the MQTT Bindings.
It can contain multiple topic levels, for example ``tinkerforge/living_room/sensors/``.
If the prefix does not end with a '/', one is inserted, except if you select an empty prefix.
Then all topics start with the operation. Note that this is not recommended. Also note, that '/'
is a valid prefix.

``<OPERATION>`` denotes the type of request. It can be one of ``request``, ``response``, ``register`` or ``callback``.
The bindings subscribe to ``request`` and ``register`` topics and will publish answers to
``requests`` under ``response``, answers to ``register`` under ``callback`` topics.
 
``<DEVICE>`` is the type of device you want to interact with. This can be the name of a
brick or bricklet in snake_case, for example ``oled_64x48_bricklet``, or ``ip_connection``.
See the documentation of devices for the exact spelling.
  
``[/<UID>]`` is the UID of the device. If the device is the ``ip_connection``,
this has to be empty and with no slashes, for example: ``.../ip_connection/enumerate``
  
``<FUNCTION>`` is the function to call, or the callback to register to, written in snake_case.
 
``[/<SUFFIX>]`` is the optional suffix to attach to responses. This can be used to allow message
filtering, for example by setting it to ``/STATUS`` for requests or callback registrations which
query status information. Another MQTT client can then register to ``[<GLOBAL_PREFIX>/]+/+/+/+/STATUS`` to
receive all status information tagged as such.
 
A typical request topic looks like this: ``tinkerforge/request/rgb_led_button_bricklet/Dod/get_color``.
The response to this request (or an error) will be published under
``tinkerforge/response/rgb_led_button_bricklet/Dod/get_color`` by the bindings.

A callback registration topic looks like this: ``tinkerforge/register/rgb_led_button_bricklet/Dod/button_state_changed``.
If you subscribe to ``tinkerforge/callback/rgb_led_button_bricklet/Dod/button_state_changed`` you will receive a message
each time the button is pressed or released.
 
MQTT Payload
^^^^^^^^^^^^

All MQTT payload is encoded as JSON objects, each member maps to a parameter or return value
of the corresponding function in the Python bindings. Occurred errors are logged to stdout
as well as inserted into returned JSON objects under the ``_ERROR`` field.

If symbolic output is not disabled (using the ``--no-symbolic-response`` command line flag),
integer constants are translated to strings. For example the button_state_changed callback of
the RGB LED Button Bricklet will be ``{"state": "pressed"}`` instead of ``{"state:" 0}``.

Integer constants in request payloads can also be replaced by their associated symbols. For
example publishing ``{"config": "show_heartbeat"}`` to ``tinkerforge/request/rgb_led_button_bricklet/Dod/set_status_led_config``
is equivalent to publishing ``{"config": 2}``.

Symbols for constants are documented where they are available.

Callback (de)registrations can use either ``{"register": true/false}`` or ``true/false`` as payload.
 
Loading initial messages from a file
------------------------------------

Messages to be processed when the bindings are started, can be read from a file. Use the ``--init-file /path/to/file``
command line argument to specify one. These files can (for example) be used to configure and register callbacks. The file
is expected to contain a JSON-Object with MQTT topics as attribute names. The attribute values are JSON objects
as used as MQTT payload. The following example shows a file which registers the all_data callback of a IMU Brick 2.0
and configures the period of the callback to 100ms::

 {
         "tinkerforge/register/imu_v2_brick/XXYYZZ/all_data": {"register": true},
         "tinkerforge/request/imu_v2_brick/XXYYZZ/set_all_data_period": {"period": 100}
 }


Command line arguments
----------------------

 * ``-h, --help`` show this help message and exit
 * ``--ipcon-host <IPCON_HOST>`` hostname or IP address of Brick Daemon, WIFI or Ethernet Extension (default: localhost)
 * ``--ipcon-port <IPCON_PORT>`` port number of Brick Daemon, WIFI or Ethernet Extension (default: 4223)
 * ``--ipcon-auth-secret <IPCON_AUTH_SECRET>`` authentication secret of Brick Daemon, WIFI or Ethernet Extension
 * ``--ipcon-timeout <IPCON_TIMEOUT>`` timeout in milliseconds for communication with Brick Daemon, WIFI or Ethernet Extension (default: 2500)
 * ``--broker-host <BROKER_HOST>`` hostname or IP address of MQTT broker (default: localhost)
 * ``--broker-port <BROKER_PORT>`` port number of MQTT broker (default: 1883)
 * ``--broker-username <BROKER_USERNAME>`` username for the MQTT broker connection
 * ``--broker-password <BROKER_PASSWORD>`` password for the MQTT broker connection
 * ``--broker-certificate <BROKER_CERTIFICATE>`` Certificate Authority certificate file used for SSL/TLS connections to the broker
 * ``--broker-tls-insecure`` disable verification of the server hostname in the server certificate for the MQTT broker connection
 * ``--global-topic-prefix <GLOBAL_TOPIC_PREFIX>`` global MQTT topic prefix (default: tinkerforge/)
 * ``--debug`` enable debug output
 * ``--no-symbolic-response`` disable translation into string constants for responses
 * ``--show-payload`` show received payload if JSON parsing fails
 * ``--init-file <INIT_FILE>`` file from where to load initial messages to publish
 
 
API Reference and Examples
--------------------------

Links to the API reference for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table. Further project descriptions can be found in the
:ref:`Starter Kits <index_kits>` section.

.. include:: API_Bindings_MQTT_links.table

.. toctree::
   :hidden:

   IP Connection <IPConnection_MQTT>
   Bricks <Bricks_MQTT>
   Bricks (Discontinued) <Bricks_MQTT_Discontinued>
   Bricklets <Bricklets_MQTT>
   Bricklets (Discontinued) <Bricklets_MQTT_Discontinued>
