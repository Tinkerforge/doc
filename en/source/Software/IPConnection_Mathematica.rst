
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-mathematica">Software</a> / Mathematica - IP Connection

.. |ref_api_bindings| replace:: :ref:`Mathematica bindings <api_bindings_mathematica>`

.. _ipcon_mathematica:

Mathematica - IP Connection
===========================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_mathematica_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.nb) <https://github.com/Tinkerforge/generators/raw/master/mathematica/ExampleEnumerate.nb>`__

.. literalinclude:: IPConnection_Mathematica_ExampleEnumerate.nb.txt
 :language: mathematica
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.nb) <https://github.com/Tinkerforge/generators/raw/master/mathematica/ExampleAuthenticate.nb>`__

.. literalinclude:: IPConnection_Mathematica_ExampleAuthenticate.nb.txt
 :language: mathematica
 :linenos:
 :tab-width: 4


.. _ipcon_mathematica_api:

API
---

The namespace for the IPConnection is ``Tinkerforge.*``.

Basic Functions
^^^^^^^^^^^^^^^

.. mathematica:function:: IPConnection[] -> ipcon

 :ret ipcon: NETObject[IPConnection]

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.

 .. code-block:: mathematica

    ipcon=NETNew["Tinkerforge.IPConnection"]

 The .NET runtime has built-in garbage collection that frees objects that are
 no longer in use by a program. But because Mathematica can not automatically
 tell when a Mathematica "program" doesn't use a .NET object anymore, this has
 to be done by the program. For this the `ReleaseNETObject[]
 <http://reference.wolfram.com/mathematica/NETLink/ref/ReleaseNETObject.html>`__
 function is used in the examples.

 For further information about object management in .NET/Link see the
 corresponding Mathematica `.NET/Link documentation
 <http://reference.wolfram.com/mathematica/NETLink/tutorial/CallingNETFromMathematica.html#14400>`__.


.. mathematica:function:: IPConnection@Connect[host, port] -> Null

 :param host: String
 :param port: Integer

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. mathematica:function:: IPConnection@Disconnect[] -> Null

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. mathematica:function:: IPConnection@Authenticate[secret] -> Null

 :param secret: String

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


.. mathematica:function:: IPConnection@GetConnectionState[] -> connectionState

 :ret connectionState: Integer

 Can return the following states:

 * IPConnection`CONNECTIONUSTATEUDISCONNECTED (0): No connection is established.
 * IPConnection`CONNECTIONUSTATEUCONNECTED (1): A connection to the Brick
   Daemon or the WIFI/Ethernet Extension  is established.
 * IPConnection`CONNECTIONUSTATEUPENDING (2): IP Connection is currently
   trying to connect.


.. mathematica:function:: IPConnection@SetAutoReconnect[autoReconnect] -> Null

 :param autoReconnect: True/False

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *True*.


.. mathematica:function:: IPConnection@GetAutoReconnect[] -> autoReconnect

 :ret autoReconnect: True/False

 Returns *True* if auto-reconnect is enabled, *False* otherwise.


.. mathematica:function:: IPConnection@SetTimeout[timeout] -> Null

 :param timeout: Integer

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. mathematica:function:: IPConnection@GetTimeout[] -> timeout

 :param timeout: Integer

 Returns the timeout as set by :mathematica:func:`SetTimeout[] <IPConnection@SetTimeout>`.


.. mathematica:function:: IPConnection@Enumerate[] -> Null

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. mathematica:function:: IPConnection@Wait[] -> Null

 Stops the current thread until :mathematica:func:`Unwait[] <IPConnection@Unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 ``Wait`` and ``Unwait`` act in the same way as ``Acquire`` and ``Release`` of a
 semaphore.


.. mathematica:function:: IPConnection@Unwait[] -> Null

 Unwaits the thread previously stopped by :mathematica:func:`Wait[] <IPConnection@Wait>`

 ``Wait`` and ``Unwait`` act in the same way as ``Acquire`` and ``Release`` of a
 semaphore.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done by appending your callback handler to the corresponding event:

.. code-block:: mathematica

    Callback[sender_,value_]:=Print["Value: "<>ToString[value]]

    AddEventHandler[ipcon@Example,Callback]

For further information about event handling using .NET/Link see the
corresponding Mathematica `.NET/Link documentation
<http://reference.wolfram.com/mathematica/NETLink/tutorial/CallingNETFromMathematica.html#17034>`__.

The available events are described below.


.. mathematica:function:: event IPConnection@EnumerateCallback[sender, uid, connectedUid, position, {hardwareVersion1, hardwareVersion2, hardwareVersion3}, {firmwareVersion1, firmwareVersion2, firmwareVersion3}, deviceIdentifier, enumerationType]

 :param sender: NETObject[IPConnection]
 :param uid: String
 :param connectedUid: String
 :param position: Integer
 :param hardwareVersioni: Integer
 :param firmwareVersioni: Integer
 :param deviceIdentifier: Integer
 :param enumerationType: Integer

 The event receives seven parameters:

 * ``uid``: The UID of the device.
 * ``connectedUid``: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position``: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * ``hardwareVersioni``: Major, minor and release number for hardware version.
 * ``firmwareVersioni``: Major, minor and release number for firmware version.
 * ``deviceIdentifier``: A number that represents the device.
 * ``enumerationType``: Type of enumeration.

 Possible enumeration types are:

 * IPConnection`ENUMERATIONUTYPEUAVAILABLE (0): Device is available
   (enumeration triggered by user).
 * IPConnection`ENUMERATIONUTYPEUCONNECTED (1): Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPConnection`ENUMERATIONUTYPEUDISCONNECTED (2): Device is disconnected
   (only possible for USB connection). In this case only ``uid`` and
   ``enumerationType`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern::

  <device-class>`DEVICEUIDENTIFIER

 For example: :mathematica:sym:`BrickMaster`DEVICEUIDENTIFIER <BrickMaster`DEVICEUIDENTIFIER>`
 or :mathematica:sym:`BrickletAmbientLight`DEVICEUIDENTIFIER <BrickletAmbientLight`DEVICEUIDENTIFIER>`.


.. mathematica:function:: event IPConnection@Connected[sender, connectReason]

 :param sender: NETObject[IPConnection]
 :param connectReason: Integer

 This event is triggered whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection`CONNECTUREASONUREQUEST (0): Connection established after
   request from user.
 * IPConnection`CONNECTUREASONUAUTOURECONNECT (1): Connection after
   auto-reconnect.


.. mathematica:function:: event IPConnection@Disconnected[sender, disconnectReason]

 :param sender: NETObject[IPConnection]
 :param disconnectReason: Integer

 This event is triggered whenever the IP Connection got disconnected from a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection`DISCONNECTUREASONUREQUEST (0): Disconnect was requested by user.
 * IPConnection`DISCONNECTUREASONUERROR (1): Disconnect because of an
   unresolvable error.
 * IPConnection`DISCONNECTUREASONUSHUTDOWN (2): Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
