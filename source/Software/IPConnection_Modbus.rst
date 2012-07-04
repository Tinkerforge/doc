.. _ipcon_modbus:

Modbus - IP Connection
======================

This is the API site for the Modbus RTU protocol of the RS485 Extension.

An overview of products that are controllable over Modbus 
can be found :ref:`here <product_overview>`.

.. _ipcon_modbus_protocol:

Protocol
--------

The RS485 Extension uses `Modbus RTU <http://en.wikipedia.org/wiki/Modbus>`__
as the protocol on the RS485 interface.

High level configurations, such as baud rate, parity and stop bits can
be done with the Brick Viewer and are stored on the EEPROM of the
RS485 extension.

The protocol used on the RS485 Extension is modeled after the concept of 
a function call. A request packet is send by the RS485 Master to the stack 
with RS485 Extension to trigger the  execution of a function on a selected
Brick or Bricklet. 
The stack answers with either a response (which can be the response of
an older function call, a response to this function call or a callback) or
a packet with an empty payload. If the answer by the RS485 slave was not
empty, the RS485 Master has to send an empty packet back (ack).

Packet Layout
^^^^^^^^^^^^^

The Modbus protocol is based on packets transfered between a RS485 Master and
potentially many RS485 Slaves. Each packet consists of:

* Modbus address as uint8 (1 byte),
* Modbus function code as uint8 (1 byte),
* Sequence number as uint8 (1 byte),
* Stack ID as uint8 (1 byte),
* Function ID as uint8 (1 byte),
* Packet length as uint16 (2 bytes),
* Payload and
* Modbus CRC16 as uint16 (2 bytes)

The *Modbus address* is the address, that is stored in the EEPROM of the
RS485 extension. It can be set with the Brick Viewer an it should be
between 1 and 255. A message to a stack and responses from this stack will
use this Modbus address.

