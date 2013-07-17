
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / Shell - IP Connection

.. _ipcon_shell:

Shell - IP Connection
=====================

This is the API description for the Shell bindings of the IP Connection.
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP Connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.


.. _ipcon_shell_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/en/source/Software/example.py>`__

.. literalinclude:: example.sh
 :language: bash
 :linenos:
 :tab-width: 4


.. _ipcon_shell_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. sh:function:: IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. sh:function:: IPConnection.connect(host, port)

 :param host: str
 :param port: int
 :rtype: None

 Creates a TCP/IP connection to the given *host* and *port*. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given
 host and port.


.. sh:function:: IPConnection.disconnect()

 :rtype: None

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. sh:function:: IPConnection.get_connection_state()

 :rtype: int

 Can return the following states:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * IPConnection.CONNECTION_STATE_CONNETED (1): A connection to the Brick Daemon
   or the WIFI/Ethernet Extension  is established.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection is currently trying
   to connect.


.. sh:function:: IPConnection.set_auto_reconnect(auto_reconnect)

 :param auto_reconnect: bool
 :rtype: None

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *True*.


.. sh:function:: IPConnection.get_auto_reconnect()

 :rtype: bool

 Returns *True* if auto-reconnect is enabled, *False* otherwise.


.. sh:function:: IPConnection.set_timeout(timeout)

 :param timeout: float
 :rtype: None

 Sets the timeout in seconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2.5.


.. sh:function:: IPConnection.get_timeout()

 :rtype: float

 Returns the timeout as set by :py:func:`set_timeout() <IPConnection.set_timeout>`.


.. sh:function:: IPConnection.enumerate()

 :rtype: None

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. sh:function:: IPConnection.wait()

 :rtype: None

 Stops the current thread until :py:func:`unwait() <IPConnection.unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 ``wait`` and ``unwait`` act in the same way as "acquire" and "release" of a
 semaphore.


.. sh:function:: IPConnection.unwait()

 :rtype: None

 Unwaits the thread previously stopped by :py:func:`wait() <IPConnection.wait>`

 ``wait`` and ``unwait`` act in the same way as "acquire" and "release" of a
 semaphore.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done with the :py:func:`register_callback() <IPConnection.register_callback>`
function. The first parameter is the callback ID and the second
parameter the callback function:

.. code-block:: python

    def my_callback(param):
        print(param)

    ipcon.register_callback(IPConnection.CALLBACK_EXAMPLE, my_callback)

The available constants with inherent number and type of parameters are
described below.


.. sh:attribute:: IPConnection.CALLBACK_ENUMERATE

 :param uid: string
 :param connected_uid: string
 :param position: char
 :param hardware_version: [int, int, int]
 :param firmware_version: [int, int, int]
 :param device_identifier: int
 :param enumeration_type: int

 The callback has seven parameters:

 * *uid*: The UID of the device.
 * *connected_uid*: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "1". With this information it is possible to
   reconstruct the complete network topology.
 * *position*: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * *hardwareVersion*: Major, minor and release number for hardware version.
 * *firmwareVersion*: Major, minor and release number for firmware version.
 * *deviceIdentifier*: A number that represents the device, instead of the name
   of the device (easier to parse).
 * *enumerationType*: Type of enumeration.

 Possible enumeration types are:

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Device is available (enumeration
   triggered by user).
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected (only
   possible for USB connection). In this case only *uid* and *enumeration_type*
   are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifiers can be found :ref:`here <device_identifier>`.
