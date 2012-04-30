.. _ipcon_java:

Java - IP Connection
======================

This is the API site for the Java bindings of the IP connection.
The IP connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP connection
can be found :ref:`here <product_overview>`.

.. _ipcon_java_examples:

Example
--------

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.java>`__

.. literalinclude:: Example.java
 :language: java
 :linenos:
 :tab-width: 4

.. _ipcon_java_api:

API
---

Basic Methods
^^^^^^^^^^^^^

.. java:function:: class IPConnection(String host, int port)

 Creates an IP connection to the Brick Daemon with the given *host*
 and *port*. With the IP connection itself it is possible to enumerate the
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

 The constructor throws an IOException if there is no Brick Daemon 
 listening at the given host and port.

.. java:function:: public void IPConnection::addDevice(Device device)

 Adds a device (Brick or Bricklet) to the IP connection. Every device
 has to be added to an IP connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. java:function:: public void IPConnection::joinThread()

 Joins the thread of the IP connection. The call will block until the
 IP connection is :java:func:`destroyed <IPConnection::destroy>`.

 This makes sense if you relies solely on callbacks from listeners or if
 the IP connection was created in a thread.

.. java:function:: public void IPConnection::destroy()

 Destroys the IP connection. The socket to the Brick Daemon will be closed
 and the thread of the IP connection terminated.

Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:function:: public void IPConnection::enumerate(EnumerateListener enumerateListener)

 This method registers the following listener:

 .. java:function:: public class IPConnection.EnumerateListener()

  .. java:function:: public void enumerate(String uid, String name, short stackID, boolean isNew)
   :noindex:

   The listener receives four parameters:

   * *uid*: The UID of the device.
   * *name*: The name of the device (includes "Brick" or "Bricklet" and a version number).
   * *stackID*: The stack ID of the device (you can find out the position in a stack with this).
   * *isNew*: True if the device is added, false if it is removed.
 
   There are three different possibilities for the listener to be called.
   Firstly, the listener is called with all currently available devices in the
   IP connection (with *isNew* true). Secondly, the listener is called if
   a new Brick is plugged in via USB (with *isNew* true) and lastly it is
   called if a Brick is unplugged (with *isNew* false).

   It should be possible to implement "plug 'n play" functionality with this
   (as is done in Brick Viewer).
