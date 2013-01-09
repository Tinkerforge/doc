.. _ipcon_delphi:

Delphi - IP Connection
======================

This is the API description for the Delphi bindings of the IP Connection.
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP Connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.


.. _ipcon_delphi_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.rb>`__

.. literalinclude:: Example.pas
 :language: delphi
 :linenos:
 :tab-width: 4


.. _ipcon_delphi_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. delphi:function:: constructor TIPConnection.Create()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. delphi:function:: destructor TIPConnection.Destroy()

 Destroys the IP Connection object. The connection to the Brick Daemon gets
 closed and the threads of the IP Connection are terminated.


.. delphi:function:: procedure TIPConnection.Connect(const host: string; const port: word)

 Creates a TCP/IP connection to the given *host* and *port*. The host and port
 can point to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given
 host and port.


.. delphi:function:: procedure TIPConnection.Disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. delphi:function:: procedure TIPConnection.GetConnectionState()

 Can return the following states:

 * CONNECTION_DISCONNECTED (0): No connection is established.
 * CONNECTION_CONNETED (1): A connection to the Brick Daemon or the
   WIFI/Ethernet Extension  is established.
 * CONNECTION_PENDING (2): IP Connection is currently trying to connect.


.. delphi:function:: procedure TIPConnection.SetAutoReconnect(const autoReconnect: boolean)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *true*.


.. delphi:function:: function TIPConnection.GetAutoReconnect(): boolean

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. delphi:function:: procedure TIPConnection.SetTimeout(const timeout: longword)

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. delphi:function:: function TIPConnection.GetTimeout(): longword

 Returns the timeout as set by :delphi:func:`SetTimeout <TIPConnection.SetTimeout>`.


.. delphi:function:: procedure TIPConnection.Enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. delphi:function:: procedure IPConnection.Wait()

 Stops the current thread until :delphi:func:`Unwait <TIPConnection.Unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 Wait and unwait act in the same way as "acquire" and "release" of a semaphore.


.. delphi:function:: procedure TIPConnection.Unwait()

 Unwaits the thread previously stopped by :delphi:func:`Wait <TIPConnection.Wait>`

 Wait and unwait act in the same way as "acquire" and "release" of a semaphore.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done by assigning a procedure to an callback property of the TIPConnection
object:

.. code-block:: delphi

    procedure TExample.MyCallback(sender: TIPConnection; const param: word);
    begin
      WriteLn(param);
    end;

    ipcon.OnExample := {$ifdef FPC}@{$endif}example.MyCallback;

The available callback property and their type of parameters are described below.


.. delphi:function:: property TIPConnection.OnEnumerate

 .. code-block:: delphi

  procedure(sender: TIPConnection; const uid: string; const connectedUid: string; const position: char; const hardwareVersion: TVersionNumber; const firmwareVersion: TVersionNumber; const deviceIdentifier: word; const enumerationType: byte) of object;

 The callback has seven parameters:

 * *uid*: The UID of the device.
 * *connectedUID*: UID where the device is connected to. For a Bricklet this
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
 * ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected (only possible
   for USB connection). In this case only *uid* and *enumerationType*
   are vaild.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

.. delphi:function:: property TIPConnection.OnEnumerate

 .. code-block:: delphi

  procedure(sender: TIPConnection; const connectReason: byte) of object;

 This callback is called whenever the IP Connection is connected,
 possible reasons are:

 * CONNECT_REASON_REQUEST (0): Connection established after request from user.
 * CONNECT_REASON_AUTO_RECONNECT (1): Connection after auto-reconnect.

.. delphi:function:: property TIPConnection.OnEnumerate

 .. code-block:: delphi

  procedure(sender: TIPConnection; const disconnectReason: byte) of object;

 This callback is called whenever the IP Connection is disconnected,
 possible reasons are:

 * DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * DISCONNECT_REASON_ERROR (1): Disconnect because of an unresolvable error.
 * DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick Daemon or
   WIFI/Ethernet Extension.
