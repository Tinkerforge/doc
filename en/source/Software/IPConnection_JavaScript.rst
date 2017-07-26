
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software-javascript">Software</a> / JavaScript - IP Connection

.. |ref_api_bindings| replace:: :ref:`JavaScript API bindings <api_bindings_javascript>`
.. |ref_install_guide| replace:: :ref:`installation guide <api_bindings_javascript_install>`
.. |bindings_name| replace:: JavaScript

.. _ipcon_javascript:

JavaScript - IP Connection
==========================

.. include:: IPConnection_Common.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


.. _ipcon_javascript_examples:

Examples
--------

The example code below is `Public Domain (CC0 1.0)
<https://creativecommons.org/publicdomain/zero/1.0/>`__.

Enumerate (Node.js)
^^^^^^^^^^^^^^^^^^^

`Download (ExampleEnumerate.js) <https://github.com/Tinkerforge/generators/raw/master/javascript/ExampleEnumerate.js>`__

.. literalinclude:: IPConnection_JavaScript_ExampleEnumerate.js
 :language: javascript
 :linenos:
 :tab-width: 4

Authenticate (Node.js)
^^^^^^^^^^^^^^^^^^^^^^

`Download (ExampleAuthenticate.js) <https://github.com/Tinkerforge/generators/raw/master/javascript/ExampleAuthenticate.js>`__

.. literalinclude:: IPConnection_JavaScript_ExampleAuthenticate.js
 :language: javascript
 :linenos:
 :tab-width: 4

Enumerate (HTML)
^^^^^^^^^^^^^^^^

`Download (ExampleEnumerate.html) <https://github.com/Tinkerforge/generators/raw/master/javascript/ExampleEnumerate.html>`__,
`Test (ExampleEnumerate.html) <https://www.tinkerforge.com/en/doc/Software/Examples/JavaScript/IPConnection_JavaScript_ExampleEnumerate.html>`__

.. literalinclude:: IPConnection_JavaScript_ExampleEnumerate.html
 :language: html
 :linenos:
 :tab-width: 4

Authenticate (HTML)
^^^^^^^^^^^^^^^^^^^

`Download (ExampleAuthenticate.html) <https://github.com/Tinkerforge/generators/raw/master/javascript/ExampleAuthenticate.html>`__,
`Test (ExampleAuthenticate.html) <https://www.tinkerforge.com/en/doc/Software/Examples/JavaScript/IPConnection_JavaScript_ExampleAuthenticate.html>`__

.. literalinclude:: IPConnection_JavaScript_ExampleAuthenticate.html
 :language: html
 :linenos:
 :tab-width: 4


.. _ipcon_javascript_api:

API
---

Generally, every method of the JavaScript bindings can take two optional
parameters, ``returnCallback`` and ``errorCallback``. These are two user
defined callback functions. The ``returnCallback`` is called with the return
values as parameters, if the method returns something. The ``errorCallback``
is called with an error code in case of an error. The error code can be one
of the following values:

* IPConnection.ERROR_ALREADY_CONNECTED = 11
* IPConnection.ERROR_NOT_CONNECTED = 12
* IPConnection.ERROR_CONNECT_FAILED = 13
* IPConnection.ERROR_INVALID_FUNCTION_ID = 21
* IPConnection.ERROR_TIMEOUT = 31
* IPConnection.ERROR_INVALID_PARAMETER = 41
* IPConnection.ERROR_FUNCTION_NOT_SUPPORTED = 42
* IPConnection.ERROR_UNKNOWN_ERROR = 43

The namespace for the JavaScript bindings is ``Tinkerforge.*``.

Basic Functions
^^^^^^^^^^^^^^^

.. javascript:function:: new IPConnection()

 Creates an IP Connection object that can be used to enumerate the available
 devices. It is also required for the constructor of Bricks and Bricklets.


.. javascript:function:: IPConnection.connect(host, port, [errorCallback])

 :param host: string
 :param port: int

 Creates a TCP/IP connection to the given ``host`` and ``port``. The host and port
 can refer to a Brick Daemon or to a WIFI/Ethernet Extension.

 Devices can only be controlled when the connection was established
 successfully.


.. javascript:function:: IPConnection.disconnect([errorCallback])

 Disconnects the TCP/IP connection from the Brick Daemon or the WIFI/Ethernet
 Extension.


.. javascript:function:: IPConnection.authenticate(secret, [returnCallback], [errorCallback])

 :param secret: string
 :noreturn: undefined

 Performs an authentication handshake with the connected Brick Daemon or
 WIFI/Ethernet Extension.
 If the handshake succeeds the connection switches from non-authenticated to
 authenticated state and communication can continue as normal. If the handshake
 fails then the connection gets closed. Authentication can fail if the wrong
 secret was used or if authentication is not enabled at all on the Brick Daemon
 or the WIFI/Ethernet Extension.

 See the :ref:`authentication tutorial <tutorial_authentication>` for more
 information.


.. javascript:function:: IPConnection.getConnectionState()

 :rtype: int

 Can return the following states:

 * IPConnection.CONNECTION_STATE_DISCONNECTED (0): No connection is established.
 * IPConnection.CONNECTION_STATE_CONNECTED (1): A connection to the Brick Daemon
   or the WIFI/Ethernet Extension  is established.
 * IPConnection.CONNECTION_STATE_PENDING (2): IP Connection is currently trying
   to connect.


