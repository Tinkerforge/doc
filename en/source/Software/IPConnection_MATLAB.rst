
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / MATLAB/Octave - IP Connection

.. |ref_api_bindings| replace:: :ref:`MATLAB/Octave bindings <api_bindings_matlab>`

.. _ipcon_matlab:

MATLAB/Octave - IP Connection
=============================

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

Authenticate (MATLAB)
^^^^^^^^^^^^^^^^^^^^^

`Download (matlab_example_authenticate.m) <https://github.com/Tinkerforge/generators/raw/master/matlab/matlab_example_authenticate.m>`__

.. literalinclude:: IPConnection_MATLAB_matlab_example_authenticate.m
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

 In MATLAB:

 .. code-block:: matlab

  import com.tinkerforge.IPConnection;

  ipcon = IPConnection();

 In Octave:

 .. code-block:: octave

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


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done with "set" function of MATLAB. The parameters consist of the
IP Connection object, the callback name and the callback function. For example,
it looks like this in MATLAB:

.. code-block:: matlab

    function cb_example(e)
        fprintf('Parameter: %s\n', e.param);
    end

    set(ipcon, 'ExampleCallback', @(h, e) cb_example(e));

Due to a difference in the Octave Java support the "set" function cannot be
used in Octave. The registration is done with "add*Callback" functions of the
IP Connection object. It looks like this in Octave:

.. code-block:: octave

    function cb_example(e)
        fprintf("Parameter: %s\n", e.param);
    end

    ipcon.addExampleCallback(@cb_example);

It is possible to add several callback functions and to remove them with the
corresponding "remove*Callback" function.

The parameters of the callback are passed to the callback function as fields of
the structure ``e``, which is derived from the ``java.util.EventObject`` class.
The available callback names with corresponding structure fields are described
below.


.. matlab:member:: public callback IPConnection.EnumerateCallback

 :param uid: String
 :param connectedUid: String
 :param position: char
 :param hardwareVersion: short[]
 :param firmwareVersion: short[]
 :param deviceIdentifier: int
 :param enumerationType: short

 The callback function receives seven parameters as fields of the
 structure ``e``:

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

 In MATLAB the ``set()`` function can be used to register a callback function
 to this callback.

 In Octave a callback function can be added to this callback using the
 ``addEnumerateCallback()`` function. An added callback function can be removed with
 the ``removeEnumerateCallback()`` function.


.. matlab:member:: public callback IPConnection.ConnectedCallback

 :param connectReason: short

 This callback is called whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.CONNECT_REASON_REQUEST (0): Connection established after
   request from user.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Connection after
   auto-reconnect.

 In MATLAB the ``set()`` function can be used to register a callback function
 to this callback.

 In Octave a callback function can be added to this callback using the
 ``addConnectedCallback()`` function. An added callback function can be removed with
 the ``removeConnectedCallback()`` function.


.. matlab:member:: public callback IPConnection.DisconnectedCallback

 :param disconnectReason: short

 This callback is called whenever the IP Connection got disconnected from a
 Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Disconnect because of an
   unresolvable error.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.

 In MATLAB the ``set()`` function can be used to register a callback function
 to this callback.

 In Octave a callback function can be added to this callback using the
 ``addDisconnectedCallback()`` function. An added callback function can be removed with
 the ``removeDisconnectedCallback()`` function.
