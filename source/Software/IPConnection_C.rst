.. _ipcon_brick_c:

C - IP Connection
======================

.. _ipcon_brick_c_examples:

This is the API site for the C bindings of the IP Connection. 
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP connection
can be found :ref:`here <product_overview>`.

Example
--------

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/IPConnection_C_example.c>`__

.. literalinclude:: IPConnection_C_example.c
 :language: c
 :linenos:
 :tab-width: 4

.. _ipcon_brick_c_api:

API
---

Every function of the C/C++ bindings returns an integer which describes an
error code.

Possible error codes are

 * E_OK = 0
 * E_TIMEOUT = -1
 * E_NO_STREAM_SOCKET = -2
 * E_HOSTNAME_INVALID = -3
 * E_NO_CONNECT = -4
 * E_NO_THREAD = -5
 * E_NOT_ADDED = -6

as defined in :file:`ip_connection.h`.

.. c:function:: int ipcon_create(IPConnection *ipcon, const char* host, const int port)

 Creates an ip connection to the Brick Daemon with the given *host* 
 and *port*. With the ip connection itself it is possible to enumerate the 
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

.. c:function:: void ipcon_enumerate(IPConnection *ipcon, enumerate_callback_func_t cb)

 This method registers a callback with the signature:: 
  
 	void callback(char *uid, char *name, uint8_t stack_id, bool is_new)  

 that receives four parameters:

 * *uid*: The UID of the device.
 * *name*: The name of the device (includes "Brick" or "Bricklet" and a version number).
 * *stack_id*: The Stack ID of the device (you can find out the position in a stack with this).
 * *is_new*: True if the device is added, false if it is removed.

 There are three different possibilities for the callback to be called.
 Firstly, the callback is called with all currently available devices in the
 IP Connection (with *is_new* true). Secondly, the callback is called if
 a new Brick is plugged in via USB (with *is_new* true) and lastely it is
 called if a brick is unplugged (with *is_new* false).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).

.. c:function:: int ipcon_add_device(IPConnection *ipcon, Device *device)

 Adds a device (Brick or Bricklet) to the IP Connection. Every device
 has to be added to an ip connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. c:function:: void ipcon_join_thread(IPConnection *ipcon)

 Joins the thread of the ip connection. The call will block until the
 ip connection is :c:func:`destroyed <ipcon_destroy>`.

 This makes sense if you relies solely on callbacks from listeners or if
 the ip connection was created in a thread.

.. c:function:: void ipcon_destroy(IPConnection *ipcon)

 Destroys the ip connection. The socket to the Brick Daemon will be closed
 and the thread of the ip connection terminated. 