.. javascript:function:: IPConnection.setAutoReconnect(autoReconnect)

 :param auto_reconnect: boolean

 Enables or disables auto-reconnect. If auto-reconnect is enabled,
 the IP Connection will try to reconnect to the previously given
 host and port, if the currently existing connection is lost.
 Therefore, auto-reconnect only does something after a successful
 :javascript:func:`connect() <IPConnection.connect>` call.

 Default value is *true*.


.. javascript:function:: IPConnection.getAutoReconnect()

 :rtype: boolean

 Returns *true* if auto-reconnect is enabled, *false* otherwise.


.. javascript:function:: IPConnection.setTimeout(timeout)

 :param timeout: int

 Sets the timeout in milliseconds for getters and for setters for which the
 response expected flag is activated.

 Default timeout is 2500.


.. javascript:function:: IPConnection.getTimeout()

 :rtype: int

 Returns the timeout as set by :javascript:func:`setTimeout() <IPConnection.setTimeout>`.


.. javascript:function:: IPConnection.enumerate([errorCallback])

 Broadcasts an enumerate request. All devices will respond with an enumerate
 callback.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. javascript:function:: IPConnection.on(callback_id, function)

 :param callback_id: int
 :param function: function

 Registers the given ``function`` with the given ``callback_id``.

 The available callback IDs with corresponding function signatures
 are described below.


Callbacks
^^^^^^^^^

Callbacks can be registered to be notified about events. The registration is
done with the :javascript:func:`on() <IPConnection.on>`
function. The first parameter is the callback ID and the second
parameter the callback function:

.. code-block:: javascript

    ipcon.on(IPConnection.CALLBACK_EXAMPLE,
        function (param) {
            console.log(param);
        }
    );

The available constants with inherent number and type of parameters are
described below.


.. javascript:attribute:: IPConnection.CALLBACK_ENUMERATE

 :param uid: string
 :param connectedUid: string
 :param position: char
 :param hardwareVersion: [int, int, int]
 :param firmwareVersion: [int, int, int]
 :param deviceIdentifier: int
 :param enumerationType: int

 The callback has seven parameters:

 * ``uid``: The UID of the device.
 * ``connectedUid``: UID where the device is connected to. For a Bricklet this
   will be a UID of the Brick where it is connected to. For a Brick it will be
   the UID of the bottom Master Brick in the stack. For the bottom Master Brick
   in a stack this will be "0". With this information it is possible to
   reconstruct the complete network topology.
 * ``position``: For Bricks: '0' - '8' (position in stack). For Bricklets:
   'a' - 'd' (position on Brick).
 * ``hardwareVersion``: Major, minor and release number for hardware version.
 * ``firmwareVersion``: Major, minor and release number for firmware version.
 * ``deviceIdentifier``: A number that represents the device.
 * ``enumeration_type``: Type of enumeration.

 Possible enumeration types are:

 * IPConnection.ENUMERATION_TYPE_AVAILABLE (0): Device is available
   (enumeration triggered by user: :javascript:func:`enumerate()
   <IPConnection.enumerate>`). This enumeration type can occur multiple times
   for the same device.
 * IPConnection.ENUMERATION_TYPE_CONNECTED (1): Device is newly connected
   (automatically send by Brick after establishing a communication connection).
   This indicates that the device has potentially lost its previous
   configuration and needs to be reconfigured.
 * IPConnection.ENUMERATION_TYPE_DISCONNECTED (2): Device is disconnected (only
   possible for USB connection). In this case only ``uid`` and
   ``enumeration_type`` are valid.

 It should be possible to implement plug-and-play functionality with this
 (as is done in Brick Viewer).

 The device identifier numbers can be found :ref:`here <device_identifier>`.
 There are also constants for these numbers named following this pattern::

  <device-class>.DEVICE_IDENTIFIER

 For example: :javascript:attr:`BrickMaster.DEVICE_IDENTIFIER`
 or :javascript:attr:`BrickletAmbientLight.DEVICE_IDENTIFIER`.


.. javascript:attribute:: IPConnection.CALLBACK_CONNECTED

 :param connectReason: int

 This callback is called whenever the IP Connection got connected to a
 Brick Daemon or to a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.CONNECT_REASON_REQUEST (0): Connection established after
   request from user.
 * IPConnection.CONNECT_REASON_AUTO_RECONNECT (1): Connection after
   auto-reconnect.


.. javascript:attribute:: IPConnection.CALLBACK_DISCONNECTED

 :param disconnectReason: int

 This callback is called whenever the IP Connection got disconnected from a
 Brick Daemon or from a WIFI/Ethernet Extension, possible reasons are:

 * IPConnection.DISCONNECT_REASON_REQUEST (0): Disconnect was requested by user.
 * IPConnection.DISCONNECT_REASON_ERROR (1): Disconnect because of an
   unresolvable error.
 * IPConnection.DISCONNECT_REASON_SHUTDOWN (2): Disconnect initiated by Brick
   Daemon or WIFI/Ethernet Extension.
