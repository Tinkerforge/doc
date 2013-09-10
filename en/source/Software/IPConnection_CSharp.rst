
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C# - IP Connection

.. |ref_api_bindings| replace:: :ref:`C# bindings <api_bindings_csharp>`

.. _ipcon_csharp:

C# - IP Connection
==================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_csharp_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/en/source/Software/Example.cs>`__

.. literalinclude:: Example.cs
 :language: csharp
 :linenos:
 :tab-width: 4


.. _ipcon_csharp_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. csharp:function:: class IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. csharp:function:: public void IPConnection::Connect(String host, int port)

 Creates a TCP/IP connection to the given *host* and *port*. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. csharp:function:: public void IPConnection::Disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. csharp:function:: public byte IPConnection::GetConnectionState()

 Can return the following states:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): A connection to the Brick
   Daemon or the WIFI/Ethernet Extension  is established.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection is currently
   trying to connect.


.. csharp:function:: public void IPConnection::SetAutoReconnect(boolean autoReconnect)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *true*.


.. csharp:function:: public boolean IPConnection::GetAutoReconnect()

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. csharp:function:: public void IPConnection::SetTimeout(int timeout)

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. csharp:function:: public int IPConnection::GetTimeout()

 Returns the timeout as set by :csharp:func:`SetTimeout() <IPConnection::SetTimeout>`.


.. csharp:function:: public void IPConnection::Enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. csharp:function:: public void IPConnection::Wait()

 Stops the current thread until :csharp:func:`Unwait() <IPConnection::Unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 ``Wait`` and ``Unwait`` act in the same way as "acquire" and "release" of a
 semaphore.


.. csharp:function:: public void IPConnection::Unwait()

 Unwaits the thread previously stopped by :csharp:func:`Wait() <IPConnection::Wait>`

 ``Wait`` and ``Unwait`` act in the same way as "acquire" and "release" of a
 semaphore.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done by appending your callback handler to the corresponding event:

.. code-block:: csharp

    void Callback(IPConnection sender, int value)
    {
        System.Console.WriteLine("Value: " + value);
    }

    ipcon.ExampleCallback += Callback;

The available events are described below.


.. csharp:function:: public event IPConnection::EnumerateCallback(IPConnection sender, string uid, string connectedUid, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)

 The Event receives seven parameters:

 * *uid*: The UID of the device.
 * *connectedUid*: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * *position*: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * *hardwareVersion*: Major, minor and release number for hardware version.
 * *firmwareVersion*: Major, minor and release number for firmware version.
 * *deviceIdentifier*: A number that represents the device.
 * *enumerationType*: Type of enumeration.

 Possible enumeration types are:

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Device is available
   (enumeration triggered by user).
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected
   (only possible for USB connection). In this case only *uid* and
   *enumerationType* are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifiers can be found :ref:`here <device_identifier>`.


.. csharp:function:: public event IPConnection::Connected(IPConnection sender, short connectReason)

 This event is triggered whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.CONNECT_REASON_REQUEST (0): Connection established after
   request from user.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Connection after
   auto-reconnect.


.. csharp:function:: public event IPConnection::Disconnected(IPConnection sender, short disconnectReason)

 This event is triggered whenever the IP Connection got disconnected from a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Disconnect because of an
   unresolvable error.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
