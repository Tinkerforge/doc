.. _ipcon_php:

PHP - IP Connection
======================

This is the API site for the PHP bindings of the IP connection.
The IP connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP connection
can be found :ref:`here <product_overview>`.

.. _ipcon_php_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/Example.php>`__

.. literalinclude:: Example.php
 :language: php
 :linenos:
 :tab-width: 4

.. _ipcon_php_api:

API
---

Basic Methods
^^^^^^^^^^^^^

.. php:function:: class IPConnection(string $host, int $port)

 Creates an IP connection to the Brick Daemon with the given *$host*
 and *$port*. With the IP connection itself it is possible to enumerate the
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

.. php:function:: void IPConnection::addDevice(Device $device)

 Adds a device (Brick or Bricklet) to the IP connection. Every device
 has to be added to an IP connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. php:function:: void IPConnection::dispatchCallbacks(float $seconds)

 Dispatches incoming callbacks for the given amount of time (negative value
 means infinity). Because PHP doesn't support threads you need to call this
 method periodically to ensure that incoming callbacks are handled. If you
 don't use callbacks you don't need to call this method.

 The recommended dispatch time is 0s. This will just dispatch all pending
 callbacks without waiting for further callbacks.

.. php:function:: void IPConnection::destroy()

 Destroys the IP connection. The socket to the Brick Daemon will be closed.

Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. php:function:: void IPConnection::enumerate(callable $callback)

 This method registers a callback with the signature:

 .. code-block:: php

  void callback(string $uid, string $name, int $stackID, bool $isNew)

 that receives four parameters:

 * *$uid* - The UID of the device.
 * *$name* - The name of the device (includes "Brick" or "Bricklet" and a version number).
 * *$stackID* - The stack ID of the device (you can find out the position in a stack with this).
 * *$isNew* - True if the device is added, false if it is removed.

 There are three different possibilities for the callback to be called.
 Firstly, the callback is called with all currently available devices in the
 IP connection (with *$isNew* true). Secondly, the callback is called if
 a new Brick is plugged in via USB (with *$isNew* true) and lastly it is
 called if a Brick is unplugged (with *$isNew* false).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).

 You need to call :php:func:`dispatchCallbacks <IPConnection::dispatchCallbacks>`
 in order to receive the callbacks. The recommended dispatch time is 2.5s.
