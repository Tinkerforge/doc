
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / PHP - IP Connection

.. |ref_api_bindings| replace:: :ref:`PHP bindings <api_bindings_php>`

.. _ipcon_php:

PHP - IP Connection
===================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_php_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.php) <https://github.com/Tinkerforge/generators/raw/master/php/ExampleEnumerate.php>`__

.. literalinclude:: IPConnection_PHP_ExampleEnumerate.php
 :language: php
 :linenos:
 :tab-width: 4

Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.php) <https://github.com/Tinkerforge/generators/raw/master/php/ExampleAuthenticate.php>`__

.. literalinclude:: IPConnection_PHP_ExampleAuthenticate.php
 :language: php
 :linenos:
 :tab-width: 4


.. _ipcon_php_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. php:function:: class IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. php:function:: void IPConnection::connect(string $host, int $port)

 Creates a TCP/IP connection to the given ``$host`` and ``$port``. The host and
 port can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given
 host and port.


.. php:function:: void IPConnection::disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. php:function:: void IPConnection::authenticate(string $secret)

 Performs an authentication handshake with the connected Brick Daemon or
 WIFI/Ethernet Extension.
 If the handshake succeeds the connection switches from non-authenticated to
 authenticated state and communication can continue as normal. If the handshake
 fails then the connection gets closed. Authentication can fail if the wrong
 secret was used or if authentication is not enabled at all on the Brick Daemon
 or the WIFI/Ethernet Extension.

 See the :ref:`authentication tutorial <tutorial_authentication>` for more
 information.

 .. versionadded:: 2.1.0


.. php:function:: int IPConnection::getConnectionState()

 Can return the following states:

 * IPConnection::CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * IPConnection::CONNECTION_STATE_CONNECTED (1): A connection to the Brick
   Daemon or the WIFI/Ethernet Extension  is established.


.. php:function:: void IPConnection::setTimeout(float $seconds)

 Sets the timeout in seconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2.5.


.. php:function:: int IPConnection::getTimeout()

 Returns the timeout as set by :php:func:`setTimeout() <IPConnection::setTimeout>`.


.. php:function:: void IPConnection::enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. php:function:: void IPConnection::dispatchCallbacks(float $seconds)

 Dispatches incoming callbacks for the given amount of time in seconds (negative
 value means infinity). Because PHP doesn't support threads you need to call
 this method periodically to ensure that incoming callbacks are handled. If you
 don't use callbacks you don't need to call this method.

 The recommended dispatch time 0. This will just dispatch all pending
 callbacks without waiting for further callbacks.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. php:function:: void IPConnection::registerCallback(int $id, callable $callback, mixed $userData = NULL)

 Registers a callback with ID ``$id`` to the function ``$callback``.

 The available IDs with corresponding callback function signatures
 are described below.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done with the :php:func:`registerCallback() <IPConnection::registerCallback>`
function. The parameters consist of the callback ID, the callback function and
optional user data:

.. code-block:: php

    function my_callback($param)
    {
        echo $param . "\n";
    }

    $ipcon->registerCallback(IPConnection::CALLBACK_EXAMPLE, 'my_callback');

The available constants with corresponding callback function signatures are
described below.


.. php:member:: int IPConnection::CALLBACK_ENUMERATE

 .. code-block:: php

  void callback(string $uid, string $connectedUid, char $position, array $hardwareVersion, array $firmwareVersion, int $deviceIdentifier, int $enumerationType [, mixed $userData])

 The callback receives seven parameters:

 * ``$uid``: The UID of the device.
 * ``$connectedUid``: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``$position``: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * ``$hardwareVersion``: Major, minor and release number for hardware version.
 * ``$firmwareVersion``: Major, minor and release number for firmware version.
 * ``$deviceIdentifier``: A number that represents the device.
 * ``$enumerationType``: Type of enumeration.

 Possible enumeration types are:

 * IPConnection::ENUMERATION_TYPE_AVAILABLE (0): Device is available
   (enumeration triggered by user).
 * IPConnection::ENUMERATION_TYPE_CONNECTED (1): Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPConnection::ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected
   (only possible for USB connection). In this case only ``$uid`` and
   ``$enumerationType`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern::

  <device-class>::DEVICE_IDENTIFIER

 For example: :php:member:`BrickMaster::DEVICE_IDENTIFIER`
 or :php:member:`BrickletAmbientLight::DEVICE_IDENTIFIER`.


.. php:member:: int IPConnection::CALLBACK_CONNECTED

 .. code-block:: php

  void callback(int $connectReason [, mixed $userData])

 This callback is called whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection::CONNECT_REASON_REQUEST (0): Connection established after
   request from user.


.. php:member:: int IPConnection::CALLBACK_DISCONNECTED

 .. code-block:: php

  void callback(int $connectReason [, mixed $userData])

 This callback is called whenever the IP Connection got disconnected from a
 Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection::DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * IPConnection::DISCONNECT_REASON_ERROR (1): Disconnect because of an
   unresolvable error.
 * IPConnection::DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
