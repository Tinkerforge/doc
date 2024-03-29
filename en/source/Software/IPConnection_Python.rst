
.. |ref_api_bindings| replace:: :ref:`Python API bindings <api_bindings_python>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_python_install>`
.. |bindings_name| replace:: Python

.. _ip_connection_python:

Python - IP Connection
======================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ip_connection_python_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate
^^^^^^^^^

`Download (example_enumerate.py) <https://github.com/Tinkerforge/generators/raw/master/python/example_enumerate.py>`__

.. literalinclude:: IPConnection_Python_example_enumerate.py
 :language: python
 :linenos:
 :tab-width: 4


Authenticate
^^^^^^^^^^^^

`Download (example_authenticate.py) <https://github.com/Tinkerforge/generators/raw/master/python/example_authenticate.py>`__

.. literalinclude:: IPConnection_Python_example_authenticate.py
 :language: python
 :linenos:
 :tab-width: 4


.. _ip_connection_python_api:

API
---

Generally, every method of the Python bindings can throw an
``tinkerforge.ip_connection.Error`` exception that has a ``value`` and a
``description`` property. ``value`` can have different values:

* Error.TIMEOUT = -1
* Error.NOT_ADDED = -6 (unused since Python bindings version 2.0.0)
* Error.ALREADY_CONNECTED = -7
* Error.NOT_CONNECTED = -8
* Error.INVALID_PARAMETER = -9
* Error.NOT_SUPPORTED = -10
* Error.UNKNOWN_ERROR_CODE = -11
* Error.STREAM_OUT_OF_SYNC = -12
* Error.INVALID_UID = -13
* Error.NON_ASCII_CHAR_IN_SECRET = -14
* Error.WRONG_DEVICE_TYPE = -15
* Error.DEVICE_REPLACED = -16
* Error.WRONG_RESPONSE_LENGTH = -17

All methods listed below are thread-safe.

Basic Functions
^^^^^^^^^^^^^^^

.. py:function:: IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. py:function:: IPConnection.connect(host, port)

 :param host: str
 :param port: int
 :rtype: None

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.

 Blocks until the connection is established and throws an exception if there
 is no Brick Daemon or WIFI/Ethernet Extension listening at the given
 host and port.


.. py:function:: IPConnection.disconnect()

 :rtype: None

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. py:function:: IPConnection.authenticate(secret)

 :param secret: str
 :rtype: None

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


.. py:function:: IPConnection.get_connection_state()

 :rtype: int

 Can return the following states:

 * IPConnection.\ **CONNECTION_STATE**\ _DISCONNECTED = 0: No connection is established.
 * IPConnection.\ **CONNECTION_STATE**\ _CONNECTED = 1: A connection to the Brick Daemon
   or the WIFI/Ethernet Extension  is established.
 * IPConnection.\ **CONNECTION_STATE**\ _PENDING = 2: IP Connection is currently trying
   to connect.


.. py:function:: IPConnection.set_auto_reconnect(auto_reconnect)

 :param auto_reconnect: bool
 :rtype: None

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the currently existing connection is lost.
 Therefore, auto-reconnect only does something after a successful
 :py:func:`connect() <IPConnection.connect>` call.

 Default value is *True*.


.. py:function:: IPConnection.get_auto_reconnect()

 :rtype: bool

 Returns *True* if auto-reconnect is enabled, *False* otherwise.


.. py:function:: IPConnection.set_timeout(timeout)

 :param timeout: float
 :rtype: None

 Sets the timeout in seconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2.5.


.. py:function:: IPConnection.get_timeout()

 :rtype: float

 Returns the timeout as set by :py:func:`set_timeout() <IPConnection.set_timeout>`.


.. py:function:: IPConnection.enumerate()

 :rtype: None

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


.. py:function:: IPConnection.wait()

 :rtype: None

 Stops the current thread until :py:func:`unwait() <IPConnection.unwait>`
 is called.

 This is useful if you rely solely on callbacks for events, if you want to
 wait for a specific callback or if the IP Connection was created in a thread.

 ``wait`` and ``unwait`` act in the same way as ``acquire`` and ``release`` of a
 semaphore.


.. py:function:: IPConnection.unwait()

 :rtype: None

 Unwaits the thread previously stopped by :py:func:`wait() <IPConnection.wait>`

 ``wait`` and ``unwait`` act in the same way as ``acquire`` and ``release`` of a
 semaphore.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: IPConnection.register_callback(callback_id, function)

 :param callback_id: int
 :param function: callable
 :rtype: None

 Registers the given ``function`` with the given ``callback_id``.

 The available callback IDs with corresponding function signatures
 are described below.


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


.. py:attribute:: IPConnection.CALLBACK_ENUMERATE

 :param uid: str
 :param connected_uid: str
 :param position: chr
 :param hardware_version: [int, int, int]
 :param firmware_version: [int, int, int]
 :param device_identifier: int
 :param enumeration_type: int

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

 * IPConnection.\ **ENUMERATION_TYPE**\ _AVAILABLE = 0: Device is available
   (enumeration triggered by user: :py:func:`enumerate()
   <IPConnection.enumerate>`). This enumeration type can occur multiple times
   for the same device.
 * IPConnection.\ **ENUMERATION_TYPE**\ _CONNECTED = 1: Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPConnection.\ **ENUMERATION_TYPE**\ _DISCONNECTED = 2: Device is disconnected (only
   possible for USB connection). In this case only ``uid`` and
   ``enumeration_type`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern::

  <device-class>.DEVICE_IDENTIFIER

 For example: :py:attr:`Master.DEVICE_IDENTIFIER`
 or :py:attr:`AmbientLight.DEVICE_IDENTIFIER`.


.. py:attribute:: IPConnection.CALLBACK_CONNECTED

 :param connect_reason: int

 This callback is called whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.\ **CONNECT_REASON**\ _REQUEST = 0: Connection established after
   request from user.
 * IPConnection.\ **CONNECT_REASON**\ _AUTO_RECONNECT = 1: Connection after
   auto-reconnect.


.. py:attribute:: IPConnection.CALLBACK_DISCONNECTED

 :param disconnect_reason: int

 This callback is called whenever the IP Connection got disconnected from a
 Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.\ **DISCONNECT_REASON**\ _REQUEST = 0: Disconnect was requested by user.
 * IPConnection.\ **DISCONNECT_REASON**\ _ERROR = 1: Disconnect because of an
   unresolvable error.
 * IPConnection.\ **DISCONNECT_REASON**\ _SHUTDOWN = 2: Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
