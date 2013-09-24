
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / C/C++ - IP Connection

.. |ref_api_bindings| replace:: :ref:`C/C++ bindings <api_bindings_c>`

.. _ipcon_c:

C/C++ - IP Connection
=====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_c_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/en/source/Software/example.c>`__

.. literalinclude:: example.c
 :language: c
 :linenos:
 :tab-width: 4


.. _ipcon_c_api:

API
---

Every function of the C/C++ bindings returns an integer which describes an
error code.

Possible error codes are:

* E_OK = 0
* E_TIMEOUT = -1
* E_NO_STREAM_SOCKET = -2
* E_HOSTNAME_INVALID = -3
* E_NO_CONNECT = -4
* E_NO_THREAD = -5
* E_NOT_ADDED = -6 (unused since bindings version 2.0.0)
* E_ALREADY_CONNECTED = -7
* E_NOT_CONNECTED = -8
* E_INVALID_PARAMETER = -9
* E_NOT_SUPPORTED = -10
* E_UNKNOWN_ERROR_CODE = -11

as defined in :file:`ip_connection.h`.


Basic Functions
^^^^^^^^^^^^^^^

.. c:function:: void ipcon_create(IPConnection *ipcon)

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. c:function:: void ipcon_destroy(IPConnection *ipcon)

 Destroys the IP Connection object. Calls :c:func:`ipcon_disconnect` internally.
 The connection to the Brick Daemon gets closed and the threads of the
 IP Connection are terminated.


.. c:function:: int ipcon_connect(IPConnection *ipcon, const char *host, uint16_t port)

 Creates a TCP/IP connection to the given *host* and *port*. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and returns an error code if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. c:function:: int ipcon_disconnect(IPConnection *ipcon)

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. c:function:: int ipcon_get_connection_state(IPConnection *ipcon)

 Can return the following states:

 * IPCON_CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * IPCON_CONNECTION_STATE_CONNECTED (1): A connection to the Brick Daemon or
   the WIFI/Ethernet Extension is established.
 * IPCON_CONNECTION_STATE_PENDING (2): IP Connection is currently trying to
   connect.


.. c:function:: void ipcon_set_auto_reconnect(IPConnection *ipcon, bool auto_reconnect)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the connection is lost.

 Default value is *true*.


.. c:function:: bool ipcon_get_auto_reconnect(IPConnection *ipcon)

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. c:function:: void ipcon_set_timeout(IPConnection *ipcon, uint32_t timeout)

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. c:function:: uint32_t ipcon_get_timeout(IPConnection *ipcon)

 Returns the timeout as set by :c:func:`ipcon_set_timeout`.


.. c:function:: int ipcon_enumerate(IPConnection *ipcon)

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. c:function:: void ipcon_wait(IPConnection *ipcon)

 Stops the current thread until :c:func:`ipcon_unwait`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 ``wait`` and ``unwait`` act in the same way as ``acquire`` and ``release`` of a
 semaphore.


.. c:function:: void ipcon_unwait(IPConnection *ipcon)

 Unwaits the thread previously stopped by :c:func:`ipcon_wait`

 ``wait`` and ``unwait`` act in the same way as ``acquire`` and ``release`` of a
 semaphore.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. c:function:: void ipcon_register_callback(IPConnection *ipcon, uint8_t id, void *callback, void *user_data)

 Registers a callback with ID *id* to the function *callback*.

 The available IDs with corresponding callback function signatures
 are described below.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done with the :c:func:`ipcon_register_callback` function. The parameters
consist of the IP Connection object, the callback ID, the callback function and
optional user data:

.. code-block:: c

    void my_callback(int p, void *user_data) {
        printf("parameter: %d\n", p);
    }

    ipcon_register_callback(&ipcon, IPCON_CALLBACK_EXAMPLE, (void*)my_callback, NULL);

The available constants with corresponding callback function signatures are
described below.


.. c:var:: IPCON_CALLBACK_ENUMERATE

 .. code-block:: c

  void callback(const char *uid, const char *connected_uid, char position, uint8_t hardware_version[3], uint8_t firmware_version[3], uint16_t device_identifier, uint8_t enumeration_type, void *user_data)

 The callback has seven parameters:

 * *uid*: The UID of the device.
 * *connected_uid*: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * *position*: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * *hardware_version*: Major, minor and release number for hardware version.
 * *firmware_version*: Major, minor and release number for firmware version.
 * *device_identifier*: A number that represents the device.
 * *enumeration_type*: Type of enumeration.

 Possible enumeration types are:

 * IPCON_ENUMERATION_TYPE_AVAILABLE (0): Device is available (enumeration
   triggered by user).
 * IPCON_ENUMERATION_TYPE_CONNECTED (1): Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPCON_ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected (only
   possible for USB connection). In this case only *uid* and *enumeration_type*
   are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifiers can be found :ref:`here <device_identifier>`.


.. c:var:: IPCON_CALLBACK_CONNECTED

 .. code-block:: c

  void callback(uint8_t connect_reason, void *user_data)

 This callback is called whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPCON_CONNECT_REASON_REQUEST (0): Connection established after request
   from user.
 * IPCON_CONNECT_REASON_AUTO_RECONNECT (1): Connection after auto-reconnect.


.. c:var:: IPCON_CALLBACK_DISCONNECTED

 .. code-block:: c

  void callback(uint8_t disconnect_reason, void *user_data)

 This callback is called whenever the IP Connection got disconnected from a
 Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

 * IPCON_DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * IPCON_DISCONNECT_REASON_ERROR (1): Disconnect because of an unresolvable
   error.
 * IPCON_DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick Daemon
   or WIFI/Ethernet Extension.
