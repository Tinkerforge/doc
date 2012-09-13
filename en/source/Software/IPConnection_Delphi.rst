.. _ipcon_delphi:

Delphi - IP Connection
======================

This is the API description for the Delphi bindings of the IP Connection.
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP Connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.


.. _ipcon_delphi_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.rb>`__

.. literalinclude:: Example.pas
 :language: delphi
 :linenos:
 :tab-width: 4


.. _ipcon_delphi_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. delphi:function:: constructor TIPConnection.Create(const host: string; const port: word)

 Creates an IP Connection to the Brick Daemon with the given *host*
 and *port*. With the IP Connection itself it is possible to enumerate the
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

.. delphi:function:: procedure TIPConnection.AddDevice(const device: TDevice)

 Adds a device (Brick or Bricklet) to the IP Connection. Every device
 has to be added to an IP Connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. delphi:function:: procedure TIPConnection.JoinThread

 Joins the threads of the IP Connection. The call will block until the
 IP Connection is :delphi:func:`destroyed <TIPConnection.Destroy>`.

 This is useful if you relies solely on callbacks for events or if
 the IP Connection was created in a threads.

.. delphi:function:: destructor TIPConnection.Destroy

 Destroys the IP Connection. The socket to the Brick Daemon will be closed
 and the threads of the IP Connection terminated.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. delphi:function:: procedure TIPConnection.Enumerate(const enumerateCallback: TIPConnectionNotifyEnumerate)

 This procedure registers a callback with the signature:
 
 .. code-block:: delphi

  procedure(const uid: string; const name: string; const stackID: byte; const isNew: boolean) of object; 

 that receives four parameters:

 * *uid*: The UID of the device.
 * *name*: The name of the device (includes "Brick" or "Bricklet" and a version number).
 * *stackID*: The stack ID of the device (you can find out the position in a stack with this).
 * *isNew*: Is *true* if the device is added, *false* if it is removed.

 There are three different possibilities for the callback to be called.
 Firstly, the callback is called with all currently connected devices
 (with *isNew* set to *true*). This is triggered by the call to
 :delphi:func:`Enumerate <TIPConnection.Enumerate>`. Secondly, the callback is called if
 a new Brick is plugged in via USB (with *isNew* set to *true*) and lastly it is
 called if a Brick is unplugged (with *isNew* set to *false*).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).
