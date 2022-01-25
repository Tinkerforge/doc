
.. _api_bindings_mqtt:

MQTT - API Bindings
===================

The MQTT bindings allow you to control :ref:`Bricks <primer_bricks>` and
:ref:`Bricklets <primer_bricklets>` using the MQTT protocol. The
:ref:`ZIP file <downloads_bindings_examples>` for the bindings contains:

* ``tinkerforge_mqtt`` a Python script that acts as a translation proxy between
  a MQTT broker and a Brick Daemon
* in ``examples/`` the examples for every Brick and Bricklet

The MQTT bindings are based on the :ref:`Python bindings <api_bindings_python>`.

Requirements
------------

* Python 3.4 or newer
* Paho MQTT 1.3.1 or newer

.. _api_bindings_mqtt_install:

Installation
------------

There are two ways to install the MQTT bindings:
from our :ref:`APT repository <api_bindings_mqtt_install_apt>` for Debian
based Linux distributions or by :ref:`manually <api_bindings_mqtt_install_manual>`
copying the files to the correct location. But can also be used without
installation.

.. _api_bindings_mqtt_install_apt:

From APT Repository
^^^^^^^^^^^^^^^^^^^

The bindings are available in our APT repository for Debian based Linux
distributions. Follow the :ref:`setup guide <apt_repository_setup>` then install
the bindings::

 sudo apt install tinkerforge-mqtt

The Debian package also installs and starts the systemd services
``tinkerforge_mqtt`` that runs the MQTT bindings.

Now you're ready to test an example. The Debian package does not include the
examples. Those are available as part of the bindings :ref:`ZIP file
<downloads_bindings_examples>`.

.. _api_bindings_mqtt_install_manual:

Manual Installation
^^^^^^^^^^^^^^^^^^^

To install the bindings manually copy the ``tinkerforge_mqtt`` file to a folder
that is in the ``PATH``. For example, this folder on Linux and macOS::

 /usr/local/bin/

On Windows the ``Scripts\`` folder of the Python installation is a good choice::

 C:\Python\Scripts\

To be able to call the bindings directly on Windows you have to create a
``tinkerforge_mqtt.bat`` file in the ``Scripts\`` folder with the following content::

 @"C:\Python\python.exe" "C:\Python\Scripts\tinkerforge_mqtt" %*

If your Python is not installed in ``C:\Python\`` then you have to adapt the
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
and mosquitto_sub commands, which are part of the Mosquitto MQTT broker.

The examples consist of a setup and a cleanup block. The setup block configures devices
and callbacks, the cleanup block stops them. Not all examples have a cleanup block.

The pseudo code denotes MQTT publish operations as ``publish <PAYLOAD> to <TOPIC>``
and subscribe operations as ``subscribe to <TOPIC>``. Subscriptions optionally
contain logic which should be run if a message arrives. These blocks end with ``endsubscribe``.

MQTT Topics
^^^^^^^^^^^

MQTT topics are structured as follows: ``[<GLOBAL_PREFIX>/]<OPERATION>/<DEVICE>[/<UID>]/<FUNCTION>[/<SUFFIX>]``

``[<GLOBAL_PREFIX>/]`` is the global prefix for all topics (default: ``tinkerforge/``).
It can be changed using the ``--global-topic-prefix`` command line flag.
The  prefix can be used to disambiguate multiple instances of the MQTT Bindings.
It can contain multiple topic levels, for example ``tinkerforge/living_room/sensors/``.
If the prefix does not end with a ``/``, one is inserted, except if you select an empty prefix.
Then all topics start with the operation. Note that this is not recommended. Also note, that ``/``
is a valid prefix.

``<OPERATION>`` denotes the type of request. It can be one of ``request``, ``response``, ``register`` or ``callback``.
The bindings subscribe to ``request`` and ``register`` topics and will publish answers to
``requests`` under ``response``, answers to ``register`` under ``callback`` topics.

``<DEVICE>`` is the type of device you want to interact with. This can be the name of a
Brick or Bricklet in snake_case, for example ``oled_64x48_bricklet``, or ``ip_connection``.
See the documentation of devices for the exact spelling.

``[/<UID>]`` is the UID of the device. If the device is the ``ip_connection``,
this has to be empty and with no slashes, for example: ``.../ip_connection/enumerate``

``<FUNCTION>`` is the function to call, or the callback to register to, written in snake_case.

