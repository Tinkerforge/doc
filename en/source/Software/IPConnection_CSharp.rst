
.. |ref_api_bindings| replace:: :ref:`C# API bindings <api_bindings_csharp>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_csharp_install>`
.. |bindings_name| replace:: C#

.. _ipcon_csharp:

C# - IP Connection
==================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_csharp_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.cs) <https://github.com/Tinkerforge/generators/raw/master/csharp/ExampleEnumerate.cs>`__

.. literalinclude:: IPConnection_CSharp_ExampleEnumerate.cs
 :language: csharp
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.cs) <https://github.com/Tinkerforge/generators/raw/master/csharp/ExampleAuthenticate.cs>`__

.. literalinclude:: IPConnection_CSharp_ExampleAuthenticate.cs
 :language: csharp
 :linenos:
 :tab-width: 4


.. _ipcon_csharp_api:

API
---

The namespace for the IPConnection is ``Tinkerforge.*``.

Basic Functions
^^^^^^^^^^^^^^^

.. csharp:function:: class IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. csharp:function:: void IPConnection::Connect(String host, int port)

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. csharp:function:: void IPConnection::Disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. csharp:function:: void IPConnection::Authenticate(string secret)

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


.. csharp:function:: byte IPConnection::GetConnectionState()

 Can return the following states:

 * IPConnection.\ **CONNECTION_STATE**\ _DISCONNECTED = 0: No connection is established.
 * IPConnection.\ **CONNECTION_STATE**\ _CONNECTED = 1: A connection to the Brick
   Daemon or the WIFI/Ethernet Extension  is established.
 * IPConnection.\ **CONNECTION_STATE**\ _PENDING = 2: IP Connection is currently
   trying to connect.


.. csharp:function:: void IPConnection::SetAutoReconnect(bool autoReconnect)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the currently existing connection is lost.
 Therefore, auto-reconnect only does something after a successful
 :csharp:func:`Connect() <IPConnection::Connect>` call.

 Default value is *true*.


.. csharp:function:: bool IPConnection::GetAutoReconnect()

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. csharp:function:: void IPConnection::SetTimeout(int timeout)

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. csharp:function:: int IPConnection::GetTimeout()

 Returns the timeout as set by :csharp:func:`SetTimeout() <IPConnection::SetTimeout>`.


.. csharp:function:: void IPConnection::Enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. csharp:function:: void IPConnection::Wait()

 Stops the current thread until :csharp:func:`Unwait() <IPConnection::Unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 ``Wait`` and ``Unwait`` act in the same way as ``Acquire`` and ``Release`` of a
 semaphore.


.. csharp:function:: void IPConnection::Unwait()

 Unwaits the thread previously stopped by :csharp:func:`Wait() <IPConnection::Wait>`

 ``Wait`` and ``Unwait`` act in the same way as ``Acquire`` and ``Release`` of a
 semaphore.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done by appending your callback handler to the corresponding event:

.. code-block:: csharp

    void MyCallback(IPConnection sender, int value)
    {
        System.Console.WriteLine("Value: " + value);
    }

    ipcon.ExampleCallback += MyCallback;

The available events are described below.


.. csharp:function:: event IPConnection::EnumerateCallback(IPConnection sender, string uid, string connectedUid, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)

 The event receives seven parameters:

 * ``uid``: The UID of the device.
 * ``connectedUid``: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position``: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'h' (position on Brick) or 'i' (position of the Raspberry Pi (Zero) HAT)
   or 'z' (Bricklet on :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``hardwareVersion``: Major, minor and release number for hardware version.
 * ``firmwareVersion``: Major, minor and release number for firmware version.
 * ``deviceIdentifier``: A number that represents the device.
 * ``enumerationType``: Type of enumeration.

 Possible enumeration types are:

 * IPConnection.\ **ENUMERATION_TYPE**\ _AVAILABLE = 0: Device is available
   (enumeration triggered by user: :csharp:func:`Enumerate()
   <IPConnection::Enumerate>`). This enumeration type can occur multiple times
   for the same device.
 * IPConnection.\ **ENUMERATION_TYPE**\ _CONNECTED = 1: Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPConnection.\ **ENUMERATION_TYPE**\ _DISCONNECTED = 2: Device is disconnected
   (only possible for USB connection). In this case only ``uid`` and
   ``enumerationType`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern::

  <device-class>.DEVICE_IDENTIFIER

 For example: :csharp:member:`BrickMaster::DEVICE_IDENTIFIER`
 or :csharp:member:`BrickletAmbientLight::DEVICE_IDENTIFIER`.


.. csharp:function:: event IPConnection::ConnectedCallback(IPConnection sender, short connectReason)

 This event is triggered whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.\ **CONNECT_REASON**\ _REQUEST = 0: Connection established after
   request from user.
 * IPConnection.\ **CONNECT_REASON**\ _AUTO_RECONNECT = 1: Connection after
   auto-reconnect.


.. csharp:function:: event IPConnection::DisconnectedCallback(IPConnection sender, short disconnectReason)

 This event is triggered whenever the IP Connection got disconnected from a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.\ **DISCONNECT_REASON**\ _REQUEST = 0: Disconnect was requested by user.
 * IPConnection.\ **DISCONNECT_REASON**\ _ERROR = 1: Disconnect because of an
   unresolvable error.
 * IPConnection.\ **DISCONNECT_REASON**\ _SHUTDOWN = 2: Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