As the *Modbus function* we use the public function code 100 in all packets
(see Modbus Application Protocol V1.1b chapter 5 "Function Code Categories).

The *Sequence number* is incremented by the RS485 Master and it is used to
make sure that every request gets a response.

The meaning of the *stack ID* depends on the transfer direction of the packet.
If the packet is send from host to stack (request packet) then the stack ID
specifies its destination. If the packet is send from stack to host (response
packet) then the stack ID specifies its source. Stack ID 0 is the broadcast
address for request packets.

In a request packet the *function ID* specifies which function to execute on the
device specified by the stack ID.
In a response packet the function ID specifies from which function or callback
the packet was send.

The *packet length* specifies the length of the inner packet (stack id,
function id, packet lenght and payload) in bytes. A packet without a payload 
has a packet length of 4. 
The function ID combined with the transfer direction defines the content of the
payload and this determines the packet length.

Last but not least, the Modbus CRC16 is calculated for every packet, as
specified in the Modbus RTU specification. 

All data is represented in little endian. A *bool* value is represented by 1
byte; 0 is false, all other values are true. A *float* value is represented by
4 bytes in IEEE 754 format. A *char* value is represented by 1 byte in ASCII
encoding.

A fixed size char array represents a string. If the string is shorter than the
capacity of the array then the remaining space is filled with 0. In this case
the contained string is null-terminated. In case that the string fills the
whole array no null-terminator can be appended and the string is *not*
null-terminated. Therefore, you cannot rely on strings being null-terminated.

Communication
^^^^^^^^^^^^^

Before you can call any functions on the connected devices, you need to
trigger the enumeration of the stacks, after that you can to discover 
which UID belongs to which stack ID. The Modbus addresses of the stacks 
have to be known in beforehand, they can not be discovered.


Triggering Stack Enumeration
""""""""""""""""""""""""""""

To start the enumeration inside of the RS485 Slave stacks and to make it 
aware that it should send out callbacks via RS485, the communication 
has to start with a :modbus:func:`stack_enumerate <IPConnection.stack_enumerate>` 
message.

The request looks as follows:

* Modbus address *MA* as uint8,
* Modbus function code 100 as uint8,
* Sequence number *SN* as uint8,
* Stack ID 0 as uint8,
* Function ID 252 as uint8,
* Packet length 5 as uint16,
* Start stack ID *SS* as uint8,
* Modbus CRC16 as uint16.

Whereby *MA* is the Modbus address of the RS485 stack you want to talk with,
*SN* is anything between 0 and 255, *SS* is the number that should be used to
start the enumeration with. For example: If you send a package with a
start stack ID of 5, all of the devices in the RS485 stack will get a
stack ID of 5 or above.

Since the RS485 Slave can't do the enumeration fast enough, the answer
will likely be an empty message:

* Modbus address *MA* as uint8,
* Modbus function code 100 as uint8,
* Sequence number *SN* as uint8,
* Stack ID 0 as uint8,
* Function ID 0 as uint8,
* Packet length 0 as uint16,
* Modbus CRC16 as uint16.

This message has to be seen as an ack for the request. If anything in this
answer is wrong (wrong function code, wrong Modbus address, wrong CRC, etc)
or there is no answer, you have to resend the request.

If everything checks out the Master can ask again for data. Since the Master 
doesn't have anything else to send, it just sends an empty message:

* Modbus address *MA* as uint8,
* Modbus function code 100 as uint8,
* Sequence number *SN* +1 as uint8,
* Stack ID 0 as uint8,
* Function ID 0 as uint8,
* Packet length 0 as uint16,
* Modbus CRC16 as uint16.

Note that you have to increase the sequence number now, otherwise the slave
will think that you didn't receive the ack and resend it!

If the RS485 Slave had enough time to generate an answer for the 
stack_enumerate request, the answer should now look like this:

* Modbus address *MA* as uint8,
* Modbus function code 100 as uint8,
* Sequence number *SN* +1 as uint8,
* Stack ID 0 as uint8,
* Function ID 252 as uint8,
* Packet length 5 as uint16,
* End stack ID *ES* as uint8,
* Modbus CRC16 as uint16.

Where the end stack ID is the last stack ID of the RS485 slave address.
For example: If a Master sends a 5 as a start stack ID to the slave and
the slave answers with 7 as the end stack ID, it means that the 
RS485 slave stack consists of 3 Bricks or Bricklets with stack ID 5, 6
and 7.

This process has to be repeated for every RS485 slave. With this process
it is possible to distribute unique stack IDs in the whole RS485 bus.
However, this is not necessary. You can use start stack ID 1 for every
RS485 slave and link the stack IDs to the Modbus address. This depends
on how you want to do the routing to and from Bricks and Bricklets
internally.


Resolve UID to Stack ID
"""""""""""""""""""""""

Now you still don't which stack ID corresponds to which UID, so you
have to resolve the UID. Please refer to the 
:ref:`TCP/IP documentation <ipcon_tcpip_resolve_uid>`
for this.

All of the documentation for the TCP/IP protocol is also true for
Modbus. Modbus just has the additional Modbus address, Modbus
function code, sequence number and Modbus CRC16.

Below we will discuss some more examples of requests and responses
and how to handle them. If you get the general idea about the
sequence number and when and when not to send an answer, it is straight
forward to implement the protocol. 

Requests and Responses
""""""""""""""""""""""

In general, every time the RS485 Master sends something to a slave (either with
or without payload), the slave will answer (again either with or without
payload) and the master has to answer again if the answer of the slave
had a payload. After this whole process, the RS485 Master increments the
sequence number.

.. image:: /Images/modbus.png
   :scale: 50 %
   :alt: Modbus protocol overview
   :align: center
   :target: ../../_images/modbus.png


If something goes wrong in the whole process (e.g. CRC wrong, buffer full, 
packet length doesn't fit etc): The slave will stop responding and induce
a timeout. In this case the RS485 master has to resend the request with
the same sequence number.

If the RS485 Master receives a response with wrong CRC or similar, he also has
to resend the request with the same sequence number again.

Otherwise (everything went OK), the sequence number is incremented by the
RS485 master. This approach ensures that there is never a request or response 
lost in the whole process.

Pleas note: If the RS485 master calls a function of a Brick or Bricklet
in a RS485 slave stack, the response by the slave will likely not be the 
response to the function call. It will either be an empty message (ACK)
or it will be a response to another function call from before or it will
be a callback.

The approach should be that you poll every slave regularly (e.g. once per ms) 
with either an empty request if you have no data to transfer or with
a request with payload if you have data to transfer. This will ensure that
no messages pile up in the RS485 slave stack and you will get the responses
to function calls and callbacks with a reasonable latency.

.. _ipcon_modbus_api:

API
---

The following functions and callbacks are supported by all devices.

Basic Methods
^^^^^^^^^^^^^

.. modbus:function:: IPConnection.stack_enumerate

 :functionid: 252
 :request start_stack_id: uint8
 :response end_stack_id: uint8

 This function will trigger the enumeration of an RS485 slave stack.
 The response is the last stack ID in the stack. For example: If a 
 Master sends a 5 as a start stack ID to the slave and the slave
 answers with 7 as the end stack ID, it means that the RS485 slave 
 stack consists of 3 Bricks or Bricklets with stack ID 5, 6 and 7.

 This is a broadcast function and the stack ID in the packet header has to be
 set to 0 (broadcast stack ID).

 You have to call this function once before the communication
 can begin. Otherwise the RS485 slave stack does not now that
 callbacks have to be sent out via RS485.


.. modbus:function:: IPConnection.get_stack_id

 :functionid: 255
 :request uid: uint64
 :response device_uid: uint64
 :response device_firmware_version: uint8[3]
 :response device_name: char[40]
 :response device_stack_id: uint8

 Returns the metadata (UID, firmware version, name and stack ID) of the device
 with the UID given in the request. No response is send if there is no Brick or
 Bricklet with the given UID.

 This is a broadcast function and the stack ID in the packet header has to be
 set to 0 (broadcast stack ID).

 Use this function to resolve a UID to the corresponding stack ID that is
 required for calling other functions of the device.

Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. modbus:function:: IPConnection.enumerate

 :functionid: 254
 :emptyrequest: empty payload
 :noresponse: no response

 Triggers the :modbus:func:`CALLBACK_ENUMERATE <IPConnection.CALLBACK_ENUMERATE>`
 callback for all  devices currently connected to the Brick Daemon.

 This is a broadcast function and the stack ID in the packet header has to be
 set to 0 (broadcast stack ID).

 Use this function to enumerate all connected devices without the need to know
 their UIDs beforehand.

Callbacks
^^^^^^^^^

.. modbus:function:: IPConnection.CALLBACK_ENUMERATE

 :functionid: 253
 :response device_uid: uint64
 :response device_name: char[40]
 :response device_stack_id: uint8
 :response is_new: bool

 There are three different possibilities for the callback to be called.
 Firstly, the callback is triggered for all currently connected devices
 (with *is_new* true) when the :modbus:func:`enumerate <IPConnection.enumerate>`
 function is called. Secondly, the callback is triggered if a new Brick is plugged
 in via USB (with *is_new* true) and lastly it is triggered if a Brick is
 unplugged (with *is_new* false).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).
