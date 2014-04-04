
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Java - IP Connection

.. |ref_api_bindings| replace:: :ref:`Java bindings <api_bindings_java>`

.. _ipcon_java:

Java - IP Connection
====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_java_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<http://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (ExampleEnumerate.java) <https://github.com/Tinkerforge/generators/raw/master/java/ExampleEnumerate.java>`__

.. literalinclude:: IPConnection_Java_ExampleEnumerate.java
 :language: java
 :linenos:
 :tab-width: 4

Authenticate
^^^^^^^^^^^^

`Download (ExampleAuthenticate.java) <https://github.com/Tinkerforge/generators/raw/master/java/ExampleAuthenticate.java>`__

.. literalinclude:: IPConnection_Java_ExampleAuthenticate.java
 :language: java
 :linenos:
 :tab-width: 4


.. _ipcon_java_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. java:function:: class IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. java:function:: public void IPConnection::connect(String host, int port)

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. java:function:: public void IPConnection::disconnect()

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. java:function:: public void IPConnection::authenticate(String secret)

 Performs an authentication handshake with the connected Brick Daemon or
 WIFI/Ethernet Extension. On success the connection switches from
 non-authenticated to authenticated state and communication can continue as
 normal. On failure the connection gets closed by the server side. Authentication
 can fail if the authentication secrets mismatch or if authentication is not
 enabled at all on the Brick Daemon or WIFI/Ethernet Extension.

 For more information about authentication see TODO.

 .. versionadded:: 2.1.0


.. java:function:: public byte IPConnection::getConnectionState()

 Can return the following states:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * IPConnection.CONNECTION_STATE_CONNETED (1): A connection to the Brick Daemon
   or the WIFI/Ethernet Extension  is established.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection is currently trying
   to connect.


.. java:function:: public void IPConnection::setAutoReconnect(boolean autoReconnect)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *true*.


.. java:function:: public boolean IPConnection::getAutoReconnect()

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. java:function:: public void IPConnection::setTimeout(int timeout)

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. java:function:: public int IPConnection::getTimeout()

 Returns the timeout as set by :java:func:`setTimeout() <IPConnection::setTimeout>`.


.. java:function:: public void IPConnection::enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


Listener Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:function:: public void IPConnection::addListener(Object object)

 Registers a listener object.

 The available listener classes with inherent methods to be overwritten
 are described below.


Listeners
^^^^^^^^^

Listeners can be registered to be notified about events. The registration is
done with "addListener" functions of the IPConnection object.

The parameter is a listener class object, for example:

.. code-block:: java

    ipcon.addExampleListener(new IPConnection.ExampleListener() {
        public void property(int value) {
            System.out.println("Value: " + value);
        }
    });

The available listener classes with inherent methods to be overwritten
are described below. It is possible to add several listeners and
to remove them with the corresponding "removeListener" function.


.. java:function:: public class IPConnection.EnumerateListener()

 This listener can be added with the ``addEnumerateListener()`` function.
 An added listener can be removed with the ``removeEnumerateListener()`` function.

 .. java:function:: public void enumerate(String uid, String connectedUid, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)
  :noindex:

  The listener receives seven parameters:

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

  For example: :java:member:`BrickMaster.DEVICE_IDENTIFIER`
  or :java:member:`BrickletAmbientLight.DEVICE_IDENTIFIER`.


.. java:function:: public class IPConnection.ConnectedListener()

 This listener can be added with the ``addConnectedListener()`` function.
 An added listener can be removed with the ``removeConnectedListener()`` function.

 .. java:function:: public void connected(short connectReason)
  :noindex:

  This listener is called whenever the IP Connection got connected to a
  Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

  * IPConnection.CONNECT_REASON_REQUEST (0): Connection established after
    request from user.
  * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Connection after
    auto-reconnect.


.. java:function:: public class IPConnection.DisconnectedListener()

 This listener can be added with the ``addDisconnectedListener()`` function.
 An added listener can be removed with the ``removeDisconnectedListener()`` function.

 .. java:function:: public void disconnected(short disconnectReason)
  :noindex:

  This listener is called whenever the IP Connection got disconnected from a
  Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

  * IPConnection.DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
  * IPConnection.DISCONNECT_REASON_ERROR (1): Disconnect because of an
    unresolvable error.
  * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
    Daemon or WIFI/Ethernet Extension.