``[/<SUFFIX>]`` is the optional suffix to attach to responses. This can be for example used to allow message
filtering. See :ref:`here <mqtt_topic_suffixes>` for details.

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
integer constants are translated to strings. For example the ``button_state_changed callback`` of
the RGB LED Button Bricklet will be ``{"state": "pressed"}`` instead of ``{"state:" 0}``.

Integer constants in request payloads can also be replaced by their associated symbols. For
example publishing ``{"config": "show_heartbeat"}`` to ``tinkerforge/request/rgb_led_button_bricklet/Dod/set_status_led_config``
is equivalent to publishing ``{"config": 2}``.

Symbols for constants are documented where they are available.

Callback (de)registrations can use either ``{"register": true/false}`` or ``true/false`` as payload.

Requests and Responses
^^^^^^^^^^^^^^^^^^^^^^

To call a Brick or Bricklet function, publish a JSON encoded message under the corresponding ``request`` topic.
For example to set the color of a RGB LED Button Bricklet with UID Enx to yellow using
the mosquitto_pub tool::

  mosquitto_pub -t tinkerforge/request/rgb_led_button_bricklet/Enx/set_color -m '{"red":255, "green":127, "blue":0}'

Functions which return values do so under the corresponding ``response`` topic.
To query the current color of the same Bricklet use::

  mosquitto_sub -t tinkerforge/response/rgb_led_button_bricklet/Enx/get_color
  mosquitto_pub -t tinkerforge/request/rgb_led_button_bricklet/Enx/get_color -m ''

Occured errors are published under the ``response`` topic. If for example a parameter is missing::

  mosquitto_sub -t tinkerforge/response/rgb_led_button_bricklet/Enx/set_color
  mosquitto_pub -t tinkerforge/request/rgb_led_button_bricklet/Enx/set_color -m '{"red":255, "blue":0}'

The message::

  {"_ERROR": "The arguments ['green'] where missing for a call of set_color of device Enx of type rgb_led_button_bricklet."}

is published under ``tinkerforge/response/rgb_led_button_bricklet/Enx/set_color``.
Error messages are also printed to the binding's stdout.

Callbacks
^^^^^^^^^

Callbacks can be registered under the ``register`` topic::

  mosquitto_pub -t tinkerforge/register/rgb_led_button_bricklet/Enx/button_state_changed -m 'true'

and will be published under the ``callback`` topic::

  mosquitto_sub -t tinkerforge/callback/rgb_led_button_bricklet/Enx/button_state_changed

returns::

  {"state": 0}
  {"state": 1}

whenever the button is pressed and released.

To deregister a callback, pass ``false`` as payload instead of ``true``. It is also
possible to use ``{"register":  true}`` and ``{"register": false}`` as (de)registration arguments.

Callback configuration functions work exactly like in other bindings,
so if a callback has to be activated and/or configured you need to:

* subscribe to the ``callback`` topic
* publish the registration to the callback using the ``register`` topic
* publish the configuration of the callbacks properties such as period
* publish the callback activation with the corresponding ``request`` topic

To deregister all callbacks from all devices and the IP connection, you can use the following topic::

  mosquitto_pub -t tinkerforge/request/bindings/reset_callbacks -m ''

Loading initial messages from a file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Messages to be processed when the bindings are started, can be read from a file. Use the ``--init-file /path/to/file``
command line argument to specify one. These files can (for example) be used to configure and register callbacks. The file
is expected to contain a JSON object with MQTT topics as attribute names. The attribute values are JSON objects
as used as MQTT payload. The following example shows a file which registers the ``all_data`` callback of a IMU Brick 2.0
and configures the period of the callback to 100ms::

 {
     "tinkerforge/register/imu_v2_brick/XXYYZZ/all_data": {"register": true},
     "tinkerforge/request/imu_v2_brick/XXYYZZ/set_all_data_period": {"period": 100}
 }

Since version 2.0.8, it is possible to separate between messages to be processed
before and after the connection to the Brick Daemon, WIFI, or Ethernet Extension
is established. This allows registration of callbacks (i.e. the connected callback
of the IP connection) before connecting. The syntax is as follows::

 {
     "pre_connect": {
         "tinkerforge/register/ip_connection/connected": {"register": true},
         "tinkerforge/register/ip_connection/enumerate": {"register": true}
     },
     "post_connect": {
         "tinkerforge/request/ip_connection/enumerate": ""
     }
 }

This will register the connected and enumerate callbacks before connecting and
immediately trigger an enumeration when connected.

Init files using the old syntax without pre/post_connect, will be executed after
the connection is established.

Topic prefix
^^^^^^^^^^^^

