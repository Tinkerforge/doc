
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / MATLAB - IP Connection

.. |ref_api_bindings| replace:: :ref:`MATLAB bindings <api_bindings_matlab>`

.. _ipcon_matlab:

MATLAB - IP Connection
======================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_matlab_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate (MATLAB)
^^^^^^^^^^^^^^^^^^

`Download (matlab_example_enumerate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/matlab_example_enumerate.m>`__

.. literalinclude:: IPConnection_MATLAB_matlab_example_enumerate.m
 :language: matlab
 :linenos:
 :tab-width: 4
 
Enumerate (Octave)
^^^^^^^^^^^^^^^^^^

`Download (octave_example_enumerate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/octave_example_enumerate.m>`__
 
 .. literalinclude:: IPConnection_MATLAB_octave_example_enumerate.m
 :language: matlab
 :linenos:
 :tab-width: 4


.. _ipcon_matlab_examples_authenticate:

Authenticate (MATLAB)
^^^^^^^^^^^^^^^^^^^^^

`Download (matlab_example_authenticate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/matlab_example_authenticate.m>`__

.. literalinclude:: IPConnection_MATLAB_matlab_example_authenticate.m
 :language: matlab
 :linenos:
 :tab-width: 4

Authenticate (Octave)
^^^^^^^^^^^^^^^^^^^^^

`Download (octave_example_authenticate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/octave_example_authenticate.m>`__

.. literalinclude:: IPConnection_MATLAB_octave_example_authenticate.m
 :language: matlab
 :linenos:
 :tab-width: 4

.. _ipcon_matlab_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. matlab:function:: class IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.
 
 In MATLAB,
 
 .. code-block:: matlab

  ipcon = new IPConnection();

 In Octave,

 .. code-block:: matlab

  ipcon = java_new("com.tinkerforge.IPConnection");

.. matlab:function:: public void IPConnection::connect(String host, int port)

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. matlab:function:: public void IPConnection::disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. matlab:function:: public void IPConnection::authenticate(String secret)

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


.. matlab:function:: public byte IPConnection::getConnectionState()

 Can return the following states:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * IPConnection.CONNECTION_STATE_CONNETED (1): A connection to the Brick Daemon
   or the WIFI/Ethernet Extension  is established.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection is currently trying
   to connect.


.. matlab:function:: public void IPConnection::setAutoReconnect(boolean autoReconnect)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *true*.


.. matlab:function:: public boolean IPConnection::getAutoReconnect()

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. matlab:function:: public void IPConnection::setTimeout(int timeout)

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. matlab:function:: public int IPConnection::getTimeout()

 Returns the timeout as set by :java:func:`setTimeout() <IPConnection::setTimeout>`.


.. matlab:function:: public void IPConnection::enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


Callbacks (MATLAB)
^^^^^^^^^^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done with "set" function of MATLAB.

For example:

.. code-block:: matlab

    set(ipcon, 'EnumerateCallback', @(h, e)cb_enumerate(e.uid, e.connectedUid, e.position,
                                                        e.hardwareVersion, e.firmwareVersion,
                                                        e.deviceIdentifier, e.enumerationType));

Callbacks can be registered by speciffying the callback in MATLAB set() function.

.. matlab:member:: public callback IPConnection.EnumerateCallback

 This callback is used to register an enumerate callback.

  The callback function receives seven parameters as members of the object "e" (event):

  * ``uid``: The UID of the device.
  * ``connectedUID``: UID where the device is connected to. For a Bricklet
    this will be a UID of the Brick where it is connected to. For a Brick it
    will be the UID of the bottom Master Brick in the stack. For the bottom
    Master Brick in a stack this will be "0". With this information it is
    possible to reconstruct the complete network topology.
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
  * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected (only
    possible for USB connection). In this case only ``uid`` and
    ``enumerationType`` are valid.

  It should be possible to implement plug-and-play functionality with this
  (as is done in Brick Viewer).

  The device identifier numbers can be found :ref:`here <device_identifier>`.
  There are also constants for these numbers named following this pattern::

   <device-class>.DEVICE_IDENTIFIER

  For example: :matlab:member:`BrickMaster.DEVICE_IDENTIFIER`
  or :matlab:member:`BrickletAmbientLight.DEVICE_IDENTIFIER`.


.. matlab:member:: public callback IPConnection.ConnectedCallback

 This callback can be used to register connected callback.

  This listener is called whenever the IP Connection got connected to a
  Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

  * IPConnection.CONNECT_REASON_REQUEST (0): Connection established after
    request from user.
  * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Connection after
    auto-reconnect.


.. matlab:member:: public callback IPConnection.DisconnectedCallback

 This callback can be used to register disconnected callback.

  This listener is called whenever the IP Connection got disconnected from a
  Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

  * IPConnection.DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
  * IPConnection.DISCONNECT_REASON_ERROR (1): Disconnect because of an
    unresolvable error.
  * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
    Daemon or WIFI/Ethernet Extension.
    
Callbacks (Octave)
^^^^^^^^^^^^^^^^^^

Listeners can be registered to be notified about events. The registration is
done with methods of the IPConnection class to register particular callbacks.

For example:

.. code-block:: matlab

    public void IPConnection.addEnumerateListener(String functionName);

 This will register function "functionName" which is defined in Octave as the
 callback function for enumerate callback.
 
 The registered functions will get the following parameters as the function arguments.

 .. py:function:: functionName(uid, connectedUid, position, hardwareVersion, firmwareVersion, deviceIdentifier, enumerationType)
  :noindex:

  :param uid: String
  :param connected_uid: String
  :param position: String
  :param hardware_version: [short, short, short]
  :param firmware_version: [short, short, short]
  :param device_identifier: int
  :param enumeration_type: short


.. matlab:function:: public void IPConnection.addConnectedListener(String functionName)

 This callback can be used to register connected callback.

  This listener is called whenever the IP Connection got connected to a
  Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

  * IPConnection.CONNECT_REASON_REQUEST (0): Connection established after
    request from user.
  * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Connection after
    auto-reconnect.


.. matlab:function:: public void IPConnection.addDisconnectedListener(String functionName)

 This callback can be used to register disconnected callback.

  This listener is called whenever the IP Connection got disconnected from a
  Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

  * IPConnection.DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
  * IPConnection.DISCONNECT_REASON_ERROR (1): Disconnect because of an
    unresolvable error.
  * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
    Daemon or WIFI/Ethernet Extension.
