.. _ipcon_php:

PHP - IP Connection
===================

This is the API description for the PHP bindings of the IP Connection.
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP Connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.


.. _ipcon_php_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.php>`__

.. literalinclude:: Example.php
 :language: php
 :linenos:
 :tab-width: 4


.. _ipcon_php_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. php:function:: class IPConnection()

 Creates an IP Connection object. The constructed object is needed for the
 constructor of Bricks and Bricklets.


.. php:function:: void IPConnection::connect(string $host, int $port)

 Creates a TCP/IP connection to the given host and port.
 The host and port can point to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an Exception
 if there is no Brick Daemon or WIFI/Ethernet Extension
 listening at the given host and port.


.. php:function:: void IPConnection::disconnect()

 Disconnects the TCP/IP connection to the Brick Daemon or to
 the WIFI/Ethernet Extension.


.. php:function:: int IPConnection::getConnectionState()

 Can return the following states:

 * CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * CONNECTION_STATE_CONNECTED (1): A connection to the Brickd Daemon or the
   WIFI/Ethernet Extension  is established.


.. php:function:: void IPConnection::setTimeout(int $seconds)

 Sets the timeout (in ms) for getters and for setters for which
 "response expected" is activated.

 Default timeout is 2500ms.


.. php:function:: int IPConnection::getTimeout()

 Returns the timeout as set by :php:func:`setTimeout <IPConnection::setTimeout>`.


.. php:function:: void IPConnection::enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. php:function:: void IPConnection::registerCallback(int $id, callable $callback, mixed $userData = NULL)

 Registers a callback for a given ID.

 The available IDs with corresponding callback function signatures
 are described below.


Callbacks
^^^^^^^^^

.. php:member:: int IPConnection::CALLBACK_ENUMERATE

 .. code-block:: php

  void callback(string $uid, string $connectedUid, char $position, array $hardwareVersion, array $firmwareVersion, int $deviceIdentifier, int $enumerationType, mixed $userData = NULL)

 The callback receives seven parameters:

 * *uid*: The UID of the device.
 * *connectedUid*: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "1". With this information it is possible to
   reconstruct the complete network topology.
 * *position*: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * *hardwareVersion*: Major, minor and release number for hardware version.
 * *firmwareVersion*: Major, minor and release number for firmware version.
 * *deviceIdentifier*: A number that represents the device, instead of the
   name of the device (easier to parse).
 * *enumerationType*: Type of enumeration.

 Possible enumeration types are:

 * ENUMERATION_TYPE_AVAILABLE (0): Device is available (enumeration triggered
   by user).
 * ENUMERATION_TYPE_CONNECTED (1): Device is newly connected (automatically
   send by Brick after establishing a communication connection). This indicates
   that the device has potentially lost its previous configuration and needs
   to be reconfigured.
 * ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected (only
   possible for USB connection). In this case only *uid* and *enumerationType*
   are vaild.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).


.. php:member:: int IPConnection::CALLBACK_CONNECTED

 .. code-block:: php

  void callback(int $connectReason)

 This callback is called whenever the IP connection is connected, possible
 reasons are:

 * CONNECT_REASON_REQUEST (0): Connection established after request from user.


.. php:member:: int IPConnection::CALLBACK_DISCONNECTED

 .. code-block:: php

  void callback(int $connectReason)

 This callback is called whenever the IP connection is disconnected, possible
 reasons are:

 * DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * DISCONNECT_REASON_ERROR (1): Disconnect because of an unresolvable error.
 * DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by brickd or
   WIFI/Ethernet Extension.
