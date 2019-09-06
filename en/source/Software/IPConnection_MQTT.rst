
.. |ref_api_bindings| replace:: :ref:`MQTT API bindings <api_bindings_mqtt>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_mqtt_install>`
.. |bindings_name| replace:: MQTT

.. _ipcon_mqtt:

MQTT - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_mqtt_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.txt) <https://raw.githubusercontent.com/Tinkerforge/generators/master/mqtt/example-enumerate.txt>`__

.. literalinclude:: IPConnection_MQTT_example-enumerate.txt
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.txt) <https://raw.githubusercontent.com/Tinkerforge/generators/master/mqtt/example-authenticate.txt>`__

.. literalinclude:: IPConnection_MQTT_example-authenticate.txt
 :linenos:
 :tab-width: 4


.. _ipcon_mqtt_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. mqtt:function:: request/ip_connection/enumerate

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.

.. mqtt:function:: request/ip_connection/get_connection_state

 :response connection_state: int (has symbols)

 Can return the following states:
 
 * "disconnected" = 0: No connection is established.
 * "connected" = 1: A connection to the Brick Daemon or the WIFI/Ethernet Extension is established.
 * "pending" = 2: IP Connection is currently trying to connect.
 
Callbacks
^^^^^^^^^


Callbacks can be registered to receive
time critical or recurring data from the device. The registration is done
with the corresponding `.../register/...` topic and an optional suffix.
This suffix can be used to deregister the callback later.

.. note::
 Using callbacks for recurring events is *always* preferred
 compared to using getters. It will use less USB bandwidth and the latency
 will be a lot better, since there is no round trip time.


.. mqtt:function:: register/ip_connection/enumerate

 :register register: bool
 :response uid: string
 :response connected_uid: string
 :response position: string
 :response hardware_version: [int,int,int]
 :response firmware_version: [int,int,int]
 :response device_identifier: int (has symbols)
 :response enumeration_type: int (has symbols)
 :response _display_name: string

 A callback can be registered for this event by publishing to the ``.../register/ip_connection/enumerate[/SUFFIX]`` topic with the payload "true".
 An added callback can be removed by publishing to the same topic with the payload "false".
 To support multiple (de)registrations, e.g. for message filtering, an optional suffix can be used.

 If the callback is triggered, a message with it's payload is published under the corresponding ``.../callback/ip_connection/enumerate[/SUFFIX]`` topic for each registered suffix.
 
 The callback receives an JSON object with eight members:

 * ``uid``: The UID of the device.
 * ``connected_uid``: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position``: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'h' (position on Brick) or 'i' (position of the Raspberry Pi (Zero) HAT)
   or 'z' (Bricklet on :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``hardware_version``: Major, minor and release number for hardware version.
 * ``firmware_version``: Major, minor and release number for firmware version.
 * ``device_identifier``: A number that represents the device. If symbolic output is not disabled,
   the device identifier is mapped to the corresponding name in the format used in topics.
 * ``enumeration_type``: Type of enumeration.
 * ``_display_name``: The name of the device in a human readable form.

 The following symbols are available for this function:
 
 for device_identifier: see :ref:`here <device_identifier>`.
 
 for enumeration_type:

 * "available" = 0: Device is available
   (enumeration triggered by user: :mqtt:func:`enumerate <request/ip_connection/enumerate>`).
   This enumeration type can occur multiple times for the same device.
 * "connected" = 1: Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * "disconnected" = 2: Device is disconnected
   (only possible for USB connection). In this case only ``uid`` and
   ``enumeration_type`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

.. mqtt:function:: register/ip_connection/connected

 :register register: bool
 :response connect_reason: int (has symbols)

 A callback can be registered for this event by publishing to the ``.../register/ip_connection/connected[/SUFFIX]`` topic with the payload "true".
 An added callback can be removed by publishing to the same topic with the payload "false".
 To support multiple (de)registrations, e.g. for message filtering, an optional suffix can be used.

 If the callback is triggered, a message with it's payload is published under the corresponding ``.../callback/ip_connection/connected[/SUFFIX]`` topic for each registered suffix.
  
 This event is triggered whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension.
 
 The following symbols are available for this function:
 
 for connect_reason:

 * "request" = 0: Connection established after request from user.
 * "auto-reconnect" = 1: Connection after auto-reconnect.


.. mqtt:function:: register/ip_connection/disconnected

 :register register: bool
 :response disconnect_reason: int (has symbols)

 A callback can be registered for this event by publishing to the ``.../register/ip_connection/disconnected[/SUFFIX]`` topic with the payload "true".
 An added callback can be removed by publishing to the same topic with the payload "false".
 To support multiple (de)registrations, e.g. for message filtering, an optional suffix can be used.

 If the callback is triggered, a message with it's payload is published under the corresponding ``.../callback/ip_connection/disconnected[/SUFFIX]`` topic for each registered suffix.
 
 This event is triggered whenever the IP Connection got disconnected from a
 Brick Daemon or to a WIFI/Ethernet Extension.
 
 The following symbols are available for this function:
 
 for disconnect_reason:

 * "request" = 0: Disconnect was requested by user.
 * "error" = 1: Disconnect because of an unresolvable error.
 * "shutdown" = 2: Disconnect initiated by Brick Daemon or WIFI/Ethernet Extension.
