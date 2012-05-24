.. _ipcon_csharp:

C# - IP Connection
======================

This is the API site for the C# bindings of the IP connection.
The IP connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP connection
can be found :ref:`here <product_overview>`.

.. _ipcon_csharp_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.cs>`__

.. literalinclude:: Example.cs
 :language: csharp
 :linenos:
 :tab-width: 4

.. _ipcon_csharp_api:

API
---

Basic Methods
^^^^^^^^^^^^^

.. csharp:function:: class IPConnection(string host, int port)

 Creates an IP connection to the Brick Daemon with the given *host*
 and *port*. With the IP connection itself it is possible to enumerate the
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

 The constructor throws an ``System.Net.Sockets.SocketException`` if there 
 is no Brick Daemon listening at the given host and port.

.. csharp:function:: public void IPConnection::AddDevice(Device device)

 Adds a device (Brick or Bricklet) to the IP connection. Every device
 has to be added to an IP connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. csharp:function:: public void IPConnection::JoinThread()

 Joins the thread of the IP connection. The call will block until the
 IP connection is :csharp:func:`destroyed <IPConnection::Destroy>`.

 This makes sense if you relies solely on callbacks or if
 the IP connection was created in a thread.

 On Windows Phone this function will do nothing (since all sockets are 
 asynchronous and there are no threads used).

.. csharp:function:: public void IPConnection::Destroy()

 Destroys the IP connection. The socket to the Brick Daemon will be closed
 and the thread of the IP connection terminated.

Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csharp:function:: public void IPConnection::Enumerate(EnumerateCallback enumerateCallback)

 This method registers the following delegate:

 .. csharp:function:: public delegate void EnumerateCallback(string uid, string name, byte stackID, bool isNew)

  The callback receives four parameters:

  * *uid*: The UID of the device.
  * *name*: The name of the device (includes "Brick" or "Bricklet" and a version number).
  * *stackID*: The stack ID of the device (you can find out the position in a stack with this).
  * *isNew*: True if the device is added, false if it is removed.

  There are three different possibilities for the callback to be called.
  Firstly, the callback is called with all currently available devices in the
  IP connection (with *isNew* true). Secondly, the callback is called if
  a new Brick is plugged in via USB (with *isNew* true) and lastly it is
  called if a Brick is unplugged (with *isNew* false).

  It should be possible to implement "plug 'n play" functionality with this
  (as is done in Brick Viewer).
