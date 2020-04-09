
.. |ref_api_bindings| replace:: :ref:`Go API bindings <api_bindings_go>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_go_install>`
.. |bindings_name| replace:: Go

.. _ipcon_go:

Go - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_go_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.go) <https://raw.githubusercontent.com/Tinkerforge/generators/master/go/example_enumerate.go>`__

.. literalinclude:: IPConnection_Go_example_enumerate.go
 :language: go
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.go) <https://raw.githubusercontent.com/Tinkerforge/generators/master/go/example_authenticate.go>`__

.. literalinclude:: IPConnection_Go_example_authenticate.go
 :language: go
 :linenos:
 :tab-width: 4


.. _ipcon_go_api:

API
---

The IPConnection is defined in the package ``github.com/Tinkerforge/go-api-bindings/ipconnection``.

Basic Functions
^^^^^^^^^^^^^^^

.. go:function:: func ipconnection.NewIPConnection() (ipcon IPConnection)

 Creates an IP Connection instance that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.

.. go:function:: func (*IPConnection) Close()

 Destroys this IP Connection and stops it's internal goroutines.

.. go:function:: func (*IPConnection) Connect(addr string) (err error)

 Creates a TCP/IP connection to the given ``addr`` with the form "host:port", as described `here <https://golang.org/pkg/net/#Dial>`_ . The host and port can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.


.. go:function:: func (*IPConnection) Disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. go:function:: func (*IPConnection) Authenticate(secret string) (err error)

 Performs an authentication handshake with the connected Brick Daemon or
 WIFI/Ethernet Extension.
 If the handshake succeeds the connection switches from non-authenticated to
 authenticated state and communication can continue as normal. If the handshake
 fails then the connection gets closed. Authentication can fail if the wrong
 secret was used or if authentication is not enabled at all on the Brick Daemon
 or the WIFI/Ethernet Extension.

 See the :ref:`authentication tutorial <tutorial_authentication>` for more
 information.


.. go:function:: func (*IPConnection) GetConnectionState() (state ConnectionState)

 Can return the following states:

 * ipconnection.\ **ConnectionState**\ Disconnected = 0: No connection is established.
 * ipconnection.\ **ConnectionState**\ Connected = 1: A connection to the Brick
   Daemon or the WIFI/Ethernet Extension is established.
 * ipconnection.\ **ConnectionState**\ Pending = 2: IP Connection is currently
   trying to connect.


.. go:function:: func (*IPConnection) SetAutoReconnect(autoReconnectEnabled bool)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 address, if the currently existing connection is lost.
 Therefore, auto-reconnect only does something after a successful
 :go:func:`Connect() <(*IPConnection) Connect>` call.

 Default value is *true*.


.. go:function:: func (*IPConnection) GetAutoReconnect() (autoReconnect bool)

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. go:function:: func (*IPConnection) SetTimeout(timeout time.Duration)

 Sets the timeout for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500 ms.


.. go:function:: func (*IPConnection) GetTimeout() (timeout time.Duration)

 Returns the timeout as set by :go:func:`SetTimeout() <(*IPConnection) SetTimeout>`.


.. go:function:: func (*IPConnection) Enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events.  The registration is
done with ``Register*Callback()`` functions of the IPConnection object. For example:

.. code-block:: go

    registrationId := ipcon.RegisterExampleCallback(func(param type) {
        fmt.Println(param)
    });

The available events are described below.  It is possible to add several callbacks and
to remove them with the corresponding ``Deregister*Callback()`` function, which expects a
registration ID returned by ``Register*Callback()``.


.. go:function:: func (*IPConnection) RegisterEnumerateCallback(func(uid string, connectedUid string, position rune, hardwareVersion [3]uint8, firmwareVersion [3]uint8, deviceIdentifier uint16, enumerationType EnumerationType)) (registrationId uint64)

 The callback receives seven parameters:

 * ``uid``: The UID of the device.
 * ``connectedUid``: UID where the device is connected to. For a Bricklet this
   is the UID of the Brick or Bricklet it is connected to. For a Brick it is
   the UID of the bottommost Brick in the stack. For the bottommost Brick
   in a stack it is "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position``: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'h' (position on Brick) or 'i' (position of the Raspberry Pi (Zero) HAT)
   or 'z' (Bricklet on :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``hardwareVersion``: Major, minor and release number for hardware version.
 * ``firmwareVersion``: Major, minor and release number for firmware version.
 * ``deviceIdentifier``: A number that represents the device.
 * ``enumerationType``: Type of enumeration.

 Possible enumeration types are:

 * ipconnection.\ **EnumerationType**\ Available = 0: Device is available
   (enumeration triggered by user: :go:func:`Enumerate()
   <(*IPConnection) Enumerate>`). This enumeration type can occur multiple times
   for the same device.
 * ipconnection.\ **EnumerationType**\ Connected = 1: Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * ipconnection.\ **EnumerationType**\ Disconnected = 2: Device is disconnected
   (only possible for USB connection). In this case only ``UID`` and
   ``EnumerationType`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern::

  <device-package>.DeviceIdentifier

 For example: :go:const:`master_brick.DeviceIdentifier`
 or :go:const:`ambient_light_bricklet.DeviceIdentifier`.


.. go:function:: func (*IPConnection) RegisterConnectCallback(func(reason ConnectReason)) (registrationId uint64)

 This event is triggered whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * ipconnection.\ **ConnectReason**\ Request = 0: Connection established after request from user.
 * ipconnection.\ **ConnectReason**\ AutoReconnect = 1: Connection after auto-reconnect.


.. go:function:: func (*IPConnection) RegisterDisconnectCallback(func(reason DisconnectReason)) (registrationId uint64)

 This event is triggered whenever the IP Connection got disconnected from a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * ipconnection.\ **DisconnectReason**\ Request = 0: Disconnect was requested by user.
 * ipconnection.\ **DisconnectReason**\ Error = 1: Disconnect because of an
   unresolvable error.
 * ipconnection.\ **DisconnectReason**\ Shutdown = 2: Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
