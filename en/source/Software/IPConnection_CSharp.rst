.. _ipcon_csharp:

C# - IP Connection
==================

This is the API description for the C# bindings of the IP Connection.
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP Connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.


.. _ipcon_csharp_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.cs>`__

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

 Creates an IP Connection object. The constructed object is needed for the
 constructor of Bricks and Bricklets.

.. csharp:function:: public void IPConnection::Connect(String host, int port)

 Creates a TCP/IP connection to the given host and port.
 The host and port can point to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an IOException 
 if there is no Brick Daemon or WIFI/Ethernet Extension
 listening at the given host and port.

.. csharp:function:: public void IPConnection::Disconnect()

 Disconnects the TCP/IP connection to the Brick Daemon or to
 the WIFI/Ethernet Extension.

.. csharp:function:: public byte IPConnection::GetConnectionState()

 Can return the following states:

 * CONNECTION_DISCONNECTED (0): No connection is established.
 * CONNECTION_CONNETED (1): A connection to the Brickd Daemon or the WIFI/Ethernet Extension  is established.
 * CONNECTION_PENDING (2): IP Connection is currently trying to connect.

.. csharp:function:: public void IPConnection::SetAutoReconnect(boolean autoReconnect)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *true*.

.. csharp:function:: public boolean IPConnection::GetAutoReconnect()

 Returns *true* if auto-reconnect is enabled, *false* otherwise.

.. csharp:function:: public void IPConnection::SetTimeout(int timeout)

 Sets the timeout (in ms) for getters and for setters for which 
 "response expected" is activated.

 Default timeout is 2500ms.

.. csharp:function:: public int IPConnection::GetTimeout()

 Returns the timeout as set by :csharp:func:`SetTimeout <IPConnection::SetTimeout>`.


.. csharp:function:: public void IPConnection::Wait()

 Stops the current thread until :csharp:func:`Unwait <IPConnection::Unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a threads.

 Wait and unwait act in the same way as require and release of a semaphore.
 
 
.. csharp:function:: public void IPConnection::Unwait()

 Unwaits the thread previously stopped by :csharp:func:`Wait <IPConnection::Wait>`

 Wait and unwait act in the same way as require and release of a semaphore.


.. csharp:function:: public void IPConnection::Enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.



Callbacks
^^^^^^^^^

*Callbacks* can be registered to receive
time critical or recurring data from the device. The registration is done
by appending your Callback-Handler to the corresponding event:

.. code-block:: csharp
    
    void Callback(object sender, int value)
    {
        System.Console.WriteLine("Value: " + value);
    }

    device.ExampleCallback += Callback;

The available events are described below.


.. csharp:function:: public event IPConnection::EnumerateCallback(object sender, string UID, string connectedUID, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)

 The Event receives seven parameters:

 * *uid*: The UID of the device.
 * *connectedUID*: UID where the device is connected to. For a Bricklet this will be a UID of the Brick where it is connected to. For a Brick it will be the UID of the bottom Master Brick in the stack. For the bottom Master Brick in a Stack this will be "1". With this information it is possible to reconstruct the complete network topology. 
 * *position*: For Bricks: '0' - '8' (position in stack). For Bricklets: 'a' - 'd' (position on Brick).
 * *hardwareVersion*: Major, minor and release number for hardware version.
 * *firmwareVersion*: Major, minor and release number for firmware version.
 * *deviceIdentifier*: A number that represents the Brick, instead of the name of the Brick (easier to parse).
 * *enumerationType*: Type of enumeration.

 Possible enumeration types are:

 * ENUMERATION_TYPE_AVAILABLE (0): Device is available (enumeration triggered by user).
 * ENUMERATION_TYPE_CONNECTED (1): Device is newly connected (automatically send by Brick after establishing a communication connection). This indicates that the device has potentially lost its previous configuration and needs to be reconfigured.
 * ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected (only possible for USB connection).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).

.. csharp:function:: public event IPConnection::Connected(object sender, int reason)

 This event is called whenever the IP connection is connected, possible reasons are:

 * CONNECT_REASON_REQUEST (0): Connection established after request from user.
 * CONNECT_REASON_AUTO_RECONNECT (1): Connection after auto-reconnect.

.. csharp:function:: public event IPConnection::Disconnected(object sender, int reason)
 
 This event is called whenever the IP connection is disconnected, possible reasons are:

 * DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * DISCONNECT_REASON_ERROR (1): Disconnect because of an unresolvable error.
 * DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by brickd or WIFI/Ethernet Extension.
