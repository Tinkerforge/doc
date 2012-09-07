.. _ipcon_c:

C/C++ - IP Connection
=====================

This is the API description the IP connection the C/C++ bindings of.
The IP connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP connection
can be found :ref:`here <product_overview>`.


.. _ipcon_c_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.c>`__

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
* E_NOT_ADDED = -6

as defined in :file:`ip_connection.h`.


Basic Functions
^^^^^^^^^^^^^^^

.. c:function:: int ipcon_create(IPConnection *ipcon, const char* host, const int port)

 Creates an IP connection to the Brick Daemon with the given *host*
 and *port*. With the IP connection itself it is possible to enumerate the
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

.. c:function:: int ipcon_add_device(IPConnection *ipcon, Device *device)

 Adds a device (Brick or Bricklet) to the IP connection. Every device
 has to be added to an IP connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. c:function:: void ipcon_join_thread(IPConnection *ipcon)

 Joins the threads of the IP connection. The call will block until the
 IP connection is :c:func:`destroyed <ipcon_destroy>`.

 This makes sense if you relies solely on callbacks for events or if
 the IP connection was created in a threads.

.. c:function:: void ipcon_destroy(IPConnection *ipcon)

 Destroys the IP connection. The socket to the Brick Daemon will be closed
 and the threads of the IP connection terminated.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. c:function:: void ipcon_enumerate(IPConnection *ipcon, enumerate_callback_func_t cb)

 This function registers a callback with the signature:
 
 .. code-block:: c

  void callback(char *uid, char *name, uint8_t stack_id, bool is_new)  

 that receives four parameters:

 * *uid*: The UID of the device.
 * *name*: The name of the device (includes "Brick" or "Bricklet" and a version number).
 * *stack_id*: The stack ID of the device (you can find out the position in a stack with this).
 * *is_new*: Is *true* if the device is added, *false* if it is removed.

 There are three different possibilities for the callback to be called.
 Firstly, the callback is called with all currently available devices in the
 IP connection (with *is_new* set to *true*). Secondly, the callback is called if
 a new Brick is plugged in via USB (with *is_new* set to *true*) and lastly it is
 called if a Brick is unplugged (with *is_new* set to *false*).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).
