
.. |ref_api_bindings| replace:: :ref:`Rust API bindings <api_bindings_rust>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_rust_install>`
.. |bindings_name| replace:: Rust

.. _ipcon_rust:

Rust - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_rust_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.rs) <https://raw.githubusercontent.com/Tinkerforge/generators/master/rust/example_enumerate.rs>`__

.. literalinclude:: IPConnection_Rust_example_enumerate.rs
 :language: rust
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.rs) <https://raw.githubusercontent.com/Tinkerforge/generators/master/rust/example_authenticate.rs>`__

.. literalinclude:: IPConnection_Rust_example_authenticate.rs
 :language: rust
 :linenos:
 :tab-width: 4


.. _ipcon_rust_api:

API
---

The IpConnection is defined in the module ``tinkerforge::ip_connection``.

Basic Functions
^^^^^^^^^^^^^^^

.. rust:function:: IpConnection::new() -> IpConnection

 Creates an IP Connection instance that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.

.. rust:function:: IpConnection::get_request_sender(&self) -> IpConnectionRequestSender
 
 The IP connection can not be shared with other threads. To still be able to use it's functionality in other threads, this method can create IP connection request senders. These offer the same functionality, but can be created, cloned, moved into other threads and destroyed at will, as the IP connection instance itself owns the connection.

.. rust:function:: IpConnection::connect<T: ToSocketAddrs>(&self, addr: T) -> Receiver<Result<(), ConnectError>>

 Creates a TCP/IP connection to the given ``addr``. ``addr`` has to implement `ToSocketAddrs <https://doc.rust-lang.org/std/net/trait.ToSocketAddrs.html>`_. For example you can use a tuple ``(host, port)`` where ``host`` is a string (either an ip address or a host name) and ``port`` is a ``u16``.
 The address can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Returns a receiver, which will receive either ``()`` or an ``ConnectError`` if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. rust:function:: IpConnection::disconnect(&self) -> Receiver<Result<(), DisconnectErrorNotConnected>>

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension. Returns a receiver, which will receive either ``()`` or an error if there is no connection to disconnect.


.. rust:function:: IpConnection::authenticate(&self, secret: &str) -> Result<ConvertingReceiver<()>, AuthenticateError>

 Performs an authentication handshake with the connected Brick Daemon or
 WIFI/Ethernet Extension.
 If the handshake succeeds the connection switches from non-authenticated to
 authenticated state and communication can continue as normal. If the handshake
 fails then the connection gets closed. Authentication can fail if the wrong
 secret was used or if authentication is not enabled at all on the Brick Daemon
 or the WIFI/Ethernet Extension.

 See the :ref:`authentication tutorial <tutorial_authentication>` for more
 information.


.. rust:function:: IpConnection::get_connection_state(&self) -> ConnectionState

 Can return the following states:

 * **ConnectionState**\ ::Disconnected = 0: No connection is established.
 * **ConnectionState**\ ::Connected = 1: A connection to the Brick
   Daemon or the WIFI/Ethernet Extension is established.
 * **ConnectionState**\ ::Pending = 2: IP Connection is currently
   trying to connect.


.. rust:function:: IpConnection::set_auto_reconnect(&mut self, auto_reconnect_enabled: bool)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 address, if the currently existing connection is lost.
 Therefore, auto-reconnect only does something after a successful
 :rust:func:`connect() <IpConnection::connect>` call.

 Default value is *true*.


.. rust:function:: IpConnection::get_auto_reconnect(&self) -> bool

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. rust:function:: IpConnection::set_timeout(&mut self, timeout: std::time::Duration)

 Sets the timeout for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500 ms.
 

.. rust:function:: IpConnection::get_timeout(&self) -> std::time::Duration

 Returns the timeout as set by :rust:func:`set_timeout() <IpConnection::set_timeout>`.


.. rust:function:: IpConnection::enumerate(&self)

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.

 
Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is done by creating a message receiver. Received messages can be handled asynchronously by spawning a new thread:

.. code-block:: rust

    let receiver = ipcon.get_example_callback_receiver();
    // No join is needed here, as the iteration over the receiver ends when the ipcon is dropped.
    thread::spawn(move || {
        for value in receiver {
            println!("Value: {:?}", value);
        }
    };

The available events are described below.


.. rust:function:: IpConnection::get_enumerate_callback_receiver(&self) -> ConvertingCallbackReceiver<EnumerateResponse>

 The event receives a struct with seven members:

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
 * ``device_identifier``: A number that represents the device.
 * ``enumeration_type``: Type of enumeration.

 Possible enumeration types are:

 * **EnumerationType**\ ::Available = 0: Device is available
   (enumeration triggered by user: :rust:func:`enumerate()
   <IpConnection::enumerate>`). This enumeration type can occur multiple times
   for the same device.
 * **EnumerationType**\ ::Connected = 1: Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * **EnumerationType**\ ::Disconnected = 2: Device is disconnected
   (only possible for USB connection). In this case only ``uid`` and
   ``enumeration_type`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern::

  <device-class>::DEVICE_IDENTIFIER

 For example: :rust:const:`MasterBrick::DEVICE_IDENTIFIER`
 or :rust:const:`AmbientLightBricklet::DEVICE_IDENTIFIER`.


.. rust:function:: IpConnection::get_connect_callback_receiver(&self) -> Receiver<ConnectReason>

 This event is triggered whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * **ConnectReason**\ ::Request = 0: Connection established after request from user.
 * **ConnectReason**\ ::AutoReconnect = 1: Connection after auto-reconnect.


.. rust:function:: IpConnection::get_disconnect_callback_receiver(&self) -> Receiver<DisconnectReason>

 This event is triggered whenever the IP Connection got disconnected from a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * **DisconnectReason**\ ::Request = 0: Disconnect was requested by user.
 * **DisconnectReason**\ ::Error = 1: Disconnect because of an unresolvable error.
 * **DisconnectReason**\ ::Shutdown = 2: Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