The bindings can be configured to use another global prefix for all topics
using the ``--global-topic-prefix`` parameter. The prefix can be used to disambiguate
between two or more binding instances connected to the same broker.
The prefix can be as long as needed, for example ``tf/instance/1/foo/bar``.

.. _mqtt_topic_suffixes:

Topic suffixes
^^^^^^^^^^^^^^

The bindings support arbitrary suffixes per topic. For example you can tag all messages
of devices located in the same room with a room number::

  mosquitto_pub -t tinkerforge/register/rgb_led_button_bricklet/Enx/button_state_changed/room/1 -m 'true'
  mosquitto_pub -t tinkerforge/register/rgb_led_button_bricklet/gBs/button_state_changed/room/2 -m 'true'
  mosquitto_pub -t tinkerforge/register/rgb_led_button_bricklet/Dod/button_state_changed/room/1 -m 'true'

To receive all callbacks sent from devices in room 1 subscribe to::

  mosquitto_sub -t tinkerforge/callback/+/+/+/room/1

This subscription will receive callback events generated by ``Enx`` and ``Dod`` but not ``gBs``.

To receive all messages subscribe to::

  mosquitto_sub -t tinkerforge/callback/#
  mosquitto_sub -t tinkerforge/response/#

Start up and shut down
----------------------

The bindings will publish a message to ``tinkerforge/callback/bindings/restart``
with ``null`` as payload directly after connecting to the MQTT broker.
This message can be used as a signal that the bindings where restarted. You then
need to re-register all required callbacks.

If the bindings are shutting down normally, they will publish a ``null`` message
to ``tinkerforge/callback/bindings/shutdown`` before disconnecting from the MQTT broker.

If the connection between the bindings and the broker is lost unexpectedly, a
``null`` message is published to ``tinkerforge/callback/bindings/last_will``
using MQTT's last will mechanism.

Note that these messages are sent before the the connection to the Brick Daemon,
WIFI or Ethernet Extension is established respectively after this connection is
disconnected. If you want to react to changes to the state of this connection,
it is recommended to use the callbacks of the :ref:`IP connection <ip_connection_mqtt>`.

Command line arguments
----------------------

* ``-h``, ``--help`` show this help message and exit
* ``-v``, ``--version`` show version and exit
* ``--cmdline-file <CMDLINE_FILE>`` file from where to load command line options
* ``--ipcon-host <IPCON_HOST>`` hostname or IP address of Brick Daemon, WIFI or Ethernet Extension (default: localhost)
* ``--ipcon-port <IPCON_PORT>`` port number of Brick Daemon, WIFI or Ethernet Extension (default: 4223)
* ``--ipcon-auth-secret <IPCON_AUTH_SECRET>`` authentication secret of Brick Daemon, WIFI or Ethernet Extension
* ``--ipcon-timeout <IPCON_TIMEOUT>`` timeout in milliseconds for communication with Brick Daemon, WIFI or Ethernet Extension (default: 2500)
* ``--broker-host <BROKER_HOST>`` hostname or IP address of MQTT broker (default: localhost)
* ``--broker-port <BROKER_PORT>`` port number of MQTT broker (default: 1883)
* ``--broker-username <BROKER_USERNAME>`` username for the MQTT broker connection
* ``--broker-password <BROKER_PASSWORD>`` password for the MQTT broker connection
* ``--broker-certificate <BROKER_CERTIFICATE>`` Certificate Authority certificate file used for SSL/TLS connections to the broker
* ``--broker-tls-secure`` verify the server hostname in the server certificate for the MQTT broker connection (enabled by default)
* ``--broker-tls-insecure`` do not verify the server hostname in the server certificate for the MQTT broker connection
* ``--global-topic-prefix <GLOBAL_TOPIC_PREFIX>`` global MQTT topic prefix (default: tinkerforge/)
* ``--debug`` show debug output
* ``--no-debug`` hide debug output (enabled by default)
* ``--symbolic-response`` translate constant values into string constants for responses (enabled by default)
* ``--no-symbolic-response`` do not translate constants values for responses
* ``--int64-string-response`` translate [u]int64 values into strings for responses
* ``--no-int64-string-response`` do not translate [u]int64 values into strings for responses (enabled by default)
* ``--show-payload`` show received payload if JSON parsing fails
* ``--hide-payload`` hide received payload if JSON parsing fails (enabled by default)
* ``--init-file <INIT_FILE>`` file from where to load initial messages to process
* ``--no-init-file`` do not process initial messages (enabled by default)

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
