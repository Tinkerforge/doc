
.. |ref_api_bindings| replace:: :ref:`C/C++ API bindings <api_bindings_c>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_c_install>`
.. |bindings_name| replace:: C/C++

.. _ip_connection_c:

C/C++ - IP Connection
=====================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ip_connection_c_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.c) <https://github.com/Tinkerforge/generators/raw/master/c/example_enumerate.c>`__

.. literalinclude:: IPConnection_C_example_enumerate.c
 :language: c
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.c) <https://github.com/Tinkerforge/generators/raw/master/c/example_authenticate.c>`__

.. literalinclude:: IPConnection_C_example_authenticate.c
 :language: c
 :linenos:
 :tab-width: 4


.. _ip_connection_c_api:

API
---

Most functions of the C/C++ bindings return an error code (``e_code``).

Possible error codes are:

* **E**\ _OK = 0
* **E**\ _TIMEOUT = -1
* **E**\ _NO_STREAM_SOCKET = -2
* **E**\ _HOSTNAME_INVALID = -3
* **E**\ _NO_CONNECT = -4
* **E**\ _NO_THREAD = -5
* **E**\ _NOT_ADDED = -6 (unused since C/C++ bindings version 2.0.0)
* **E**\ _ALREADY_CONNECTED = -7
* **E**\ _NOT_CONNECTED = -8
* **E**\ _INVALID_PARAMETER = -9
* **E**\ _NOT_SUPPORTED = -10
* **E**\ _UNKNOWN_ERROR_CODE = -11
* **E**\ _STREAM_OUT_OF_SYNC = -12
* **E**\ _INVALID_UID = -13
* **E**\ _NON_ASCII_CHAR_IN_SECRET = -14
* **E**\ _WRONG_DEVICE_TYPE = -15
* **E**\ _DEVICE_REPLACED = -16
* **E**\ _WRONG_RESPONSE_LENGTH = -17

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

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and returns an error code if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given host
 and port.


.. c:function:: int ipcon_disconnect(IPConnection *ipcon)

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. c:function:: int ipcon_authenticate(IPConnection *ipcon, const char *secret)

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


.. c:function:: int ipcon_get_connection_state(IPConnection *ipcon)

 Can return the following states:

 * IPCON\_\ **CONNECTION_STATE**\ _DISCONNECTED = 0: No connection is established.
 * IPCON\_\ **CONNECTION_STATE**\ _CONNECTED = 1: A connection to the Brick Daemon or
   the WIFI/Ethernet Extension is established.
 * IPCON\_\ **CONNECTION_STATE**\ _PENDING = 2: IP Connection is currently trying to connect.


.. c:function:: void ipcon_set_auto_reconnect(IPConnection *ipcon, bool auto_reconnect)

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the currently existing connection is lost.
 Therefore, auto-reconnect only does something after a successful
 :c:func:`ipcon_connect` call.

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

.. c:function:: void ipcon_register_callback(IPConnection *ipcon, int16_t callback_id, void (*function)(void), void *user_data)

 Registers the given ``function`` with the given ``callback_id``. The
 ``user_data`` will be passed as the last parameter to the ``function``.

 The available callback IDs with corresponding function signatures
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

    ipcon_register_callback(&ipcon, IPCON_CALLBACK_EXAMPLE, (void (*)(void))my_callback, NULL);

The available constants with corresponding callback function signatures are
described below.


.. c:var:: IPCON_CALLBACK_ENUMERATE

 .. code-block:: c

  void callback(const char *uid, const char *connected_uid, char position, uint8_t hardware_version[3], uint8_t firmware_version[3], uint16_t device_identifier, uint8_t enumeration_type, void *user_data)

 The callback has seven parameters:

 * ``uid``: The UID of the device.
 * ``connected_uid``: UID where the device is connected to. For a Bricklet this
   is the UID of the Brick or Bricklet it is connected to. For a Brick it is
   the UID of the bottommost Brick in the stack. For the bottommost Brick
   in a stack it is "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position``: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'h' (position on Brick) or 'i' (position of the Raspberry Pi (Zero) HAT)
   or 'z' (Bricklet on :ref:`Isolator Bricklet <isolator_bricklet>`).
 * ``hardware_version``: Major, minor and release number for hardware version.
 * ``firmware_version``: Major, minor and release number for firmware version.
 * ``device_identifier``: A number that represents the device.
 * ``enumeration_type``: Type of enumeration.

 Possible enumeration types are:

 * IPCON\_\ **ENUMERATION_TYPE**\ _AVAILABLE = 0: Device is available (enumeration
   triggered by user: :c:func:`ipcon_enumerate`). This enumeration type can
   occur multiple times for the same device.
 * IPCON\_\ **ENUMERATION_TYPE**\ _CONNECTED = 1: Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPCON\_\ **ENUMERATION_TYPE**\ _DISCONNECTED = 2: Device is disconnected (only
   possible for USB connection). In this case only ``uid`` and
   ``enumeration_type`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern:

 .. code-block:: none

  <device-type>_DEVICE_IDENTIFIER

 For example: :c:data:`MASTER_DEVICE_IDENTIFIER`
 or :c:data:`AMBIENT_LIGHT_DEVICE_IDENTIFIER`.


.. c:var:: IPCON_CALLBACK_CONNECTED

 .. code-block:: c

  void callback(uint8_t connect_reason, void *user_data)

 This callback is called whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPCON\_\ **CONNECT_REASON**\ _REQUEST = 0: Connection established after request from user.
 * IPCON\_\ **CONNECT_REASON**\ _AUTO_RECONNECT = 1: Connection after auto-reconnect.


.. c:var:: IPCON_CALLBACK_DISCONNECTED

 .. code-block:: c

  void callback(uint8_t disconnect_reason, void *user_data)

 This callback is called whenever the IP Connection got disconnected from a
 Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

 * IPCON\_\ **DISCONNECT_REASON**\ _REQUEST = 0: Disconnect was requested by user.
 * IPCON\_\ **DISCONNECT_REASON**\ _ERROR = 1: Disconnect because of an unresolvable error.
 * IPCON\_\ **DISCONNECT_REASON**\ _SHUTDOWN = 2: Disconnect initiated by Brick Daemon
   or WIFI/Ethernet Extension.
