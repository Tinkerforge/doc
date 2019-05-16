
.. |ref_api_bindings| replace:: :ref:`LabVIEW API bindings <api_bindings_labview>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_labview_install>`
.. |bindings_name| replace:: LabVIEW

.. _ipcon_labview:

LabVIEW - IP Connection
=======================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_labview_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (Example Enumerate.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Enumerate.vi>`__,
`Download (Example Enumerate - EnumerateCallback Callback.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Enumerate%20-%20EnumerateCallback%20Callback.vi>`__

.. raw:: html

   <div class="horizontal-image-scroll">

.. image:: /Images/Screenshots/LabVIEW/IPConnection_LabVIEW_Example_Enumerate.vi.png
   :scale: 100 %
   :alt: LabVIEW Enumerate Example
   :align: center

.. raw:: html

   </div>


Authenticate
^^^^^^^^^^^^

`Download (Example Authenticate.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Authenticate.vi>`__,
`Download (Example Authenticate - Connected Callback.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Authenticate%20-%20Connected%20Callback.vi>`__
`Download (Example Authenticate - EnumerateCallback Callback.vi) <https://github.com/Tinkerforge/generators/raw/master/labview/Example%20Authenticate%20-%20EnumerateCallback%20Callback.vi>`__

.. raw:: html

   <div class="horizontal-image-scroll">

.. image:: /Images/Screenshots/LabVIEW/IPConnection_LabVIEW_Example_Authenticate.vi.png
   :scale: 100 %
   :alt: LabVIEW Authenticate Example
   :align: center

.. raw:: html

   </div>


.. _ipcon_labview_api:

API
---

The namespace for the IPConnection is ``Tinkerforge.*``.

Basic Functions
^^^^^^^^^^^^^^^

.. labview:function:: IPConnection() -> ipcon

 :output ipcon: .NET Refnum (IPConnection)

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. labview:function:: IPConnection.Connect(host, port)

 :input host: String
 :input port: Int32

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. labview:function:: IPConnection.Disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. labview:function:: IPConnection.Authenticate(secret)

 :input secret: String

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


.. labview:function:: IPConnection.GetConnectionState() -> connectionState

 :output connectionState: Byte

 Can return the following states:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): A connection to the Brick
   Daemon or the WIFI/Ethernet Extension  is established.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection is currently
   trying to connect.


.. labview:function:: IPConnection.SetAutoReconnect(autoReconnect)

 :input autoReconnect: Boolean

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the currently existing connection is lost.
 Therefore, auto-reconnect only does something after a successful
 :labview:func:`Connect() <IPConnection.Connect>` call.

 Default value is *true*.


.. labview:function:: IPConnection.GetAutoReconnect() -> autoReconnect

 :output autoReconnect: Boolean

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. labview:function:: IPConnection.SetTimeout(timeout)

 :input timeout: Int32

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. labview:function:: IPConnection.GetTimeout() -> timeout

 :output timeout: Int32

 Returns the timeout as set by :labview:func:`SetTimeout() <IPConnection.SetTimeout>`.


.. labview:function:: IPConnection.Enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. labview:function:: IPConnection.Wait()

 Stops the current thread until :labview:func:`Unwait() <IPConnection.Unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 ``Wait`` and ``Unwait`` act in the same way as ``Acquire`` and ``Release`` of a
 semaphore.


.. labview:function:: IPConnection.Unwait()

 Unwaits the thread previously stopped by :labview:func:`Wait() <IPConnection.Wait>`

 ``Wait`` and ``Unwait`` act in the same way as ``Acquire`` and ``Release`` of a
 semaphore.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done by appending your callback handler to the corresponding event.
The available events are described below.


.. labview:function:: event IPConnection.EnumerateCallback(sender, uid, connectedUid, position, hardwareVersion, firmwareVersion, deviceIdentifier, enumerationType)

 :input sender: .NET Refnum (IPConnection)
 :input uid: String
 :input connectedUid: String
 :input position: Char
 :input hardwareVersion: Byte[3]
 :input firmwareVersion: Byte[3]
 :input deviceIdentifier: Int32
 :input enumerationType: Int16

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

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Device is available
   (enumeration triggered by user: :labview:func:`Enumerate()
   <IPConnection.Enumerate>`). This enumeration type can occur multiple times
   for the same device.
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

 For example: :labview:sym:`BrickMaster.DEVICE_IDENTIFIER <BrickMaster.DEVICE_IDENTIFIER>`
 or :labview:sym:`BrickletAmbientLight.DEVICE_IDENTIFIER <BrickletAmbientLight.DEVICE_IDENTIFIER>`.


.. labview:function:: event IPConnection.ConnectedCallback(sender, connectReason)

 :input sender: .NET Refnum (IPConnection)
 :input connectReason: Int16
 
 This event is triggered whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.CONNECT_REASON_REQUEST (0): Connection established after
   request from user.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Connection after
   auto-reconnect.


.. labview:function:: event IPConnection.DisconnectedCallback(sender, disconnectReason)

 :input sender: .NET Refnum (IPConnection)
 :input disconnectReason: Int16

 This event is triggered whenever the IP Connection got disconnected from a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Disconnect because of an
   unresolvable error.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
