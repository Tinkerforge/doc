.. _ipcon_brick_python:

Python - IP Connection
======================

.. _ipcon_brick_python_examples:

This is the API site for the Python bindings of the IP Connection. 
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP connection
can be found :ref:`here <product_overview>`.

Example
--------

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.py>`__

.. literalinclude:: example.py
 :language: python
 :linenos:
 :tab-width: 4

.. _ipcon_brick_python_api:

API
---

.. py:function:: IPConnection(host, port)

 :param host: str
 :param port: int

 Creates an ip connection to the Brick Daemon with the given *host* 
 and *port*. With the ip connection itself it is possible to enumerate the 
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

.. py:function:: IPConnection.enumerate(callback)

 :param callback: func(uid, name, stack_id, is_new)
 :rtype: None

 This method registers a callback that receives four parameters:

 * *uid* - str: The UID of the device.
 * *name* - str: The name of the device (includes "Brick" or "Bricklet" and a version number).
 * *stack_id* - int: The Stack ID of the device (you can find out the position in a stack with this).
 * *is_new* - bool: True if the device is added, false if it is removed.

 There are three different possibilities for the callback to be called.
 Firstly, the callback is called with all currently available devices in the
 IP Connection (with *is_new* true). Secondly, the callback is called if
 a new Brick is plugged in via USB (with *is_new* true) and lastely it is
 called if a brick is unplugged (with *is_new* false).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).

.. py:function:: IPConnection.add_device(device)

 :param device: Device
 :rtype: None

 Adds a device (Brick or Bricklet) to the IP Connection. Every device
 has to be added to an ip connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. py:function:: IPConnection.join_thread()

 :rtype: None

 Joins the thread of the ip connection. The call will block until the
 ip connection is :py:func:`destroyed <IPConnection.destroy>`.

 This makes sense if you relies solely on callbacks from listeners or if
 the ip connection was created in a thread.

.. py:function:: IPConnection.destroy()
 
 :rtype: None

 Destroys the ip connection. The socket to the Brick Daemon will be closed
 and the thread of the ip connection terminated. 
