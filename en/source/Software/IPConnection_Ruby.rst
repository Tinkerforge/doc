.. _ipcon_ruby:

Ruby - IP Connection
====================

This is the API description for the Ruby bindings of the IP connection.
The IP connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP connection
can be found :ref:`here <product_overview>`.


.. _ipcon_ruby_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.rb>`__

.. literalinclude:: example.rb
 :language: ruby
 :linenos:
 :tab-width: 4


.. _ipcon_ruby_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. rb:function:: IPConnection::new(host, port) -> ipcon

 :param host: str
 :param port: int

 Creates an IP connection to the Brick Daemon with the given *host*
 and *port*. With the IP connection itself it is possible to enumerate the
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

.. rb:function:: IPConnection#add_device(device) -> nil

 :param device: Device

 Adds a device (Brick or Bricklet) to the IP connection. Every device
 has to be added to an IP connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. rb:function:: IPConnection#join_thread() -> nil

 Joins the threads of the IP connection. The call will block until the
 IP connection is :rb:func:`destroyed <IPConnection.destroy>`.

 This makes sense if you relies solely on callbacks for events or if
 the IP connection was created in a threads.

.. rb:function:: IPConnection#destroy() -> nil

 Destroys the IP connection. The socket to the Brick Daemon will be closed
 and the threads of the IP connection terminated.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rb:function:: IPConnection#enumerate { |uid, name, stack_id, is_new| block } -> nil

 This method registers a callback that receives four parameters:

 * *uid* - str: The UID of the device.
 * *name* - str: The name of the device (includes "Brick" or "Bricklet" and a version number).
 * *stack_id* - int: The stack ID of the device (you can find out the position in a stack with this).
 * *is_new* - bool: Is *true* if the device is added, *false* if it is removed.

 There are three different possibilities for the callback to be called.
 Firstly, the callback is called with all currently available devices in the
 IP connection (with *is_new* set to *true*). Secondly, the callback is called if
 a new Brick is plugged in via USB (with *is_new* set to *true*) and lastly it is
 called if a Brick is unplugged (with *is_new* set to *false*).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).
