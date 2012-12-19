.. _ipcon_java:

Java - IP Connection
====================

This is the API description for the Java bindings of the IP Connection.
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP Connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.


.. _ipcon_java_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.java>`__

.. literalinclude:: Example.java
 :language: java
 :linenos:
 :tab-width: 4


.. _ipcon_java_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. java:function:: class IPConnection()

 Creates an IP Connection object. The constructed object is needed for the
 constructor of Bricks and Bricklets.

.. java:function:: public void IPConnection::connect(String host, int port)

 Creates a TCP/IP connection to the given host and port.
 The host and port can point to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an IOException 
 if there is no Brick Daemon or WIFI/Ethernet Extension
 listening at the given host and port.

.. java:function:: public void IPConnection::disconnect()

 Disconnects the TCP/IP connection to the Brick Daemon or to
 the WIFI/Ethernet Extension.

.. java:function:: public byte IPConnection::getConnectionState()

 Can return the following states:

 * CONNECTION_DISCONNECTED (0): No connection is established.
 * CONNECTION_CONNETED (1): A connection to the Brickd Daemon or the WIFI/Ethernet Extension  is established.
 * CONNECTION_PENDING (2): IP Connection is currently trying to connect.

.. java:function:: public void IPConnection::setAutoReconnect(boolean autoReconnect)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *true*.

.. java:function:: public boolean IPConnection::getAutoReconnect()

 Returns *true* if auto-reconnect is enabled, *false* otherwise.

.. java:function:: public void IPConnection::setTimeout(int timeout)

 Sets the timeout (in ms) for getters and for setters for which 
 "response expected" is activated.

 Default timeout is 2500ms.

.. java:function:: public int IPConnection::getTimeout()

 Returns the timeout as set by :java:func:`setTimeout <IPConnection::setTimeout>`.

.. java:function:: public void IPConnection::wait()

 holds the current thread until :java:func:`unwait <IPConnection::unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a threads.

 Wait and unwait act in the same way as require and release of a semaphore.
 
.. java:function:: public void IPConnection::unwait()

 Unwaits the thread previously set to hold by :java:func:`wait <IPConnection::wait>`

 Wait and unwait act in the same way as require and release of a semaphore.

.. java:function:: public void IPConnection::enumerate()

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


Listener Configuration
^^^^^^^^^^^^^^^^^^^^^^

.. java:function:: public void IPConnection::addListener(Object o)

 This method registers the following listener:

 .. java:function:: public class IPConnection.EnumerateListener()

  .. java:function:: public void enumerate(String UID, String connectedUID, char position, short[] hardwareVersion, short[] firmwareVersion, int deviceIdentifier, short enumerationType)
   :noindex:

   The listener receives seven parameters:

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

 .. java:function:: public class IPConnection.ConnectedListener()

  .. java:function:: public void connected(int reason)
   :noindex:
	
   This listener is called whenever the IP connection is connected, possible reasons are:

   * CONNECT_REASON_REQUEST (0): Connection established after request from user.
   * CONNECT_REASON_AUTO_RECONNECT (1): Connection after auto-reconnect.

 .. java:function:: public class IPConnection.DisconnectedListener()

  .. java:function:: public void disconnected(int reason)
   :noindex:

   This listener is called whenever the IP connection is disconnected, possible reasons are:

   * DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
   * DISCONNECT_REASON_ERROR (1): Disconnect because of an unresolvable error.
   * DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by brickd or WIFI/Ethernet Extension.
