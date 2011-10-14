.. _ipcon_brick_csharp:

C# - IP Connection
======================

.. _ipcon_brick_csharp_examples:

This is the API site for the C# bindings of the IP Connection. 
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP connection
can be found :ref:`here <product_overview>`.

Example
--------

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.cs>`__

.. literalinclude:: Example.cs
 :language: csharp
 :linenos:
 :tab-width: 4

.. _ipcon_brick_csharp_api:

API
---

.. csharp:function:: class IPConnection(string host, int port)

 Creates an ip connection to the Brick Daemon with the given *host* 
 and *port*. With the ip connection itself it is possible to enumerate the 
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

 The constructor throws an ``System.Net.Sockets.SocketException`` if there 
 is no Brick Daemon listening at the given host and port.

.. csharp:function:: public void IPConnection::Enumerate(EnumerateCallback enumerateCallback)

 This method registers the following delegate:

 .. csharp:function:: public delegate void EnumerateCallback(string uid, string name, byte stackID, bool isNew)

  The callback receives four parameters:

  * *uid*: The UID of the device.
  * *name*: The name of the device (includes "Brick" or "Bricklet" and a version number).
  * *stackID*: The Stack ID of the device (you can find out the position in a stack with this).
  * *isNew*: True if the device is added, false if it is removed.
 
  There are three different possibilities for the callback to be called.
  Firstly, the callback is called with all currently available devices in the
  IP Connection (with *isNew* true). Secondly, the callback is called if
  a new Brick is plugged in via USB (with *isNew* true) and lastely it is
  called if a brick is unplugged (with *isNew* false).

  It should be possible to implement "plug 'n play" functionality with this
  (as is done in Brick Viewer).

.. csharp:function:: public void IPConnection::AddDevice(Device device)

 Adds a device (Brick or Bricklet) to the IP Connection. Every device
 has to be added to an ip connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. csharp:function:: public void IPConnection::JoinThread()

 Joins the thread of the ip connection. The call will block until the
 ip connection is :csharp:func:`destroyed <IPConnection::Destroy>`.

 This makes sense if you relies solely on callbacks or if
 the ip connection was created in a thread.

.. csharp:function:: public void IPConnection::Destroy()

 Destroys the ip connection. The socket to the Brick Daemon will be closed
 and the thread of the ip connection terminated. 
