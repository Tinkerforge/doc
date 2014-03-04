
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Visual Basic .NET - IP Connection

.. |ref_api_bindings| replace:: :ref:`Visual Basic .NET bindings <api_bindings_vbnet>`

.. _ipcon_vbnet:

Visual Basic .NET - IP Connection
=================================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_vbnet_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.vb) <https://github.com/Tinkerforge/generators/raw/master/vbnet/ExampleEnumerate.vb>`__

.. literalinclude:: IPConnection_VBNET_ExampleEnumerate.vb
 :language: vbnet
 :linenos:
 :tab-width: 4


.. _ipcon_vbnet_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. vbnet:function:: Class IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. vbnet:function:: Sub IPConnection.Connect(ByVal host As String, ByVal port As Integer)

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given
 host and port.


.. vbnet:function:: Sub IPConnection.Disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. vbnet:function:: Function IPConnection.GetConnectionState() As Short

 Can return the following states:

 * IPConnection.CONNECTION_DISCONNECTED (0): No connection is established.
 * IPConnection.CONNECTION_CONNETED (1): A connection to the Brick Daemon or the
   WIFI/Ethernet Extension  is established.
 * IPConnection.CONNECTION_PENDING (2): IP Connection is currently trying to connect.


.. vbnet:function:: Sub IPConnection.SetAutoReconnect(ByVal autoReconnect As Boolean)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *true*.


.. vbnet:function:: Function IPConnection.GetAutoReconnect() As Boolean

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. vbnet:function:: Sub IPConnection.SetTimeout(ByVal timeout As Integer)

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. vbnet:function:: Function IPConnection.GetTimeout() As Integer

 Returns the timeout as set by :vbnet:func:`SetTimeout() <IPConnection.SetTimeout>`.


.. vbnet:function:: Sub IPConnection.Enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. vbnet:function:: Sub IPConnection.Wait()

 Stops the current thread until :vbnet:func:`Unwait() <IPConnection.Unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 ``Wait`` and ``Unwait`` act in the same way as ``Acquire`` and ``Release`` of a
 semaphore.


.. vbnet:function:: Sub IPConnection.Unwait()

 Unwaits the thread previously stopped by :vbnet:func:`Wait() <IPConnection.Wait>`

 ``Wait`` and ``Unwait`` act in the same way as ``Acquire`` and ``Release`` of a
 semaphore.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done by appending your callback handler to the corresponding event:

.. code-block:: vbnet

    Sub Callback(ByVal sender As IPConnection, ByVal value As Short)
        Console.WriteLine("Value: {0}", value)
    End Sub

    AddHandler ipcon.Example, AddressOf Callback

The available events are described below.


.. vbnet:function:: Event IPConnection.EnumerateCallback(ByVal sender As IPConnection, ByVal uid As String, ByVal connectedUid As String, ByVal position As Char, ByVal hardwareVersion() As Short, ByVal firmwareVersion() As Short, ByVal deviceIdentifier As Integer, ByVal enumerationType As Short)

 The Event receives seven parameters:

 * ``uid``: The UID of the device.
 * ``connectedUid``: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position``: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * ``hardwareVersion``: Major, minor and release number for hardware version.
 * ``firmwareVersion``: Major, minor and release number for firmware version.
 * ``deviceIdentifier``: A number that represents the device.
 * ``enumerationType``: Type of enumeration.

 Possible enumeration types are:

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Device is available
   (enumeration triggered by user).
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected
   (only possible for USB connection). In this case only ``uid`` and
   ``enumerationType`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern::

  <device-class>.DEVICE_IDENTIFIER

 For example: :vbnet:attr:`BrickMaster.DEVICE_IDENTIFIER`
 or :vbnet:attr:`BrickletAmbientLight.DEVICE_IDENTIFIER`.


.. vbnet:function:: Event IPConnection.Connected(ByVal sender As IPConnection, ByVal connectReason As Short)

 This event is triggered whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.CONNECT_REASON_REQUEST (0): Connection established after
   request from user.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Connection after
   auto-reconnect.


.. vbnet:function:: Event IPConnection.Disconnected(ByVal sender As IPConnection, ByVal disconnectReason As Short)

 This event is triggered whenever the IP Connection got disconnected from a
 Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Disconnect because of an
   unresolvable error.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
